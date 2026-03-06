import streamlit as st
from src.components.sidebar import render_sidebar
from src.state.session import init_session

st.set_page_config(
    page_title="CL Circular Dash",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()
render_sidebar()

st.title("CL Circular Dash")
st.write("Navega con el menú de la izquierda (páginas detectadas desde la carpeta `pages/`).")