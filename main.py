import streamlit as st

revs_input = st.number_input("Current REVS", min_value=0, step=1, key="rev_input")
