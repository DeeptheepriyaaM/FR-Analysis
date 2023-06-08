import streamlit as st
from streamlit_echarts import st_echarts

st.title("Income and Expense Tracker")

# Data for the bar graph
bar_option = {
    "tooltip": {
        "trigger": 'axis',
        "axisPointer": {
            "type": 'shadow'
        }
    },
    "legend": {
        "data": ['Balance-Amount', 'Expenses', 'Income']
    },
    "grid": {
        "left": '3%',
        "right": '4%',
        "bottom": '3%',
        "containLabel": True
    },
    "xAxis": [
        {
            "type": 'value'
        }
    ],
    "yAxis": [
        {
            "type": 'category',
            "axisTick": {
                "show": False
            },
            "data": ['2020', '2021', '2022']
        }
    ],
    "series": [
        {
            "name": 'Balance-Amount',
            "type": 'bar',
            "label": {
                "show": True,
                "position": 'inside'
            },
            "emphasis": {
                "focus": 'series'
            },
            "data": [47165, 22970, 0]
        },
        {
            "name": 'Income',
            "type": 'bar',
            "stack": 'Total',
            "label": {
                "show": True
            },
            "emphasis": {
                "focus": 'series'
            },
            "data": [146581, 101690, 0]
        },
        {
            "name": 'Expenses',
            "type": 'bar',
            "stack": 'Total',
            "label": {
                "show": True,
                "position": 'left'
            },
            "emphasis": {
                "focus": 'series'
            },
            "data": [-99461, -125885, 0]
        }
    ]
}
st_echarts(options=bar_option, height="400px")
# Render the bar graph

