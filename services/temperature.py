def classify_temperature(celsius: float) -> str:
    """-20..80 -> NORMAL|WARNING|CRITICAL"""

    if not -20 <= celsius <= 80:
        raise ValueError("อุณหภูมิต้องอยู่ระหว่าง -20 ถึง 80 °C")

    if celsius <= 30:
        return "NORMAL"
    elif celsius <= 35:
        return "WARNING"
    else:
        return "CRITICAL"