import pytest
from services.temperature import classify_temperature


def test_normal():
    assert classify_temperature(25) == "NORMAL"


def test_normal_boundary():
    assert classify_temperature(30) == "NORMAL"


def test_warning():
    assert classify_temperature(33) == "WARNING"


def test_warning_boundary():
    assert classify_temperature(35) == "WARNING"


def test_critical():
    assert classify_temperature(40) == "CRITICAL"


def test_invalid_high():
    with pytest.raises(ValueError):
        classify_temperature(81)


def test_invalid_low():
    with pytest.raises(ValueError):
        classify_temperature(-21)