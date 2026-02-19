# Project 8: Financial Anomaly Detector 💰
> **Category:** FinOps / Fraud Detection & Compliance

## 💼 Business Use Case
Large-scale financial environments process thousands of invoices and expense reports daily. Human auditors cannot catch every anomaly, leading to "leakage" or fraud. This project builds an **Automated Auditor** that analyzes transaction data against strict corporate rules (e.g., spending limits, vendor blacklists, and duplicate detection) using AI-driven reasoning.

## 🛠️ Tech Stack
- **AI Framework:** Pydantic AI (for type-safe, validated reasoning)
- **Data Handling:** Pydantic (Schema enforcement)
- **Model:** GPT-4o
- **Environment:** Python 3.11+

## 🏗️ Technical Architecture
1. **Schema Layer:** Defines what a "Valid Transaction" looks like (Amount, Vendor, Category, Timestamp).
2. **Policy Agent:** A specialized AI agent that reviews a transaction against a set of dynamic corporate policies.
3. **Anomaly Scoring:** The agent assigns a risk score (0-100) and provides a "Justification" for its decision.
4. **Structured Output:** Results are returned as a validated JSON object, ready to be pushed to an ERP system like SAP or Oracle.

## 🎯 Consultant's Strategic Impact
- **Risk Mitigation:** Identifies potentially fraudulent or non-compliant spend before payment is processed.
- **Audit Preparedness:** Every flag includes a technical "Reasoning" field, simplifying year-end financial audits.
- **Cost Efficiency:** Reduces the manual workload of the Accounts Payable (AP) team by up to 70%.
