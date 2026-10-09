"""20 golden inputs for each tool. Used by run_eval.py to score the
end-to-end model+tool path."""
from __future__ import annotations

# Each row: (user prompt, expected tool, partial expected result keys/values)
DATASET = [
    # flight_status (7 cases)
    ("What's the status of UA123 on 2026-01-15?",
     "flight_status", {"status": "ON_TIME"}),
    ("Is UA123 on time on 2026-01-16?",
     "flight_status", {"status": "DELAYED"}),
    ("Has DL456 started boarding on 2026-01-15?",
     "flight_status", {"status": "BOARDING"}),
    ("Did AA789 get cancelled on 2026-01-15?",
     "flight_status", {"status": "CANCELLED"}),
    ("Status of ZZ999 on 2026-01-15?",
     "flight_status", {"status": "UNKNOWN"}),
    ("Is UA123 delayed tomorrow 2026-01-16?",
     "flight_status", {"status": "DELAYED"}),
    ("Tell me the gate for UA123 on 2026-01-15.",
     "flight_status", {"gate": "B12"}),

    # currency_convert (7 cases)
    ("Convert 100 USD to EUR.",
     "currency_convert", {"to_ccy": "EUR"}),
    ("How much is 50 GBP in USD?",
     "currency_convert", {"from_ccy": "GBP"}),
    ("Convert 1000 JPY to USD.",
     "currency_convert", {"from_ccy": "JPY"}),
    ("What is 200 INR in EUR?",
     "currency_convert", {"to_ccy": "EUR"}),
    ("Convert 75 CAD to USD.",
     "currency_convert", {"from_ccy": "CAD"}),
    ("How many USD is 500 EUR?",
     "currency_convert", {"from_ccy": "EUR"}),
    ("Convert 10 USD to GBP.",
     "currency_convert", {"to_ccy": "GBP"}),

    # weather_now (6 cases)
    ("What's the weather in San Francisco?",
     "weather_now", {"city": "San Francisco"}),
    ("Current conditions in New York?",
     "weather_now", {"city": "New York"}),
    ("How's the weather in London now?",
     "weather_now", {"city": "London"}),
    ("Is it humid in Tokyo?",
     "weather_now", {"city": "Tokyo"}),
    ("Weather in Mumbai right now?",
     "weather_now", {"city": "Mumbai"}),
    ("Conditions in Sydney?",
     "weather_now", {"city": "Sydney"}),
]
