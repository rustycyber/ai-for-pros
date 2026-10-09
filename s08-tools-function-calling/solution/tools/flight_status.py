"""Mock flight status lookup. Deterministic for testability."""
from __future__ import annotations

from datetime import date as date_cls

FLIGHT_STATUS_SCHEMA = {
    "type": "function",
    "function": {
        "name": "flight_status",
        "description": "Look up the current status of a commercial flight.",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_no": {
                    "type": "string",
                    "description": "Flight number, e.g. UA123",
                },
                "date": {
                    "type": "string",
                    "description": "Date in YYYY-MM-DD format",
                },
            },
            "required": ["flight_no", "date"],
        },
    },
}

_FIXTURE = {
    ("UA123", "2026-01-15"): {"status": "ON_TIME", "gate": "B12"},
    ("UA123", "2026-01-16"): {"status": "DELAYED", "gate": "B12", "delay_min": 45},
    ("DL456", "2026-01-15"): {"status": "BOARDING", "gate": "A07"},
    ("AA789", "2026-01-15"): {"status": "CANCELLED"},
}


def flight_status(flight_no: str, date: str) -> dict:
    flight_no = flight_no.upper().strip()
    try:
        date_cls.fromisoformat(date)
    except ValueError as e:
        return {"error": f"invalid date: {e}"}
    key = (flight_no, date)
    if key in _FIXTURE:
        return {"flight_no": flight_no, "date": date, **_FIXTURE[key]}
    return {
        "flight_no": flight_no,
        "date": date,
        "status": "UNKNOWN",
        "note": "no record",
    }
