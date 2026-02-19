import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()

# 1. Define the Tools the AI can use
@tool
def get_inventory_status(product_name: str):
    """Returns the current stock level and daily sales velocity for a product."""
    # Simulation: In a real app, this would query a SQL DB
    inventory_db = {
        "Enterprise Firewall": {"stock": 5, "velocity": 2},
        "Cloud License Pack": {"stock": 500, "velocity": 10}
    }
    return inventory_db.get(product_name, "Product not found")

@tool
def update_pricing(product_name: str, new_price: float):
    """Updates the price of a product in the system."""
    return f"Price for {product_name} updated to ${new_price}."

tools = [get_inventory_status, update_pricing]

# 2. Setup the Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an Inventory Manager. Use tools to check stock and adjust prices if stock is low (below 10 units)."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 3. Execute
if __name__ == "__main__":
    print("🤖 Inventory Agent Starting...")
    agent_executor.invoke({"input": "Check the status of 'Enterprise Firewall' and take action if needed."})
