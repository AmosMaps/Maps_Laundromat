import streamlit as st
import urllib.parse
from datetime import datetime, time, timedelta
import folium
import streamlit.components.v1 as components

# Sidebar Navigation
st.sidebar.image("images/Maps_no_bg.png", use_column_width=True)
menu_options = ["About", "Predict Your Cost", "Booking Page", "Directions"]
selected_page = st.sidebar.radio("Navigate To", menu_options)

# Reusable function to add footer
def add_footer():
    footer_html = """
    <div style='text-align: center;'>
        <p>Developed by Map's Holdings | Contact us at: amosphashe@gmail.com</p>
    </div>
    """
    st.markdown("#")
    st.divider()
    st.markdown(footer_html, unsafe_allow_html=True)

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
    - **Cost Prediction**: Get an estimate of your total cost before scheduling your appointment.
    - **Convenient Booking**: Choose a time that suits you best to drop off or collect your laundry.
    - **Directions**: Find detailed directions to our laundromat with maps and landmarks.
    
    ---
    ### <span style="color:DarkSlateBlue">Learn More</span>
    Use the navigation menu on the sidebar to explore our features and enjoy a stress-free laundry experience.
    """, unsafe_allow_html=True)

    # Price List Section
    st.markdown("### Price List")
    st.image("images/Poster.png", use_column_width=True)

    # Clothes Section
    st.markdown("### Clothes")
    cols = st.columns(2)
    with cols[0]:
        st.image("images/Clothes1.png", caption="Clothes 1", use_column_width=True)
        st.image("images/Clothes3.png", caption="Clothes 3", use_column_width=True)
    with cols[1]:
        st.image("images/Clothes2.png", caption="Clothes 2", use_column_width=True)
        st.image("images/Clothes4.png", caption="Clothes 4", use_column_width=True)

    # Sneakers Section
    st.markdown("### Sneakers")
    cols = st.columns(2)
    with cols[0]:
        st.image("images/Sneaker1.png", caption="Sneaker 1", use_column_width=True)
    with cols[1]:
        st.image("images/Sneaker2.png", caption="Sneaker 2", use_column_width=True)

    # Blankets Section
    st.markdown("### Blankets")
    cols = st.columns(2)
    with cols[0]:
        st.image("images/Blanket1.png", caption="Blanket 1", use_column_width=True)
    with cols[1]:
        st.image("images/Blanket2.png", caption="Blanket 2", use_column_width=True)

    # Transport System Section
    st.markdown("### Transport System")
    cols = st.columns(2)
    with cols[0]:
        st.image("images/Transport1.png", caption="Transport 1", use_column_width=True)
        st.image("images/Transport3.png", caption="Transport 3", use_column_width=True)
    with cols[1]:
        st.image("images/Transport2.png", caption="Transport 2", use_column_width=True)

    add_footer()


# Predict Your Cost Page
if selected_page == "Predict Your Cost":
    st.title("Predict Your Cost")
    st.write("Estimate your laundry cost by entering the quantities of the items you'd like washed.")

    # Inputs for cost prediction
    blanket = st.number_input("Blankets/Comforters/Duvets (R50 each)", min_value=0, value=0) * 50
    carpet = st.number_input("Carpets (R45 each)", min_value=0, value=0) * 45
    sneakers = st.number_input("Sneakers (R50 each)", min_value=0, value=0) * 50
    crocs_slides = st.number_input("Crocs/Slides (R20 each)", min_value=0, value=0) * 20
    wash = st.number_input("Washes (R25 each)", min_value=0, value=0) * 25
    dry = st.number_input("Dries (R25 each)", min_value=0, value=0) * 25
    soap = st.number_input("Soap (R5 each)", min_value=0, value=0) * 5
    stasoft = st.number_input("Sta-Soft (R5 each)", min_value=0, value=0) * 5
    plastic = st.number_input("Plastic (R7 each)", min_value=0, value=0) * 7

    # Transport selection
    transport_options = {
        "Drop-off & pickup": 0,
        "Local (Return)": 30,
        "Hospital (Return)": 40,
        "Toronto/Unit F (Return)": 40,
        "Ga-Makanye (Return)": 40,
        "Paledi (Return)": 60
    }
    transport = st.selectbox("Select Transport Option", options=list(transport_options.keys()))
    transport_cost = transport_options[transport]

    # Calculate total cost
    total_cost = blanket + carpet + wash + dry + soap + stasoft + sneakers + crocs_slides + transport_cost + plastic
    st.subheader(f"Your Estimated Cost: R {total_cost}")
    add_footer()

# Booking Page
if selected_page == "Booking Page":
    st.title("Booking Page")

    # Initialize booking_count in session state
    if "booking_count" not in st.session_state:
        st.session_state.booking_count = {}

    today = datetime.today().date()
    min_booking_date = today + timedelta(days=1)

    if today not in st.session_state.booking_count:
        st.session_state.booking_count[today] = 0

    if st.session_state.booking_count[today] >= 10:
        st.warning("Maximum bookings for today reached. Please choose another date.")
    else:
        with st.form("booking_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            booking_date = st.date_input("Booking Date", value=min_booking_date, min_value=min_booking_date)
            allowed_times = [time(hour, minute) for hour in range(6, 14) for minute in (0, 30)]
            booking_time = st.selectbox("Booking Time", options=allowed_times)
            message = st.text_area("Additional Message")
            submitted = st.form_submit_button("Submit Booking")

            if submitted:
                st.session_state.booking_count[booking_date] = st.session_state.booking_count.get(booking_date, 0) + 1
                whatsapp_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {booking_date}\nTime: {booking_time}\nMessage: {message}"
                whatsapp_link = f"https://wa.me/27828492746?text={urllib.parse.quote(whatsapp_message)}"
                st.success("Booking submitted! Your details have been sent to WhatsApp.")
                st.markdown(f"[Click here to confirm on WhatsApp]({whatsapp_link})")

    remaining_bookings = max(0, 10 - st.session_state.booking_count[today])
    st.info(f"Remaining bookings for today: {remaining_bookings}")
    add_footer()


# Directions Page
if selected_page == "Directions":
    st.title("Get Directions")
    st.write("Navigate to our laundromat via Google Maps for precise directions and landmarks.")

    laundromat_location = [-23.875124, 29.743984]
    m = folium.Map(location=laundromat_location, zoom_start=16, control_scale=True)
    folium.Marker(laundromat_location, popup="Map's Laundromat").add_to(m)
    components.html(m._repr_html_(), height=500)

    google_maps_url = f"https://www.google.com/maps/dir/?api=1&destination={laundromat_location[0]},{laundromat_location[1]}"
    if st.button("Get Directions"):
        st.markdown(f"[Click here for Google Maps Directions]({google_maps_url})", unsafe_allow_html=True)
    add_footer()
