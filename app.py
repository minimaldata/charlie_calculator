import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Function to calculate the increase in booking-to-call percentage based on the number of bookings per month
# def calculate_increase(bookings_per_month):
#     if bookings_per_month <= 1:
#         return 25
#     elif bookings_per_month <= 100:
#         return 25
#     elif bookings_per_month <= 500:
#         return 25 + (50 - 25) * (bookings_per_month - 100) / (500 - 100)
#     elif bookings_per_month <= 1000:
#         return 50 + (10 - 50) * (bookings_per_month - 500) / (1000 - 500)
#     else:
#         return 10

# # Function to calculate customers
# def calculate_customers(bookings, booking_to_call, bad_fit, good_fit):
#     return bookings * (booking_to_call / 100) * (1 - bad_fit / 100) * (good_fit / 100)

# # Title of the app
# st.title("Is Charlie AI worth it?")
# st.subheader("12-month Incremental Value calculator")

# st.write("### This is the new bookings per month section.")
# st.write("I need to fill in my answers to these 3 questions:")

# Question 1
# Question 1
st.write("1. Right now I'm getting between")
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    current_min = st.text_input("X", value="10", key="current_min", label_visibility="collapsed")
with col2:
    st.write("and")
with col3:
    current_max = st.text_input("Y", value="20", key="current_max", label_visibility="collapsed")
    st.write("new bookings per month.")

# Convert input values to integers
current_min = int(current_min)
current_max = int(current_max)

# Create a new column for the chart
col_chart, _ = st.columns([4, 1])
with col_chart:
    # Generate some data for the cumulative bookings
    months = range(1, 13)  # 12 months
    min_bookings = [current_min * month for month in months]
    max_bookings = [current_max * month for month in months]

    # Create a DataFrame for the chart
    data = {
        "Month": months,
        "Min Bookings": min_bookings,
        "Max Bookings": max_bookings
    }
    df = pd.DataFrame(data)

    # Display the cumulative bookings values at the end of the lines
    last_min_booking = min_bookings[-1]
    last_max_booking = max_bookings[-1]
    st.write(f"Last Min Booking: {last_min_booking}")
    st.write(f"Last Max Booking: {last_max_booking}")

    # Plot the line chart
    st.line_chart(df.set_index('Month'))

# # Question 2
# st.write("### What % of bookings result in a call?")
# st.write("Right now, I get between")
# col4, col5, col6 = st.columns([1, 1, 4])
# with col4:
#     current_min_call = st.text_input("X%", value="50", key="current_min_call", label_visibility="collapsed")
# with col5:
#     st.write("and")
# with col6:
#     current_max_call = st.text_input("Y%", value="70", key="current_max_call", label_visibility="collapsed")
#     st.write("% of bookings resulting in a call.")

# # Question 3
# st.write("### What % of calls would you say are just 'bad fits'?")
# st.write("Right now between")
# col7, col8, col9 = st.columns([1, 1, 4])
# with col7:
#     current_min_bad_fit = st.text_input("X%", value="20", key="current_min_bad_fit", label_visibility="collapsed")
# with col8:
#     st.write("and")
# with col9:
#     current_max_bad_fit = st.text_input("Y%", value="30", key="current_max_bad_fit", label_visibility="collapsed")
#     st.write("% of calls are 'bad fits'.")

# # Question 4
# st.write("### And what % of the 'good fits' are you able to close?")
# st.write("Right now between")
# col10, col11, col12 = st.columns([1, 1, 4])
# with col10:
#     current_min_close = st.text_input("X%", value="60", key="current_min_close", label_visibility="collapsed")
# with col11:
#     st.write("and")
# with col12:
#     current_max_close = st.text_input("Y%", value="80", key="current_max_close", label_visibility="collapsed")
#     st.write("% of 'good fits' are closed.")

# # Calculate the increase in booking-to-call percentage
# try:
#     current_min = int(current_min)
#     current_max = int(current_max)
#     increase_min = calculate_increase(current_min)
#     increase_max = calculate_increase(current_max)
# except ValueError:
#     st.error("Please enter valid numbers for current bookings range.")

