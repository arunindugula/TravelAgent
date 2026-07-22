from langchain_openai import ChatOpenAI
from agents.system import System

class TravelAgent: 
    def __init__(self):
        system = System()
        