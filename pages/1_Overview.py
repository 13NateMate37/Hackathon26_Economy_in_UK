import streamlit as st
import pandas as pd 

from HelperFuncs import loadDataframe

# Load the verified csv

df = loadDataframe()

# Group just the countries in Western Europe
western_europe = [
    "Austria",
    "Belgium",
    "France",
    "Germany",
    "Ireland",
    "Luxembourg",
    "Netherlands",
    "Switzerland",
    "United Kingdom"
]

# Isolating a copy of the dataframe
group_df = df[df["country"].isin(western_europe)].copy

st.title("Western Europe Affordability Overview")

st.write(
    """
    This dashaboard currently comapares the countries of Western Europe, to explore the balance between
    living costs and local purchasing power.
     
    Rather than just working to identify where is the least expensive country to live, our analysis considers
    if the local purchasing power is strong against the living cost. 
    """
)

st.subheader("How is affordability measured?")

st.write(
    """
    The project uses a simple comparative measure:

    **Affordability Rule = Local Purchasing Power Index ÷
    Cost of Living Plus Rent Index**

    A higher value suggests stronger purchasing power relative
    to combined living and rental costs.

    This is a project-defined comparison tool and should not be
    interpreted as an official affordability threshold.
    """
)
