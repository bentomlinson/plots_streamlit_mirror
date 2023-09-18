import streamlit as st
# from plots.plot1 import plot_wind_speed_vs_9999



if "fig1" in st.session_state:
    for i in range(1, 6):
        st.write(f"LIDAR wind speed vs 9999 ({i})")
        st.plotly_chart(st.session_state["fig1"], use_container_width=True)


# if "all_data" in st.session_state:
#     if "fig1" not in st.session_state:
#         df = st.session_state["all_data"]
#         fig = plot_wind_speed_vs_9999(df)
#         st.session_state["fig1"] = fig

#     st.write("LIDAR wind speed vs 9999")
#     st.plotly_chart(st.session_state["fig1"], use_container_width=True)

#     st.write("LIDAR wind speed vs 9999")
#     st.plotly_chart(st.session_state["fig1"], use_container_width=True)

#     st.write("LIDAR wind speed vs 9999")
#     st.plotly_chart(st.session_state["fig1"], use_container_width=True)

#     st.write("LIDAR wind speed vs 9999")
#     st.plotly_chart(st.session_state["fig1"], use_container_width=True)


# if "all_data" in st.session_state:
#     df = st.session_state["all_data"]
#     fig = plot_wind_speed_vs_9999(df)

#     st.write("LIDAR wind speed vs 9999")
#     st.plotly_chart(fig, use_container_width=True)