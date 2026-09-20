# pages/1_Temperature.py
import streamlit as st
from services.temperature import classify_temperature

st.set_page_config(
    page_title="Temperature Monitoring",
    page_icon="🌡️",
    layout="wide"
)

# --- Header Section ---
st.title("🌡️ Temperature Monitoring Dashboard")
st.caption("ระบบจำลองการติดตามอุณหภูมิอุตสาหกรรมแบบ Real-time")
st.markdown("---")

# --- Sidebar Info ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.info("💡 **คำแนะนำ:** ปรับเปลี่ยนค่าอุณหภูมิด้านล่างเพื่อจำลองสถานะของเซนเซอร์")

# --- Main Layout ---
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🎛️ Sensor Input")
    # Slider รับค่าอุณหภูมิ -20.0 ถึง 80.0 °C
    temp = st.slider(
        "กำหนดค่าอุณหภูมิ (°C)",
        min_value=-20.0,
        max_value=80.0,
        value=28.0,
        step=0.5,
        help="เลื่อนเพื่อจำลองอุณหภูมิของระบบ (-20 ถึง 80 °C)"
    )

    # คำนวณเปอร์เซ็นต์สำหรับ Progress Bar (สเกลจาก -20 ถึง 80 รวม 100 ช่วง)
    progress_val = int((temp - (-20)) / (80 - (-20)) * 100)
    st.caption("ระดับสเกลอุณหภูมิปัจจุบัน:")
    st.progress(progress_val)

with col2:
    st.subheader("📊 System Status")
    try:
        status = classify_temperature(temp)
        
        # เลือกสีและไอคอนตามสถานะ
        status_config = {
            "NORMAL": {"color": "green", "icon": "✅", "desc": "อุณหภูมิอยู่ในเกณฑ์ปกติ (<= 30°C)"},
            "WARNING": {"color": "orange", "icon": "⚠️", "desc": "อุณหภูมิเริ่มสูง ควรกำหนดการเฝ้าระวัง (30 - 35°C)"},
            "CRITICAL": {"color": "red", "icon": "🚨", "desc": "อุณหภูมิสูงเกินขีดความปลอดภัย! (> 35°C)"}
        }
        
        current_cfg = status_config[status]

        # แสดง Display Card ขนาดใหญ่
        st.metric(
            label="ค่าอุณหภูมิที่วัดได้",
            value=f"{temp:.1f} °C",
            delta=f"Status: {status}",
            delta_color="normal" if status == "NORMAL" else ("off" if status == "WARNING" else "inverse")
        )

        # แสดงกล่องแจ้งเตือนสถานะ
        if status == "NORMAL":
            st.success(f"### {current_cfg['icon']} สถานะ: {status}\n{current_cfg['desc']}")
        elif status == "WARNING":
            st.warning(f"### {current_cfg['icon']} สถานะ: {status}\n{current_cfg['desc']}")
        else:
            st.error(f"### {current_cfg['icon']} สถานะ: {status}\n{current_cfg['desc']}")

    except ValueError as e:
        st.error(f"❌ เกิดข้อผิดพลาด: {e}")

st.markdown("---")

# --- Expander อธิบายเกณฑ์ Contract ---
with st.expander("📖 ดูเกณฑ์การประเมินสถานะอุณหภูมิ (Contract Specifications)"):
    st.markdown("""
    | ระดับสถานะ | ช่วงอุณหภูมิ (°C) | คำแนะนำ/การดำเนินการ |
    | :--- | :--- | :--- |
    | 🟢 **NORMAL** | $\le 30.0^\circ\text{C}$ | ระบบทำงานปกติ |
    | 🟡 **WARNING** | $> 30.0$ ถึง $35.0^\circ\text{C}$ | ควรตรวจสอบระบบระบายความร้อน |
    | 🔴 **CRITICAL** | $> 35.0^\circ\text{C}$ | หยุดการทำงานของเครื่องจักรทันที |
    | ❌ **Error** | $< -20.0^\circ\text{C}$ หรือ $> 80.0^\circ\text{C}$ | นอกช่วงการวัดของเซนเซอร์ (`ValueError`) |
    """)