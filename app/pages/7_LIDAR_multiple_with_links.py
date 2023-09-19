import streamlit as st
# from plots.plot1 import plot_wind_speed_vs_9999

st.set_page_config(layout="wide")

st.subheader("Quick links to figures")

st.markdown("[LIDAR wind speed vs 9999 (1)](#lidar-wind-speed-vs-9999-1)")
st.markdown("[LIDAR wind speed vs 9999 (2)](#lidar-wind-speed-vs-9999-2)")
st.markdown("[LIDAR wind speed vs 9999 (3)](#lidar-wind-speed-vs-9999-3)")
st.markdown("[LIDAR wind speed vs 9999 (4)](#lidar-wind-speed-vs-9999-4)")
st.markdown("[LIDAR wind speed vs 9999 (5)](#lidar-wind-speed-vs-9999-5)")
st.markdown("[LIDAR wind speed vs 9999 (6)](#lidar-wind-speed-vs-9999-6)")
st.markdown("[LIDAR wind speed vs 9999 (7)](#lidar-wind-speed-vs-9999-7)")
st.markdown("[LIDAR wind speed vs 9999 (8)](#lidar-wind-speed-vs-9999-8)")
st.markdown("[LIDAR wind speed vs 9999 (9)](#lidar-wind-speed-vs-9999-9)")
st.markdown("[LIDAR wind speed vs 9999 (10)](#lidar-wind-speed-vs-9999-10)")



st.subheader("LIDAR wind speed vs 9999 (1)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (2)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (3)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (4)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (5)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (6)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (7)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (8)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (9)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


st.subheader("LIDAR wind speed vs 9999 (10)")
if "fig1" in st.session_state:
    st.plotly_chart(st.session_state["fig1"], use_container_width=True)


# if "fig1" in st.session_state:
#     for i in range(1, 6):
#         st.write(f"LIDAR wind speed vs 9999 ({i})")
#         st.plotly_chart(st.session_state["fig1"], use_container_width=True)

