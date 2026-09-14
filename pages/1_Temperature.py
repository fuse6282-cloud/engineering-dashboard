import streamlit as st
from services.temperature import classify_temperature

st.title("🌡️ Temperature Monitoring")

temp = st.slider(
    "อุณหภูมิ (°C)",
    -20.0,
    80.0,
    28.0,
    0.5
)

status = classify_temperature(temp)

st.metric("อุณหภูมิ", f"{temp:.1f} °C")

if status == "NORMAL":
    st.success(f"สถานะ: {status}")
elif status == "WARNING":
    st.warning(f"สถานะ: {status}")
else:
    st.error(f"สถานะ: {status}")