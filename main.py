import streamlit as st
import math

revs_input = st.number_input("Current REVS", min_value=0, value=None, step=1, placeholder=None, key="rev_input")
rpms_input = st.number_input("Current RPMS", min_value=0, value=None, step=1, key="rpm_input")
doff_input = st.number_input("Doff REVS", min_value=0, value=None, step=1, key="doff_input")
calculate_time = st.button("Calculate")

if calculate_time:
    revs_left = doff_input - revs_input
    time_1_left = revs_left / rpms_input
    if time_1_left > 60:
        time_2_left = round(time_1_left / 60, 2)
        first_cal = round(float(str(time_2_left-int(time_2_left))[1:]), 2)
        minutes = math.floor(first_cal * 60)
        st.write(str(int(time_2_left)) + "h", str(minutes) + "m")
    else:
        time_left = round(time_1_left, 2)
        sec_cal = round(float(str(time_left-int(time_left))[1:]), 2)
        seconds = math.floor(sec_cal * 60)
        st.write(str(int(time_1_left)) + "m", str(seconds) + "s")
