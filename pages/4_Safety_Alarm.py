# pages/4_Safety_Alarm.py

import streamlit as st
from services.alarm import generate_alarms

st.title("🚨 Safety Alarm")
st.write("เลือกสถานะของแต่ละโมดูลเพื่อตรวจสอบการแจ้งเตือน")

STATUS_OPTIONS = ["NORMAL", "WARNING", "CRITICAL"]

col1, col2, col3 = st.columns(3)
with col1:
    temp_status = st.selectbox("🌡 Temperature", STATUS_OPTIONS)
with col2:
    humid_status = st.selectbox("💧 Humidity", STATUS_OPTIONS)
with col3:
    power_status = st.selectbox("⚡ Power", STATUS_OPTIONS)

alarms = generate_alarms(temp_status, humid_status, power_status)

st.divider()

if not alarms:
    st.success("✅ ทุกระบบปกติ ไม่มีการแจ้งเตือน")
else:
    st.subheader(f"พบ {len(alarms)} การแจ้งเตือน")
    for msg in alarms:
        if msg.startswith("CRITICAL"):
            st.error(msg)
        else:
            st.warning(msg)