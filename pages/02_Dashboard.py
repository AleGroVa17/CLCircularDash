import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard")

df = pd.DataFrame(
    {"x": [1, 2, 3, 4, 5], "y": [10, 12, 9, 14, 13], "id": ["A", "B", "C", "D", "E"]}
)

fig = px.scatter(df, x="x", y="y", hover_data=["id"])
st.plotly_chart(fig, use_container_width=True)

st.write("Luego aquí haremos la selección de puntos y enviaremos el ID al detalle.")