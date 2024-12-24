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

    # Behind the Scenes page
    elif selection == "Behind the Scenes":
        st.title("Behind the Scenes")
        st.write("This section explains how the recommendation system works.")
        # Add more content here as needed.

# Required to let Streamlit instantiate our web app
if __name__ == "__main__":
    main()
