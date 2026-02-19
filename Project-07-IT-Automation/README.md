# Project 7: Self-Healing IT Operations (n8n Workflow) ⚡
> **Category:** AIOps / Hyper-Automation

## 💼 Business Use Case
IT Operations teams are often stuck in a "reactive" loop, manually responding to the same server alerts (e.g., "Service Down" or "Disk Full") dozens of times a week. This project demonstrates a **Self-Healing Workflow** built in n8n. It intercepts system alerts, uses an AI Agent to diagnose the root cause, and autonomously executes a remediation script—reducing Mean Time to Repair (MTTR) from hours to seconds.

## 🛠️ Tech Stack
- **Orchestration:** n8n (Low-code workflow engine)
- **Intelligence:** n8n AI Agent Node + GPT-4o
- **Connectivity:** Webhooks (Ingestion) & SSH/HTTP (Execution)
- **Notifications:** Slack / Microsoft Teams

## 🏗️ Technical Architecture
1. **Trigger:** An HTTP Webhook receives an alert from a monitoring tool (like Datadog or UptimeRobot).
2. **Diagnosis:** The n8n AI Node analyzes the error message against a "Common Fixes" database.
3. **Execution:** If the fix is low-risk (e.g., `systemctl restart nginx`), n8n executes the command via SSH.
4. **Escalation:** If the AI is unsure, it automatically creates a Jira ticket and alerts the team on Slack.

5. Note: In n8n, "Code" is stored as a JSON file that you can import directly into the canvas.

## 🎯 Consultant's Strategic Impact
- **Operational Scalability:** Allows IT teams to manage 5x more infrastructure without increasing headcount.
- **Error Reduction:** Eliminates human typos during high-pressure system outages.
- **Auditability:** Every automated action is logged in n8n for compliance and post-mortem review.
