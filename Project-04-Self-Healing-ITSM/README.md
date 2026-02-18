# Project 4: The "Self-Healing" IT Service Desk 🛠️
> **Category:** AIOps / Multi-Agent Systems (CrewAI)

## 💼 Business Use Case
The cost of Level-1 (L1) support tickets is a major drain on IT budgets. Most of these tickets (password resets, disk space, service restarts) follow predictable patterns. This project uses a **Multi-Agent Crew** to autonomously triage a ticket, research the specific technical environment, and generate a resolution script.

## 🛠️ Tech Stack
- **Agent Framework:** CrewAI
- **Orchestration:** LangChain
- **Model:** GPT-4o
- **Tools:** Custom Python Search & Scripting tools

## 🏗️ Technical Architecture (The "Crew")
This project utilizes three specialized agents working in sequence:
1. **The Triage Agent:** Analyzes the incoming ticket to identify the core technical issue.
2. **The Systems Researcher:** Looks up the standard operating procedure (SOP) for that specific issue.
3. **The Automation Engineer:** Writes the Python or PowerShell script required to resolve the issue.

## 🎯 Consultant's Strategic Impact
- **Cost Reduction:** Automates high-volume, low-complexity tasks.
- **Consistency:** Ensures every ticket is handled according to enterprise-standard SOPs.
- **Escalation Efficiency:** If the agents cannot solve it, they provide a full "investigation summary" to the L2 engineer, saving them 15-20 minutes of research.
