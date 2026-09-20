import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from services.temperature import classify_temperature


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Temperature Monitoring",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background: #f4f8ff;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #071b3a 0%,
        #0b2b55 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Main */

.block-container {
    max-width: 1500px;
    padding-top: 25px;
}


/* Header */

.dashboard-header {
    background: linear-gradient(
        120deg,
        #123d78,
        #1768c5,
        #5bb5ff
    );

    padding: 30px 35px;
    border-radius: 22px;

    color: white;

    box-shadow:
        0 10px 30px rgba(30,100,200,0.20);

    margin-bottom: 25px;
}

.dashboard-header h1 {
    font-size: 38px;
    margin: 0;
}

.dashboard-header p {
    font-size: 16px;
    margin-top: 8px;
}


/* Cards */

.card {
    background: white;
    border-radius: 20px;

    padding: 25px;

    box-shadow:
        0 5px 20px rgba(30,70,120,0.10);

    border: 1px solid #e4edf8;

    margin-bottom: 20px;
}


/* Temperature */

.temperature-number {
    font-size: 48px;
    font-weight: 800;

    color: #1768d1;

    text-align: center;

    margin: 10px;
}


/* Status */

.normal-box {
    background: linear-gradient(
        135deg,
        #dff9ed,
        #c4f1dc
    );

    border: 1px solid #6bd5a2;

    border-radius: 18px;

    padding: 35px;

    text-align: center;

    color: #08794d;
}

.warning-box {
    background: linear-gradient(
        135deg,
        #fff4c9,
        #ffe29a
    );

    border: 1px solid #f3c94d;

    border-radius: 18px;

    padding: 35px;

    text-align: center;

    color: #8a6100;
}

.critical-box {
    background: linear-gradient(
        135deg,
        #ffe0e4,
        #ffc5cc
    );

    border: 1px solid #f05b69;

    border-radius: 18px;

    padding: 35px;

    text-align: center;

    color: #bd1f32;
}


/* Gauge */

.gauge {
    width: 230px;
    height: 115px;

    border-radius: 230px 230px 0 0;

    background: conic-gradient(
        from 270deg,
        #1689ff 0deg,
        #22c985 110deg,
        #f4c542 160deg,
        #ef3d4f 180deg,
        transparent 180deg
    );

    margin: 25px auto 0;

    position: relative;
}

.gauge-inner {
    width: 175px;
    height: 88px;

    background: white;

    border-radius: 175px 175px 0 0;

    position: absolute;

    bottom: 0;
    left: 27px;

    display: flex;

    justify-content: center;

    align-items: flex-end;

    padding-bottom: 10px;
}


/* Range cards */

.range-normal {
    background: #dff9ed;
    color: #08794d;

    border-radius: 15px;

    padding: 20px;

    text-align: center;
}

.range-warning {
    background: #fff1c4;
    color: #8a6100;

    border-radius: 15px;

    padding: 20px;

    text-align: center;
}

.range-critical {
    background: #ffe0e4;
    color: #bd1f32;

    border-radius: 15px;

    padding: 20px;

    text-align: center;
}


/* Advice */

.advice {
    background: linear-gradient(
        135deg,
        #edf6ff,
        #e3f0ff
    );

    border-left: 5px solid #2585e8;

    border-radius: 15px;

    padding: 20px;

    color: #24527d;
}


/* Info */

