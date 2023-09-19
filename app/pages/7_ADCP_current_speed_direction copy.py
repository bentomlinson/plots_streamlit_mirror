import streamlit as st
# from plots.plot2 import plot_adcp

st.set_page_config(layout="wide")

if "fig2" in st.session_state:
    for i in range(1, 2):
        st.write(f"ADCP current speed and direction ({i})")
        st.plotly_chart(st.session_state["fig2"], use_container_width=True)



# if "all_data" in st.session_state:
#     if "fig2" not in st.session_state:
#         df = st.session_state["all_data"]
#         fig2 = plot_adcp(df)
#         st.session_state["fig2"] = fig2
    
#     st.write("ADCP current speed and direction")
#     st.plotly_chart(st.session_state["fig2"], use_container_width=True)

#     st.write("ADCP current speed and direction")
#     st.plotly_chart(st.session_state["fig2"], use_container_width=True)

#     st.write("ADCP current speed and direction")
#     st.plotly_chart(st.session_state["fig2"], use_container_width=True)


# if "all_data" in st.session_state:
#     df = st.session_state["all_data"]
#     fig = plot_adcp(df)
#     st.plotly_chart(fig, use_container_width=True)

#     st.write("ADCP current speed and direction")
#     st.plotly_chart(fig, use_container_width=True)

#     st.write("ADCP current speed and direction")
#     st.plotly_chart(fig, use_container_width=True)
