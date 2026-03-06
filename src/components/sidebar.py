import streamlit as st

def render_sidebar():
    st.sidebar.title("CL Circular Dash")
    st.sidebar.caption("Navegación por páginas")
    st.sidebar.divider()

    # Lugar para filtros globales después
    # Ej: fechas, cliente, etc.