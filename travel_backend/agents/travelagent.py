from langchain_openai import ChatOpenAI
from agents.system import System

class TravelAgent: 
    def __init__(self):
        system = System()
        self.llm = ChatOpenAI(
            model=system.model_name,
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