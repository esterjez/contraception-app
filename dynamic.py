import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Connect to your SQLite DB
conn = sqlite3.connect("contraception.db")

st.title("Hormonal Contraception Use Over Time by Region")

# Query data for hormonal contraceptive method only
query = """
SELECT region, year, value_indicator_1
FROM region_data
WHERE contraceptive_method = 'hormone'
ORDER BY region, year
"""

df = pd.read_sql_query(query, conn)

# Convert year to string for plotting (optional)
df['year'] = df['year'].astype(str)

# Plot line chart
fig = px.line(df, x='year', y='value_indicator_1', color='region',
              title='Hormonal Contraception (Indicator 1) Over Time by Region',
              markers=True)

# Show plot and data table
st.plotly_chart(fig)
st.write(df)
