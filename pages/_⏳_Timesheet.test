import streamlit as st
import datetime

st.subheader("Enter Your Time sheet for working on FR/Hopetrust Tasks ")
option = st.selectbox(
    ':blue[Your Name]:',
    ('Abdul Kalam Azad', ' E.Subashini', 'Madhusudhan T','P. Mythili','S.Goutham','J.Richard Franklin','VA Naveen','A Sundhareshwaran','M Deepthee Priyaa'))


fromdate = st.date_input(
    ":blue[Week Start Date]:",
    datetime.date(2023, 5, 1))

todate = st.date_input(
    ":blue[Week End Date]:",
    datetime.date(2023, 5, 1),key = "Enddate")
days = todate-fromdate

number = int(st.number_input(':blue[Number Of Hours You Worked For this Week]'))

title = st.text_input(':blue[Task You have been Working on]:', 'Enter Your Task')

if st.button('Submit'):
    st.balloons()
    st.success("Thanks for Submitting the Time Sheet")

hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
