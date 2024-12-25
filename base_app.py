import streamlit as st
import urllib.parse
from datetime import datetime, time
import folium
from folium.plugins import MarkerCluster
import streamlit.components.v1 as components

# Sidebar Navigation
st.sidebar.title("Map's Laundromat")
st.sidebar.image("images/Maps_no_bg.png", use_column_width=True)
menu_options = ["About", "Predict Your Cost", "Booking Page", "Directions"]
selected_page = st.sidebar.radio("Navigate To", menu_options)

# Store booking count
if "booking_count" not in st.session_state:
    st.session_state.booking_count = {}

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
    - **Cost Prediction**: Get an estimate of your total cost before scheduling your appointment.
    - **Convenient Booking**: Choose a time that suits you best to drop off or collect your laundry.
    
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
    sneakers = st.number_input("Sneakers", min_value=0, value=0) * 50
    crocs_slides = st.number_input("Crocs/Slides", min_value=0, value=0) * 20
    wash = st.number_input("Washes", min_value=0, value=0) * 25
    dry = st.number_input("Dries", min_value=0, value=0) * 25
    soap = st.number_input("Soap", min_value=0, value=0) * 5
    stasoft = st.number_input("Sta-Soft", min_value=0, value=0) * 5
    plastic = st.number_input("Plastic", min_value=0, value=0) * 7

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
    total_cost = blanket + carpet + wash + dry + soap + stasoft + sneakers + crocs_slides + transport_cost + plastic
    st.subheader(f"Your Estimated Cost: R {total_cost}")

# Booking Page
if selected_page == "Booking Page":
    st.title("Booking Page")

    # Initialize session state for booking counts
    if "booking_count" not in st.session_state:
        st.session_state.booking_count = {}

    # Get today's date
    today = datetime.today().date()

    # Ensure booking count for today is initialized
    if today not in st.session_state.booking_count:
        st.session_state.booking_count[today] = 0

    # Check if the maximum bookings for today have been reached
    if st.session_state.booking_count[today] >= 10:
        st.warning("We have reached the maximum number of bookings for today. Please choose another date.")
    else:
        with st.form("booking_form"):
            # Booking form inputs
            name = st.text_input("Name", key="name")
            email = st.text_input("Email", key="email")
            phone = st.text_input("Phone Number", key="phone")
            booking_date = st.date_input("Booking Date", value=today, key="booking_date")
            
            # Allowed times for booking (06:00 to 13:00, every 30 minutes)
            allowed_times = [
                time(hour, minute)
                for hour in range(6, 14)  # 6:00 to 13:00
                for minute in (0, 30)
            ]
            booking_time = st.selectbox("Booking Time", options=allowed_times, key="booking_time")

            # Additional message field
            message = st.text_area("Additional Message", key="message")
            submitted = st.form_submit_button("Submit Booking")

            if submitted:
                # Increment booking count for the selected date
                if booking_date not in st.session_state.booking_count:
                    st.session_state.booking_count[booking_date] = 0
                st.session_state.booking_count[booking_date] += 1

                # Generate WhatsApp message and link
                whatsapp_message = (
                    f"Name: {name}\nEmail: {email}\nPhone: {phone}\n"
                    f"Date: {booking_date}\nTime: {booking_time}\nMessage: {message}"
                )
                encoded_message = urllib.parse.quote(whatsapp_message)
                whatsapp_link = f"https://wa.me/27828492746?text={encoded_message}"

                st.success("Booking submitted! Your details have been sent to WhatsApp.")
                st.markdown(f"[Click here to confirm on WhatsApp]({whatsapp_link})")

    # Display the number of remaining bookings for today
    remaining_bookings = max(0, 10 - st.session_state.booking_count[today])
    st.info(f"Remaining bookings for today: {remaining_bookings}")


# Directions Page
if selected_page == "Directions":
    st.title("Get Directions")
    st.write("Get directions to our laundromat with a map showing roads and houses.")

    # Coordinates of the laundromat location
    laundromat_location = [-23.875124, 29.743984]

    # Create a map with OpenStreetMap tiles
    m = folium.Map(
        location=laundromat_location,
        zoom_start=16,
        control_scale=True,
        tiles='OpenStreetMap',
        attr="Map data © OpenStreetMap contributors"
    )

    # Add a marker for the laundromat
    folium.Marker(laundromat_location, popup="Map's Laundromat").add_to(m)

    # Display map in Streamlit
    components.html(m._repr_html_(), height=500)

    # Google Maps directions button
    google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={laundromat_location[0]},{laundromat_location[1]}"
    if st.button("Get Directions"):
        st.markdown(f"[Click here to open directions in Google Maps]({google_maps_url})", unsafe_allow_html=True)
