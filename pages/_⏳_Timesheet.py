
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import datetime


st.title("Time Sheet")

st.markdown("Fill/Edit/Delete your Timesheet ")


url = "https://docs.google.com/spreadsheets/d/1H-yHHNhlauj_U4-5KWmtY50fB_iklMHDYsRwjLNtKHE/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(spreadsheet=url, worksheet=0, usecols=list(range(5)), ttl=4)
existing_data = existing_data.dropna(how="all")
# st.dataframe(data)

team_Members = ['S.Goutham', 'VA Naveen', 'Thiyagu', 'A Sundhareshwaran', 'M Deepthee Priyaa','Praveen kumar','Deepthi','Anand']

with st.form("Time-sheet"):
    with st.container():
        option = st.selectbox(":blue[Your Name]", team_Members)

    with st.container():
        fromdate = st.date_input(":blue[Week Start Date]", datetime.date.today())

    with st.container():
        todate = st.date_input(":blue[Week End Date]", datetime.date.today(), key="Enddate")
        days = (todate - fromdate).days

    with st.container():
        number = st.number_input(':blue[Number Of Hours You Worked For this Week]', value=0)

    with st.container():
        task = st.text_input(':blue[Task You have been Working on]', '')

    if st.form_submit_button('Submit'):
        if number<=0:
            st.warning("Please Enter Timings")
            st.stop()
        elif not task:
            st.warning("Please write what you have worked on in small words")
            st.stop()     
        else:
            updated_data = pd.DataFrame(
                [
                {
                "Your Name" : option,
                "Week Start Date" : fromdate,
                "Week End Date" : todate,
                "Number Of Hours You Worked For this Week" : number,
                "Task You have been Working on" : task
                }
            ] 
            )
            updated_values = pd.concat([existing_data, updated_data], ignore_index=True)
            conn.update(spreadsheet=url, worksheet=0, data = updated_values)
            st.balloons()
            st.success("Thanks for Submitting the Time Sheet")
            working_hour_averages = updated_values.groupby("Your Name")["Number Of Hours You Worked For this Week"].sum().reset_index()


# st.write(working_hour_averages)
