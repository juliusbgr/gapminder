import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.title('Gapminder')
st.write("BIPM Project - Unlocking Lifetimes: Visualizing Progress in Longevity and Poverty Eradication ")

data_path = Path(__file__).parent / "merged.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(data_path)
    return df

df = load_data()

years = sorted(df['year'].unique())
countries = sorted(df['country'].unique())

st.sidebar.header("Controls")
selected_countries = st.sidebar.multiselect(
    label="Select Countries",
    options=countries,
    default=countries[:10]
)

filtered_df = df[df['country'].isin(selected_countries)]

gni_min, gni_max = df['gniPPP'].min(), df['gniPPP'].max()

fig = px.scatter(
    filtered_df,
    x="gniPPP",
    y="lifeExp",
    size="population",
    color="country",
    hover_name="country",
    log_x=True,
    size_max=60,
    animation_frame="year",
    animation_group="country",
    range_x=[gni_min, gni_max],
    range_y=[df['lifeExp'].min(), df['lifeExp'].max()]
)

fig.update_layout(
    title="Life Expectancy vs. GNI per Capita over time",
    xaxis_title="GNI per Capita",
    yaxis_title="Life Expectancy",
    legend_title="Country"
)

st.plotly_chart(fig, use_container_width=True)
