import streamlit as st
from services.power import calculate_power, classify_power


st.title("Power Monitoring")

# รับค่า Voltage และ Current
voltage = st.number_input(
    "Voltage (V)",
    min_value=0.01,
    value=220.0,
    step=1.0
)

current = st.number_input(
    "Current (A)",
    min_value=0.0,
    value=1.0,
    step=0.1
)

# คำนวณ Power
power = calculate_power(voltage, current)

# ตรวจสอบสถานะ
status = classify_power(power)

# แสดงค่าที่คำนวณได้
st.metric("Voltage", f"{voltage:.2f} V")
st.metric("Current", f"{current:.2f} A")
st.metric("Power", f"{power:.2f} W")

# แสดงสถานะ
if status == "NORMAL":
    st.success("สถานะ: NORMAL")
elif status == "WARNING":
    st.warning("สถานะ: WARNING")
else:
    st.error("สถานะ: CRITICAL")