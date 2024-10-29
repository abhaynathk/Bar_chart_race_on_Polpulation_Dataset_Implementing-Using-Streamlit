import streamlit as st
import pandas as pd
import bar_chart_race as bcr

def show_bar_race():
    # Load data
    df = pd.read_csv(r"D:\VIT\Programming for DataScience\Lab_work\APP deployment using streamlit\Hackathon\dataset\Countries Population from 1995 to 2020.csv")

     # Drop unwanted columns
    columns = ['Year', 'Country', 'Population']
    df1 = df[columns]

      # Pivot the data to create a table format suitable for bar chart race
    df2 = df1.pivot_table('Population', 'Year', 'Country')

     # Specify the path for the GIF
    bcr_gif_path = r"D:\VIT\Programming for DataScience\Lab_work\APP deployment using streamlit\Hackathon\bar_chart_race_output.gif"

    # Create the bar chart race and save it as a GIF
    bcr.bar_chart_race(df=df2, filename=bcr_gif_path, n_bars=10)



      # Streamlit app setup
    st.title("Countries Population Bar Chart Race")

    # Show the data
    st.write("Here is the data used:")
    st.write(df2.head())

     # Display the GIF in Streamlit
    st.image(bcr_gif_path, use_column_width=True)