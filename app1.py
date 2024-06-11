import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(
    page_title="Charlie Opportunity Calculator",
    page_icon="https://charlieai.io/wp-content/uploads/2023/12/sm-charlie-icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set the title of the app
st.image("https://charlieai.io/wp-content/uploads/2023/12/CharlieAILogo.png", width=300)
st.title("What is Charlie Worth to you?")

# Initialize session state if not already present
if 'newBookings_current' not in st.session_state:
    st.session_state.newBookings_current = 300
if 'percCall_current' not in st.session_state:
    st.session_state.percCall_current = 50
if 'percFit_current' not in st.session_state:
    st.session_state.percFit_current = 50
if 'percClose_current' not in st.session_state:
    st.session_state.percClose_current = 50
if 'rev12months_current' not in st.session_state:
    st.session_state.rev12months_current = 1000

if 'newBookings_business' not in st.session_state:
    st.session_state.newBookings_business = st.session_state.newBookings_current
if 'newBookings_core' not in st.session_state:
    st.session_state.newBookings_core = st.session_state.newBookings_current * 1.2

if 'percCall_business' not in st.session_state:
    st.session_state.percCall_business = st.session_state.percCall_current * 1.2
if 'percCall_core' not in st.session_state:
    st.session_state.percCall_core = st.session_state.percCall_current * 1.3

if 'calls_current' not in st.session_state:
    st.session_state.calls_current = st.session_state.newBookings_current * st.session_state.percCall_current / 100
if 'calls_business' not in st.session_state:
    st.session_state.calls_business = st.session_state.newBookings_business * st.session_state.percCall_business / 100
if 'calls_core' not in st.session_state:
    st.session_state.calls_core = st.session_state.newBookings_core * st.session_state.percCall_core / 100

if 'percFit_business' not in st.session_state:
    st.session_state.percFit_business = st.session_state.percFit_current * 1.2
if 'percFit_core' not in st.session_state:
    st.session_state.percFit_core = st.session_state.percFit_current * 1.3

if 'qualityCalls_current' not in st.session_state:
    st.session_state.qualityCalls_current = st.session_state.calls_current * st.session_state.percFit_current / 100
if 'qualityCalls_business' not in st.session_state:
    st.session_state.qualityCalls_business = st.session_state.calls_business * st.session_state.percFit_business / 100
if 'qualityCalls_core' not in st.session_state:
    st.session_state.qualityCalls_core = st.session_state.calls_core * st.session_state.percFit_core / 100

if 'percClose_business' not in st.session_state:
    st.session_state.percClose_business = st.session_state.percClose_current * 1.05
if 'percClose_core' not in st.session_state:
    st.session_state.percClose_core = st.session_state.percClose_current * 1.2

if 'newCustomers_current' not in st.session_state:
    st.session_state.newCustomers_current = st.session_state.qualityCalls_current * st.session_state.percClose_current / 100
if 'newCustomers_business' not in st.session_state:
    st.session_state.newCustomers_business = st.session_state.qualityCalls_business * st.session_state.percClose_business / 100
if 'newCustomers_core' not in st.session_state:
    st.session_state.newCustomers_core = st.session_state.qualityCalls_core * st.session_state.percClose_core / 100

if 'rev12months_business' not in st.session_state:
    st.session_state.rev12months_business = st.session_state.rev12months_current
if 'rev12months_core' not in st.session_state:
    st.session_state.rev12months_core = st.session_state.rev12months_current * 1.2


if 'marketing_spend_current' not in st.session_state:
    st.session_state.marketing_spend_current = 5000

if 'newleads_current' not in st.session_state:
    st.session_state.newleads_current = 500

if 'newleads_business' not in st.session_state:
    st.session_state.newleads_business = st.session_state.newleads_current

if 'newleads_core' not in st.session_state:
    st.session_state.newleads_core = st.session_state.newleads_current

if 'lead_to_booking_current' not in st.session_state:
    st.session_state.lead_to_booking_current = 60

if 'lead_to_booking_business' not in st.session_state:
    st.session_state.lead_to_booking_business = st.session_state.lead_to_booking_current

if 'lead_to_booking_core' not in st.session_state:
    st.session_state.lead_to_booking_core = st.session_state.lead_to_booking_current


# if 'spend_per_lead_current' not in st.session_state:
#     st.session_state.current_spend_per_booking = marketing_spend_current / newBookings_current
# if 'spend_per_booking_business' not in st.session_state:
#     st.session_state.business_spend_per_booking = marketing_spend_current / newBookings_current
# if 'spend_per_booking_core' not in st.session_state:
#     st.session_state.core_spend_per_booking = marketing_spend_current / newBookings_current


# Sidebar inputs to set current state values
st.sidebar.title("Current State")
st.session_state.marketing_spend_current = st.sidebar.number_input("What is your current monthly marketing spend?", min_value=0, max_value=100000000, value=5000)
st.session_state.newleads_current = st.sidebar.number_input("How many leads are you getting per month?", min_value=0, max_value=100000000, value=500)
st.session_state.lead_to_booking_current = st.sidebar.number_input("What % of those leads result in a booking?", min_value=0, max_value=100, value=60)
st.session_state.percCall_current = st.sidebar.number_input("What % of those bookings result in a call?", min_value=0, max_value=100, value=50)
st.session_state.percFit_current = st.sidebar.number_input("What % of those calls are potential fits for your business?", min_value=0, max_value=100, value=50)
st.session_state.percClose_current = st.sidebar.number_input("What % of those potential fits do you actually close?", min_value=0, max_value=100, value=50)
st.session_state.rev12months_current = st.sidebar.number_input("How much revenue is each new customer worth in their first 12 months?", min_value=0, max_value=100000000, value=1000)

# Recalculate necessary variables based on updated inputs
st.session_state.newBookings_business = st.session_state.newBookings_current


#Chart Components
def generate_new_leads_chart(slider1_value, slider2_value, slider3_value):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Create three separate lines, one for each slider value
    line1 = np.cumsum(np.repeat(slider1_value, 12))
    line2 = np.cumsum(np.repeat(slider2_value, 12))
    line3 = np.cumsum(np.repeat(slider3_value, 12))
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background

    
    ax.plot(months, line2, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, line3, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, line1, marker='o', linestyle='-', color='#999999', label='Current')

    ax.set_title('Leads next 12 Months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative Leads', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')

    st.pyplot(fig)

def generate_new_bookings_chart(current_bookings, current_call_perc, business_bookings,business_call_perc, core_bookings, core_call_perc):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Create three separate lines, one for each slider value
    line1 = np.cumsum(np.repeat(current_bookings * current_call_perc/100, 12))
    line2 = np.cumsum(np.repeat(business_bookings * business_call_perc/100, 12))
    line3 = np.cumsum(np.repeat(core_bookings * core_call_perc/100, 12))
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background

    
    ax.plot(months, line2, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, line3, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, line1, marker='o', linestyle='-', color='#999999', label='Current')

    ax.set_title('New Bookings next 12 months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative New Bookings', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')

    st.pyplot(fig)
def generate_new_calls_chart(current_bookings, current_call_perc, business_bookings,business_call_perc, core_bookings, core_call_perc):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Create three separate lines, one for each slider value
    line1 = np.cumsum(np.repeat(current_bookings * current_call_perc/100, 12))
    line2 = np.cumsum(np.repeat(business_bookings * business_call_perc/100, 12))
    line3 = np.cumsum(np.repeat(core_bookings * core_call_perc/100, 12))
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background

    ax.plot(months, line2, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, line3, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, line1, marker='o', linestyle='-', color='#999999', label='Current')
    
    ax.set_title('New Calls next 12 months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative New Calls', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')

    st.pyplot(fig)

#actually same as above, but can change variables later
def generate_new_quality_calls_chart(current_bookings, current_call_perc, business_bookings,business_call_perc, core_bookings, core_call_perc):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Create three separate lines, one for each slider value
    line1 = np.cumsum(np.repeat(current_bookings * current_call_perc/100, 12))
    line2 = np.cumsum(np.repeat(business_bookings * business_call_perc/100, 12))
    line3 = np.cumsum(np.repeat(core_bookings * core_call_perc/100, 12))
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background

    ax.plot(months, line2, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, line3, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, line1, marker='o', linestyle='-', color='#999999', label='Current')
    
    ax.set_title('New Quality Calls next 12 months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative New Quality Calls', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    
    st.pyplot(fig)

#actually same as above, but can change variables later
def generate_new_customers_chart(current_bookings, current_call_perc, business_bookings,business_call_perc, core_bookings, core_call_perc):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Create three separate lines, one for each slider value
    line1 = np.cumsum(np.repeat(current_bookings * current_call_perc/100, 12))
    line2 = np.cumsum(np.repeat(business_bookings * business_call_perc/100, 12))
    line3 = np.cumsum(np.repeat(core_bookings * core_call_perc/100, 12))
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background

    ax.plot(months, line2, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, line3, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, line1, marker='o', linestyle='-', color='#999999', label='Current')
    
    ax.set_title('New Customers next 12 months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative New Customers', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    
    st.pyplot(fig)
def calculate_monthly_revenue(new_customers_per_month, annual_revenue_per_customer):
    # Calculate monthly revenue per customer
    monthly_revenue_per_customer = annual_revenue_per_customer / 12
    
    # Initialize an array to store the cumulative revenue for each month
    monthly_revenue = np.zeros(12)
    
    # Calculate the cumulative revenue for each month
    for month in range(12):
        for past_month in range(month + 1):
            monthly_revenue[month] += new_customers_per_month * monthly_revenue_per_customer
    
    return np.cumsum(monthly_revenue)
def generate_new_revenue_chart(current_customers, current_12month_rev, business_customers, business_12month_rev, core_customers, core_12month_rev):
    # Generate monthly values based on the sliders
    months = np.arange(1, 13)
    
    # Calculate monthly revenue for each scenario
    current_monthly_revenue = calculate_monthly_revenue(current_customers, current_12month_rev)
    business_monthly_revenue = calculate_monthly_revenue(business_customers, business_12month_rev)
    core_monthly_revenue = calculate_monthly_revenue(core_customers, core_12month_rev)
    
    # Generate the line chart
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0d1117')  # Dark background
    ax.set_facecolor('#0d1117')  # Dark background


    ax.plot(months, business_monthly_revenue, marker='o', linestyle='-', color='#00BFFF', label='Conservative')
    ax.plot(months, core_monthly_revenue, marker='o', linestyle='-', color='#ff69b4', label='Aggressive')
    ax.plot(months, current_monthly_revenue, marker='o', linestyle='-', color='#999999', label='Current')

    ax.set_title('Revenue from New Customers next 12 Months', color='white', fontsize=16)
    ax.set_xlabel('Months', color='white', fontsize=12)
    ax.set_ylabel('Cumulative New Customer Revenue', color='white', fontsize=12)

    legend = ax.legend(facecolor='#0d1117', edgecolor='white', fontsize=10)
    for text in legend.get_texts():
        text.set_color('white')

    # Set tick color
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set spine color
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    
    st.pyplot(fig)

# Grid Components
def leads_component(keyvalue):
    st.subheader('New Leads / Month')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.newleads_business = st.slider("", min_value=0, max_value=st.session_state.newleads_current * 2,value=st.session_state.newleads_current, disabled=True,  key = f"business_newleads_{keyvalue}", label_visibility="collapsed",)

    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Aggressive')
    with col2:
        st.session_state.newleads_core = st.slider('', min_value=0, max_value=st.session_state.newleads_current * 2, value=int(st.session_state.newleads_current * 1.1), key = f"core_newleads_{keyvalue}", label_visibility="collapsed")
            
    generate_new_leads_chart(st.session_state.newleads_current,st.session_state.newleads_business,st.session_state.newleads_core)

def bookings_component(keyvalue):
    st.subheader('% Leads to Bookings')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.lead_to_booking_business = st.slider('', min_value=0, max_value=100, disabled = True,value=int(st.session_state.lead_to_booking_current), key = f"business_lead_to_booking_Perc_{keyvalue}", label_visibility="collapsed")
        st.session_state.newBookings_business = st.session_state.newleads_business * st.session_state.lead_to_booking_business/100
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Aggressive')
    with col2:
        st.session_state.lead_to_booking_core = st.slider('', min_value=0, max_value=100, value=int(st.session_state.lead_to_booking_current + (100 - st.session_state.lead_to_booking_current) * .3), key = f"core_lead_to_booking_Perc_{keyvalue}", label_visibility="collapsed")
        st.session_state.newBookings_core = st.session_state.newleads_core * st.session_state.lead_to_booking_core/100    
    generate_new_bookings_chart(st.session_state.newleads_current,st.session_state.lead_to_booking_current,st.session_state.newleads_business,st.session_state.lead_to_booking_business, st.session_state.newleads_core, st.session_state.lead_to_booking_core)


def calls_component(keyvalue):
    st.subheader('% Bookings to Call')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.percCall_business = st.slider('', min_value=0, max_value=100, value=int(st.session_state.percCall_current + (100 - st.session_state.percCall_current) * .2), key = f"business_callPerc_{keyvalue}", label_visibility="collapsed")
        st.session_state.calls_business = st.session_state.newBookings_business * st.session_state.percCall_business/100
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('Aggressive')
    with col2:
        st.session_state.percCall_core = st.slider('', min_value=0, max_value=100, value=int(st.session_state.percCall_current + (100 - st.session_state.percCall_current) * .3), key = f"core_callPerc_{keyvalue}", label_visibility="collapsed")
        st.session_state.calls_core = st.session_state.newBookings_core * st.session_state.percCall_core/100    
    generate_new_calls_chart(st.session_state.newBookings_current,st.session_state.percCall_current,st.session_state.newBookings_business,st.session_state.percCall_business, st.session_state.newBookings_core, st.session_state.percCall_core)

def fit_component(keyvalue):
    st.subheader('% Calls Potential Fit')
    col1,col2 = st.columns(2)
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.percFit_business = st.slider('', min_value=0, max_value=100, value=int(st.session_state.percFit_current + (100 - st.session_state.percFit_current) * .3), key = f"business_fitPerc_{keyvalue}", label_visibility="collapsed")
        st.session_state.qualityCalls_business = st.session_state.calls_business * st.session_state.percFit_business/100
    col1,col2 = st.columns(2)
    with col1: 
        st.write('Aggressive')
    with col2: 
        st.session_state.percFit_core = st.slider('', min_value=0, max_value=100, value=int(st.session_state.percFit_current + (100 - st.session_state.percFit_current) * .4), key = f"core_fitPerc_{keyvalue}", label_visibility="collapsed")
        st.session_state.qualityCalls_core = st.session_state.calls_core * st.session_state.percFit_core/100
    st.session_state.calls_current = st.session_state.newBookings_current * st.session_state.percCall_current / 100
    generate_new_quality_calls_chart(st.session_state.calls_current, st.session_state.percFit_current, st.session_state.calls_business, st.session_state.percFit_business, st.session_state.calls_core, st.session_state.percFit_core)

def customers_component(keyvalue):
    st.subheader('% Potential Fits Closed')
    col1,col2 = st.columns(2)
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.percClose_business = st.slider("", min_value=0, max_value=100,value=st.session_state.percClose_current, disabled=True,  key = f"percClose_business_{keyvalue}", label_visibility="collapsed",)
        st.session_state.newCustomers_business = st.session_state.qualityCalls_business * st.session_state.percClose_business/100
    col1,col2 = st.columns(2)
    with col1: 
        st.write('Aggressive')
    with col2: 
        st.session_state.percClose_core = st.slider('', min_value=0, max_value=100, value=int(st.session_state.percClose_current + (100 - st.session_state.percClose_current) * .2), key = f"core_closePerc_{keyvalue}", label_visibility="collapsed")
        st.session_state.newCustomers_core = st.session_state.qualityCalls_core * st.session_state.percClose_core/100
    st.session_state.qualityCalls_current = st.session_state.calls_current * st.session_state.percFit_current / 100
    st.session_state.newCustomers_current = st.session_state.qualityCalls_current * st.session_state.percClose_current / 100
    generate_new_customers_chart(st.session_state.qualityCalls_current, st.session_state.percClose_current, st.session_state.qualityCalls_business, st.session_state.percClose_business, st.session_state.qualityCalls_core, st.session_state.percClose_core)

def revenue_component(keyvalue):
    st.subheader('New Customer Revenue')
    col1,col2 = st.columns(2)
    with col1:
        st.write('Conservative')
    with col2:
        st.session_state.rev12months_business = st.slider("", min_value=0, max_value=st.session_state.rev12months_current * 2,value=st.session_state.rev12months_current, disabled=True,  key = f"rev12months_business_{keyvalue}", label_visibility="collapsed",)
    col1,col2 = st.columns(2)
    with col1: 
        st.write('Aggressive')
    with col2: 
        st.session_state.rev12months_core = st.slider('', min_value=0, max_value=st.session_state.rev12months_current * 2, value=int(st.session_state.rev12months_current * 1.2), key = f"rev12months_core_{keyvalue}", label_visibility="collapsed")

    generate_new_revenue_chart(st.session_state.newCustomers_current, st.session_state.rev12months_current, st.session_state.newCustomers_business, st.session_state.rev12months_business, st.session_state.newCustomers_core, st.session_state.rev12months_core)

# Create grid layout manually
r1col1, r1col2, r1col3 = st.columns(3)

# First row
with r1col1:
    leads_component(1)
with r1col2:
    bookings_component(1)
with r1col3:
    calls_component(1)

r2col1, r2col2, r2col3 = st.columns(3)
with r2col1:
    fit_component(1)
with r2col2:
    st.session_state.newCustomers_current = st.session_state.newBookings_current * st.session_state.percCall_current / 100 * st.session_state.percClose_current / 100 * st.session_state.percFit_current / 100
    customers_component(1)
with r2col3:
    revenue_component(1)

st.title("Opportunity: 12 Months New Revenue")
r3col1, r3col2, r3col3 = st.columns(3)

with r3col1:
    st.header("Current")
    
    # st.subheader("12 Months of Marketing Spend")
    # marketing_12mos = st.session_state.marketing_spend_current * 12
    # st.subheader(f"${marketing_12mos:,.2f}")
    current_opportunity = calculate_monthly_revenue(st.session_state.newCustomers_current, st.session_state.rev12months_current)
    st.subheader(f"${current_opportunity.max():,.2f}")

with r3col2:
    st.header("Conservative")
    business_opportunity = calculate_monthly_revenue(st.session_state.newCustomers_business, st.session_state.rev12months_business)
    st.subheader(f"${business_opportunity.max():,.2f}")

    business_difference = business_opportunity.max() - current_opportunity.max()
    st.subheader(f"Difference: ${business_difference:,.2f}")

with r3col3:
    st.header("Aggressive")
    core_opportunity = calculate_monthly_revenue(st.session_state.newCustomers_core, st.session_state.rev12months_core)
    st.subheader(f"${core_opportunity.max():,.2f}")

    core_difference = core_opportunity.max() - current_opportunity.max()
    st.subheader(f"Difference: ${core_difference:,.2f}")

