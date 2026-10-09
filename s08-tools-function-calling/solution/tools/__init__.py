"""Full tool implementations."""
from __future__ import annotations

from .flight_status import flight_status, FLIGHT_STATUS_SCHEMA
from .currency_convert import currency_convert, CURRENCY_CONVERT_SCHEMA
from .weather_now import weather_now, WEATHER_NOW_SCHEMA

TOOLS = {
    "flight_status": (flight_status, FLIGHT_STATUS_SCHEMA),
    "currency_convert": (currency_convert, CURRENCY_CONVERT_SCHEMA),
    "weather_now": (weather_now, WEATHER_NOW_SCHEMA),
}

__all__ = [
    "TOOLS",
    "flight_status",
    "currency_convert",
    "weather_now",
    "FLIGHT_STATUS_SCHEMA",
    "CURRENCY_CONVERT_SCHEMA",
    "WEATHER_NOW_SCHEMA",
]
