from agents import travelagent
from agents.travelagent import TravelAgent
from agents.itinerary_research_agent import ItineraryResearchAgent

def main():
    print("Hello from travel-backend!")
    travelagent = TravelAgent()
    itinerary_agent = ItineraryResearchAgent()
    result = itinerary_agent.itinerary_search_agent.invoke(
        {"messages": [
            {
                "role": "user", 
                "content": "Plan a 5 day travel iternerary for a food & hstorical sites lover during winter in Delhi"
            }
        ]})
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()
