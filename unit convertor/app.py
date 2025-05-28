import streamlit as st
from design.style import load_custom_css

# Page config
st.set_page_config(page_title="My Unit Convertor", layout="centered")

# Load CSS
load_custom_css()

# App Title
st.markdown('<h1 class="app-title">My Unit Convertor</h1>', unsafe_allow_html=True)

# Units and conversion logic
units = {
    "Metre": 1.0,
    "Centimetre": 100.0,
    "Millimetre": 1000.0,
    "Kilometre": 0.001,
    "Inch": 39.3701,
    "Foot": 3.28084,
    "Yard": 1.09361,
    "Mile": 0.000621371,
}

# UI layout with side-by-side boxes
st.markdown('<div class="converter-box">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    val = st.number_input("", value=1.0, label_visibility="collapsed")
    from_unit = st.selectbox("", list(units.keys()), index=0, label_visibility="collapsed")

with col2:
    to_unit = st.selectbox("", list(units.keys()), index=1, label_visibility="collapsed")
    result = val * units[to_unit] / units[from_unit]
    st.markdown(f"<div class='result'>{result:.4f}</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Show formula
st.markdown(
    f"<div class='formula'><b>Formula:</b> multiply the length value by {units[to_unit] / units[from_unit]:.4f}</div>",
    unsafe_allow_html=True
)
