# 🛠️ Setup & Run Guide: Project 3
Follow these steps to deploy and test the Security Triage Agent.

## 1. Prerequisites
- Python 3.9+ installed.
- An OpenAI API Key.

## 2. Environment Setup
1. Open your terminal in this folder.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

## 3. Installation
Install the required AI libraries:
`pip install -r requirements.txt`

## 4. Configuration
1. Rename `.env.example` to `.env`.
2. Paste your API key: `OPENAI_API_KEY=your_actual_key_here`.

## 5. Execution
Run the triage agent:
`python triage_agent.py`
