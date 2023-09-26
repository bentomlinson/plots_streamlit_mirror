import pandas as pd
import streamlit as st
from plots.dynamic import make_dynamic_plot
from streamlit_extras.switch_page_button import switch_page

if "all_data" not in st.session_state:
    switch_page("home")

VARS = list(st.session_state["all_data"].columns)
AXES = ["Left", "Right"]
PLOT_TYPES = ["Line", "Scatter"]
COLORS = [
    "#F90000",
    "#F99500",
    "#57F900",
    "#00F9AF",
    "#00AFF9",
    "#0009F9",
    "#8C00F9",
    "#EC00F9",
]


def add_row():
    st.session_state.rows += 1


def delete_row(idx):
    st.session_state.rows -= 1
    parameters_df = st.session_state.parameters_df
    parameters_df = parameters_df.drop(idx).reset_index(drop=True)
    st.session_state.parameters_df = parameters_df
    del st.session_state.deletes[idx]


def get_range(axis):
    slider_percent = 0.2
    start_percent = 0.05
    parameters_df = st.session_state["parameters_df"]
    df = st.session_state["all_data"]
    vars_ = parameters_df[parameters_df["axis"] == axis]["variable"]
    min_value = df[vars_].min().min()
    max_value = df[vars_].max().max()
    diff = max_value - min_value
    slider_min = min_value - slider_percent * diff
    slider_max = max_value + slider_percent * diff
    start_min = min_value - start_percent * diff
    start_max = max_value + start_percent * diff
    return (slider_min, slider_max, (start_min, start_max))


if "rows" not in st.session_state:
    st.session_state.rows = 0
    st.session_state.parameters_df = pd.DataFrame(
        columns=["variable", "axis", "plot_type", "color"]
    )
    st.session_state.deletes = []
    st.session_state.fig_params = dict()


st.set_page_config(layout="wide")

st.header("Select variables to plot")


for i in range(st.session_state.rows):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        params = st.session_state.parameters_df
        index = VARS.index(params.loc[i, "variable"]) if len(params) > i else 0
        var = st.selectbox("Variable", VARS, index=index, key=f"var{i}")
        st.session_state.parameters_df.loc[i, "variable"] = var

    with col2:
        axis = st.session_state.parameters_df.loc[i, "axis"]
        index = AXES.index(axis) if axis in AXES else 0
        axis = st.selectbox("Y-axis", AXES, index=index, key=f"axis{i}")
        st.session_state.parameters_df.loc[i, "axis"] = axis

    with col3:
        plot_type = st.session_state.parameters_df.loc[i, "plot_type"]
        index = PLOT_TYPES.index(plot_type) if plot_type in PLOT_TYPES else 0
        plot_type = st.selectbox(
            "Plot type", PLOT_TYPES, index=index, key=f"plot_type{i}"
        )
        st.session_state.parameters_df.loc[i, "plot_type"] = plot_type

    with col4:
        color = st.session_state.parameters_df.loc[i, "color"]
        value = color if isinstance(color, str) else COLORS[i % len(COLORS)] 
        color = st.color_picker("Color", value, key=f"color{i}")
        st.session_state.parameters_df.loc[i, "color"] = color

    with col5:
        del_var = st.button("❌", key=f"delete{i}", on_click=delete_row, args=(i,))
        st.session_state.deletes.append(del_var)

st.button("➕ Add variable", on_click=add_row)

# debugging purposes
# st.dataframe(st.session_state.parameters_df)
# st.write(get_range("Left"))
# st.write(get_range("Right"))


col11, col12, _, _ = st.columns(4)

with col11:
    if "Left" in st.session_state.parameters_df["axis"].values:
        min_value, max_value, value = get_range("Left")
        left_range = st.slider(
            "Left y-axis range", min_value, max_value, value, key="left_range"
        )
        st.session_state.fig_params["left_range"] = left_range

with col12:
    if "Right" in st.session_state.parameters_df["axis"].values:
        min_value, max_value, value = get_range("Right")
        right_range = st.slider(
            "Right y-axis range", min_value, max_value, value, key="right_range"
        )
        st.session_state.fig_params["right_range"] = right_range


if st.button("Create plot"):
    df = st.session_state["all_data"]
    parameters_df = st.session_state["parameters_df"]
    fig_params = st.session_state["fig_params"]
    fig = make_dynamic_plot(df, parameters_df, fig_params)
    st.plotly_chart(fig, use_container_width=True)


# with st.form(key='columns_in_form'):
#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         var1 = st.selectbox("Variable", VARS, key="var1")
#         var2 = st.selectbox("", VARS, key="var2")

#     with col2:
#         var1_axis = st.selectbox("Vertical axis", AXES, key="var1_axis")
#         var2_axis = st.selectbox("", AXES, key="var2_axis")

#     submitButton = st.form_submit_button(label = 'Create plot')


# if submitButton:
#     df = st.session_state["all_data"]
#     fig = make_dynamic_plot(df, var1, var2, var1_axis, var2_axis)
#     st.plotly_chart(fig, use_container_width=True)


# if st.button('Create plot'):
#     df = st.session_state["all_data"]
#     fig = make_dynamic_plot(df, var1, var2, var1_axis, var2_axis)
#     st.plotly_chart(fig, use_container_width=True)
