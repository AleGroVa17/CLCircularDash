import streamlit as st

st.set_page_config(page_title="Mi App", layout="wide")

st.title("Mi App en Streamlit")
st.write("Navega con el menú de la izquierda. Streamlit detecta automáticamente los archivos dentro de la carpeta `pages/`.")

st.subheader("Debug: páginas detectadas")
st.json(list(st.get_pages("").values()))