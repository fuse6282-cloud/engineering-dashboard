import sys
from pathlib import Path

# ดึงตำแหน่งรากโปรเจกต์เพื่อเรียกใช้ service
sys.path.append(str(Path(__file__).parent.parent))
from services.humidity import evaluate_humidity

def test_dry_zone():
    res = evaluate_humidity(20.0)
    assert res["status"] == "Dry Zone"
    assert res["type"] == "error"

def test_optimal_zone():
    res = evaluate_humidity(45.0)
    assert res["status"] == "Optimal Zone"
    assert res["type"] == "success"

def test_humid_zone():
    res = evaluate_humidity(75.0)
    assert res["status"] == "Humid Zone"
    assert res["type"] == "warning"