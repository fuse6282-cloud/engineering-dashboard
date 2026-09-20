import streamlit as st
from services.temperature import classify_temperature

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Temperature Monitoring",
    page_icon="🌡️",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f5f8fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header */
.header {
    background: linear-gradient(135deg, #16243d, #274c77);
    padding: 25px 30px;
    border-radius: 18px;
    color: white;
    margin-bottom: 25px;
}

.header h1 {
    font-size: 40px;
    margin-bottom: 5px;
}

.header p {
    font-size: 17px;
    opacity: 0.85;
}

/* Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.07);
    border: 1px solid #e5eaf1;
    margin-bottom: 20px;
}

/* Temperature value */
.temp-value {
    font-size: 45px;
    font-weight: bold;
    color: #1e5aa8;
    text-align: center;
}

/* Status */
.status-normal {
    background: #d9f7e5;
    color: #087443;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.status-warning {
    background: #fff1bf;
    color: #8a6100;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

.status-critical {
    background: #ffd9dd;
    color: #b4232c;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}

/* Range */
.range-normal {
    background: #3cc982;
    color: white;
    padding: 15px;
    text-align: center;
    border-radius: 10px 0 0 10px;
    font-weight: bold;
}

.range-warning {
    background: #f6c945;
    color: #5e4800;
    padding: 15px;
    text-align: center;
    font-weight: bold;
}

.range-critical {
    background: #ef3b4f;
    color: white;
    padding: 15px;
    text-align: center;
    border-radius: 0 10px 10px 0;
    font-weight: bold;
}

/* Info */
.info-box {
    background: #eef5ff;
    padding: 18px;
    border-radius: 12px;
    color: #285b9c;
    margin-top: 15px;
}

/* Advice */
.advice {
    background: #eef7ff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #3987e8;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Header
# =========================

st.markdown("""
<div class="header">
    <h1>🌡️ Temperature Monitoring</h1>
    <p>ระบบติดตามและตรวจสอบอุณหภูมิของระบบแบบจำลอง</p>
</div>
""", unsafe_allow_html=True)


# =========================
# Temperature Input
# =========================

col1, col2 = st.columns([1.5, 1])

with col1:

    st.markdown("""
    <div class="card">
        <h2>🌡️ ปรับค่าอุณหภูมิ</h2>
        <p>เลือกค่าอุณหภูมิที่ต้องการจำลอง</p>
    </div>
    """, unsafe_allow_html=True)

    temp = st.slider(
        "อุณหภูมิ (°C)",
        min_value=-20.0,
        max_value=80.0,
        value=28.0,
        step=0.5
    )

    st.markdown(
        f'<div class="temp-value">{temp:.1f} °C</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
        ℹ️ ช่วงการใช้งาน: <b>-20 ถึง 80 °C</b><br>
        ความละเอียดของ Slider: <b>0.5 °C</b>
    </div>
    """, unsafe_allow_html=True)


# =========================
# Status
# =========================

status = classify_temperature(temp)

with col2:

    st.markdown("""
    <div class="card">
        <h2>🛡️ สถานะของระบบ</h2>
    </div>
    """, unsafe_allow_html=True)

    if status == "NORMAL":

        st.markdown("""
        <div class="status-normal">
            ✅ ปกติ<br>
            <span style="font-size:18px;">NORMAL</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("อุณหภูมิอยู่ในช่วงที่ปลอดภัย")

    elif status == "WARNING":

        st.markdown("""
        <div class="status-warning">
            ⚠️ เฝ้าระวัง<br>
            <span style="font-size:18px;">WARNING</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("อุณหภูมิเริ่มสูง ควรติดตามระบบ")

    else:

        st.markdown("""
        <div class="status-critical">
            🚨 วิกฤต<br>
            <span style="font-size:18px;">CRITICAL</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("อุณหภูมิสูงเกินเกณฑ์ ควรตรวจสอบระบบ")


# =========================
# Current Value + Criteria
# =========================

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns([1, 2])

with col3:

    st.markdown("""
    <div class="card">
        <h2>📊 ค่าปัจจุบัน</h2>
    """, unsafe_allow_html=True)

    st.metric(
        "Temperature",
        f"{temp:.1f} °C"
    )

    st.write("ค่าที่วัดได้จาก Slider (จำลอง)")

    st.markdown("</div>", unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="card">
        <h2>📋 เกณฑ์สถานะอุณหภูมิ</h2>

        <div style="display:flex; margin-top:20px;">
            <div class="range-normal" style="width:33.33%;">
                NORMAL
            </div>

            <div class="range-warning" style="width:33.33%;">
                WARNING
            </div>

            <div class="range-critical" style="width:33.33%;">
                CRITICAL
            </div>
        </div>

        <div style="display:flex; text-align:center; margin-top:10px;">
            <div style="width:33.33%;">
                ≤ 30 °C<br>
                <small>ปกติ</small>
            </div>

            <div style="width:33.33%;">
                &gt; 30 ถึง 35 °C<br>
                <small>เฝ้าระวัง</small>
            </div>

            <div style="width:33.33%;">
                &gt; 35 °C<br>
                <small>วิกฤต</small>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================
# Advice
# =========================

st.markdown("""
<div class="advice">

<h2>💡 คำแนะนำ</h2>

<ul>
<li>หากอุณหภูมิไม่เกิน 30 °C → ระบบอยู่ในสถานะ NORMAL</li>
<li>หากอุณหภูมิมากกว่า 30 ถึง 35 °C → ระบบอยู่ในสถานะ WARNING</li>
<li>หากอุณหภูมิมากกว่า 35 °C → ระบบอยู่ในสถานะ CRITICAL</li>
</ul>

</div>
""", unsafe_allow_html=True)