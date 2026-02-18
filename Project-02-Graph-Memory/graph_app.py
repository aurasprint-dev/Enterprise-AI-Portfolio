import os
from typing import TypedDict, Annotated, List, Union
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# 1. Define the 'State' of the graph
# This is what allows the AI to "remember" previous steps
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], "The conversation history"]

# 2. Define the Model
model = ChatOpenAI(model="gpt-4o", temperature=0)

# 3. Define the Node (The Logic)
def call_model(state: AgentState):
    messages = state['messages']
    response = model.invoke(messages)
    # We return a list, because we want to append the new message to history
    return {"messages": [response]}

# 4. Build the Graph
workflow = StateGraph(AgentState)

# Add the node to the graph
workflow.add_node("agent", call_model)

# Set the entry point (where the conversation starts)
workflow.set_entry_point("agent")

# Set the end point
workflow.add_edge("agent", END)

# 5. Compile the Graph
app = workflow.compile()

# --- Portfolio Testing Block ---
if __name__ == "__main__":
    # Simulate a multi-turn conversation
    inputs = {"messages": [HumanMessage(content="My name is Alex and I am the Project Manager.")]}
    config = {"configurable": {"thread_id": "1"}} # This ID is the "Memory Key"
    
    for output in app.stream(inputs, config=config):
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print(value["messages"][-1].content)
