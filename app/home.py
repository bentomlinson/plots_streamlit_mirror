import streamlit as st
from plots.utils import import_df
from plots.plot1 import plot_wind_speed_vs_9999
from plots.plot2 import plot_adcp

fig_map = {
    "fig1": plot_wind_speed_vs_9999,
    "fig2": plot_adcp,
}



@st.cache_resource
def load_data(file_path):
    return import_df(file_path)


def uploader_callback():
    for fig_name in fig_map.keys():
        if fig_name in st.session_state:
            del st.session_state[fig_name]


st.set_page_config(layout="centered")


uploaded_file =  st.file_uploader("Upload a data file.", on_change=uploader_callback)

if uploaded_file is not None:
    st.session_state["file_name"] = uploaded_file.name
    st.session_state["all_data"] = load_data(uploaded_file)

if "file_name" in st.session_state:
    st.write(st.session_state["file_name"])

if "all_data" in st.session_state:
    df = st.session_state["all_data"]
    st.dataframe(df)

    for fig_name, plot_func in fig_map.items():
        if fig_name not in st.session_state:
            fig = plot_func(df)
            # fig.update_layout({"uirevision": "foo"}, overwrite=True)
            st.session_state[fig_name] = fig

