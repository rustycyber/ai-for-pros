"""TODO: implement weather_now() with a small fixture per city."""
from __future__ import annotations

WEATHER_NOW_SCHEMA = {
    "type": "function",
    "function": {
        "name": "weather_now",
        "description": "Get the current weather snapshot for a city.",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}


def weather_now(city: str) -> dict:
    raise NotImplementedError("Fill in: 6+ cities, deterministic snapshots.")
