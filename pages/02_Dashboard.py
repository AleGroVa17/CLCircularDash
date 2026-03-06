import streamlit as st
from src.components.sidebar import render_sidebar
from src.state.session import init_session
from src.services.data_service import load_example_data

st.set_page_config(page_title="Dashboard", layout="wide")
init_session()
render_sidebar()

st.title("Dashboard")

df = load_example_data()
st.dataframe(df, use_container_width=True)

selected = st.selectbox("Selecciona un ID para detalle", df["id"].tolist())
st.session_state["selected_id"] = selected
st.success(f"Seleccionado: {selected}")