import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts


check = st.selectbox(
    'Select the Events to see the Event Related Data',
    ('Event 22', 'Event 23', 'Event 25',"Event 26","Event 30","Event 32","Event 33-35","Event 36-37","Event 38","Event 40-43"))
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
elif check == "Event 26":
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 6000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px") 

elif check == "Event 30":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 30",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 7156, "name": "S.Sathish Kumar"},
                    {"value": 312, "name": "Rekha M"},
                    {"value": 780, "name": "R.Venkataramanan"},
                    {"value": 156, "name": "Y.M.Jagadeesh"},
                    {"value": 812, "name": "K.Habeebulla"},
                    {"value": 980, "name": "A.N.Mohamed Ismail Fazil"},
                    {"value": 256, "name": "P.B.Ravi Chandhar"},
                    {"value": 1700, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 156, "name": "K.R.Harish"},
                    {"value": 1716, "name": "B.Rupesh Kumar"},
                    {"value": 1468, "name": "N.Evangelin Ruby"},
                    {"value": 3556, "name": "A.Sandeep"},
                    {"value": 700, "name": "T.M Jai Pranesh"},
                    {"value": 156, "name": "T.Suriya Venkatesh"},
                    {"value": 512, "name": "R.Albert Paul"},
                    {"value": 1400, "name": "P.Sivaprashanth"},
                    {"value": 2156, "name": "P.Mythili "},
                    {"value": 500, "name": "Vignesh .R"},
                    {"value": 3546, "name": "S.Jothiram"},
                    {"value": 1000, "name": "S.Bharath kumar"},
                    {"value": 1000, "name": "V.Pranav Sabareesh"},
                    {"value": 1406, "name": "R.Pavithra"},
                    {"value": 500, "name": "A Mohan Raj"},
                    {"value": 1000, "name": "R.Rajesh"},
                    {"value": 2060, "name": "J Jacob Israel "},
                    {"value": 8356, "name": "S.Govindarajulu"},
                    {"value": 7500, "name": "M.Nishanth"},
                    {"value": 2500, "name": "Abirami"},
                    {"value": 1500, "name": "Sizana"},
                    {"value": 1500, "name": "Suji"},
                    {"value": 1500, "name": "N. Sai Charu"},
                    {"value": 2300, "name": "S.Sabarish"},
                    {"value": 800, "name": "Sridharan"},
                    {"value": 1000, "name": "Akshyan"},
                    {"value": 380, "name": "RM Nachammai"},
                    {"value": 2588, "name": "E. Dhinesh"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 9000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="900px") 


