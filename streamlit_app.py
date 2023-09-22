import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
df = pd.read_csv("Fish.csv")

# Create a scatter plot
plt.scatter(df['Weight'], df['Height'])

# Set labels and title
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Scatter Plot: Weight vs. Height')

# Display the plot in Streamlit
st.pyplot()









