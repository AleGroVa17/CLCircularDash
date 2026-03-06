import streamlit as st

st.set_page_config(
    page_title="Mi App",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Mi App en Streamlit")
st.write("Usa el menú de la izquierda para navegar entre las páginas.")

st.divider()
st.subheader("Navegación rápida")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/01_Inicio.py", label="Inicio", icon="🏠")

with col2:
    st.page_link("pages/02_Dashboard.py", label="Dashboard", icon="📊")

with col3:
    st.page_link("pages/03_Detalle.py", label="Detalle", icon="🔎")