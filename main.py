from math import trunc

import streamlit as st

machine_1 = 1600
machine_1_rpms = 15

machine_2 = 1600
machine_2_rpms = 15

machine_3 = 1600
machine_3_rpms = 15

machine_4 = 1600
machine_4_rpms = 15

machine_5 = 1600
machine_5_rpms = 15

machine_6 = 1600
machine_6_rpms = 15

machine_7 = 1600
machine_7_rpms = 15

machine_8 = 1600
machine_8_rpms = 15

machine_9 = 1600
machine_9_rpms = 15

machine_10 = 1600
machine_10_rpms = 15

machine_11 = 1600
machine_11_rpms = 15

machine_12 = 1600
machine_12_rpms = 15

machine_13 = 1600
machine_13_rpms = 15

machine_14 = 1600
machine_14_rpms = 15

machine_15 = 1600
machine_15_rpms = 15

machine_16 = 1600
machine_16_rpms = 15

machine_17 = 1600
machine_17_rpms = 10

machine_18 = 1600
machine_18_rpms = 8

machine_19 = 1600
machine_19_rpms = 15

machine_20 = 1600
machine_20_rpms = 15

machine_21 = 1600
machine_21_rpms = 15

machine_22 = 1600
machine_22_rpms = 15

st.header("Inman Mills | Doff Calculator [V1.0.0]", divider="rainbow")

st.subheader("Machine #1 | :red[Status Down]")
st.write("DOFF = ", int(machine_1))
st.write("RPMS = ", int(machine_1_rpms))
machine_current_revs = st.text_input("Current REVS", "0", key="1")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_1 - machine_current_revs
    calculation = calculation / machine_1_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #2 | :red[Status Down]")
st.write("DOFF = ", int(machine_2))
st.write("RPMS = ", int(machine_2_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="2")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_2 - machine_current_revs
    calculation = calculation / machine_2_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #3 | :green[Status Running]")
st.write("DOFF = ", int(machine_3))
st.write("RPMS = ", int(machine_3_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="3")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #4 | :green[Status Running]")
st.write("DOFF = ", int(machine_4))
st.write("RPMS = ", int(machine_4_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="4")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #5 | :green[Status Running]")
st.write("DOFF = ", int(machine_5))
st.write("RPMS = ", int(machine_5_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="5")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #6 | :green[Status Running]")
st.write("DOFF = ", int(machine_6))
st.write("RPMS = ", int(machine_6_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="6")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #7 | :green[Status Running]")
st.write("DOFF = ", int(machine_7))
st.write("RPMS = ", int(machine_7_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="7")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #8 | :green[Status Running]")
st.write("DOFF = ", int(machine_8))
st.write("RPMS = ", int(machine_8))
machine_current_revs = st.text_input("Current Revs", "0", key="8")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #9 | :green[Status Running]")
st.write("DOFF = ", int(machine_9))
st.write("RPMS = ", int(machine_9_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="9")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #10 | :red[Status Down]")
st.write("DOFF = ", int(machine_10))
st.write("RPMS = ", int(machine_10_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="10")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #11 | :green[Status Running]")
st.write("DOFF = ", int(machine_11))
st.write("RPMS = ", int(machine_11_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="11")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #12 | :green[Status Running]")
st.write("DOFF = ", int(machine_12))
st.write("RPMS = ", int(machine_12_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="12")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #13 | :green[Status Running]")
st.write("DOFF = ", int(machine_13))
st.write("RPMS = ", int(machine_13_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="13")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #14 | :red[Status Down]")
st.write("DOFF = ", int(machine_14))
st.write("RPMS = ", int(machine_14_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="14")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #15 | :green[Status Running]")
st.write("DOFF = ", int(machine_15))
st.write("RPMS = ", int(machine_15_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="15")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #16 | :green[Status Running]")
st.write("DOFF = ", int(machine_16))
st.write("RPMS = ", int(machine_16_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="16")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #17 | :green[Status Running]")
st.write("DOFF = ", int(machine_17))
st.write("RPMS = ", int(machine_17_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="17")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #18 | :green[Status Running]")
st.write("DOFF = ", int(machine_18))
st.write("RPMS = ", int(machine_18_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="18")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #19 | :green[Status Running]")
st.write("DOFF = ", int(machine_19))
st.write("RPMS = ", int(machine_19_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="19")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #20 | :green[Status Running]")
st.write("DOFF = ", int(machine_20))
st.write("RPMS = ", int(machine_20_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="20")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #21 | :green[Status Running]")
st.write("DOFF = ", int(machine_21))
st.write("RPMS = ", int(machine_21_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="21")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #22 | :green[Status Running]")
st.write("DOFF = ", int(machine_22))
st.write("RPMS = ", int(machine_22_rpms))
machine_current_revs = st.text_input("Current Revs", "0", key="22")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        number_dec1 = trunc(calculation)
        number_dec2 = str(calculation - int(calculation))[1:]
        minutes_calc = float(number_dec2) * 60
        minutes_calc = trunc(minutes_calc)
        calculation = str(calculation)
        st.write(str(number_dec1), "hour and",str(minutes_calc),"minutes")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass
