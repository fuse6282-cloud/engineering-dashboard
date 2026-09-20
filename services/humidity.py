def evaluate_humidity(humidity: float):
    """
    ประเมินสถานะและคำแนะนำตามระดับความชื้นสัมพัทธ์ (%RH)
    """
    if humidity < 30.0:
        return {
            "status": "Dry Zone",
            "message": "⚠️ สถานะ: ความชื้นต่ำเกินไป",
            "recommendation": "💡 คำแนะนำ: ควรเปิดระบบพ่นหมอก หรือเครื่องเพิ่มความชื้นในอากาศ",
            "type": "error"
        }
    elif 30.0 <= humidity <= 60.0:
        return {
            "status": "Optimal Zone",
            "message": "✅ สถานะ: สภาพแวดล้อมเหมาะสม",
            "recommendation": "💡 คำแนะนำ: ระดับความชื้นอยู่ในเกณฑ์ปกติ ไม่ต้องดำเนินการใดๆ",
            "type": "success"
        }
    else:
        return {
            "status": "Humid Zone",
            "message": "🔥 สถานะ: ความชื้นสูงเกินไป",
            "recommendation": "💡 คำแนะนำ: ควรเปิดระบบระบายอากาศเพื่อลดความเสี่ยงการเกิดเชื้อรา",
            "type": "warning"
        }