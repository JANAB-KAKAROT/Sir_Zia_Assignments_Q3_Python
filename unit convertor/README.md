---
# 📏 Unit Converter App

A simple and interactive Unit Converter built with [Streamlit](https://myconvertor.streamlit.app/). This app allows users to convert between various units of **length**, **weight**, **temperature**, and more — all in an intuitive web-based interface.

---

## 🚀 Features

- 🌡️ Temperature conversion (Celsius, Fahrenheit, Kelvin)
- 📏 Length conversion (meters, kilometers, inches, feet, etc.)
- ⚖️ Weight conversion (kilograms, pounds, grams, etc.)
- 🧪 Clean user interface with custom CSS styling
- 🧠 Powered by Python and Streamlit

---

## 🛠️ Folder Structure

```

unit-convertor/
├── app.py                     # Main Streamlit app
├── design/
│   ├── style.py               # CSS loader logic
│   └── style.css              # Custom styling
└── README.md                  # You're reading it 😉

````

---

## 🔧 Requirements

- Python 3.8 or above
- Streamlit

Install dependencies with:

```bash
pip install -r requirements.txt
````

---

## 🧪 How to Run

```bash
streamlit run app.py
```

Your app will open in your default web browser. If not, copy the local URL from the terminal.

---

## 🧰 Example Conversion

```python
# Length: meters to feet
convert_length(1, "meters", "feet")  # Output: 3.28084

# Temperature: Celsius to Fahrenheit
convert_temperature(100, "Celsius", "Fahrenheit")  # Output: 212.0
```

---

## 🎨 Customize the UI

You can edit the CSS file at `design/style.css` to match your theme preferences.

```css
body {
    background-color: #f9f9f9;
    font-family: 'Segoe UI', sans-serif;
}
```
## 🙌 Acknowledgments

* Sir Zia Khan – for the Python Quarter 3 assignment inspiration
* Streamlit – for making Python web apps easy
