import streamlit as st

machine_1 = 1600
machine_1_rpms = 15
machine_2 = 1600
machine_2_rpms = 15
machine_3 = 1600
machine_3_rpms = 15

st.header("Inman Mills | Doff Calculator [V1.0.0]", divider="rainbow")

st.subheader("Machine #1")
machine_current_revs = st.text_input("Current Revs", "0", key="1")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_1 - machine_current_revs
    calculation = calculation / machine_1_rpms
    if calculation > 60:
        calculation = calculation / 60
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "hours left")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #2")
machine_current_revs = st.text_input("Current Revs", "0", key="2")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_2 - machine_current_revs
    calculation = calculation / machine_2_rpms
    if calculation > 60:
        calculation = calculation / 60
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "hours left")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass

st.divider()

st.subheader("Machine #3")
machine_current_revs = st.text_input("Current Revs", "0", key="3")
try:
    machine_current_revs = float(machine_current_revs)
    calculation = machine_3 - machine_current_revs
    calculation = calculation / machine_3_rpms
    if calculation > 60:
        calculation = calculation / 60
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "hours left")
    else:
        calculation = round(calculation, 2)
        calculation = str(calculation)
        st.write(calculation, "minutes")
except:
    pass
