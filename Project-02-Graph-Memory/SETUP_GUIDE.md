# 🛠️ Setup & Run Guide: Project 2 (Graph-Based Memory)
This guide explains how to run the stateful LangGraph agent.

## 1. Prerequisites
- Python 3.9+
- OpenAI API Key

## 2. Environment Setup
1. Navigate to the project folder.
2. Create and activate a virtual environment:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate` | Mac: `source venv/bin/activate`

## 3. Installation
Install LangGraph and LangChain:
`pip install -r requirements.txt`

## 4. Configuration
Ensure your `.env` file contains:
`OPENAI_API_KEY=your_key_here`

## 5. Testing the "Memory"
Run the script:
`python graph_app.py`

**How to verify:** The script is hardcoded with a `thread_id`. You can modify the `__main__` block to send two separate messages. The agent will remember your name and role across both turns because of the Graph State.
