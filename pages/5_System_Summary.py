import streamlit as st

st.title("📊 System Summary & เกณฑ์การวัด")

st.markdown("""
### 📌 เกณฑ์การตัดสินสถานะของแต่ละโมดูล
---
#### 1. 🌡️ Temperature Monitoring (ช่วงข้อมูล: -20 ถึง 80 °C)
- **NORMAL:** $\le 30$ °C
- **WARNING:** $> 30$ ถึง $35$ °C
- **CRITICAL:** $> 35$ °C

#### 2. 💧 Humidity Monitoring (ช่วงข้อมูล: 0 ถึง 100%)
- **NORMAL:** $40 - 60$ %
- **WARNING:** $30 - 70$ % (ที่ไม่ใช่ช่วง NORMAL)
- **CRITICAL:** น้อยกว่า $30$ % หรือ มากกว่า $70$ %

#### 3. ⚡ Power Monitoring ($P = V \\times I$)
- **NORMAL:** $< 500$ W
- **WARNING:** $500 - 1000$ W
- **CRITICAL:** $> 1000$ W

#### 4. 🚨 Safety Alarm System
- รับสถานะจากทั้ง 3 โมดูล และแสดงรายการข้อความแจ้งเตือนตามลำดับ:
  `Temperature` ➔ `Humidity` ➔ `Power`
---
""")

st.subheader("👥 สมาชิกในกลุ่มและบทบาทหน้าที่")
st.markdown("""
- **คนที่ 1 (Temperature Monitoring):** 
นาย นพรัตน์ ท้วมแก้ว รับผิดชอบ `services/temperature.py`, `pages/1_Temperature.py`, `tests/test_temperature.py`
- **คนที่ 2 (Humidity Monitoring):** 
นาย อโนทัย คำใส รับผิดชอบ `services/humidity.py`, `pages/2_Humidity.py`, `tests/test_humidity.py`
- **คนที่ 3 (Power Monitoring):** 
นาย อชิตะ หนองเทา รับผิดชอบ `services/power.py`, `pages/3_Power.py`, `tests/test_power.py`
- **คนที่ 4 (Safety Alarm):** 
นาย ภูบดินทร์ แก้วยองผาง รับผิดชอบ `services/alarm.py`, `pages/4_Safety_Alarm.py`, `tests/test_alarm.py`
- **คนที่ 5 (System Summary & QA):** 
นาย อณาจักร หลวงสว่าง รับผิดชอบ `app.py`, `pages/5_System_Summary.py`, `README.md` และการตรวจ Code Review
""")