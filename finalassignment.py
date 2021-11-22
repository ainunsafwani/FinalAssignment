import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Tourist Arrivals')
st.header('TOP 10 COUNTRIES THAT FREQUENTLY VISIT MALAYSIA (2012 - 2020)')
st.header("")
st.write(":pushpin: Open the sidebar for an overview info about this WebApp.")

### --- LOAD DATAFRAME
excel_file = 'TouristArrivals.xlsx'
sheet_name = 'TouristArrivals'

df = pd.read_excel(excel_file,
                   sheet_name = sheet_name,
                   usecols='A:C',
                   header=0)

# --- SIDEBAR

st.sidebar.title(":sparkles: Hello! Welcome :sparkles:")
st.sidebar.write("You will be able to use this WebApp to:-")
st.sidebar.write("1. Choose the range of year and the top ten countries that you want to analyse.")
st.sidebar.write("2. Compare the total number of tourist arrivals from the top ten countries that frequently visit Malaysia from 2012 till 2020.")
st.sidebar.write("")

col1, col2 = st.sidebar.columns(2)

image = Image.open('profile.png')
col1.image(image, use_column_width=True)

col2.write(':blossom: :blossom: :blossom: :blossom: :blossom: :blossom:')
col2.write('*Made with* :heart: *by*')
col2.write('[*Ainun Safwani*](https://www.linkedin.com/in/ainunsafwani/) :crescent_moon:')
col2.write(':blossom: :blossom: :blossom: :blossom: :blossom: :blossom:')

# --- STREAMLIT SELECTION & SLIDER
country = df['Country'].unique().tolist()
year = df['Year'].unique().tolist()

st.header("")
st.write(" :bulb: If you want to choose only one specific year, you can slide both of the start and end points to meet.")
year_selection = st.slider('Year:',
                          min_value=min(year),
                          max_value=max(year),
                          value=(min(year), max(year)))

st.header("")
st.write(":bulb: You can *clear all* the selections by clicking the 'x' button at the farthest right.")
country_selection = st.multiselect('Country:',
                                      country,
                                     default=country)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Year'].between(*year_selection)) & (df['Country'].isin(country_selection))
number_of_result = df[mask].shape[0]

st.header("")
st.write(":bulb: Sort the results in ascending or descending order by clicking at the chosen column's name.")
st.markdown(f'*Available Results: {number_of_result}*')
df[mask]

# --- GROUP DATAFRANE AFTER SELECTION
df_grouped = df[mask].groupby(by=['Country']).sum()[['NumArrivals']]
df_grouped = df_grouped.rename(columns={'NumArrivals': 'Total'})
df_grouped = df_grouped.reset_index()


# --- PLOT PIE CHART
pie_chart = px.pie(df_grouped,
                   title='Total Number of Tourist Arrivals',
                   values='Total',
                   names='Country')

st.plotly_chart(pie_chart)
st.write(":bulb: Click on the legend to isolate one trace.")

# --- FOOTNOTE
st.header("")
st.write(":pushpin: FOOTNOTE:-")
st.write("1. The data that was used can be found at [MyTourism Data.](http://mytourismdata.tourism.gov.my/?page_id=232)")
st.write("2. The repository of this WebApp can be found at [github.](https://github.com/ainunsafwani/FinalAssignment)")