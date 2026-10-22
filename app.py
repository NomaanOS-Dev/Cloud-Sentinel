import streamlit as st
import pandas as pd
from analyzer import analyze_cloud_security

st.set_page_config(page_title="Cloud-Sentinel", page_icon="☁️", layout="wide")
st.title("☁️ Cloud-Sentinel")
st.subheader("Multi-Cloud IAM & Misconfiguration Auditor")
st.write("AI-assisted AWS, Azure and GCP security findings analysis.")

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("OpenAI API Key", type="password")

sample_findings = [
    {"cloud": "AWS", "resource": "demo-storage-bucket", "finding": "Public storage access", "severity": "High"},
    {"cloud": "Azure", "resource": "demo-service-principal", "finding": "Excessive permissions", "severity": "High"},
    {"cloud": "GCP", "resource": "demo-admin-role", "finding": "Broad administrative role", "severity": "Medium"},
]

st.info("Demo findings only. No live cloud account is scanned.")

if st.button("Load Sample Findings"):
    st.session_state["findings"] = pd.DataFrame(sample_findings)

uploaded = st.file_uploader("Upload findings CSV (optional)", type=["csv"])
if uploaded:
    try:
        df = pd.read_csv(uploaded)
        if df.empty:
            st.warning("Uploaded CSV is empty.")
        else:
            st.session_state["findings"] = df
    except Exception as exc:
        st.error(f"CSV error: {exc}")

if "findings" in st.session_state:
    df = st.session_state["findings"]
    st.subheader("Cloud Security Findings")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download Findings CSV",
        df.to_csv(index=False).encode("utf-8"),
        "cloud_sentinel_findings.csv",
        "text/csv",
    )

    if st.button("Audit Findings", type="primary"):
        with st.spinner("Auditing findings..."):
            report = analyze_cloud_security(api_key, df.to_dict("records"))
        st.subheader("Security Audit Report")
        st.markdown(report)
        st.download_button(
            "Download Audit Report",
            report,
            "cloud_sentinel_audit.txt",
            "text/plain",
        )

st.caption("AI recommendations require human verification.")
