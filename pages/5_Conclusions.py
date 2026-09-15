import streamlit as st

from HelperFuncs import loadDataframe
df = loadDataframe()

st.title("Conclusions")

st.write(
    """
    This project explored affordability across selected Western
    European countries by comparing living costs with local
    purchasing power.

    The analysis shows that affordability cannot be judged from
    cost alone. A country may have higher living costs but still
    offer a stronger overall balance if local purchasing power is
    also high.
    """
)

st.subheader("Key Findings")

st.markdown(
    """
    - Rental costs are an important factor in overall affordability,
      particularly in countries where rent is substantially higher.

    - Local purchasing power varies considerably between countries
      and helps explain why the cheapest country is not always the
      most affordable.

    - The project-defined affordability rule provides a simple way
      to compare purchasing power against combined living and rental
      costs.

    - Affordability changes over time, so looking at a single year
      does not provide the full picture.
    """
)

st.subheader("Limitations")

st.write(
    """
    The dataset uses country-level indices, so the results represent
    broad national comparisons rather than individual household
    circumstances.

    Actual affordability will vary depending on factors such as
    salary, location within a country, household size and personal
    spending habits.

    The affordability rule used in this project is a comparative
    measure developed by the project team and should not be treated
    as an official affordability score or threshold.
    """
)

st.subheader("Overall Conclusion")

st.success(
    """
    When deciding where offers the strongest affordability balance,
    both living costs and local purchasing power should be considered
    together.

    The dashboard therefore supports comparison rather than simply
    identifying the lowest-cost country.
    """
)

