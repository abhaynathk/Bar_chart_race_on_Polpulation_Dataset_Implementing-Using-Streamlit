import streamlit as st
from home import show_home
from pyplot import show_pyplot
from bar_race import show_bar_race


st.sidebar.title("Navigation")
pages= {
    "Home": show_home,
    "Vgraphs Using Plotly Express": show_pyplot,
    "Vgraphs Using bar_chart_race": show_bar_race
}


selection =st.sidebar.radio("Go to",list(pages.keys()))

#show the selected page
pages[selection]()
