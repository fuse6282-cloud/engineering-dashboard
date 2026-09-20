# services/temperature.py

def classify_temperature(celsius: float) -> str:
    """
    จำแนกสถานะตามอุณหภูมิ (°C):
    -20..80 -> NORMAL, WARNING, CRITICAL; นอกช่วง -> ValueError
    - NORMAL: <= 30 °C
    - WARNING: > 30 ถึง 35 °C
    - CRITICAL: > 35 °C
    """
    if not (-20.0 <= celsius <= 80.0):
        raise ValueError("อุณหภูมิต้องอยู่ระหว่าง -20 ถึง 80 °C")
    
    if celsius <= 30.0:
        return "NORMAL"
    elif celsius <= 35.0:
        return "WARNING"
    else:
        return "CRITICAL"