import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Graph
from streamlit_echarts import st_pyecharts
from pyecharts import options as opts

st.subheader("Welcome to the FR Team page where we can analyse our previous data")

st.write(":blue[Timesheets]: to Fill your tasks you have worked on for FR /Hope Trust Activites")

st.write(":blue[HopeTrust Expense]: You can submit you receipts here ")

st.write(":blue[Monthly Funds Tracker]: We can visualize our Monthly funds data,Track the Growth rate and analyze for future use")

st.write(":blue[Event Contributors]: We can visualize our Event Contributons done by our volunter, we can filter based on amount of donations and display it in chart")

st.write("We are still testing the application")

def main():
    st.title("Introducing Our Team")

    nodes = [
        {"name": "Subashini", "symbolSize": 50},
        {"name": "Madhusudhan", "symbolSize": 50},
        {"name": "Goutham", "symbolSize": 50},
        {"name": "Richard", "symbolSize": 50},
        {"name": "Naveen", "symbolSize": 50},
        {"name": "Sundhareshan", "symbolSize": 50},
        {"name": "Deepthe Priya", "symbolSize": 50},
        {"name": "Thiyagi", "symbolSize": 50},

    ]
    
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})

    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Welcome to Fund Raising Team"))
    )
    
    st_pyecharts(c, height = 500)


if __name__ == "__main__":
    main()


hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
