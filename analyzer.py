import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

def audit_cloud_config(api_key, config_data):
    if not api_key:
        return "Error: OpenAI API Key is missing."
    
    os.environ["OPENAI_API_KEY"] = api_key
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    
    prompt = PromptTemplate(
        input_variables=["config"],
        template="""
You are an expert Cloud Security Posture Management (CSPM) Architect and Multi-Cloud Compliance Engineer.
Analyze the following cloud infrastructure configuration (IAM policy, Terraform, Kubernetes manifest, or Docker security config) for security vulnerabilities, excessive privileges, and compliance drift:

CLOUD CONFIGURATION:
{config}

Provide a structured Cloud Security & Compliance Audit Report containing:
1. **Compliance Risk Score (1-10) & Posture Status**
2. **Identified Misconfigurations & Privileged Access Flaws**
3. **CIS Benchmark / NIST SP 800-53 Control Correlation**
4. **Remediated Configuration Snippet (Secure JSON/YAML format)**
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(config=config_data)
