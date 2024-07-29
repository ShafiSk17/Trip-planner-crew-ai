# main.py
import streamlit as st
from crewai import Crew
from agents import agency_manager, local_travel_agent, transport_accomodation_agent
from tasks import travels_recommendations, local_places, transport_accomodation

def init_crew(from_place, to_place, travel_date):
    crew = Crew(
        agents=[agency_manager, local_travel_agent, transport_accomodation_agent],
        tasks=[
            travels_recommendations(agency_manager, from_place, to_place, travel_date),
            local_places(local_travel_agent, to_place, travel_date),
            transport_accomodation(transport_accomodation_agent, from_place, to_place, travel_date)
        ]
    )
    return crew

# Streamlit UI components
st.title("Trip Planner App")

api_key= st.text_input("Enter Your Api key")
from_place = st.text_input("Enter the starting location (From):")
to_place = st.text_input("Enter the destination location (To):")
travel_date = st.date_input("Enter the date of journey:")



# Button to initiate the trip planning process
if st.button("Plan My Trip"):
    if from_place and to_place and travel_date:
        # Initialize the crew and get the results
        crew = init_crew(from_place, to_place, travel_date)
        st.success("Trip planned successfully!")
        # Display results (assuming `crew` has a method to summarize or display results)
        # This might need to be adapted based on how `crew` is expected to provide output
        st.write(crew)
    else:
        st.error("Please fill in all the details.")
