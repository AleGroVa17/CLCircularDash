import streamlit as st

st.title("Detalle")

selected_id = st.session_state.get("selected_id")
if not selected_id:
    st.warning("No hay selección. Ve al Dashboard y selecciona un punto.")
else:
    st.write(f"Mostrando detalle de: {selected_id}")
    # aquí consultas/cargas info según selected_id
    