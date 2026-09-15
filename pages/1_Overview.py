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

# Creating metrics for displaying
latest_year = group_df["year"].max()

latest_df = group_df[
    group_df["year"] == latest_year
].copy()

best_country = (
    latest_df
    .sort_values("affordability_rule", ascending=False)
    .iloc[0]
)

highest_cost = (
    latest_df
    .sort_values("cost_of_living_plus_rent_index", ascending=False)
    .iloc[0]
)

highest_power = (
    latest_df
    .sort_values("local_purchasing_power_index", ascending=False)
    .iloc[0]
)

st.caption(f"Latest available data: {latest_year}")

# Creating streamlit columns to display the metric 
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Strongest Affordability Balance",
        best_country["country"],
        f'{best_country["affordability_rule"]:.2f}'
    )

with col2:
    st.metric(
        "Highest Cost + Rent",
        highest_cost["country"],
        f'{highest_cost["cost_of_living_plus_rent_index"]:.1f}'
    )

with col3:
    st.metric(
        "Highest Purchasing Power",
        highest_power["country"],
        f'{highest_power["local_purchasing_power_index"]:.1f}'
    )

st.subheader(f"Affordability Ranking - {latest_year}")

ranking = (
    latest_df[
        [
            "country",
            "cost_of_living_plus_rent_index",
            "local_purchasing_power_index",
            "affordability_rule"
        ]
    ]
    .sort_values(
        "affordability_rule",
        ascending=False
    )
    .reset_index(drop=True)
)

ranking.index = ranking.index + 1

st.dataframe(ranking)