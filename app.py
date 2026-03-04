import streamlit as st 
import pandas as pd 
import plotly.express as px 

# Load Excel file
rfm = pd.read_excel("category_summary.xlsx") 

st.title("Superstore RFM Dashboard")
st.dataframe(rfm)
fig_pie = px.pie(rfm, 
                 names='Segment', 
                 values='Customer_Count', 
                 title='Customer Count per Cluster')
st.plotly_chart(fig_pie)

import plotly.express as px

fig_scatter = px.scatter(
    rfm,
    x='Recency_Mean',      
    y='Monetary_Mean',      
    size='Frequency_Mean',  
    color='Segment',
    hover_data=['Recency_Mean', 'Frequency_Mean', 'Monetary_Mean']
)

st.plotly_chart(fig_scatter)




##open terminal and run the following command to start the Streamlit app:
# pip install streamlit 
# pip install plotly
#venv\Scripts\activate (create venv and activate it if you haven't already)
# streamlit run "app.py"(the terminal should be in the same directory as app.py)
#install streamlit and plotly if you haven't already:

