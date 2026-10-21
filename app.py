import streamlit as st
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from analyzer import audit_cloud_config

st.set_page_config(page_title="Cloud-Sentinel | Multi-Cloud IAM Auditor", page_icon="☁️", layout="wide")

st.title("☁️ Cloud-Sentinel")
st.markdown("### Multi-Cloud IAM & Misconfiguration Auditor")
st.markdown("Audit cloud infrastructure policies, Kubernetes manifests, and IAM configurations against CIS Benchmarks instantly.")

st.sidebar.header("🔐 Configuration")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Sample Config / IAM Policy")
sample_config = """{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "OverlyPermissiveIAM",
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    },
    {
      "Sid": "PublicS3BucketAccess",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::company-sensitive-backups/*",
      "Principal": "*"
    }
  ]
}"""

if st.sidebar.button("Load Sample IAM Policy"):
    st.session_state["config_input"] = sample_config

config_input = st.text_area("Paste Cloud Configuration / IAM / Terraform JSON:", value=st.session_state.get("config_input", ""), height=200)

if st.button("🚀 Audit Cloud Posture", type="primary"):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
    elif not config_input.strip():
        st.error("Please enter configuration data to audit.")
    else:
        with st.spinner("Analyzing cloud policies and checking compliance..."):
            result = audit_cloud_config(api_key, config_input)
            st.session_state["cloud_result"] = result

if "cloud_result" in st.session_state:
    st.markdown("---")
    st.subheader("📋 Cloud-Sentinel Security Audit Report")
    st.markdown(st.session_state["cloud_result"])
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download Markdown Report",
            data=st.session_state["cloud_result"],
            file_name="Cloud_Sentinel_Report.md",
            mime="text/markdown"
        )
        
    with col2:
        def create_pdf(text):
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            p.drawString(50, height - 50, "Cloud-Sentinel Security Audit Report")
            textobject = p.beginText(50, height - 80)
            textobject.setFont("Helvetica", 10)
            
            for line in text.split("\n"):
                if textobject.getY() < 50:
                    p.drawText(textobject)
                    p.showPage()
                    textobject = p.beginText(50, height - 50)
                    textobject.setFont("Helvetica", 10)
                textobject.textLine(line[:90])
                
            p.drawText(textobject)
            p.save()
            buffer.seek(0)
            return buffer.getvalue()

        pdf_data = create_pdf(st.session_state["cloud_result"])
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name="Cloud_Sentinel_Report.pdf",
            mime="application/pdf"
        )
