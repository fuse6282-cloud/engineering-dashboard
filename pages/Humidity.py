import streamlit as st
import sys
from pathlib import Path

# ดึงตำแหน่งรากโปรเจกต์เพื่อให้ import services ได้
sys.path.append(str(Path(__file__).parent.parent))
from services.humidity import evaluate_humidity

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(
    page_title="Humidity Dashboard",
    page_icon="💧",
    layout="wide"
)

# 2. ใส่ Custom CSS ปรับแต่งความสวยงาม
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
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

# 3. ส่วนหัวเรื่อง
st.title("💧 Humidity Monitoring System")
st.caption("ระบบติดตามและเฝ้าระวังระดับความชื้นสัมพัทธ์ในอากาศ")
st.divider()

# 4. ส่วนตัวปรับตั้งค่า (Sidebar)
with st.sidebar:
    st.header("⚙️ ตัวควบคุมจำลอง")
    humidity = st.slider("ปรับค่าความชื้น (%RH)", 0.0, 100.0, 45.0, 0.5)

# 5. ประมวลผลสถานะผ่าน Service
result = evaluate_humidity(humidity)

# 6. แสดงผล UI แบบแบ่งคอลัมน์
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Relative Humidity</div>
            <div class="metric-value">{humidity:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("**ระดับความชื้นเทียบสเกล:**")
    st.progress(humidity / 100.0)

with col2:
    st.subheader("📌 การประเมินสถานะระบบ")
    
    # แสดงผลตามประเภทการเตือน
    if result["type"] == "error":
        st.error(f"**{result['message']}**")
    elif result["type"] == "success":
        st.success(f"**{result['message']}**")
    else:
        st.warning(f"**{result['message']}**")
        
    st.info(result["recommendation"])

    st.divider()
    
    st.write("**ช่วงค่าความชื้นมาตรฐาน:**")
    c1, c2, c3 = st.columns(3)
    c1.caption("🔴 แห้ง: < 30%")
    c2.caption("🟢 ปกติ: 30% - 60%")
    c3.caption("🟡 ชื้นมาก: > 60%")