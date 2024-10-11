import streamlit as st
from math import trunc

revs = st.text_input("Machines Current REVS")
rpm = st.text_input("Machines Current RPM")
doff = st.text_input("Machine DOFF REVS")
revs_input = int(revs)
rpm_input = int(rpm)
doff_input = int(doff)

revs_left = doff_input - revs_input
time_left_1 = revs_left / rpm_input
calculation = time_left_1
if time_left_1 > 60:
	calculation = time_left_1 / 60
	number_dec1 = trunc(calculation)
	number_dec2 = str(calculation - int(calculation))[1:]
	minutes_calc = float(number_dec2) * 60
	minutes_calc = trunc(minutes_calc)
	calculation = str(calculation)
	st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
else:
	calculation = round(calculation, 2)
	calculation = str(calculation)
	st.write(calculation, "minutes")