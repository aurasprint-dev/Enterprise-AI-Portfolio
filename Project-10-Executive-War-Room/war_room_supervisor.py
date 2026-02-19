import os
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

load_dotenv()

# 1. Define the State
class WarRoomState(TypedDict):
    executive_query: str
    department_reports: List[str]
    final_brief: str

# 2. Simulate Domain Expert Nodes
def security_expert(state: WarRoomState):
    # In reality, this would call Project 3's logic
    return {"department_reports": state["department_reports"] + ["Security: All systems nominal. 2 low-level threats blocked."]}

def finance_expert(state: WarRoomState):
    # In reality, this would call Project 8's logic
    return {"department_reports": state["department_reports"] + ["Finance: 1 anomaly detected in 'Office Supplies' ($12k). Marked for review."]}

def supervisor_synthesizer(state: WarRoomState):
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    reports = "\n".join(state["department_reports"])
    prompt = f"Executive Query: {state['executive_query']}\n\nDepartment Data:\n{reports}\n\nProvide a 3-bullet point 'Executive Brief' and a 'Business Health Score' (0-100)."
    response = llm.invoke(prompt)
    return {"final_brief": response.content}

# 3. Build the Graph
workflow = StateGraph(WarRoomState)

workflow.add_node("security", security_expert)
workflow.add_node("finance", finance_expert)
workflow.add_node("synthesizer", supervisor_synthesizer)

workflow.set_entry_point("security")
workflow.add_edge("security", "finance")
workflow.add_edge("finance", "synthesizer")
workflow.add_edge("synthesizer", END)

app = workflow.compile()

# 4. Execute for the CEO
if __name__ == "__main__":
    inputs = {"executive_query": "Give me a morning briefing on company operations.", "department_reports": []}
    result = app.invoke(inputs)
    print("\n🏛️ --- EXECUTIVE WAR ROOM BRIEF --- 🏛️")
    print(result["final_brief"])
