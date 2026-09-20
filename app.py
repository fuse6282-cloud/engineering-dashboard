import streamlit as st

st.set_page_config(page_title="Engineering Dashboard", layout="wide")
st.title("🛠️ Engineering Monitoring Dashboard")
st.write("ยินดีต้อนรับสู่ระบบจำลองการติดตามสถานะทางวิศวกรรม")
st.info("กรุณาเลือกโมดูลที่ต้องการตรวจสอบจากเมนูด้านซ้าย")

st.subheader("รายชื่อสมาชิกในกลุ่ม")
st.markdown("""
1. คนที่ 1: (นาย นพรัตน์ ท้วมแก้ว) - Temperature Monitoring
2. คนที่ 2: (นาย อโนทัย คำใส) - Humidity Monitoring
3. คนที่ 3: (นาย อชิตะ หนองเทา) - Power Monitoring
4. คนที่ 4: (นาย ภูบดินทร์ แก้วยองผาง) - Safety Alarm
5. คนที่ 5: (นาย อณาจักร หลวงสว่าง) - System Summary + QA + README
""")