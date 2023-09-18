import streamlit as st
# from plots.plot1 import plot_wind_speed_vs_9999



if "fig1" in st.session_state:
    for _ in range(1):
        st.write("LIDAR wind speed vs 9999")
        st.plotly_chart(st.session_state["fig1"], use_container_width=True)

