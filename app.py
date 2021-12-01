import altair as alt
import pandas as pd
import numpy as np
import streamlit as st


netflix_data = pd.read_csv('netflix_titles.csv')
ratings_ages= {
    'TV-PG': 'Child(TV-PG)',
    'TV-MA': 'Adult(TV-MA)',
    'TV-Y7-FV': 'Child(TV-Y7-FV)',
    'TV-Y7': 'Child(TV-Y7)',
    'TV-14': 'Adolesent(TV-14)',
    'R': 'Adolecent(R)',
    'TV-Y': 'Infant(TV-Y)',
    'NR': 'Adult(NR)',
    'PG-13': 'Teen(PG-13)',
    'TV-G': 'Infant(TV-G)',
    'PG': 'Child(PG)',
    'G': 'Infant(G)',
    'UR': 'Adult(UR)',
    'NC-17': 'Adult(NC-17)'}
netflix_data["ratings_ages"] = netflix_data['rating'].replace(ratings_ages)
value_counts = netflix_data['ratings_ages'].value_counts()

# converting to df and assigning new names to the columns
df_value_counts = pd.DataFrame(value_counts)
df_value_counts = df_value_counts.reset_index()
df_value_counts.columns = ['rating', 'count'] # change column names

age_rating = alt.Chart(df_value_counts).mark_bar().encode(
    x='rating',
    y='count'
).properties(
    title='Sample title',
    width=600,
    height=500,
)


#Numbers data
netflix_numbers = pd.read_csv('netflix_numbers.csv')
columns = ['Revenue', 'Profit', 'Subscribers']
value_type = st.sidebar.selectbox('Parameters', columns)

attribute = ''
title = ''
chart_title = ''
if value_type == 'Revenue':
    attribute = 'revenue'
    title = 'Revenue in billions'
    chart_title = 'Revenue over years'
elif value_type == 'Profit':
    attribute = 'profit'
    title = 'Profit in Millions'
    chart_title = 'Profit over years'
elif value_type == 'Subscribers':
    attribute = 'subscribers'
    title = 'Subscribers in Millions'
    chart_title = 'Subscribers over years'
else:
    attribute = 'revenue'
    title = 'Revenue in billions'
    chart_title = 'Revenue over years'

ch = alt.Chart(netflix_numbers).mark_line(point = True).encode(
    # x = 'year:O',
    # y=value_type+":Q",
    x=alt.X('year:O', title='Year'),
    y=alt.Y(attribute+':Q', title=title)
    #color=alt.Color("symbol:N")
).properties(
    title=chart_title,
    width=600,
    height=500,
)

st.write(ch)
st.write(age_rating)