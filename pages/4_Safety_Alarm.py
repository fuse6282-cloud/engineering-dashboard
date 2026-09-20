import streamlit as st
from services.alarm import generate_alarms

st.set_page_config(page_title="Safety Alarm System", page_icon="🚨", layout="wide")

st.title("🚨 Safety Alarm Monitoring System")
st.write("ระบบตรวจสอบและรวบรวมการแจ้งเตือนความปลอดภัยจากทุกโมดูล")

st.subheader("⚙️ จำลองสถานะของแต่ละเซนเซอร์")
STATUS_OPTIONS = ["NORMAL", "WARNING", "CRITICAL"]

col1, col2, col3 = st.columns(3)
with col1:
    temp_status = st.selectbox("🌡 สถานะ Temperature:", STATUS_OPTIONS, index=0)
with col2:
    humid_status = st.selectbox("💧 สถานะ Humidity:", STATUS_OPTIONS, index=0)
with col3:
    power_status = st.selectbox("⚡ สถานะ Power:", STATUS_OPTIONS, index=0)

alarms = generate_alarms(temp_status, humid_status, power_status)

st.divider()

st.subheader("📋 ผลการตรวจจับสัญญาณเตือนภัย (Alarm Log)")

if not alarms:
    st.success("✅ ระบบทั้งหมดทำงานอยู่ในเกณฑ์ปกติ (NORMAL) — ไม่พบสัญญาณเตือนภัย")
else:
    st.caption(f"พบทั้งหมด {len(alarms)} การแจ้งเตือน")
    for alarm in alarms:
        if "CRITICAL" in alarm:
            st.error(f"🚨 {alarm}")
        else:
            st.warning(f"⚠️ {alarm}")
