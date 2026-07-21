from dotenv import load_dotenv
import os

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
        self._initialized = True