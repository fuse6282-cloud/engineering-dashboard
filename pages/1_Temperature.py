# pages/1_Temperature.py
import streamlit as st
from services.temperature import classify_temperature

st.set_page_config(page_title="Temperature Monitoring", page_icon="🌡️")

st.title("🌡️ Temperature Monitoring")
st.write("จำลองการติดตามอุณหภูมิและประเมินสถานะความปลอดภัยของระบบ")

# Slider รับค่าอุณหภูมิ -20.0 ถึง 80.0 °C
temp = st.slider("อุณหภูมิ (°C)", min_value=-20.0, max_value=80.0, value=28.0, step=0.5)

# ประมวลผลสถานะ
try:
    status = classify_temperature(temp)
    
    # แสดงค่าปัจจุบันด้วย st.metric
    st.metric(label="ค่าอุณหภูมิปัจจุบัน", value=f"{temp:.1f} °C")
    
    # แสดงสถานะด้วย st.success, st.warning หรือ st.error
    status_display = {
        "NORMAL": st.success,
        "WARNING": st.warning,
        "CRITICAL": st.error
    }
    
    status_display[status](f"สถานะระบบ: {status}")

except ValueError as e:
    st.error(f"ข้อผิดพลาด: {e}")