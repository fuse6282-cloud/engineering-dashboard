# tests/test_alarm.py

import pytest
from services.alarm import generate_alarms


def test_all_normal_returns_empty():
    """ทุกโมดูล NORMAL → คืน []"""
    assert generate_alarms("NORMAL", "NORMAL", "NORMAL") == []


def test_one_warning():
    """Temperature เป็น WARNING → มีแค่ 1 ข้อความ"""
    result = generate_alarms("WARNING", "NORMAL", "NORMAL")
    assert result == ["WARNING: Temperature requires attention"]


def test_warning_and_critical_together():
    """Humidity CRITICAL + Power WARNING → 2 ข้อความ ลำดับถูกต้อง"""
    result = generate_alarms("NORMAL", "CRITICAL", "WARNING")
    assert result == [
        "CRITICAL: Humidity is unsafe",
        "WARNING: Power consumption is high",
    ]


def test_all_critical():
    """ทุกโมดูล CRITICAL → 3 ข้อความ ลำดับ Temp → Humid → Power"""
    result = generate_alarms("CRITICAL", "CRITICAL", "CRITICAL")
    assert result == [
        "CRITICAL: Temperature is unsafe",
        "CRITICAL: Humidity is unsafe",
        "CRITICAL: Power consumption is unsafe",
    ]


def test_invalid_status_raises_value_error():
    """Input ที่ไม่ใช่ NORMAL/WARNING/CRITICAL → ValueError"""
    with pytest.raises(ValueError):
        generate_alarms("OK", "NORMAL", "NORMAL")


# (โบนัส) ตรวจ invalid ที่ตำแหน่งอื่น
def test_invalid_in_second_param():
    with pytest.raises(ValueError):
        generate_alarms("NORMAL", "ERROR", "NORMAL")