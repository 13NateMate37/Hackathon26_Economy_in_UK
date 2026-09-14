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
group_df = df[df["country"].isin(western_europe)].copy()

st.title("Country Comparison")

st.write(
   """
   Use this page to compare selected countries across the main cost of living
   and purchashing power measures
   """
)

# Creating a year selector

selected_year = st.selectbox(
    "Select a year",
    sorted(group_df["year"].unique(),reverse=True)
)

year_df = group_df[
    group_df["year"] == selected_year
    ].copy()

selected_countries = st.multiselect(
    "Select countries to compare",
    options=western_europe,
    default=western_europe
    )

# Creating a filtered dataframe for comparison
comparison_df = year_df[
    year_df["country"].isin(selected_countries)
    ].copy()

# Protection against bad user input
if not selected_countries:
    st.warning("Please select at least one country to compare")
    st.stop()

# Metrics to compare
measure_options = {
    "Cost of Living": "cost_of_living_index",
    "Rent": "rent_index",
    "Cost of Living + Rent": "cost_of_living_plus_rent_index",
    "Groceries": "groceries_index",
    "Restaurant Prices": "restaurant_price_index",
    "Local Purchasing Power": "local_purchasing_power_index"
}

# Selection box for comparison metrics
selected_measure = st.selectbox(
    "Select a measure",
    options=list(measure_options.keys())
)

measure_column = measure_options[selected_measure]