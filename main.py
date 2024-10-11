import streamlit as st

revs_input = st.number_input("Current REVS", min_value=0, step=1, key="rev_input")
rpms_input = st.number_input("Current RPMS", min_value=0, step=1, key="rpm_input")
doff_input = st.number_input("Doff REVS", min_value=0, step=1, key="doff_input")
calculate_time = st.button("Calculate")
