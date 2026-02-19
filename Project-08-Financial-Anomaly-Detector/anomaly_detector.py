import os
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

# 1. Define the Structured Response
class TransactionAnalysis(BaseModel):
    is_anomaly: bool = Field(description="True if the transaction looks suspicious")
    risk_score: int = Field(description="Risk score from 0 (Safe) to 100 (High Alert)")
    reasoning: str = Field(description="Technical explanation for the score")
    suggested_action: str = Field(description="Action for the finance team: Approve, Flag, or Reject")

# 2. Define the Agent
# We use Pydantic AI to ensure the agent outputs EXACTLY what the finance team needs
detector_agent = Agent(
    'openai:gpt-4o',
    result_type=TransactionAnalysis,
    system_prompt=(
        "You are a Senior Financial Auditor. Review transactions for: "
        "1. Out-of-policy spending (e.g., $5000 on 'Lunch') "
        "2. Known high-risk vendors "
        "3. Unusual spending patterns."
    )
)

# 3. Simulate a Suspect Transaction
suspect_tx = {
    "vendor": "Unknown Global Tech Ltd",
    "amount": 12500.00,
    "category": "Office Supplies",
    "description": "Premium desk chairs for home office"
}

async def analyze_spend():
    print(f"🧐 Auditing transaction from {suspect_tx['vendor']} for ${suspect_tx['amount']}...")
    
    result = await detector_agent.run(f"Analyze this transaction: {suspect_tx}")
    
    data = result.data
    print(f"\n[RESULT] Anomaly: {data.is_anomaly}")
    print(f"[SCORE] {data.risk_score}/100")
    print(f"[REASON] {data.reasoning}")
    print(f"[ACTION] {data.suggested_action.upper()}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(analyze_spend())
