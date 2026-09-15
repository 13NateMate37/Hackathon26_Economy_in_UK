import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

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

st.title("Affordability Balance")

st.write(
    """
    This page explores the balance between local purchasing power
    and the combined cost of living and rent.

    **Affordability Rule = Local Purchasing Power Index ÷
    Cost of Living Plus Rent Index**

    A higher value represents stronger purchasing power relative
    to living costs.

    This is a comparative measure created for this project and
    is not an official affordability threshold.
    """
)

# Starting a rank filter
latest_year = group_df["year"].max()

latest_df = group_df[
    group_df["year"] == latest_year
].copy()

st.subheader(f"Affordability Balance - {latest_year}")

affordability_ranking = (
    latest_df[
        ["country", "affordability_rule"]
    ]
    .sort_values(
        "affordability_rule",
        ascending=False
    )
    .set_index("country")
)

st.bar_chart(affordability_ranking)

# Adding a plot
st.subheader("Living Costs vs Purchasing Power")

fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=latest_df,
    x="cost_of_living_plus_rent_index",
    y="local_purchasing_power_index",
    hue="country",
    s=120,
    ax=ax
)

ax.set_xlabel("Cost of Living + Rent Index")
ax.set_ylabel("Local Purchasing Power Index")
ax.set_title(f"Cost vs Purchasing Power - {latest_year}")

st.pyplot(fig)

st.info(
    """
    Countries positioned higher on the chart have stronger local
    purchasing power, while countries further to the right have
    higher combined living and rental costs.

    The affordability rule considers the relationship between
    these two measures rather than judging affordability from
    living costs alone.
    """
)