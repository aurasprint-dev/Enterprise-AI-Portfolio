# Project 3: AI Security Threat Triaging Agent 🛡️
> **Category:** Cybersecurity / Autonomous SOC

## 💼 Business Use Case
Enterprise security teams (SOC) suffer from "alert fatigue," often missing critical breaches because they are buried under thousands of low-priority system logs. This project builds an Intelligent Triage Agent that analyzes incoming security logs in real-time, categorizes them, and automatically escalates high-risk anomalies to human engineers.

## 🛠️ Tech Stack
- **AI Framework:** PydanticAI (for strict data validation)
- **Log Analysis:** Python / Pandas
- **Schema Validation:** Pydantic (ensuring AI outputs follow security protocols)
- **Model:** GPT-4o-mini (Optimized for speed/cost)

## 🏗️ Technical Architecture
1. **Ingestion Layer:** Simulates a stream of system logs (IP addresses, access attempts, port scans).
2. **Analysis Node:** The agent evaluates the log against standard security frameworks (like MITRE ATT&CK).
3. **Reasoning Engine:**
   - **Low Risk:** Logs the event and moves on.
   - **Medium Risk:** Tags for daily review.
   - **High Risk:** Triggers an immediate "Escalation Report" with a suggested mitigation plan.
4. **Structured Output:** Forces the AI to return data in a JSON format that can be read by other security tools (SIEM).

## 🎯 Consultant's Strategic Impact
- **MTTD Reduction:** Drastically lowers the "Mean Time to Detect" critical threats.
- **Operational Efficiency:** Filters out 90% of noise, allowing human experts to focus on complex hunting tasks.
- **Audit Trail:** Every AI decision is logged with a "Reasoning Path," satisfying compliance requirements for SOC2/ISO 27001.
