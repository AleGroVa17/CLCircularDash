import streamlit as st
from src.components.sidebar import render_sidebar
from src.state.session import init_session

init_session()
render_sidebar()

st.title("Detalle")

selected_id = st.session_state.get("selected_id")
if not selected_id:
    st.warning("No hay selección. Ve al Dashboard y elige un ID.")
else:
    st.write(f"Mostrando detalle para: {selected_id}")