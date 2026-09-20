import pytest
from services.temperature import classify_temperature


# 1. ทดสอบสถานะ NORMAL
def test_normal():
    assert classify_temperature(25) == "NORMAL"


# 2. ทดสอบสถานะ WARNING
def test_warning():
    assert classify_temperature(33) == "WARNING"


# 3. ทดสอบสถานะ CRITICAL
def test_critical():
    assert classify_temperature(40) == "CRITICAL"


# 4. ทดสอบค่าที่อยู่นอกช่วง
def test_invalid():
    with pytest.raises(ValueError):
        classify_temperature(100)