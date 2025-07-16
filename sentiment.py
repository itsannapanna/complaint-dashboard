import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('cleaned_complaints.csv')
df['Date received'] = pd.to_datetime(df['Date received'])
print(df.head())  # Check if the last few columns include 'sentiment'


# Sidebar Filters
products = st.sidebar.multiselect('Select Products:', df['Product'].unique(), default=df['Product'].unique())
issues = st.sidebar.multiselect('Select Issues:', df['Issue'].unique(), default=df['Issue'].unique())
sentiments = st.sidebar.multiselect('Select Sentiment:', df['sentiment'].unique(), default=df['sentiment'].unique())

filtered_df = df[
    df['Product'].isin(products) &
    df['Issue'].isin(issues) &
    df['sentiment'].isin(sentiments)
]

# Title
st.title("Complaint Intelligence Dashboard")

# Time Trend
monthly = filtered_df.set_index('Date received').resample('M').size()
st.subheader("Complaint Volume Over Time")
st.line_chart(monthly)

# Product Breakdown
st.subheader("Complaints by Product")
st.bar_chart(filtered_df['Product'].value_counts())

# Sentiment Breakdown
st.subheader("Sentiment Distribution")
st.bar_chart(filtered_df['sentiment'].value_counts())

# KPIs
total = len(filtered_df)
timely = (filtered_df['Timely response?'] == 'Yes').sum()
disputed = (filtered_df['Consumer disputed?'] == 'Yes').sum()

st.metric("Total Complaints", total)
st.metric("% Timely Response", f"{timely / total * 100:.2f}%")
st.metric("% Disputed", f"{disputed / total * 100:.2f}%")
