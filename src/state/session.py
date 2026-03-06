import streamlit as st

def init_session():
    defaults = {
        "selected_id": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v