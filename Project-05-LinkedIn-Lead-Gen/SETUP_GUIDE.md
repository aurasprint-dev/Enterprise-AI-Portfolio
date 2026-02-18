# 🛠️ Setup & Run Guide: Project 5
How to run your Autonomous AI SDR.

## 1. Prerequisites
- Python 3.10+
- OpenAI API Key
- **Serper API Key:** (Get a free key at [serper.dev](https://serper.dev) for web search capabilities).

## 2. Installation
1. Navigate to the folder: `cd Project-05-LinkedIn-Lead-Gen`
2. Create virtual environment: `python -m venv venv`
3. Activate:
   - Windows: `venv\Scripts\activate` | Mac: `source venv/bin/activate`
4. Install: `pip install -r requirements.txt`

## 3. Configuration
1. Update your `.env` file with:
   - `OPENAI_API_KEY=your_key`
   - `SERPER_API_KEY=your_key`

## 4. Execution
Run the SDR Agent:
`python ai_sdr_crew.py`

**Customization:** You can change the `prospect_name` and `company_name` in the `if __name__ == "__main__":` block to research anyone you like!
