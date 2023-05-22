import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts


check = st.selectbox(
    'Select the Event to see the Event Related Data',
    ('Event 22', 'Event 6-10', 'Event 11-15',"Event 11-15","Event 11-15","Event 11-15","Event 11-15"))

if check == 'Event 22':
    st.title('Fund Raised  :blue[By Our Volunteer] :sunglasses: for Event 22')
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%"},
        "series": [
            {
                "name": "Event 22",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "R.Venkataramanan"},
                    {"value": 600, "name": "R.M Abdul Khudus"},
                    {"value": 500, "name": "Y.M Jagadeesh"},
                    {"value": 1100, "name": "Habeebulla"},
                    {"value": 1050, "name": "P.B Ravi Chandhar"},
                    {"value": 500, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 700, "name": "K.R.Harish"},
                    {"value": 300, "name": "B.Rupesh Kumar"},
                    {"value": 1000, "name": "S.Parthasarathy"},
                    {"value": 6000, "name": "N.Evangelin Ruby"},
                    {"value": 700, "name": "A.Sandeep"},
                    {"value": 1200, "name": "E.Subhashini"},
                    {"value": 200, "name": "V. Akash"},
                    {"value": 2201, "name": "T. Madhusudhan"},
                    {"value": 300, "name": "A.Karthick"},
                    {"value": 2000, "name": "M.Kumar swamy "},
                    {"value": 550, "name": "P.Mythili "},
                    {"value": 5000, "name": "S.Jothiram"},
                    {"value": 650, "name": "S.Bharath Kumar"},
                    {"value": 1000, "name": "V.Pranav Sabareesh"},
                    {"value": 2500, "name": "B.Santhosh "},
                    {"value": 1600, "name": "J Jacob Israel "},
                    {"value": 1000, "name": "Navudu Devi Anudeesh "},
                    {"value": 3090, "name": "S.Govindarajulu"},
                    {"value": 200, "name": "Vignesh.s"},
                    {"value": 2600, "name": "N Jacqulin Jancy Rani"},
                    {"value": 1000, "name": "Gowtham "},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Value", 0, 6000, 0, 100)
    st.write("Selected Contribution >= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data

    # Display the chart using st_echarts
    st_echarts(options=options, height="800px")
