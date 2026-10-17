import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # LLM and Embedding API Keys
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    
    # Pinecone Vector Store Configuration
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_ENV = os.getenv('PINECONE_ENV') # Optional, depending on your pinecone client setup

    # Pinecone Index Settings (Cohere embed-english-v3.0 uses dimension 1024)
    PINECONE_INDEX_NAME = os.getenv('PINECONE_INDEX_NAME', 'knowledge-management-system-index')
    PINECONE_CLOUD = os.getenv('PINECONE_CLOUD', 'aws')
    PINECONE_REGION = os.getenv('PINECONE_REGION', 'us-east-1')
    
    # Local path (kept for reference if needed elsewhere)
    VECTOR_DB_PATH = 'vector_db'    