import streamlit as st

st.set_page_config(layout="wide")

col1, col2, _, _ = st.columns(4)

with col1:
    option1 = st.selectbox("Select a figure to plot", ("-", "fig1", "fig2"), key="option1")

with col2:
    option2 = st.selectbox("Select a figure to plot", ("-", "fig1", "fig2"), key="option2")


if option1 in st.session_state:
    st.plotly_chart(st.session_state[option1], use_container_width=True)

if option2 in st.session_state:
    st.plotly_chart(st.session_state[option2], use_container_width=True)
