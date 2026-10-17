from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from config import Config
from langchain_core.runnables import RunnablePassthrough
class LLMService:
    def __init__(self, vector_store):
        # 1. Initialize the Groq chat model
        self.llm = ChatGroq(
            temperature=0.7,
            model_name="openai/gpt-oss-120b",
            groq_api_key=Config.GROQ_API_KEY # or Config.GROQ_API_KEY depending on your config setup
        )
        
        # 2. Extract the retriever from your vector store
        self.retriever = vector_store.vector_store.as_retriever()
        
        # 3. Define a modern prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's questions strictly based on the provided context below:\n\n{context}"),
            ("human", "{input}"),
        ])
        
        # 4. Build the modern LCEL chain
        # - "context" retrieves documents and formats them into a single string.
        # - "input" passes the raw query through.
        # - The output feeds into the prompt, then the LLM, and parses out the string content.
        self.chain = (
            {
                "context": self.retriever | self._format_docs,
                "input": RunnablePassthrough()
            }
            | self.prompt
            | self.llm
        )

    def _format_docs(self, docs):
        """Helper function to join retrieved document page contents."""
        return "\n\n".join(doc.page_content for doc in docs)

    def get_response(self, query):
        try:
            # Invoke the modern LCEL chain
            response = self.chain.invoke(query)
            # ChatGroq returns an AIMessage object, so we access its .content
            return response.content
        except Exception as e:
            print(f"Error getting LLM response: {e}")
            return "I encountered an error processing your request."
        