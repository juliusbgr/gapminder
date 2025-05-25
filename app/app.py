import streamlit as st
import pandas as pd
import plotly.express as px
import time
from data_preprocessing import load_and_clean_data

@st.cache_data
def get_data():
    return load_and_clean_data()

df = get_data()

st.title('Gapminder')
st.write("BIPM Project - Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication ")

years = sorted(df["year"].unique())
min_year, max_year = min(years), max(years)

if "year_slider" not in st.session_state:
    st.session_state.year_slider = min_year
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False

st.sidebar.subheader("Controls")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(df["country"].unique()),
    default=sorted(df["country"].unique())
)

if st.sidebar.button("▶ Play"):
    st.session_state.is_playing = True
if st.sidebar.button("⏹ Stop"):
    st.session_state.is_playing = False

year = st.slider(
    "Select Year",
    min_value=min_year,
    max_value=max_year,
    value=st.session_state.year_slider,
    step=1,
    key="year_slider"
)

if st.session_state.is_playing:
    next_year_idx = years.index(st.session_state.year_slider) + 1
    if next_year_idx < len(years):
        st.session_state.year_slider = years[next_year_idx]
        time.sleep(0.2)
        st.experimental_rerun()
    else:
        st.session_state.is_playing = False 

filtered_df = df[df["year"] == st.session_state.year_slider]
if selected_countries:
    filtered_df = filtered_df[filtered_df["country"].isin(selected_countries)]

filtered_df = filtered_df.dropna(subset=["population", "gni_per_capita", "life_expectancy"])

fig = px.scatter(
    filtered_df,
    x="gni_per_capita",
    y="life_expectancy",
    size="population",
    color="country",
    log_x=True,
    size_max=60,
    range_x=[100, 150000],
    title=f"Life Expectancy vs GNI per Capita - {st.session_state.year_slider}"
)

st.plotly_chart(fig, use_container_width=True)
