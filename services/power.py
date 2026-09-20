def calculate_power(voltage: float, current: float) -> float:
    """คำนวณกำลังไฟฟ้า P = V × I"""

    if voltage <= 0:
        raise ValueError("Voltage ต้องมากกว่า 0")

    if current < 0:
        raise ValueError("Current ต้องมากกว่าหรือเท่ากับ 0")

    return voltage * current


def classify_power(power_watt: float) -> str:
    """แบ่งสถานะตามกำลังไฟฟ้า"""

    if power_watt < 500:
        return "NORMAL"

    if power_watt <= 1000:
        return "WARNING"

    return "CRITICAL"