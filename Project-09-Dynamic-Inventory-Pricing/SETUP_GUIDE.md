# 🛠️ Setup & Run Guide: Project 9
Deploying the Dynamic Inventory & Pricing Agent.

## 1. Prerequisites
- Python 3.10+
- OpenAI API Key

## 2. Installation
1. Navigate to: `cd Project-09-Dynamic-Inventory-Pricing`
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`

## 3. Configuration
Ensure your `.env` file contains your `OPENAI_API_KEY`.

## 4. Execution
Run the agent:
`python inventory_agent.py`

**What is happening?**
The agent will:
1. Call `get_inventory_status` for the Firewall.
2. See that stock is only 5 units (low).
3. Determine that a price increase is necessary to manage demand.
4. Call `update_pricing` automatically.
