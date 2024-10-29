import streamlit as st
def show_home():
    st.title("Welcome to My APP for Vgraphs")
    st.write("This is a app which shows Vgraphs (Interactive Race Chart of World Population)")
    

    logo_path2 = "C:\\Users\\Abhay\\Downloads\\racechart-removebg-preview.png"
 

    # Display the image
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the proportions as needed

    # Use the middle column to display the image
    with col1:
        st.image(logo_path2, use_column_width=False, width=800) 
