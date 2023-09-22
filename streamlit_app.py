import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("Fish.csv")
  
# Group by species and calculate mean
group_mean = df.groupby('Species').mean()

# Display the bar chart using Streamlit
st.bar_chart(group_mean['Weight'])

# Customize the chart's appearance
st.title("The average weight for each species")
plt.xlabel('Species')
plt.ylabel('Average weight')

