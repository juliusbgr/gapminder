import streamlit as st
import pandas as pd
from data_preprocessing import load_and_clean_data
import plotly.express as px

@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

st.title('Gapminder')

st.write("Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication")

years = sorted(df["year"].unique())
min_year = min(years)
max_year = max(years)

# Sidebar widgets
selected_year = st.slider("Select Year", min_year, max_year, step=1)
selected_countries = st.multiselect("Select Countries", sorted(df["country"].unique()), default=sorted(df["country"].unique()))

# Filter by selected year and countries
filtered_df = df[df["year"] == selected_year]
if selected_countries:
    filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

# Drop rows with missing population (size of bubble must be valid)
filtered_df = filtered_df.dropna(subset=["population"])


# Bubble chart
fig = px.scatter(
    filtered_df,
    x="gni_per_capita",
    y="life_expectancy",
    size="population",
    color="country",
    log_x=True,
    size_max=60,
    range_x=[100, 150000],  # keep max X range constant
    title=f"Life Expectancy vs GNI per Capita - {selected_year}"
)

st.plotly_chart(fig, use_container_width=True)