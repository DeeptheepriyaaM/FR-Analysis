import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts

st.title("Monthly Funds Tracker")

options = {
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["2023","2022", "2021", "2020"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug","Sep","Oct","Nov","Dec"],
    },
    "yAxis": {"type": "value"},
    "series": [
                {
            "name": "2023",
            "type": "line",
            "stack": "Total",
            "data": [1000, 1000, 900, 900, 600],
        },
        {
            "name": "2022",
            "type": "line",
            "stack": "Total",
            "data": [2100, 2100, 2100, 1900, 1800, 1600, 1400, 1300, 1100, 1000, 600, 600],
        },
        {
            "name": "2021",
            "type": "line",
            "stack": "Total",
            "data": [3500, 3000, 3000, 3000, 2900, 2700, 2500, 2300, 2200, 2000, 1800, 1400],
        },
        {
            "name": "2020",
            "type": "line",
            "stack": "Total",
            "data": [5150, 4900, 4600, 4700, 4900, 4600, 4400, 4000, 3600, 2800, 2200, 2000],
        },
    ],
}
st_echarts(options=options, height="400px")

st.divider()
st.subheader("Total Monthly Funds Collected based On Catagories")

st.write("Total: of 2023 :","?")
st.write("Total: of 2022 :", 17600)
st.write("Total: of 2021 :",30300)
st.write("Total: of 2020 :",47850)

options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Working People", "Students", "Jobless"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["2022", "2021", "2020"],
    },
    "series": [
        {
            "name": "Working People",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [15000,25000,38000]
        },
        {
            "name": "Students",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [1600, 4800, 6850],
        },
        {
            "name": "Jobless",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [1000, 500, 3000],
        },
    ],
}
st_echarts(options=options, height="500px")
