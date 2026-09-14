import streamlit as st

st.set_page_config(page_title="Engineering Dashboard", layout="wide")
st.title("🛠️ Engineering Monitoring Dashboard")

temp = st.slider("อุณหภูมิ (°C)", -20.0, 80.0, 28.0, 0.5)
st.metric("Temperature", f"{temp:.1f} °C")

if temp <= 30:
    st.success("สถานะ: ปกติ")
elif temp <= 35:
    st.warning("สถานะ: เฝ้าระวัง")
else:
    st.error("สถานะ: วิกฤต")