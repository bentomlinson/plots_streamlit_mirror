import streamlit as st  

from plots.utils import import_and_prepare_data


@st.cache_resource
def load_data(file_path):
    return import_and_prepare_data(file_path)

st.set_page_config(layout="centered")

uploaded_file =  st.file_uploader("Upload a data file.")

if uploaded_file is not None:
    st.session_state["file_name"] = uploaded_file.name
    df = load_data(uploaded_file)
    st.session_state["all_data"] = df

if "file_name" in st.session_state:
    st.write(st.session_state["file_name"])

if "all_data" in st.session_state:
    df = st.session_state["all_data"]
    st.dataframe(df)
