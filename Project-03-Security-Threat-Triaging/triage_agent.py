import os
import json
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

# 1. Define the Strict Output Schema
class SecurityTriage(BaseModel):
    risk_level: str = Field(description="Low, Medium, or High")
    category: str = Field(description="e.g., Brute Force, Unauthorized Access, Port Scan")
    summary: str = Field(description="A brief 1-sentence technical summary")
    action_required: bool = Field(description="True if an engineer needs to be alerted immediately")

# 2. Initialize the AI Agent
agent = Agent('openai:gpt-4o-mini', result_type=SecurityTriage)

# 3. Simulate a Security Log
raw_log = """
Jan 18 22:45:01 server-01 sshd[1234]: Failed password for root from 192.168.1.50 port 5678 ssh2
Jan 18 22:45:02 server-01 sshd[1234]: Failed password for root from 192.168.1.50 port 5679 ssh2
Jan 18 22:45:03 server-01 sshd[1234]: Failed password for root from 192.168.1.50 port 5680 ssh2
"""

async def run_triage():
    print("🛡️ Analyzing Security Log...")
    result = await agent.run(f"Triage the following log: {raw_log}")
    
    # Print the structured result
    print(f"\n[RISK: {result.data.risk_level.upper()}]")
    print(f"Category: {result.data.category}")
    print(f"Summary: {result.data.summary}")
    print(f"Escalated: {'🚨 YES' if result.data.action_required else '✅ NO'}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_triage())
