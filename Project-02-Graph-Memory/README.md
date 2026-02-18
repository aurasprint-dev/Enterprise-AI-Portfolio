# Project 2: Graph-Based Enterprise Memory 🧠
> **Category:** Advanced RAG / Agentic Workflows

## 💼 Business Use Case
Standard AI chatbots suffer from "context drift"—they forget what was discussed 10 minutes ago or can't connect information between different departments (e.g., how a Sales update affects a Technical roadmap). This project uses **LangGraph** to create a persistent, stateful memory that tracks multi-layered business logic across sessions.

## 🛠️ Tech Stack
- **Orchestration:** LangGraph (Stateful Multi-Agent Framework)
- **Framework:** LangChain
- **Persistence:** SQLite (for thread-scoped checkpointing)
- **Model:** GPT-4o / Claude 3.5 Sonnet

## 🏗️ Technical Architecture
Unlike a linear chain, this project models the conversation as a **Directed Acyclic Graph (DAG)**:
1. **Node - State Loader:** Checks the `thread_id` to retrieve previous conversation context.
2. **Node - Logic Router:** Determines if the query is a new request or an update to an existing project.
3. **Node - Knowledge Graph Update:** Merges new information into the persistent state without overwriting old data.
4. **Edge - Conditional Check:** Validates if the "Memory" is sufficient to answer or if more details are needed.

## 🎯 Consultant's Strategic Impact
- **Context Continuity:** Enables "Thread-ID" based memory, allowing users to resume complex planning sessions days later.
- **Cross-Functional Logic:** Connects dots between "Silo A" and "Silo B" by maintaining a shared state.
- **Human-in-the-Loop:** Built-in "breakpoints" allow managers to review the AI's "memory" before it acts on it.
