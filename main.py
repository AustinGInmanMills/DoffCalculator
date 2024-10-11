import streamlit as st
from math import trunc

revs_input = st.number_input("Current REVS", min_value=0, value=None, step=1, placeholder=None, key="rev_input")
rpms_input = st.number_input("Current RPMS", min_value=0, value=None, step=1, key="rpm_input")
doff_input = st.number_input("Doff REVS", min_value=0, value=None, step=1, key="doff_input")
calculate_time = st.button("Calculate")

if calculate_time:
    try:
        revs_left = float(doff_input) - float(revs_input)
        time_1_left = revs_left / float(rpms_input)
        if time_1_left > 60:
            time_2_left = time_1_left / 60
            st.write(time_2_left)
            calculation_1 = trunc(time_2_left)
            st.write(calculation_1)
    except:
        pass
