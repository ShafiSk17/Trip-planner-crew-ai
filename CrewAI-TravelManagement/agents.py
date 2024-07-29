from crewai import Agent
import os
from tools.search_tools import SearchTools
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
import openai
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chat_models import ChatOpenAI
import streamlit as st
from main import api_key


api_key = api_key




openai_llm = ChatOpenAI(openai_api_key=api_key,  # Use the correct parameter name
        model="gpt-4o-mini",  # model name
        temperature=0.2,  # controls the randomness of predictions
        max_tokens=1500,)

search_tools = DuckDuckGoSearchRun()

# travel agency manager
agency_manager = Agent(
    role='Travel Agency Manager',
    goal='To greet customers, and manage the customers travel requirements',
    verbose=True,
    backstory="A manager in a reputed travel agency, which helps users to recommend and resolve all the requirements of users",
    llm=openai_llm,
    tools=[
        DuckDuckGoSearchRun()
    ]
)

# local agent
local_travel_agent = Agent(
    role='Local Tourist Guide',
    goal='To make travellers visit all the local tourist spots based on day itenary',
    verbose=True,
    backstory="A famous local tourist guide who can speak multiple languages and have very good idea about all the tourist spots and also the history about the spots",
    llm=openai_llm,
    tools=[
        DuckDuckGoSearchRun()
    ]
)

# transport and accomodation agent
transport_accomodation_agent = Agent(
    role='Transport & Accomodation Travel Agent',
    goal='to provide travel recommendations based on weather, and accomodation details',
    verbose=True,
    backstory="You've all details about travel options, accomodation options for user requirements which are not too expensive",
    llm=openai_llm,
    tools=[
        DuckDuckGoSearchRun()
    ]
)

