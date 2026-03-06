import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Dashboard")

df = pd.DataFrame({"x": [1,2,3,4,5], "y": [10,12,9,14,13]})
st.line_chart(df.set_index("x"))