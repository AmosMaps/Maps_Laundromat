import streamlit as st
import urllib.parse
from datetime import datetime
import folium
from folium.plugins import MarkerCluster
import streamlit.components.v1 as components

# Sidebar Navigation
st.sidebar.title("Map's Laundromat")
st.sidebar.image("images/Maps.png")
menu_options = ["About", "Predict Your Cost", "Booking Page", "Directions"]
selected_page = st.sidebar.radio("Navigate To", menu_options)

# About Page
if selected_page == "About":
    st.markdown("# <span style='color:#EF5454'>Map's Laundromat</span>", unsafe_allow_html=True)
    st.markdown("""
    ---
    
    ### <span style="color:DarkSlateBlue">Introduction</span>
    Welcome to **Map's Laundromat**, where we provide fast, reliable, and affordable same-day laundry services in Turfloop. 
    From everyday garments to delicate fabrics, we make laundry day a breeze!
    
    ---
    
    ### <span style="color:DarkSlateBlue">App Features</span>
    Our app offers a seamless and user-friendly experience by providing:
    * **Cost Prediction**: Get an estimate of your total cost before scheduling your appointment.
    * **Convenient Booking**: Choose a time that suits you best to drop off or collect your laundry.
    
    ---
    
    ### <span style="color:DarkSlateBlue">How It Works</span>
    Getting started is simple!  
    1. Use the navigation menu on the sidebar to explore our features.
    2. Visit the *About* page to learn more about us or head to *Predict Your Cost* to calculate your laundry expenses.  
    3. Book your appointment directly through the app and enjoy stress-free laundry service.
    """, unsafe_allow_html=True)

# Predict Your Cost Page
if selected_page == "Predict Your Cost":
    st.title("Predict Your Cost")
    st.write("Estimate your laundry cost by entering the quantities of the items you'd like washed.")

    # Inputs for cost prediction
    blanket = st.number_input("Blankets", min_value=0, value=0) * 50
    carpet = st.number_input("Carpets", min_value=0, value=0) * 45
    wash = st.number_input("Washes", min_value=0, value=0) * 25
    dry = st.number_input("Dries", min_value=0, value=0) * 25
    soap = st.number_input("Soap", min_value=0, value=0) * 5
    stasoft = st.number_input("Sta-Soft", min_value=0, value=0) * 5
    sneakers = st.number_input("Sneakers", min_value=0, value=0) * 50
    crocs_slides = st.number_input("Crocs/Slides", min_value=0, value=0) * 20

    # Transport selection
    transport_options = {
        "Drop-off & pickup": 0,
        "Local (Return)": 30,
        "Hospital (Return)": 30,
        "Pakedi (Return)": 60
    }
    transport = st.selectbox("Select Transport Option", options=list(transport_options.keys()))
    transport_cost = transport_options[transport]

    # Calculate total cost
    total_cost = blanket + carpet + wash + dry + soap + stasoft + sneakers + crocs_slides + transport_cost
    st.subheader(f"Your Estimated Cost: R {total_cost}")

# Booking Page
if selected_page == "Booking Page":
    st.title("Booking Page")
    with st.form("booking_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        booking_date = st.date_input("Booking Date", value=datetime.today())
        booking_time = st.time_input("Booking Time")
        message = st.text_area("Additional Message")

        submitted = st.form_submit_button("Submit Booking")

        if submitted:
            # Generate WhatsApp link
            whatsapp_message = (
                f"Name: {name}\nEmail: {email}\nPhone: {phone}\n"
                f"Date: {booking_date}\nTime: {booking_time}\nMessage: {message}"
            )
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_link = f"https://wa.me/27828492746?text={encoded_message}"
            
            st.success("Booking submitted! Your details have been sent to WhatsApp.")
            st.markdown(f"<meta http-equiv='refresh' content='0; url={whatsapp_link}'>", unsafe_allow_html=True)

# Directions Page
if selected_page == "Directions":
    st.title("Get Directions")
    st.write("Get directions to our laundromat with a satellite view on the map.")

    # Coordinates of the laundromat location (example coordinates for Turfloop)
    laundromat_location = [-23.875124, 29.743984]  

    # Create a map with a satellite view
    m = folium.Map(location=laundromat_location, zoom_start=16, control_scale=True, tiles='Stamen Terrain')
    folium.Marker(laundromat_location, popup="Map's Laundromat").add_to(m)

    # Display map in Streamlit
    components.html(m._repr_html_(), height=500)
