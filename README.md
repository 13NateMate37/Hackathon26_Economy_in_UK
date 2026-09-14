# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# You Wanna Live Where?

## Code Institute Data Analytics & AI Hackathon – Team 3

**Project:** You Wanna Live Where?  
**Team:** Hackathon Group 3  
**Region:** Western Europe  
**Focus:** Cost of Living, Rent, Purchasing Power and Affordability

**GitHub Repository:**  
https://github.com/Oliver-code26/Hackathon_Where_You_Wanna_Live

---

## Project Overview

**You Wanna Live Where?** is a Data Analytics & AI Hackathon project exploring the cost of living across countries in Western Europe.

The project uses historical cost-of-living data from **2018 to 2026** to investigate how different countries compare in terms of:

- Cost of living
- Rent
- Cost of living plus rent
- Groceries
- Restaurant prices
- Local purchasing power
- A project-defined affordability measure

The purpose of the project is to use data analysis and visualisation to help users compare countries and understand where living may be relatively more affordable based on the selected indicators.

The analysis is intended as a **comparative data analysis project** rather than financial, economic or relocation advice.

---

## Project Objectives

The main objectives of the project are to:

1. Investigate cost-of-living differences across selected Western European countries.
2. Compare countries using consistent cost-of-living indicators.
3. Analyse rent and combined living costs.
4. Examine local purchasing power.
5. Explore the relationship between living costs and purchasing power.
6. Create a project-defined affordability measure for comparison.
7. Present the findings through clear data visualisations.
8. Contribute country-level analysis towards the wider Western Europe analysis.
9. Use the findings to support the final Streamlit dashboard and project conclusions.

---

## Dataset

The project uses the following Kaggle dataset:

**Global Cost of Living Index by Country (2018–2026)**

Dataset source:

https://www.kaggle.com/datasets/naifnoor/global-cost-of-living-index-by-country-20182026

The dataset contains country-level cost-of-living indicators covering the period from 2018 to 2026.

Key variables used in the analysis include:

- `country`
- `cost_of_living_index`
- `rent_index`
- `cost_of_living_plus_rent_index`
- `groceries_index`
- `restaurant_price_index`
- `local_purchasing_power_index`

---

## Data Preparation and ETL

Before conducting country-level exploratory data analysis, the dataset was inspected and prepared as part of the team's data preparation process.

### Nathan's Data Preparation / ETL Contribution

**Contributor: Nathan (`13NateMate37`)**

Nathan worked on the dataset preparation and ETL process.

His work included:

- Loading the raw cost-of-living dataset.
- Performing an initial inspection of the data.
- Checking the dataset structure and contents.
- Checking for missing values.
- Checking data types.
- Confirming that no missing-value or data-type corrections were required.
- Checking country counts within the dataset.
- Preparing a verified version of the dataset.
- Exporting the verified dataset without adding an unnecessary pandas index.
- Working with the project's helper functions through `HelperFuncs.py`.

The verified dataset is stored as:

`Dataset/Verified/cost_of_living_verified.csv`

The raw dataset is stored as:

`Dataset/Raw/cost_of_living.csv`

This preparation provided a consistent dataset for the team's subsequent exploratory data analysis.

---

## Exploratory Data Analysis

The team divided the Western Europe analysis between members so that different countries could be investigated using a consistent methodology.

The EDA focused on:

- Descriptive statistics
- Country-level comparisons
- Cost of living
- Rent
- Cost of living plus rent
- Groceries
- Restaurant prices
- Local purchasing power
- Trends across the available years
- Relationships between living costs and purchasing power
- The project-defined affordability measure

The same general analytical approach was used across the assigned countries to make the results easier to compare.

---

## Nathan's Exploratory Data Analysis

**Contributor: Nathan (`13NateMate37`)**

Nathan's EDA focused on:

- **Austria**
- **Belgium**
- **Ireland**

His analysis followed the team's agreed EDA methodology.

### Nathan's analysis included:

- Filtering the verified dataset by country.
- Examining descriptive statistics.
- Using `groupby` and summary statistics to understand country-level patterns.
- Analysing cost-of-living trends.
- Analysing rent trends.
- Analysing local purchasing power.
- Comparing cost of living plus rent with local purchasing power.
- Using visualisations to identify trends and differences.
- Using scatter analysis to explore the relationship between combined living costs and purchasing power.
- Applying the project-defined affordability rule.
- Drawing conclusions from the results for Austria, Belgium and Ireland.

**Nathan's EDA / project work:**  
https://github.com/Oliver-code26/Hackathon_Where_You_Wanna_Live/blob/Nate_EDA/jupyter_notebooks/Nate_EDA.ipynb

