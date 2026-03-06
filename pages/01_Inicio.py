import streamlit as st
from src.components.sidebar import render_sidebar
from src.state.session import init_session

init_session()
render_sidebar()

st.title("Inicio")
st.write("Aquí puedes poner resumen, KPIs principales, y links internos.")