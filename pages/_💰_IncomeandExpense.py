import streamlit as st
from streamlit_echarts import st_echarts
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from streamlit_echarts import st_pyecharts
import pandas as pd

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



st.header("Year wise Expenses")

# Define data
attr = ["Events", "Office Expenses", "Donations", "Event Other Expenses", "Other Expenses"]
# Replace the following values with your own data for each year
values_2018 = [100, 200, 150, 300, 120]
values_2019 = [120, 150, 180, 250, 110]
values_2021 = [80, 120, 250, 180, 90]
values_2022 = [200, 180, 160, 280, 150]
values_2023 = [150, 220, 170, 260, 100]

tl = Timeline()

# Create Pie charts for each year in the timeline
for i, values in zip(range(2018, 2023), [values_2018, values_2019, values_2021, values_2022, values_2023]):
    pie = (
        Pie()
        .add(
            "Check",
            [list(z) for z in zip(attr, values)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("{}".format(i)))
    )
    tl.add(pie, "{}".format(i))

# Render the Pie chart timeline using st_echarts

st_pyecharts(tl,height = 500)

if st.checkbox("Show Data Table"):
    st.subheader("Year-wise Expenses Data")
    st.write("2018")
    st.write(pd.DataFrame({"Categories": attr, "Expenses": values_2018}))
    st.write("2019")
    st.write(pd.DataFrame({"Categories": attr, "Expenses": values_2019}))
    st.write("2021")
    st.write(pd.DataFrame({"Categories": attr, "Expenses": values_2021}))
    st.write("2022")
    st.write(pd.DataFrame({"Categories": attr, "Expenses": values_2022}))
    st.write("2023")
    st.write(pd.DataFrame({"Categories": attr, "Expenses": values_2023}))

hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
