import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import calendar

# Load data
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
data.columns = data.columns.str.strip()  # Clean column names
data.rename(columns={
    'Region': 'State',
    'Date': 'Date',
    'Frequency': 'Frequency',
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labor_Participation_Rate',
    'Region.1': 'Region',
    'Longitude': 'Latitude',
    'Latitude': 'Longitude'
}, inplace=True)

# Data Preprocessing
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data['Month'] = data['Date'].dt.month
data.dropna(inplace=True)

# Streamlit App
st.title("Unemployment Rate Analysis")
st.write("This app provides insights into the unemployment rate across different states in India.")

# Sidebar for navigation
st.sidebar.title("Analysis Options")
analysis_type = st.sidebar.selectbox("Select the analysis type", ["Overview", "Unemployment Rate Histogram", "Line Plot of Unemployment Rate", 
                                                              "Box Plot by Region", "Scatter Plot Employed vs Labor Participation", 
                                                              "Monthly Average Unemployment Rate", "Correlation Heatmap", 
                                                              "Geographical Unemployment Impact", "Statewise Unemployment"])

# Show Overview
if analysis_type == "Overview":
    st.write(data.head())
    st.write(f"Dataset contains {data.shape[0]} rows and {data.shape[1]} columns.")
    st.write(f"Columns: {', '.join(data.columns)}")

# Unemployment Rate Histogram
elif analysis_type == "Unemployment Rate Histogram":
    st.write("Histogram of Unemployment Rate")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data['Unemployment_Rate'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

# Line Plot of Unemployment Rate
elif analysis_type == "Line Plot of Unemployment Rate":
    st.write("Unemployment Rate over Time")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=data, ax=ax)
    st.pyplot(fig)

# Box Plot by Region
elif analysis_type == "Box Plot by Region":
    st.write("Unemployment Rate by Region")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Region', y='Unemployment_Rate', data=data, ax=ax)
    st.pyplot(fig)

# Scatter Plot of Employed vs Labor Participation Rate
elif analysis_type == "Scatter Plot Employed vs Labor Participation":
    st.write("Employed vs Labor Participation Rate")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Employed', y='Labor_Participation_Rate', data=data, ax=ax)
    st.pyplot(fig)

# Monthly Average Unemployment Rate
elif analysis_type == "Monthly Average Unemployment Rate":
    st.write("Monthly Average Unemployment Rate")
    monthly_avg_unemployment = data.groupby('Month')['Unemployment_Rate'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=monthly_avg_unemployment.index, y=monthly_avg_unemployment.values, ax=ax)
    ax.set_xticks(np.arange(0, 12))
    ax.set_xticklabels(calendar.month_abbr[1:13], rotation=45)
    st.pyplot(fig)

# Correlation Heatmap
elif analysis_type == "Correlation Heatmap":
    st.write("Correlation Matrix Heatmap")
    numeric_columns = data.select_dtypes(include=[np.number])
    correlation_matrix = numeric_columns.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    st.pyplot(fig)

# Geographical Unemployment Impact
elif analysis_type == "Geographical Unemployment Impact":
    st.write("Geographical Representation of Unemployment Rate Impact")
    
    # Ensure columns are correct (check 'Latitude' and 'Longitude' columns directly)
    fig = px.scatter_geo(data, 
                     lat='longitude', lon='latitude', color="State",
                     hover_name="State", size="Unemployment_Rate",
                     animation_frame="Month", scope='asia',
                     title='Impact of Lockdown on Employment in India',
                     projection='natural earth',
                     color_continuous_scale='viridis',
                     size_max=30)

    # Update geographical appearance (Optional styling)
    fig.update_geos(
        showcoastlines=True, coastlinecolor="RebeccaPurple", coastlinewidth=1,
        showland=True, landcolor="LightGreen", 
        showocean=True, oceancolor="LightBlue", 
        showcountries=True, countrycolor="Black", countrywidth=1, 
        showlakes=True, lakecolor="LightBlue"
    )
    fig.update_geos(center=dict(lon=78, lat=23), projection_scale=4)

    # Display the map in Streamlit
    st.plotly_chart(fig)


# Statewise Unemployment
elif analysis_type == "Statewise Unemployment":
    st.write("Statewise Average Unemployment Rate")
    state_unemployment = data.groupby('State')['Unemployment_Rate'].mean().reset_index()
    state_unemployment_sorted = state_unemployment.sort_values(by='Unemployment_Rate', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='State', y='Unemployment_Rate', data=state_unemployment_sorted, ax=ax)
    ax.set_xticklabels(state_unemployment_sorted['State'], rotation=90)
    ax.set_xlabel('State')
    ax.set_ylabel('Average Unemployment Rate')
    ax.set_title('Average Unemployment Rate by State')
    plt.tight_layout()
    st.pyplot(fig)
