# 🛠️ Setup & Run Guide: Project 8
Deploying the Financial Anomaly Detector.

## 1. Prerequisites
- Python 3.10+
- OpenAI API Key

## 2. Installation
1. Navigate to: `cd Project-08-Financial-Anomaly-Detector`
2. Create virtual environment: `python -m venv venv`
3. Activate:
   - Windows: `venv\Scripts\activate` | Mac: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## 3. Configuration
Ensure your `.env` file contains your `OPENAI_API_KEY`.

## 4. Execution
Run the auditor:
`python anomaly_detector.py`

**Testing Strategy:** Change the `suspect_tx` values in the code to see how the AI reacts to different amounts and categories. (e.g., Change amount to $50.00 to see it mark the transaction as 'Safe').
