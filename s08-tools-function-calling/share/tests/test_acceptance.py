"""Offline acceptance tests for shared infrastructure (scorer + schemas).

Run from labs/s08-tools-function-calling/:
    uv run pytest share/tests/
"""
import sys
from pathlib import Path

# Setup paths
_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_root / "share"))
sys.path.insert(0, str(_root / "solution"))  # Use solution tools
del _root

from eval.scorer import expected_keys_match, score_run
from agents import openrouter_tool_schemas
from tools import (
    CURRENCY_CONVERT_SCHEMA,
    FLIGHT_STATUS_SCHEMA,
    TOOLS,
    WEATHER_NOW_SCHEMA,
    currency_convert,
    flight_status,
    weather_now,
)


# --- tools (using solution implementation)

def test_flight_status_known_route():
    out = flight_status("UA123", "2026-01-15")
    assert out["status"] == "ON_TIME"
    assert out["gate"] == "B12"


def test_flight_status_unknown_route():
    out = flight_status("ZZ999", "2026-01-15")
    assert out["status"] == "UNKNOWN"


def test_flight_status_bad_date():
    out = flight_status("UA123", "not-a-date")
    assert "error" in out


def test_currency_convert_known_pair():
    out = currency_convert(100, "USD", "EUR")
    assert out["converted"] == 92.00


def test_currency_convert_inverse():
    out = currency_convert(92, "EUR", "USD")
    assert abs(out["converted"] - 100.00) < 0.01


def test_currency_convert_unknown_ccy():
    out = currency_convert(1, "USD", "ZZZ")
    assert "error" in out


def test_currency_convert_negative_amount():
    out = currency_convert(-5, "USD", "EUR")
    assert "error" in out


def test_weather_now_known_city():
    out = weather_now("San Francisco")
    assert "temp_c" in out and out["conditions"] == "Cloudy"


def test_weather_now_unknown_city():
    out = weather_now("Atlantis")
    assert "error" in out


# --- schemas

def test_each_tool_has_a_schema():
    for name, (_, schema) in TOOLS.items():
        assert schema["function"]["name"] == name
        assert "parameters" in schema["function"]


def test_openrouter_schemas_translated():
    out = openrouter_tool_schemas()
    names = {s["function"]["name"] for s in out}
    assert names == {"flight_status", "currency_convert", "weather_now"}
    for s in out:
        assert "parameters" in s["function"]


# --- scorer

def test_scorer_keys_match_strings_case_insensitive():
    assert expected_keys_match({"status": "on_time"}, {"status": "ON_TIME"})


def test_scorer_keys_match_missing_key():
    assert not expected_keys_match({}, {"status": "ON_TIME"})


def test_score_run_pass():
    calls = [{"name": "flight_status", "args": {}, "result": {"status": "ON_TIME"}}]
    ok, _ = score_run(calls, "flight_status", {"status": "ON_TIME"})
    assert ok


def test_score_run_wrong_tool():
    calls = [{"name": "weather_now", "args": {}, "result": {"temp_c": 1}}]
    ok, reason = score_run(calls, "flight_status", {"status": "ON_TIME"})
    assert not ok and "not called" in reason


def test_score_run_right_tool_wrong_result():
    calls = [{"name": "flight_status", "args": {}, "result": {"status": "DELAYED"}}]
    ok, reason = score_run(calls, "flight_status", {"status": "ON_TIME"})
    assert not ok and "did not match" in reason


# --- dataset sanity

def test_dataset_has_20_rows_with_known_tools():
    from eval.dataset import DATASET
    assert len(DATASET) == 20
    known = set(TOOLS.keys())
    for _, tool, _ in DATASET:
        assert tool in known
