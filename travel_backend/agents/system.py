from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

class System:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        
        load_dotenv()
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("MODEL_NAME")
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        self.serpapi_api_key = os.getenv("SERPAPI_API_KEY")
        self.llm = ChatOpenAI(
            model=self.model_name,
            # stream_usage=True,
            temperature=0.2,
            # max_tokens=None,
            # timeout=None,
            # reasoning_effort="low",
            # max_retries=2,
            # api_key="...",  # If you prefer to pass api key in directly
            # base_url="...",
            # organization="...",
            # other params...
        )
        self._initialized = True