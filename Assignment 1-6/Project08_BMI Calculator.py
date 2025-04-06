import streamlit as st


st.title("💪 BMI Calculator")

height = st.slider("📏 Select your height (in cm):", 100, 250, 175)
weight = st.slider("⚖️ Select your weight (in kg):", 40, 200, 70)


bmi = weight / ((height / 100) ** 2)


st.subheader(f"📊 Your BMI is: {bmi:.2f}")

# BMI Categories
st.markdown("### 🧭 BMI Categories")
st.markdown("""
- 🔹 **Underweight**: BMI less than 18.5  
- 🟢 **Normal weight**: BMI between 18.5 and 24.9  
- 🟡 **Overweight**: BMI between 25 and 29.9  
- 🔴 **Obesity**: BMI 30 or greater
""")
