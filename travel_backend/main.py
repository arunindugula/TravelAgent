from agents import travelagent
from agents.travelagent import TravelAgent
from agents.itinerary_research_agent import ItineraryResearchAgent
from agents.flight_hotel_seach_agent import FlightHotelSearchAgent

def main():
    print("Hello from travel-backend!")
    travelagent = TravelAgent()
    itinerary_agent = ItineraryResearchAgent()
    flight_hotel_search_agent = FlightHotelSearchAgent()
    """
    result = itinerary_agent.itinerary_search_agent.invoke(
        {"messages": [
            {
                "role": "user", 
                "content": "Plan a 5 day travel iternerary for a food & hstorical sites lover during winter in Delhi"
            }
        ]})
    """
    """
    result = flight_hotel_search_agent.search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Find me flight, returning on August 22, 2026 from New York to London on August 18, 2026 for 1 adults only"
            }
        ]
    })
    """
    result = flight_hotel_search_agent.search_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Find me hotels on August 20, 2026 in New York for 1 adults only for 2 nights"
            }
        ]
    })
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()
