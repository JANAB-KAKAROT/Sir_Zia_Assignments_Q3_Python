import streamlit as st
import os

def load_custom_css():
    with open(os.path.join("design", "style.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
