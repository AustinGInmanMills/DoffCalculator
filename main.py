import streamlit as st
from math import trunc

revs_input = st.number_input("Current REVS", min_value=0, value=None, step=1, placeholder=None, key="rev_input")
rpms_input = st.number_input("Current RPMS", min_value=0, value=None, step=1, key="rpm_input")
doff_input = st.number_input("Doff REVS", min_value=0, value=None, step=1, key="doff_input")
calculate_time = st.button("Calculate")

if calculate_time:
    revs_left = float(doff_input) - float(revs_input)
    time_1_left = revs_left / float(rpms_input)
    if time_1_left > 60:
        time_2_left = time_1_left / 60
        calculation_1 = trunc(time_2_left)
        calculation_2 = str(calculation_1 - calculation_1)[1:]
        min_cal = calculation_2 * 60
        min_cal = trunc(min_cal)
        calculation = str(time_2_left)
        st.write(str(calculation_1), "hour and", str(min_cal), "minutes left")
    else:
        time_1_left = round(time_1_left, 2)
        time_1_left = str(time_1_left)
        st.write(time_1_left, "minutes left")