.info {
    color: #55718f;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 5px 30px 5px;
    ">
        <div style="font-size:55px;">🌡️</div>

        <h1 style="
            font-size:25px;
            margin:0;
        ">
            Engineering<br>
            Monitoring
        </h1>

        <p style="
            color:#a9c9ed !important;
            font-size:13px;
        ">
            Smart Monitoring<br>
            for Better Engineering
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Dashboard")

    st.markdown("🌡️  **Temperature**")
    st.markdown("💧  Humidity")
    st.markdown("⚡  Power")
    st.markdown("🛡️  Safety Alarm")
    st.markdown("📈  System Summary")

    st.markdown("---")

    st.markdown("""
    ### 👥 Team 5

    1. Temperature
    2. Humidity
    3. Power
    4. Safety Alarm
    5. Summary + QA
    """)

    st.markdown("---")

    st.markdown("⚙️ Settings")
    st.markdown("🐙 GitHub Repository")


# =========================================================
# HEADER
# =========================================================

now = datetime.now()

st.markdown(f"""
<div class="dashboard-header">

    <h1>🌡️ Temperature Monitoring</h1>

    <p>
        ติดตามและตรวจสอบอุณหภูมิของระบบแบบเรียลไทม์
        (จำลองด้วย Slider)
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# TEMPERATURE + STATUS
# =========================================================

left, right = st.columns([1.6, 1])


# =========================================================
# LEFT : TEMPERATURE
# =========================================================

with left:

    st.markdown("""
    <div class="card">

        <h2>🌡️ ปรับค่าอุณหภูมิ</h2>

        <p class="info">
            เลือกค่าอุณหภูมิที่ต้องการจำลอง (°C)
        </p>

    </div>
    """, unsafe_allow_html=True)

    temp = st.slider(
        "อุณหภูมิ (°C)",
        min_value=-20.0,
        max_value=80.0,
        value=25.5,
        step=0.5
    )

    st.markdown(
        f"""
        <div class="temperature-number">
            {temp:.1f} °C
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info">
        ❄️ ช่วงการใช้งาน: <b>-20 ถึง 80 °C</b><br>
        ความละเอียด Slider: <b>0.5 °C</b>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# STATUS
# =========================================================

status = classify_temperature(temp)

with right:

    st.markdown("""
    <div class="card">

        <h2>🛡️ สถานะของระบบ</h2>

    """, unsafe_allow_html=True)

    if status == "NORMAL":

        st.markdown("""
        <div class="normal-box">

            <div style="font-size:55px;">
                ✓
            </div>

            <div style="
                font-size:32px;
                font-weight:bold;
            ">
                ปกติ
            </div>

            <div style="font-size:17px;">
                NORMAL
            </div>

            <br>

            อุณหภูมิอยู่ในช่วงที่ปลอดภัย

        </div>
        """, unsafe_allow_html=True)

    elif status == "WARNING":

        st.markdown("""
        <div class="warning-box">

            <div style="font-size:55px;">
                ⚠️
            </div>

            <div style="
                font-size:32px;
                font-weight:bold;
            ">
                เฝ้าระวัง
            </div>

            <div style="font-size:17px;">
                WARNING
            </div>

            <br>

            ควรติดตามอุณหภูมิของระบบ

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="critical-box">

            <div style="font-size:55px;">
                🚨
            </div>

            <div style="
                font-size:32px;
                font-weight:bold;
            ">
                วิกฤต
            </div>

            <div style="font-size:17px;">
                CRITICAL
            </div>

            <br>

            ควรตรวจสอบระบบทันที

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# CURRENT VALUE + TREND
# =========================================================

left2, right2 = st.columns([1, 2])


# =========================================================
# GAUGE
# =========================================================

with left2:

    st.markdown("""
    <div class="card">

        <h2>📊 ค่าปัจจุบัน</h2>

        <div class="gauge">

            <div class="gauge-inner">

                <div style="
                    font-size:25px;
                    font-weight:bold;
                    color:#1768d1;
                ">
                    """ + f"{temp:.1f} °C" + """
                </div>

            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "Temperature",
        f"{temp:.1f} °C"
    )


# =========================================================
# TREND GRAPH
# =========================================================

with right2:

    st.markdown("""
    <div class="card">

        <h2>📈 แนวโน้มอุณหภูมิ</h2>

        <p class="info">
            ย้อนหลัง 12 ชั่วโมง
        </p>

    """, unsafe_allow_html=True)

    # สร้างข้อมูลจำลอง
    np.random.seed(10)

    hours = pd.date_range(
        end=datetime.now(),
        periods=12,
        freq="h"
    )

    values = (
        temp
        + np.random.normal(0, 1.0, 12)
    )

    chart_data = pd.DataFrame(
        {
            "Temperature": values
        },
        index=hours
    )

    st.line_chart(
        chart_data,
        height=280
    )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# RANGE
# =========================================================

st.markdown("""
<div class="card">

<h2>🛡️ เกณฑ์สถานะอุณหภูมิ</h2>

</div>
""", unsafe_allow_html=True)


r1, r2, r3 = st.columns(3)


with r1:

    st.markdown("""
    <div class="range-normal">

        <h3>🟢 NORMAL</h3>

        <h2>≤ 30 °C</h2>

        <p>ปกติ</p>

    </div>
    """, unsafe_allow_html=True)


with r2:

    st.markdown("""
    <div class="range-warning">

        <h3>🟡 WARNING</h3>

        <h2>> 30 ถึง 35 °C</h2>

        <p>เฝ้าระวัง</p>

    </div>
    """, unsafe_allow_html=True)


with r3:

    st.markdown("""
    <div class="range-critical">

        <h3>🔴 CRITICAL</h3>

        <h2>> 35 °C</h2>

        <p>วิกฤต</p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ADVICE
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="advice">

<h2>💡 คำแนะนำ</h2>

<p>
🔵 หากอุณหภูมิไม่เกิน 30 °C
→ ระบบอยู่ในสถานะ <b>NORMAL</b>
</p>

<p>
🟡 หากอุณหภูมิมากกว่า 30 ถึง 35 °C
→ ระบบอยู่ในสถานะ <b>WARNING</b>
</p>

<p>
🔴 หากอุณหภูมิมากกว่า 35 °C
→ ระบบอยู่ในสถานะ <b>CRITICAL</b>
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<br>

<div style="
    text-align:center;
    color:#7890aa;
    font-size:13px;
">
    Engineering Monitoring Dashboard • Temperature Module
</div>
""", unsafe_allow_html=True)