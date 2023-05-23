import streamlit as st

st.subheader("Hope Trust Income and Expenses Tracker")
source = st.radio(
    "Select Type Of Spendings",
    ('Income', 'Expenses'))
option = st.selectbox(
    'Your Team',
    ('Fund Raisers', 'Needy Hunters','Event Management','President','Vice President','Seceratary','Admin Team','Internal Strenthening'),key="Team")

if option == "Fund Raisers":
    frsource = st.radio(
    "Select Type Of Spendings",
    ('Income', 'Expenses'),key='FR')
    if frsource == 'Income':
        frsource1 = st.selectbox("Select Type Of Spendings",('Monthly Funds', 'Donations','Unknown Donors'))
        uploaded_files = st.file_uploader("Enter your Income Receipt", accept_multiple_files=True)
    else:
        uploaded_files = st.file_uploader("Enter your Expenses Receipt", accept_multiple_files=True)
        frsource1 = st.selectbox( "Select Type Of Spendings",('Event Donation', 'Event Other Expenses','Mobile-Recharge'))
elif option == "Needy Hunters":
        nhsource1 = st.selectbox( "Select Your Expenses",('Previsits',''))
        uploaded_files = st.file_uploader("Enter your Expenses Receipt", accept_multiple_files=True)
elif option == "Event Management":
        title = st.text_input('Enter the Event Number', '')
        emsource1 = st.selectbox( "Select Your Expenses",('Event Expenses',''))
        uploaded_files = st.file_uploader("Enter your Expenses Receipt", accept_multiple_files=True)
elif option == "President":
        st.write("Need to discuss")
elif option == "Vice President":
        st.write("Need to discuss")
elif option == "Seceratary":
        st.write("Need to discuss")
elif option == "Admin Team":
        emsource1 = st.selectbox( "Select Your Expenses",('Event Expenses','Letters/Printout/Postal','Website','Mobile-Recharge'))
        uploaded_files = st.file_uploader("Enter your Expenses Receipt", accept_multiple_files=True)
elif option == "Internal Strenthening":
        st.write("Need to discuss")
