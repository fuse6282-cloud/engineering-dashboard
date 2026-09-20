# services/alarm.py

VALID_STATUSES = {"NORMAL", "WARNING", "CRITICAL"}

ALARM_MESSAGES = {
    "temperature": {
        "WARNING":  "WARNING: Temperature requires attention",
        "CRITICAL": "CRITICAL: Temperature is unsafe",
    },
    "humidity": {
        "WARNING":  "WARNING: Humidity requires attention",
        "CRITICAL": "CRITICAL: Humidity is unsafe",
    },
    "power": {
        "WARNING":  "WARNING: Power consumption is high",
        "CRITICAL": "CRITICAL: Power consumption is unsafe",
    },
}

def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str,
) -> list[str]:
    """คืน list ข้อความเตือน; ถ้าปกติทั้งหมดคืน []"""

    # ตรวจ Input ทุกตัว
    for status in (temp_status, humid_status, power_status):
        if status not in VALID_STATUSES:
            raise ValueError(f"สถานะไม่ถูกต้อง: '{status}'")

    alarms = []

    # ตรวจตามลำดับคงที่: Temperature → Humidity → Power
    if temp_status != "NORMAL":
        alarms.append(ALARM_MESSAGES["temperature"][temp_status])

    if humid_status != "NORMAL":
        alarms.append(ALARM_MESSAGES["humidity"][humid_status])

    if power_status != "NORMAL":
        alarms.append(ALARM_MESSAGES["power"][power_status])

    return alarms