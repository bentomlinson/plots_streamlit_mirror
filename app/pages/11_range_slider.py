import streamlit as st
from plots.utils import add_range_slider

st.set_page_config(layout="wide")

if "fig1" in st.session_state:
    st.write("LIDAR wind speed vs 9999")
    fig = st.session_state["fig1"]
    fig = add_range_slider(fig)
    st.plotly_chart(fig, use_container_width=True)

# if "fig2" in st.session_state:
#     st.write("ADCP current speed and direction")
#     fig = st.session_state["fig2"]
#     fig = add_range_slider(fig)
#     st.plotly_chart(fig, use_container_width=True)
