# 🛠️ Setup & Run Guide: Project 4
How to deploy the Multi-Agent Self-Healing Service Desk.

## 1. Prerequisites
- Python 3.10+
- OpenAI API Key

## 2. Installation
1. Navigate to the folder: `cd Project-04-Self-Healing-ITSM`
2. Create virtual environment: `python -m venv venv`
3. Activate:
   - Windows: `venv\Scripts\activate` | Mac: `source venv/bin/activate`
4. Install: `pip install -r requirements.txt`

## 3. Configuration
1. Ensure your `.env` file in the root or this folder has your `OPENAI_API_KEY`.

## 4. Execution
Run the crew:
`python service_desk_crew.py`

**What to expect:** You will see the agents "talking" to each other in the terminal. The Triager will explain the problem, and the Engineer will then output a Python script to solve it.
