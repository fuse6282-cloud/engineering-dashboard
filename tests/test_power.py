import pytest
from services.power import calculate_power, classify_power


def test_power_calculation():
    assert calculate_power(220, 2) == 440


def test_power_normal():
    assert classify_power(499.99) == "NORMAL"


def test_power_warning():
    assert classify_power(500) == "WARNING"


def test_power_warning_upper_boundary():
    assert classify_power(1000) == "WARNING"


def test_power_critical():
    assert classify_power(1000.01) == "CRITICAL"


def test_power_invalid_voltage():
    with pytest.raises(ValueError):
        calculate_power(0, 1)


def test_power_invalid_current():
    with pytest.raises(ValueError):
        calculate_power(220, -1)