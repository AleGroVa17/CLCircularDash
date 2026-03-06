import streamlit as st
from src.components.sidebar import render_sidebar
from src.state.session import init_session
from src.services.model_service import run_model_example

st.set_page_config(page_title="Modelos", layout="wide")
init_session()
render_sidebar()

st.title("Modelos")

x = st.number_input("Input de prueba", value=10)
res = run_model_example(x)
st.json(res)