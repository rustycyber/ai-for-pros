"""Currency conversion against a frozen rate table.

Real production would call an FX API; the lab uses a fixed table so
the eval harness is reproducible.
"""
from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP

CURRENCY_CONVERT_SCHEMA = {
    "type": "function",
    "function": {
        "name": "currency_convert",
        "description": "Convert an amount from one currency to another at fixed rates.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {"type": "number", "description": "Amount to convert"},
                "from_ccy": {"type": "string", "description": "3-letter ISO currency code"},
                "to_ccy": {"type": "string", "description": "3-letter ISO currency code"},
            },
            "required": ["amount", "from_ccy", "to_ccy"],
        },
    },
}

RATES_USD = {
    "USD": Decimal("1.00"),
    "EUR": Decimal("0.92"),
    "GBP": Decimal("0.79"),
    "JPY": Decimal("149.50"),
    "INR": Decimal("83.20"),
    "CAD": Decimal("1.35"),
}


def currency_convert(amount: float, from_ccy: str, to_ccy: str) -> dict:
    f = from_ccy.upper().strip()
    t = to_ccy.upper().strip()
    if f not in RATES_USD or t not in RATES_USD:
        return {"error": f"unsupported currency: {f if f not in RATES_USD else t}"}
    if amount < 0:
        return {"error": "amount must be non-negative"}
    usd = Decimal(str(amount)) / RATES_USD[f]
    out = usd * RATES_USD[t]
    out = out.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {
        "amount": float(amount),
        "from_ccy": f,
        "to_ccy": t,
        "converted": float(out),
    }