---
## Oliver's Exploratory Data Analysis

**Contributor: Oliver Hodierne (`Oliver-code26`)**

Oliver's EDA focused on:

- **Switzerland**
- **Netherlands**
- **Luxembourg**

### Oliver's analysis included:

- Descriptive Comparisons
- Regional Statistics
- Ethical Consideration
- Time Analysis
- Predictive Analysis
- Critical Thinking for results in given time. (Continents = weeks, Countries = days)
- Set clear agenda

### Oliver's EDA Notebook
**OH_Notebook.ipynb**

https://github.com/Oliver-code26/Hackathon_Where_You_Wanna_Live/blob/oh_notebook/jupyter_notebooks/OH_Notebook.ipynb


**Oliver's Tableau Dashboard**

https://public.tableau.com/views/HackathonProjectCostofLivinginEurope/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## Areeba's Exploratory Data Analysis

**Contributor: Areeba Ashraf (`Areeba89023`)**

Areeba's EDA focused on:

- **France**
- **Germany**
- **United Kingdom**

### Areeba's analysis included:

- Descriptive statistics.
- Country-level comparisons.
- Cost of Living Index analysis.
- Rent Index analysis.
- Cost of Living Plus Rent Index analysis.
- Groceries Index analysis.
- Restaurant Price Index analysis.
- Local Purchasing Power Index analysis.
- Visual analysis.
- Affordability Rule calculations.
- Country-level conclusions.

### Areeba's EDA Notebook

**Areeba_EDA.ipynb:**  
https://github.com/Oliver-code26/Hackathon_Where_You_Wanna_Live/blob/main/Areeba_EDA.ipynb

---

## Areeba's Key Findings

The analysis compared France, Germany and the United Kingdom across the selected cost-of-living indicators.

| Country | Avg. Cost of Living | Avg. Rent | Avg. Cost of Living + Rent | Avg. Purchasing Power |
|---|---:|---:|---:|---:|
| France | 72.00 | 24.66 | 49.72 | 92.31 |
| Germany | 66.23 | 26.62 | 47.60 | 112.71 |
| United Kingdom | 66.81 | 31.23 | 50.09 | 100.98 |

### France

France had the highest average Cost of Living Index of the three countries at **72.00**.

It also had the lowest average Local Purchasing Power Index at **92.31**.

However, France had the lowest average Rent Index at **24.66**.

### Germany

Germany had the lowest average Cost of Living Index at **66.23**.

It also had the lowest average Cost of Living Plus Rent Index at **47.60**.

Germany had the highest average Local Purchasing Power Index at **112.71**.

### United Kingdom

The United Kingdom had an average Cost of Living Index of **66.81**.

It had the highest average Rent Index at **31.23** and the highest average Cost of Living Plus Rent Index at **50.09**.

Its average Local Purchasing Power Index was **100.98**, higher than France but lower than Germany.

---

## Affordability Rule

The team used a project-defined comparative affordability measure:

`local_purchasing_power_index / cost_of_living_plus_rent_index`

This measure compares local purchasing power with the combined cost of living and rent.

A higher value indicates a stronger relationship between purchasing power and the combined cost measure **within this project-defined comparison**.

For France, Germany and the United Kingdom, the average results were:

| Country | Mean Affordability Score |
|---|---:|
| Germany | 2.38 |
| United Kingdom | 2.02 |
| France | 1.89 |

Based on this project-defined measure:

1. **Germany** performed strongest.
2. **United Kingdom** ranked second.
3. **France** ranked third.

### Important qualification

The Affordability Rule is a **project-defined comparative measure** created for this analysis.

It is **not an official affordability threshold, economic standard or financial recommendation.**

---

## Overall Findings

Germany performed strongest among France, Germany and the United Kingdom under the project's selected indicators.

Germany combined:

- The lowest average Cost of Living Index.
- The lowest average Cost of Living Plus Rent Index.
- The highest average Local Purchasing Power Index.
- The highest average project-defined Affordability Score.

The United Kingdom had stronger purchasing power than France but also had the highest average rent and highest average combined Cost of Living Plus Rent Index.

France had the highest average Cost of Living Index and the lowest Local Purchasing Power Index of the three countries, although it had the lowest average Rent Index.

These findings are based on the selected dataset and indicators and should therefore be interpreted within the scope of the project.

---

## Technologies and Tools

The project uses Python-based data analysis and visualisation tools.

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Visualisation

- Matplotlib
- Seaborn

### Development / Notebook Environment

- Jupyter Notebook
- Google Colab

### Dashboard

- Streamlit

### Version Control

- Git
- GitHub
