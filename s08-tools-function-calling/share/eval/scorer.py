"""Score a single result against an expected partial."""
from __future__ import annotations

from typing import Any


def expected_keys_match(result: dict[str, Any], expected_partial: dict[str, Any]) -> bool:
    """True iff every key in expected_partial is in result with matching value
    (case-insensitive for strings)."""
    for key, want in expected_partial.items():
        got = result.get(key)
        if got is None:
            return False
        if isinstance(want, str) and isinstance(got, str):
            if want.lower() != got.lower():
                return False
        elif want != got:
            return False
    return True


def score_run(tool_calls: list[dict], expected_tool: str, expected_partial: dict) -> tuple[bool, str]:
    """A run passes if the expected tool was called at least once AND
    returned a result containing the expected fields.

    Returns (passed, reason)."""
    matching = [tc for tc in tool_calls if tc["name"] == expected_tool]
    if not matching:
        called = [tc["name"] for tc in tool_calls] or ["(no tools called)"]
        return False, f"tool {expected_tool} not called (called: {called})"
    for tc in matching:
        if expected_keys_match(tc["result"], expected_partial):
            return True, "ok"
    return False, (
        f"{expected_tool} called but result did not match expected "
        f"{expected_partial}"
    )
