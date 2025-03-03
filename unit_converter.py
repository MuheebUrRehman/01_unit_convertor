import streamlit as st

conversion_factors = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
}

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Length Unit Converter")
st.write("Convert between different length units.")

value = st.number_input("Enter the value", value=1.0)

from_unit = st.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.selectbox("To Unit", list(conversion_factors.keys()))

if st.button("Convert"):
    value_in_meters = value * conversion_factors[from_unit]
    result = value_in_meters / conversion_factors[to_unit]
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
