"""Mock weather lookup. Returns a deterministic snapshot per city."""
from __future__ import annotations

WEATHER_NOW_SCHEMA = {
    "type": "function",
    "function": {
        "name": "weather_now",
        "description": "Get the current weather snapshot for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name, e.g. 'San Francisco'",
                },
            },
            "required": ["city"],
        },
    },
}

_FIXTURE = {
    "san francisco": {"temp_c": 16, "conditions": "Cloudy", "humidity": 78},
    "new york":      {"temp_c": 4,  "conditions": "Snow",   "humidity": 85},
    "london":        {"temp_c": 8,  "conditions": "Rain",   "humidity": 90},
    "tokyo":         {"temp_c": 12, "conditions": "Clear",  "humidity": 55},
    "mumbai":        {"temp_c": 29, "conditions": "Humid",  "humidity": 80},
    "sydney":        {"temp_c": 22, "conditions": "Sunny",  "humidity": 60},
}


def weather_now(city: str) -> dict:
    key = city.lower().strip()
    if key in _FIXTURE:
        return {"city": city.strip(), **_FIXTURE[key]}
    return {"city": city.strip(), "error": "no record for this city"}
