import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Scatter
from streamlit_echarts import st_pyecharts

def main():
    st.title(" Total Contributions done by our volunteers till now")

    # List of x-axis values (names)
    x_data = [
        "VL-01S.Sathish Kumar", "VL-02Rekha M", "VL-03Yuvashree S", "VL-57Khuthubudin",
        "VL-06R.Venkataramanan", "VL-07R.Abhinav", "VL-08R.PraveenKumar", "VL-09R.M.AbdulKhudus",
        "VL-11Y.M.Jagadeesh", "VL-12P.L.Raju", "VL-13K.Habeebulla", "VL-15A.N.Mohamed Ismail Fazil",
        "VL-17P.B.Ravi Chandhar", "VL-19J.H.Abdul Kalam Azad", "VL-21K.R.Harish", "VL-23S.Chaitanya Karthik",
        "VL-24B.Rupesh Kumar", "VL-25S.Parthasarathy", "VL-29N.Venkateshwaran", "VL-35K.Arun Kumar",
        "VL-142Richard", "VL-143Bharath", "VL-144Ram", "VL-146Karthick", "VL-147Abirami",
        "VL-148Sizana", "VL-149Suji", "VL-150Sai charu", "VL-151Sabarish", "VL-152Sridharan",
        "VL-153Santhosh", "VL-154Naveen", "VL-155Muthuvel", "VL-156Madhan", "VL-157Sridhar",
        "VL-158Kousalya", "VL-159Anand", "VL-160Hemesh", "VL-161Andrew", "VL-162Akshyan",
        "VL-163Yashwanth", "VL-164Nachammai", "VL-165Sriddhi", "VL-166Priya", "VL-167P.R.Ravichandran",
        "VL-168D.Sudharsan", "VL-169J.Mathumitha", "VL-170S.Niveditha", "VL-171K.Vignesh Kumar",
        "VL-172J.Jency", "VL-173N.Deepika", "VL-174D.Joshva Samvel", "VL-175E.Dhinesh",
        "VL-176A.Babu", "VL-177A.Sandhiya", "VL-178V. A. Naveen", "VL-179D.Kalaivani", "VL-180R.Prabhu",
        "VL-181R. Dinesh Balaji", "VL-182J.Subash Chander Bose", "VL-183S.Samaya Prasanna Giridharan",
        "VL-184J.Amalesh", "VL-185M.Bremi", "VL-186C.Sukesh Sai Ram", "VL-187M.Abishek",
        "VL-188P.Madhan", "VL-189K.Mohanaganesh", "VL-190K.Thiyagarajan", "VL-191A.Ramachandran",
        "VL-192Mahalakshmi .L", "VL-193A.Sundhareshwaran", "VL-194R.Vengkat Raman", "VL-195M.Keerthana",
        "VL-196M.Deepthee priyaa", "VL-197S.Gayathri", "VL-198S.Padmaja", "VL-199R.Vikraman",
        "Vl-183S.Samaya Prasanna Giridharan", "VL-184J.Amalesh", "VL-185M.Bremi", "VL-186C.Sukesh Sai Ram",
        "VL-187M.Abishek", "VL-188P.Madhan", "VL-189K.Mohanaganesh", "VL-190K.Thiyagarajan", "VL-191A.Ramachandran",
        "VL-192Mahalakshmi .L", "VL-193A.Sundhareshwaran", "VL-194R.Vengkat Raman", "VL-195M.Keerthana",
        "VL-196M.Deepthee priyaa", "VL-197S.Gayathri", "VL-198S.Padmaja", "VL-199R.Vikraman"
    ]

    # List of y-axis values (numerical data)
    y_data = [
        60520, 0, 0, 1300, 2200, 0, 0, 1900, 1700, 0, 1400, 700, 4150, 6700, 1700, 1200, 800, 2200, 800, 1310,
        300, 8800, 600, 3100, 2500, 0, 0, 700, 4800, 1200, 1100, 3301, 100, 1200, 3600, 900, 600, 0, 0, 900, 1000,
        0, 200, 3200, 1100, 1300, 2850, 1300, 1100, 800, 200, 20750, 1200, 3350, 700, 2350, 900, 0, 800, 500, 500,
        1200, 4000, 1000, 3300, 5500, 3590, 600, 600, 4450, 500, 5800, 700, 0, 100, 0, 3000, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]

    # Filter for selecting a range of numbers
    range_filter = st.slider("Select a range of numbers:", min(y_data), max(y_data), (min(y_data), max(y_data)))

    # Filter to remove zeros from y_data
    remove_zeros = st.checkbox("Remove zeros from the bar graph")

    # Applying the filters
    filtered_x_data = []
    filtered_y_data = []
    for x, y in zip(x_data, y_data):
        if remove_zeros and y == 0:
            continue
        if y >= range_filter[0] and y <= range_filter[1]:
            filtered_x_data.append(x)
            filtered_y_data.append(y)

    # Creating the bar chart
    c = (
        Bar()
        .add_xaxis(filtered_x_data)
        .add_yaxis("Values", filtered_y_data, color="#3182bd")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom (slider+inside)"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )

    # Display the bar chart using Streamlit
    st_pyecharts(c,height = 600)

if __name__ == "__main__":
    main()


def scatter_visualmap_size(data_x, data_y1, data_y2,data_y3, data_y4):
    c = (
        Scatter()
        .add_xaxis(data_x)
        .add_yaxis("Event Management", data_y1)
        .add_yaxis("Needy Hunters", data_y2)
        .add_yaxis("Internal Stren", data_y3)
        .add_yaxis("DM", data_y4)
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
        )
    )
    
    return c

# Replace these lists with your actual data
data_x = ["2020", "2021", "2022", "2023"]
data_y1 = [100, 80, 120, 70]
data_y2 = [20, 60, 90, 70]
data_y3 = [43, 34, 340, 30]
data_y4 = [30, 40, 60, 70]

st.subheader("Funds Contributions(Monthlyfunds + Event Contributions) Totally based on the Team ")
final_chart = scatter_visualmap_size(data_x, data_y1, data_y2,data_y3, data_y4)
st_pyecharts(final_chart, height=500)

hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
