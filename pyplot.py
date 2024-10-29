import streamlit as st
import pandas as pd
import plotly.express as px

def show_pyplot():
    # Load data
    df = pd.read_csv(r"D:\VIT\Programming for DataScience\Lab_work\APP deployment using streamlit\Hackathon\dataset\Countries Population from 1995 to 2020.csv")

    # Drop unwanted columns
    columns = ['Year', 'Country', 'Population']
    df1 = df[columns]

    # Ensure years are in ascending order by converting Year to string
    df1['Year'] = df1['Year'].astype(str)  # Keep Year as a string

    # Sort by Year
    df1 = df1.sort_values(by='Year')

    # Create a unique color for each country
    colors = px.colors.qualitative.Plotly  # You can choose any color set
    unique_countries = df1['Country'].unique()
    country_colors = {country: colors[i % len(colors)] for i, country in enumerate(unique_countries)}

    # Streamlit app setup
    st.title("Countries Population Bar Chart Race")

    # Show the data
    st.write("Here is the data used:")
    st.write(df1.head())

    # Create a bar chart race using Plotly
    fig = px.bar(df1, x='Population', y='Country', color='Country', 
              animation_frame='Year', range_x=[0, df['Population'].max()],
              title="Countries Population Over Years", 
              labels={'Population': 'Population', 'Country': 'Country'},
              color_discrete_sequence=[country_colors[country] for country in unique_countries])

    # Adjust the layout to make the graph larger
    fig.update_layout(width=1200, height=800, transition={'duration': 1000})  # Duration in milliseconds
 
    # Display the interactive chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    