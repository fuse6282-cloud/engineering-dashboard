import pytest
from services.temperature import classify_temperature


def test_normal():
    assert classify_temperature(25) == "NORMAL"


def test_warning():
    assert classify_temperature(33) == "WARNING"


def test_critical():
    assert classify_temperature(40) == "CRITICAL"


def test_invalid():
    with pytest.raises(ValueError):
        classify_temperature(100)