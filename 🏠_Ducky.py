import streamlit as st

import helpers.sidebar

st.set_page_config(
    page_title="Ducky",
    page_icon="static/ducky_logo2.png",
    layout="wide"
)

helpers.sidebar.show()

st.toast("Welcome to Ducky!", icon="🐥")

st.markdown("Welcome to Ducky, your AI-powered software developer assistant!")
st.write("Ducky is designed to help you deliver software faster and better.")
