import streamlit as st

st.set_page_config(page_title="Engineering Dashboard", layout="wide")
st.title("🛠️ Engineering Monitoring Dashboard")
st.write("ยินดีต้อนรับสู่ระบบจำลองการติดตามสถานะทางวิศวกรรม")
st.info("กรุณาเลือกโมดูลที่ต้องการตรวจสอบจากเมนูด้านซ้าย")

st.subheader("รายชื่อสมาชิกในกลุ่ม")
st.markdown("""
1. คนที่ 1: (F) - Temperature Monitoring
2. คนที่ 2: (A) - Humidity Monitoring
3. คนที่ 3: (s) - Power Monitoring
4. คนที่ 4: (e) - Safety Alarm
5. คนที่ 5: (r) - System Summary + QA + README
""")