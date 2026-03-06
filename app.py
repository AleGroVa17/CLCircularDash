import streamlit as st

st.set_page_config(page_title="Mi App", layout="wide")

st.title("Mi App en Streamlit")
st.write("Accesos rápidos:")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/01_Inicio.py", label="Inicio")

with col2:
    st.page_link("pages/02_Dashboard.py", label="Dashboard")

with col3:
    st.page_link("pages/03_Detalle.py", label="Detalle")