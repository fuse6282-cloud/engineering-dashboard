import streamlit as st

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(
    page_title="Humidity Dashboard",
    page_icon="💧",
    layout="wide"
)

# 2. ใส่ Custom CSS ปรับแต่งความสวยงาม
st.markdown("""
    <style>
    /* ซ่อน Header/Footer ของ Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* สไตล์การ์ดแสดงผล */
    .metric-card {
        background-color: #1E293B;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-title {
        color: #94A3B8;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .metric-value {
        color: #38BDF8;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนหัวเรื่อง (Header Section)
st.title("💧 Humidity Monitoring System")
st.caption("ระบบติดตามและเฝ้าระวังระดับความชื้นสัมพัทธ์ในอากาศ")
st.divider()

# 4. ส่วนตัวปรับตั้งค่า (Control Section)
with st.sidebar:
    st.header("⚙️ ตัวควบคุมจำลอง")
    humidity = st.slider("ปรับค่าความชื้น (%RH)", 0.0, 100.0, 45.0, 0.5)

# 5. แสดงผล UI แบบแบ่งคอลัมน์ (Dashboard Layout)
col1, col2 = st.columns([1, 2])

with col1:
    # การ์ดแสดงค่าความชื้นหลัก
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Relative Humidity</div>
            <div class="metric-value">{humidity:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress Bar แสดงระดับ
    st.write("**ระดับความชื้นเทียบสเกล:**")
    st.progress(humidity / 100.0)

with col2:
    st.subheader("📌 การประเมินสถานะระบบ")
    
    # เงื่อนไขเช็กสถานะพร้อมดีไซน์กล่องแจ้งเตือน
    if humidity < 30.0:
        st.error("⚠️ **สถานะ: ความชื้นต่ำเกินไป (Dry Zone)**")
        st.info("💡 **คำแนะนำ:** ควรเปิดระบบพ่นหมอก หรือเครื่องเพิ่มความชื้นในอากาศ")
    elif 30.0 <= humidity <= 60.0:
        st.success("✅ **สถานะ: สภาพแวดล้อมเหมาะสม (Optimal Zone)**")
        st.info("💡 **คำแนะนำ:** ระดับความชื้นอยู่ในเกณฑ์ปกติ ไม่ต้องดำเนินการใดๆ")
    else:
        st.warning("🔥 **สถานะ: ความชื้นสูงเกินไป (Humid Zone)**")
        st.info("💡 **คำแนะนำ:** ควรเปิดระบบระบายอากาศเพื่อลดความเสี่ยงการเกิดเชื้อรา")

    st.divider()
    
    # แสดงช่วงค่าความชื้นอ้างอิง
    st.write("**ช่วงค่าความชื้นมาตรฐาน:**")
    c1, c2, c3 = st.columns(3)
    c1.caption("🔴 แห้ง: < 30%")
    c2.caption("🟢 ปกติ: 30% - 60%")
    c3.caption("🟡 ชื้นมาก: > 60%")