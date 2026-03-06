import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard")

df = pd.DataFrame({
    "x": [1,2,3,4,5],
    "y": [10,12,9,14,13],
    "id": ["A","B","C","D","E"]
})

fig = px.scatter(df, x="x", y="y", hover_data=["id"])
event = st.plotly_chart(fig, use_container_width=True, on_select="rerun")

# Streamlit captura selección (si tu versión lo soporta con Plotly)
# Si no, lo resolvemos con tabla + selector.
if event and "selection" in event and event["selection"]["points"]:
    selected = event["selection"]["points"][0]
    st.session_state["selected_id"] = df.iloc[selected["pointIndex"]]["id"]
    st.success(f"Seleccionaste: {st.session_state['selected_id']}")
    st.page_link("pages/03_Detalle.py", label="Ir a detalle", icon="➡️")