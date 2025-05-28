import streamlit as st
import os

# page setup
st.set_page_config(page_title="Unit Converter", layout="wide")

# load css file
def load_css():
    css_file = os.path.join("design", "style.css")
    if os.path.exists(css_file):
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# load html template
def load_html():
    html_file = os.path.join("design", "template.html")
    if os.path.exists(html_file):
        with open(html_file) as f:
            return f.read()
    return ""

# my conversion data
units_data = {
    "Length": {
        "Millimetre": 0.001,
        "Centimetre": 0.01,
        "Metre": 1.0,
        "Kilometre": 1000.0,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    },
    "Weight": {
        "Milligram": 0.000001,
        "Gram": 0.001,
        "Kilogram": 1.0,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Ton": 1000.0
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F", 
        "Kelvin": "K"
    },
    "Volume": {
        "Millilitre": 0.001,
        "Litre": 1.0,
        "Gallon": 3.78541,
        "Fluid Ounce": 0.0295735,
        "Cup": 0.236588
    }
}

# temperature converter i made
def convert_temp(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # first convert to celsius
    if from_unit == "Fahrenheit":
        celsius_val = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius_val = value - 273.15
    else:
        celsius_val = value
    
    # then convert to target unit
    if to_unit == "Fahrenheit":
        return celsius_val * 9/5 + 32
    elif to_unit == "Kelvin":
        return celsius_val + 273.15
    else:
        return celsius_val

# main converter function
def convert_units(val, unit_from, unit_to, category):
    if val == 0:
        return 0
    
    if category == "Temperature":
        return convert_temp(val, unit_from, unit_to)
    else:
        from_factor = units_data[category][unit_from]
        to_factor = units_data[category][unit_to]
        result = val * from_factor / to_factor
        return result

# formula text generator
def get_formula_text(from_u, to_u, cat):
    if cat == "Length":
        if from_u == "Metre" and to_u == "Centimetre":
            return "multiply the length value by 100"
        elif from_u == "Centimetre" and to_u == "Metre":
            return "divide the length value by 100"
        elif from_u == "Kilometre" and to_u == "Metre":
            return "multiply the length value by 1000"
        else:
            return f"multiply the length value by conversion factor"
    elif cat == "Weight":
        if from_u == "Kilogram" and to_u == "Gram":
            return "multiply the mass value by 1000"
        elif from_u == "Gram" and to_u == "Kilogram":
            return "divide the mass value by 1000"
        else:
            return f"multiply the mass value by conversion factor" 
    elif cat == "Temperature":
        if from_u == "Celsius" and to_u == "Fahrenheit":
            return "multiply the temperature by 9/5 and add 32"
        elif from_u == "Fahrenheit" and to_u == "Celsius":
            return "subtract 32 and multiply by 5/9"
        else:
            return f"convert temperature using standard formula"
    else:
        return f"multiply the value by appropriate conversion factor"

# load styling
load_css()

# main converter interface
st.markdown('<div class="converter-main">', unsafe_allow_html=True)

# get category selection first
category = st.selectbox("", list(units_data.keys()), index=0, key="category")

# category header
st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)

# conversion area
st.markdown('<div class="conversion-area">', unsafe_allow_html=True)

# conversion row
st.markdown('<div class="conversion-row">', unsafe_allow_html=True)

# create three columns
col1, col2, col3 = st.columns([1, 0.15, 1])

with col1:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    input_value = st.number_input("", value=1.0, step=0.01, format="%.6f", key="input_val")
    from_unit = st.selectbox("", 
                            list(units_data[category].keys()), 
                            index=2 if category == "Length" else 0,
                            key="from_unit")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="equals-sign">=</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="output-box">', unsafe_allow_html=True)
    
    to_unit = st.selectbox("", 
                          list(units_data[category].keys()),
                          index=1 if category == "Length" else 1, 
                          key="to_unit")
    
    # calculate result
    if input_value is not None:
        converted_val = convert_units(input_value, from_unit, to_unit, category)
        
        # format result exactly like google
        if converted_val == 0:
            result_text = "0"
        elif abs(converted_val) >= 1000000:
            result_text = f"{converted_val:.3g}"
        elif abs(converted_val) >= 1:
            if converted_val == int(converted_val):
                result_text = str(int(converted_val))
            else:
                result_text = f"{converted_val:.10f}".rstrip('0').rstrip('.')
        else:
            result_text = f"{converted_val:.10g}"
        
        st.markdown(f'<div class="result-value">{result_text}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end conversion-row
st.markdown('</div>', unsafe_allow_html=True)  # end conversion-area

# formula section at bottom
formula_text = get_formula_text(from_unit, to_unit, category)
st.markdown(f'''
<div class="formula-section">
    <span class="formula-badge">Formula</span>
    <span class="formula-text">{formula_text}</span>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end converter-main