# try:
#     current_min_call = int(current_min_call)
#     current_max_call = int(current_max_call)
#     new_min_call = current_min_call * (increase_min / 100) + current_min_call
#     new_max_call = current_max_call * (increase_max / 100) + current_max_call
# except ValueError:
#     st.error("Please enter valid percentages for current call rates.")

# # Display the increased booking-to-call percentage
# st.write("### Increase in Booking-to-Call Percentage")
# st.write(f"With the tool, your booking-to-call percentage will increase by {increase_min}% to {increase_max}%")
# st.write(f"New booking-to-call percentage: between {new_min_call}% and {new_max_call}%")

# # User-adjustable belief about the future with Charlie AI
# belief_min_call = st.slider("Adjust your belief about the future min booking-to-call percentage", min_value=current_min_call, max_value=100, value=int(new_min_call))
# belief_max_call = st.slider("Adjust your belief about the future max booking-to-call percentage", min_value=current_max_call, max_value=100, value=int(new_max_call))

# # Extracting remaining values from the input fields
# try:
#     current_min_bad_fit = int(current_min_bad_fit)
#     current_max_bad_fit = int(current_max_bad_fit)
# except ValueError:
#     st.error("Please enter valid percentages for current 'bad fit' rates.")

# try:
#     current_min_close = int(current_min_close)
#     current_max_close = int(current_max_close)
# except ValueError:
#     st.error("Please enter valid percentages for current close rates.")

# # Create a cumulative line chart for conservative customers (current min, new min, and belief min)
# months = np.arange(1, 13)
# current_min_customers = np.cumsum([calculate_customers(current_min, current_min_call, current_min_bad_fit, current_min_close)] * 12)
# new_min_customers = np.cumsum([calculate_customers(current_min, new_min_call, current_min_bad_fit, current_min_close)] * 12)
# belief_min_customers = np.cumsum([calculate_customers(current_min, belief_min_call, current_min_bad_fit, current_min_close)] * 12)

# conservative_data = {
#     "Month": months,
#     "Current Min Customers": current_min_customers,
#     "New Min Customers": new_min_customers,
#     "Belief Min Customers": belief_min_customers
# }

# conservative_df = pd.DataFrame(conservative_data)
# conservative_df.set_index("Month", inplace=True)

# st.write("### Conservative Cumulative Customers Over 12 Months")
# st.line_chart(conservative_df)

# # Create a cumulative line chart for aggressive customers (current max, new max, and belief max)
# current_max_customers = np.cumsum([calculate_customers(current_max, current_max_call, current_max_bad_fit, current_max_close)] * 12)
# new_max_customers = np.cumsum([calculate_customers(current_max, new_max_call, current_max_bad_fit, current_max_close)] * 12)
# belief_max_customers = np.cumsum([calculate_customers(current_max, belief_max_call, current_max_bad_fit, current_max_close)] * 12)

# aggressive_data = {
#     "Month": months,
#     "Current Max Customers": current_max_customers,
#     "New Max Customers": new_max_customers,
#     "Belief Max Customers": belief_max_customers
# }

# aggressive_df = pd.DataFrame(aggressive_data)
# aggressive_df.set_index("Month", inplace=True)

# st.write("### Aggressive Cumulative Customers Over 12 Months")
# st.line_chart(aggressive_df)

# # Display the inputs for confirmation
# st.write("### Your Inputs")
# st.write(f"Current bookings per month: between {current_min} and {current_max}")
# st.write(f"Current % of bookings resulting in a call: between {current_min_call}% and {current_max_call}%")
# st.write(f"New % of bookings resulting in a call: between {new_min_call}% and {new_max_call}%")
# st.write(f"Belief % of bookings resulting in a call: between {belief_min_call}% and {belief_max_call}%")
# st.write(f"Current % of calls that are 'bad fits': between {current_min_bad_fit}% and {current_max_bad_fit}%")
# st.write(f"Current % of 'good fits' that are closed: between {current_min_close}% and {current_max_close}%")