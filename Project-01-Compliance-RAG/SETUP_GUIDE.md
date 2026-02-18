# 🛠️ Setup & Run Guide: Project 1 (Compliance RAG)
Follow these steps to initialize the Multi-Doc Compliance engine.

## 1. Prerequisites
- Python 3.9+ 
- OpenAI API Key
- Pinecone Account (or a local Vector DB like Chroma)

## 2. Environment Setup
1. Open your terminal in this folder.
2. Create and activate a virtual environment:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate` | Mac: `source venv/bin/activate`

## 3. Installation
Install the enterprise RAG stack:
`pip install -r requirements.txt`

## 4. Data Preparation
1. Create a folder named `data/` inside this project folder.
2. Drop your target PDF or Text policies into that folder.

## 5. Configuration & Run
1. Update your `.env` file with your credentials.
2. Run the ingestion and query script:
   `python rag_engine.py`
