import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
uploaded_file = 'Canada.csv'
df = pd.read_csv(uploaded_file)

# Streamlit app
st.title("Canada Data Analysis")

# Sidebar
st.sidebar.header("Filter Options")
columns = df.columns.tolist()

# Filter for columns to analyze
selected_column = st.sidebar.selectbox("Select column to visualize", columns)

# Display dataset and column details
st.write("## Dataset Preview")
st.write(df.head())

if selected_column:
    st.write(f"## Data Analysis for: {selected_column}")
    # Summary statistics for the selected column
    st.write(df[selected_column].describe())
    
    # Plot
    fig, ax = plt.subplots()
    df[selected_column].hist(ax=ax, bins=20)
    plt.xlabel(selected_column)
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {selected_column}")
    st.pyplot(fig)

# Optional feature
st.sidebar.write("Additional options coming soon!")
