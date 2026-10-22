# Cloud-Sentinel

AI-assisted Multi-Cloud IAM & Misconfiguration Auditor.

Cloud-Sentinel helps security teams review cloud security findings across AWS, Azure, and Google Cloud Platform (GCP), identify risky IAM permissions and misconfigurations, and generate evidence-based remediation guidance.

Developed by NomaanOS-Dev.

## Key Features

- Multi-cloud findings review across AWS, Azure, and GCP
- IAM and privilege-escalation risk assessment
- Misconfiguration analysis for public exposure and weak access controls
- AI-assisted evidence, severity, and remediation recommendations
- CSV upload and export workflow for security findings
- Interactive Streamlit dashboard for review and reporting

## Tech Stack

- Python 3.x
- Streamlit
- OpenAI Python SDK
- Pandas

## Installation

```bash
git clone https://github.com/NomaanOS-Dev/Cloud-Sentinel.git
cd Cloud-Sentinel
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then add your OpenAI API key in the application sidebar.

## How It Works

1. Upload a CSV of cloud security findings or load the sample dataset.
2. Review the findings in the dashboard.
3. Run the AI security audit to assess:
   - excessive IAM privileges
   - public exposure risks
   - weak access controls
   - misconfiguration patterns
4. Export the generated audit report for internal review.

## Security Notice

This application is designed for demonstration and security review workflows. It does not scan live cloud accounts unless additional integrations are added. Demo findings are illustrative, and all AI-generated recommendations should be validated by a human reviewer before being applied in production environments.

## License

This project is provided as-is for research, evaluation, and security review workflows.
