"""
A Streamlit web application for generating user ratings and managing bookings.
"""

# Import dependencies
import os
import re
import string
import time
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st
import urllib.parse
from PIL import Image

# Function to read markdown files
def read_markdown(file_path):
    """Reads a markdown file and returns its content."""
    return Path(file_path).read_text()

# Main function to build the app
def main():
    """Main function to run the Streamlit app."""

    # Sidebar with logo and navigation
    st.sidebar.title("Navigation")
    image_maps = Image.open("images/Maps.png")
    st.sidebar.image(image_maps)

    options = [
        "About",
        "Predict Your Cost",
        "Booking Page",
        "Behind the Scenes",
    ]

    selection = st.sidebar.radio("Navigate To", options)

    # About page
    if selection == "About":
        st.image(
            "https://blog.playstation.com/tachyon/2016/10/unnamed-file-6.jpg",
            use_column_width=True,
        )
        about_markdown = read_markdown("markdown/about.md")
        st.markdown(about_markdown, unsafe_allow_html=True)

        # Footer
        footer_html = """
        <div style='text-align: center;'>
        <p>Developed by Amos Maponya | Contact us at: amosphashe@gmail.com</p>
        </div>
        """
        st.markdown("#")
        st.divider()
        st.markdown(footer_html, unsafe_allow_html=True)
        st.image(image_maps)
        
    # Predict Your Cost page
    if selection == "Predict Your Cost":
        st.title("Predict Your Cost")

        # Input form for items and services
        st.write("Enter the quantities for each item/service:")
        blanket_count = st.number_input("How many blankets?", min_value=0, value=0)
        carpet_count = st.number_input("How many carpets?", min_value=0, value=0)
        wash_count = st.number_input("How many washes?", min_value=0, value=0)
        dry_count = st.number_input("How many dry items?", min_value=0, value=0)
        sneakers_count = st.number_input("How many sneakers?", min_value=0, value=0)
        crocs_count = st.number_input("How many crocs/slides?", min_value=0, value=0)
        
        # Detergent selection
        soap_count = st.number_input("How many soaps?", min_value=0, value=0)
        stasoft_count = st.number_input("How many Stasoft?", min_value=0, value=0)
        
        # Transport selection
        transport_options = {
            "Local (Return)": 30,
            "Hospital (Return)": 30,
            "Pakedi (Return)": 60,
        }
        selected_transport = st.selectbox("Select transport option:", options=transport_options.keys())
        transport_cost = transport_options[selected_transport]

        # Cost calculation
        total_cost = (
            blanket_count * 50 +
            carpet_count * 45 +
            wash_count * 25 +
            dry_count * 25 +
            sneakers_count * 50 +
            crocs_count * 20 +
            soap_count * 5 +
            stasoft_count * 5 +
            transport_cost
        )

        # Display the result
        st.subheader(f"Total Predicted Cost: R {total_cost}")


    # Behind the Scenes page
    if selection == "Behind the Scenes":
        st.title("Behind the Scenes")
        st.write("This section explains how the recommendation system works.")
        # Add more content here as needed.

# Required to let Streamlit instantiate our web app
if __name__ == "__main__":
    main()
