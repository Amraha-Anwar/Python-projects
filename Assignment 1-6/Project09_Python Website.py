import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Initialize session state for conversion history
if 'conversion_history' not in st.session_state:
    st.session_state.conversion_history = []

# Set page config
st.set_page_config(page_title="Advanced Unit Converter", layout="wide", page_icon="🛠")

st.title("🌠 Advanced Unit Converter")
st.markdown("_Convert units with style and precision_")

# Conversion factors dictionary
CONVERSION_FACTORS = {
    "Length": {
        "Meters": {"Kilometers": 0.001, "Feet": 3.28084, "Miles": 0.000621371},
        "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Miles": 0.621371},
        "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280}
    },
    "Weight": {
        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
        "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625}
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        "Celsius": {
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        },
        "Fahrenheit": {
            "Celsius": lambda x: (x - 32) * 5/9,
            "Kelvin": lambda x: (x - 32) * 5/9 + 273.15
        },
        "Kelvin": {
            "Celsius": lambda x: x - 273.15,
            "Fahrenheit": lambda x: (x - 273.15) * 9/5 + 32
        }
    }
    return conversions[from_unit][to_unit](value)

# main layout
col1, col2 = st.columns([2, 1])

with col1:
    unit_type = st.selectbox(
        "Choose the type of unit to convert:",
        ["Length", "Weight", "Temperature"]
    )

    units = {
        "Length": ["Meters", "Kilometers", "Feet", "Miles"],
        "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }[unit_type]

    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    value = st.slider(
        "Enter value to convert:",
        min_value=0.0 if unit_type != "Temperature" else -100.0,
        max_value=1000.0,
        value=10.0,
        step=0.1
    )

    if st.button("Convert"):
        if unit_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            if from_unit == to_unit:
                result = value
            else:
                result = value * CONVERSION_FACTORS[unit_type][from_unit][to_unit]

        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.conversion_history.append({
            'timestamp': timestamp,
            'from_value': value,
            'from_unit': from_unit,
            'to_value': result,
            'to_unit': to_unit,
            'unit_type': unit_type
        })

        st.success(f"🎯 Converted value: {result:.4f} {to_unit}")

        if unit_type == "Length" and to_unit in ["Meters", "Kilometers"]:
            comparison = result / 1.7
            st.info(f"📏 Approx. {comparison:.1f} times the height of an average person.")
        elif unit_type == "Weight" and to_unit in ["Kilograms", "Pounds"]:
            comparison = result / 70
            st.info(f"⚖️ Approx. {comparison:.1f} times the weight of an average person.")

with col2:
    st.subheader("📜 Recent Conversions")
    if st.session_state.conversion_history:
        for conv in reversed(st.session_state.conversion_history[-5:]):
            st.write(f"**{conv['timestamp']}**: {conv['from_value']} {conv['from_unit']} → "
                     f"{conv['to_value']:.4f} {conv['to_unit']}")
        if st.button("Clear History"):
            st.session_state.conversion_history = []
    else:
        st.info("No conversion history yet")

    if st.session_state.conversion_history:
        st.subheader("📊 Conversion Trend")
        latest_conversions = st.session_state.conversion_history[-10:]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[conv['timestamp'] for conv in latest_conversions],
            y=[conv['to_value'] for conv in latest_conversions],
            mode='lines+markers',
            name='Converted Values'
        ))
        fig.update_layout(
            height=300,
            xaxis_title="Time",
            yaxis_title="Converted Value"
        )
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
with st.expander("ℹ️ Help & Tips"):
    st.markdown("""
    - Use dropdowns to select units
    - Adjust value using slider
    - Click Convert to get result
    - Check recent conversions and trends on the right
    """)

if st.session_state.conversion_history:
    import pandas as pd
    history_df = pd.DataFrame(st.session_state.conversion_history)
    csv = history_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Conversion History",
        data=csv,
        file_name="conversion_history.csv",
        mime="text/csv"
    )

st.markdown("Made with ❤️ by Amraha Anwar")
