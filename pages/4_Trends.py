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

st.title("Trends Over Time")

st.write(
    """
    Explore how living costs, rental costs, purchasing power
    and affordability have changed over time across the selected
    Western European countries.
    """
)

# Country selector
selected_countries = st.multiselect(
    "Select countries to compare",
    options=western_europe,
    default=western_europe
    )

if not selected_countries:
    st.warning("Please select at least one country to compare")
    st.stop()

# Filter
trend_df = group_df[
    group_df["country"].isin(selected_countries)
    ].copy()

# Tuple of options to compare
trend_options = {
    "Cost of Living": "cost_of_living_index",
    "Rent": "rent_index",
    "Cost of Living + Rent": "cost_of_living_plus_rent_index",
    "Local Purchasing Power": "local_purchasing_power_index",
    "Affordability Balance": "affordability_rule"
}

# Selector
selected_trend = st.selectbox(
    "Select a measure",
    options=list(trend_options.keys())
)

trend_column = trend_options[selected_trend]

# Displaying the selection
st.subheader(f"{selected_trend} Over Time")

chart_data = (
    trend_df[
        ["year", "country", trend_column]
    ]
    .pivot(
        index="year",
        columns="country",
        values=trend_column
    )
)

st.line_chart(chart_data)

st.info(
    """
    Use the country selector to compare how the selected measure
    has changed over time.

    For cost-based indices, higher values indicate higher relative
    costs.

    For Local Purchasing Power and Affordability Balance,
    higher values indicate stronger purchasing power or a stronger
    balance between purchasing power and living costs.
    """
)