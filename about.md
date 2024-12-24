# <span style="color:#EF5454">Map's Laundromat</span>

---

### <span style="color:DarkSlateBlue">Introduction</span>
Welcome to **Map's Laundromat**, where we provide fast, reliable, and affordable same-day laundry services in Turfloop. From everyday garments to delicate fabrics, we make laundry day a breeze!

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

---

### <span style="color:DarkSlateBlue">Booking Page</span>
Navigate to the **Booking Page** from the sidebar to schedule your laundry appointment.  

Here’s what you can expect on the **Booking Page**:
```python
elif selection == "Booking Page":
    st.title("Booking Page")
    with st.form("booking_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        booking_date = st.date_input("Booking Date")
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
            whatsapp_link = f"https://wa.me/<0828492746>?text={encoded_message}"
            
            st.success("Booking submitted!")
            st.markdown(f"[Contact on WhatsApp]({whatsapp_link})", unsafe_allow_html=True)
