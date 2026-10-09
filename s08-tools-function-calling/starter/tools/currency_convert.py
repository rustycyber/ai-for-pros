"""TODO: implement currency_convert() with a small fixed rate table."""
from __future__ import annotations

CURRENCY_CONVERT_SCHEMA = {
    "type": "function",
    "function": {
        "name": "currency_convert",
        "description": "Convert an amount between currencies at fixed rates.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount":   {"type": "number"},
                "from_ccy": {"type": "string"},
                "to_ccy":   {"type": "string"},
            },
            "required": ["amount", "from_ccy", "to_ccy"],
        },
    },
}


def currency_convert(amount: float, from_ccy: str, to_ccy: str) -> dict:
    raise NotImplementedError("Fill in the rate table and the math.")
