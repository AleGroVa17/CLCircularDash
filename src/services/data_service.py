import pandas as pd
import streamlit as st

@st.cache_data
def load_example_data():
    return pd.DataFrame({
        "id": ["A", "B", "C", "D", "E"],
        "x": [1, 2, 3, 4, 5],
        "y": [10, 12, 9, 14, 13],
    })