from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Conversion data - base units for calculations
conversion_data = {
    "Length": {
        "Metre": 1.0,
        "Kilometre": 1000.0,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34,
        "Nautical Mile": 1852.0
    },
    "Weight": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Ton": 1000.0,
        "Stone": 6.35029
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    },
    "Volume": {
        "Litre": 1.0,
        "Millilitre": 0.001,
        "Gallon (US)": 3.78541,
        "Gallon (UK)": 4.54609,
        "Quart": 0.946353,
        "Pint": 0.473176,
        "Cup": 0.236588,
        "Fluid Ounce": 0.0295735
    },
    "Area": {
        "Square Metre": 1.0,
        "Square Kilometre": 1000000.0,
        "Square Centimetre": 0.0001,
        "Square Inch": 0.00064516,
        "Square Foot": 0.092903,
        "Square Yard": 0.836127,
        "Hectare": 10000.0,
        "Acre": 4046.86
    },
    "Speed": {
        "Metre per Second": 1.0,
        "Kilometre per Hour": 0.277778,
        "Mile per Hour": 0.44704,
        "Knot": 0.514444,
        "Foot per Second": 0.3048
    }
}

@app.route('/')
def home():
    return render_template('index.html', categories=list(conversion_data.keys()))

@app.route('/get_units/<category>')
def get_units(category):
    """Get available units for a specific category"""
    if category in conversion_data:
        return jsonify(list(conversion_data[category].keys()))
    return jsonify([])

@app.route('/convert', methods=['POST'])
def convert():
    """Handle unit conversion"""
    data = request.get_json()
    category = data.get('category')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    value = data.get('value', 0)
    
    try:
        value = float(value)
    except (ValueError, TypeError):
        return jsonify({'result': '0', 'error': 'Invalid number'})
    
    if category not in conversion_data:
        return jsonify({'result': '0', 'error': 'Invalid category'})
    
    category_data = conversion_data[category]
    
    # Special handling for temperature
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        # Standard conversion using base units
        if from_unit not in category_data or to_unit not in category_data:
            return jsonify({'result': '0', 'error': 'Invalid units'})
        
        # Convert to base unit first, then to target unit
        base_value = value * category_data[from_unit]
        result = base_value / category_data[to_unit]
    
    # Format the result nicely
    if result == int(result):
        formatted_result = str(int(result))
    elif abs(result) >= 1000000:
        formatted_result = f"{result:.2e}"
    elif abs(result) >= 1:
        formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
    else:
        formatted_result = f"{result:.8f}".rstrip('0').rstrip('.')
    
    return jsonify({'result': formatted_result})

def convert_temperature(value, from_unit, to_unit):
    """Special temperature conversion function"""
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # Celsius
        celsius = value
    
    # Convert from Celsius to target
    if to_unit == "Fahrenheit":
        return celsius * 9/5 + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:  # Celsius
        return celsius

if __name__ == '__main__':
    print("Starting MY UNIT CONVERTOR...")
    print("Server will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='127.0.0.1', port=5000)