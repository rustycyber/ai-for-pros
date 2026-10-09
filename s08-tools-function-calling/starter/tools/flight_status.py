"""TODO: implement flight_status() per the schema below."""
from __future__ import annotations

FLIGHT_STATUS_SCHEMA = {
    "type": "function",
    "function": {
        "name": "flight_status",
        "description": "Look up the current status of a commercial flight.",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_no": {"type": "string"},
                "date":      {"type": "string"},
            },
            "required": ["flight_no", "date"],
        },
    },
}


def flight_status(flight_no: str, date: str) -> dict:
    raise NotImplementedError(
        "Fill in: validate the date, look up the fixture, return a status dict."
    )
