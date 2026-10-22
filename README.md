# Cloud-Sentinel

An AI-assisted Multi-Cloud IAM and Misconfiguration Auditor designed to review cloud security findings, identify risky permissions, and recommend practical remediation.

Developed by NomaanOS-Dev.

## 🚀 Key Features

- **Multi-Cloud Security Review:** Organize security findings across AWS, Microsoft Azure, and Google Cloud Platform (GCP).
- **IAM Risk Assessment:** Highlight excessive permissions and potentially risky administrative roles.
- **Misconfiguration Analysis:** Review findings involving public storage access and access-control weaknesses.
- **AI-Assisted Auditing:** Generate evidence-based assessments, severity estimates, and remediation recommendations.
- **CSV Import and Export:** Upload findings and download audit data.
- **Interactive Dashboard:** Review findings and export AI-generated audit reports through Streamlit.

## 🛠️ Tech Stack

Python 3.x | Streamlit | OpenAI API | Pandas

## 📦 Installation

```bash
git clone https://github.com/NomaanOS-Dev/Cloud-Sentinel.git
cd Cloud-Sentinel
pip install -r requirements.txt
streamlit run app.py
Configure your OpenAI API key in the application sidebar.
🛡️ Security Notice
Demo findings are illustrative. This application does not scan live cloud accounts unless additional integrations are implemented. Verify findings and validate remediation steps before applying changes to production environments.
