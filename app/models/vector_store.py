from langchain_pinecone import PineconeVectorStore
from langchain_cohere import CohereEmbeddings
from pinecone import Pinecone
from pinecone import Pinecone, ServerlessSpec
from config import Config
import os
import certifi



class VectorStore:
    def __init__(self, index_name: str):
        # Initialize Pinecone client
        self.pc = Pinecone(api_key=Config.PINECONE_API_KEY)
        self.index_name = index_name

        # Check and create Pinecone index if it doesn't exist
        existing_indexes = [idx.name for idx in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            self.pc.create_index(
                name=self.index_name,
                dimension=1024,  # Dimension for Cohere embed-english-v3.0
                metric="cosine",
                spec=ServerlessSpec(
                    cloud=Config.PINECONE_CLOUD,
                    region=Config.PINECONE_REGION
                )
            )

        # Initialize Cohere embeddings
        os.environ['SSL_CERT_FILE'] = certifi.where()
        self.embeddings = CohereEmbeddings(
            model="embed-english-v3.0",
            cohere_api_key=Config.COHERE_API_KEY
        )
        
        # Modern Pinecone vector store integration
        self.vector_store = PineconeVectorStore(
            index_name=self.index_name,
            embedding=self.embeddings,
            pinecone_api_key=Config.PINECONE_API_KEY
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)    