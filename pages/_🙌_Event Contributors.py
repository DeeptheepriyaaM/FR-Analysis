import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts


check = st.selectbox(
    'Select the Events to see the Event Related Data',
    ('Event 22', 'Event 23', 'Event 25',"Event 26"))
st.subheader(":blue[Fund Raised By our Voulunteer For the Events]:")

if check == 'Event 22':
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 6000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="800px")
elif check == "Event 23":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 23",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 2000, "name": "S.Sathish Kumar"},
                    {"value": 1000, "name": "N. Evangelin Ruby"},
                    {"value": 500, "name": "Thalin Dakshi"},
                    {"value": 500, "name": "S. Bharath Kumar"},
                    {"value": 1000, "name": "Navudu Devi Anudeesh"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 2000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px")
elif check == "Event 25":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 25",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 24530, "name": "S.Sathish Kumar"},
                    {"value": 1300, "name": "P.B.Ravi Chandhar"},
                    {"value": 500, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 600, "name": "N.Evangelin Ruby"},
                    {"value": 1500, "name": "A.Sandeep"},
                    {"value": 300, "name": "J.Jai Bharath"},
                    {"value": 1500, "name": "T.M.Jai Pranesh"},
                    {"value": 3300, "name": "R.Albert Paul"},
                    {"value": 500, "name": "P.Mythili"},
                    {"value": 8100, "name": "S.Jothiram"},
                    {"value": 500, "name": "S.Bharath kumar"},
                    {"value": 450, "name": "V.Pranav Sabareesh"},
                    {"value": 300, "name": "V.Lisanraj"},
                    {"value": 1000, "name": "B.Santhosh"},
                    {"value": 300, "name": "R.Rajesh"},
                    {"value": 1000, "name": "J Jacob Israel"},
                    {"value": 1500, "name": "Navudu Devi Anudeesh"},
                    {"value": 1150, "name": "N Jacqulin Jancy Rani"},
                    {"value": 1000, "name": "Goutham"},
                    {"value": 100, "name": "Richard"},
                    {"value": 3000, "name": "Ram"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 25000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)
    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px")
else:
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 26",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 500, "name": "P.B.Ravi Chandhar"},
                    {"value": 3500, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 700, "name": "S.Parthasarathy"},
                    {"value": 1310, "name": "K.Arun Kumar"},
                    {"value": 2000, "name": "T.M.Jai Pranesh"},
                    {"value": 500, "name": "P.Mythili"},
                    {"value": 5850, "name": "S.Jothiram"},
                    {"value": 700, "name": "S.Bharath kumar"},
                    {"value": 1000, "name": "Navudu Devi Anudeesh"},
                    {"value": 3000, "name": "Goutham"},
                    {"value": 300, "name": "Nishanth"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 25000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px") 
