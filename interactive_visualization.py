import streamlit as st
import plotly.express as px
import pandas as pd

# Sample Data
data = px.data.gapminder().query("year == 2007")

# Streamlit App
st.title("Interactive World GDP Visualization (2007)")

# Dropdown for selecting continents
continents = data['continent'].unique()
selected_continent = st.selectbox("Select Continent", ['All'] + list(continents))

# Filter data based on selection
if selected_continent != 'All':
    filtered_data = data[data['continent'] == selected_continent]
else:
    filtered_data = data

# Plot
fig = px.scatter(
    filtered_data, 
    x='gdpPercap', 
    y='lifeExp', 
    size='pop', 
    color='continent', 
    hover_name='country', 
    log_x=True, 
    size_max=60,
    title=f'GDP vs Life Expectancy in {selected_continent if selected_continent != "All" else "All Continents"} (2007)'
)

st.plotly_chart(fig)

# Instructions
st.markdown("Select a continent to filter the data. Hover over the bubbles for country details.")