elif check == "Event 32":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 32",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 7700, "name": "S.Sathish Kumar"},
                    {"value": 1200, "name": "Y.M.Jagadeesh"},
                    {"value": 500, "name": "E.Subhashini"},
                    {"value": 500, "name": "T.M.Jai Pranesh"},
                    {"value": 4000, "name": "R.SathishKumar"},
                    {"value": 200, "name": "J.Joshva"},
                    {"value": 500, "name": "S.Bharath kumar"},
                    {"value": 900, "name": "S.Goutham"},
                    {"value": 2000, "name": "Ramkrish"},
                    {"value": 1500, "name": "Sridharan"},
                    {"value": 2000, "name": "Marketing"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 8000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px") 

elif check == "Event 33-35":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 33-35",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 5640, "name": "S.Sathish Kumar"},
                    {"value": 1000, "name": "R.Venkataramanan"},
                    {"value": 600, "name": "R.M.AbdulKhudus"},
                    {"value": 500, "name": "T.M.Jai Pranesh"},
                    {"value": 2170, "name": "K.Habeebulla"},
                    {"value": 700, "name": "A.N.Mohamed Ismail Fazil"},
                    {"value": 2000, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 227, "name": "K.R.Harish"},
                    {"value": 300, "name": "S.Chaitanya Karthik"},
                    {"value": 2000, "name": "A.Sandeep"},
                    {"value": 500, "name": "J.Jai Bharath"},
                    {"value": 500, "name": "S. Manigandan "},
                    {"value": 2000, "name": "R.SathishKumar"},
                    {"value": 1500, "name": "J.Joshva"},
                    {"value": 300, "name": "P.Mythili "},
                    {"value": 500, "name": "S.Bharath kumar"},
                    {"value": 2600, "name": "S.Goutham"},
                    {"value": 700, "name": "M.Nishanth"},
                    {"value": 900, "name": "Sizana "},
                    {"value": 250, "name": "Sridharan"},
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
    st_echarts(options=options, height="600px") 

elif check == "Event 36-37":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 33-37",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 3425, "name": "S.Sathish Kumar"},
                    {"value": 500, "name": "Rekha M"},
                    {"value": 500, "name": "Yuvashree S"},
                    {"value": 1200, "name": "B.Rupesh Kumar"},
                    {"value": 800, "name": "S.Parthasarathy"},
                    {"value": 125, "name": "K.Arun Kumar"},
                    {"value": 500, "name": "N.Evangelin Ruby"},
                    {"value": 500, "name": "A.Sandeep"},
                    {"value": 600, "name": "E.Subhashini"},
                    {"value": 15699, "name": "S. Manigandan "},
                    {"value": 2000, "name": "R.SathishKumar"},
                    {"value": 2850, "name": "P.Sivaprashanth"},
                    {"value": 5125, "name": "P.Mythili "},
                    {"value": 12675, "name": "S.Jothiram"},
                    {"value": 300, "name": "S.Bharath kumar"},
                    {"value": 16000, "name": "V.Pranav Sabareesh"},
                    {"value": 4000, "name": "R.Pavithra"},
                    {"value": 1000, "name": "V.Pratheba"},
                    {"value": 170, "name": "A.Franklin Yesudas "},
                    {"value": 4000, "name": " S.Govindarajulu"},
                    {"value": 250, "name": "N Jacqulin Jancy Rani"},
                    {"value": 1925, "name": "S.Goutham"},
                    {"value": 2000, "name": "Akshyan"},
                    {"value": 1000, "name": "P.R.Ravichandran"},
                    {"value": 500, "name": "S.Niveditha"},
                    {"value": 1000, "name": "D.Joshva Samvel"},
                    {"value": 1000, "name": "A.Sandhiya"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 16000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="800px") 

elif check == "Event 40-43":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 40-43",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 21650, "name": "S.Sathish Kumar"},
                    {"value": 1000, "name": "Rekha M"},
                    {"value": 500, "name": "R.Venkataramanan"},
                    {"value": 300, "name": "Y.M.Jagadeesh"},
                    {"value": 115, "name": "A.N.Mohamed Ismail Fazil"},
                    {"value": 200, "name": "K.Arun Kumar"},
                    {"value": 1000, "name": "A.Sandeep"},
                    {"value": 800, "name": "E.Subhashini"},
                    {"value": 500, "name": "J.Jai Bharath"},
                    {"value": 2000, "name": "R.Albert Paul"},
                    {"value": 500, "name": "R.Sakthi Vel"},
                    {"value": 115, "name": "K.Sridhar"},
                    {"value": 3000, "name": "P.Mythili "},
                    {"value": 300, "name": "S.Bharath kumar"},
                    {"value": 2000, "name": "A.Franklin Yesudas"},
                    {"value": 115, "name": "R.Rajesh"},
                    {"value": 780, "name": "S.Goutham"},
                    {"value": 1230, "name": "M.Nishanth"},
                    {"value": 445, "name": "R.Dinesh Balaji "},
                    {"value": 2110, "name": "Marketing"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 22000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="800px") 

elif check == "Event 38":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Event 38",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 9325, "name": "S.Sathish Kumar"},
                    {"value": 350, "name": "J.H.Abdul Kalam Azad"},
                    {"value": 700, "name": "K.R.Harish"},
                    {"value": 1500, "name": "S.Chaitanya Karthik"},
                    {"value": 800, "name": "B.Rupesh Kumar"},
                    {"value": 500, "name": "S.Parthasarathy"},
                    {"value": 10950, "name": "A.Sandeep"},
                    {"value": 800, "name": "S. Manigandan "},
                    {"value": 1000, "name": "R.Albert Paul"},
                    {"value": 2230, "name": "A.Franklin Yesudas"},
                    {"value": 600, "name": "R.Rajesh"},
                    {"value": 4000, "name": "S.Govindarajulu"},
                    {"value": 500, "name": "S.Goutham"},
                    {"value": 1175, "name": "M.Nishanth"},
                    {"value": 500, "name": "P.R.Ravichandran"},
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
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 16000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="800px") 
