import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA

# 1. SETUP: Configuration & API Keys
# Tip: As a consultant, always use environment variables for security.
OPENAI_API_KEY = "your_openai_key"
PINECONE_API_KEY = "your_pinecone_key"
INDEX_NAME = "compliance-index"

def build_compliance_rag(pdf_path):
    # 2. INGESTION: Load the IT Policy PDF
    loader = PyPDFLoader(pdf_path)
    data = loader.load()

    # 3. CHUNKING: Split text for better retrieval
    # Senior Tip: 1000 char chunks with 10% overlap is standard for IT docs.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)

    # 4. EMBEDDING: Convert text to math (vectors)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # 5. VECTOR STORE: Upload to Pinecone
    vectorstore = PineconeVectorStore.from_documents(
        chunks, embeddings, index_name=INDEX_NAME, pinecone_api_key=PINECONE_API_KEY
    )

    # 6. RAG CHAIN: Connect the dots
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever()
    )
    
    return qa_chain

# --- Execution ---
if __name__ == "__main__":
    # Replace with a sample IT Policy PDF
    rag_tool = build_compliance_rag("company_it_policy.pdf")
    query = "What is our policy on remote work security?"
    print(f"AI Response: {rag_tool.run(query)}")
