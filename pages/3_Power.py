import streamlit as st
from services.power import calculate_power, classify_power


st.title("Power Monitoring")

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

power = calculate_power(voltage, current)
status = classify_power(power)

st.metric("Power", f"{power:.2f} W")

if status == "NORMAL":
    st.success("NORMAL")
elif status == "WARNING":
    st.warning("WARNING")
else:
    st.error("CRITICAL")

st.write(f"Status: **{status}**")