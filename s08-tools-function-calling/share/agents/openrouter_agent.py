"""Minimal OpenRouter tool-use loop using DeepSeek V3.

Uses OpenAI-compatible API via OpenRouter. Works with DeepSeek V3
and other OpenAI-shape tool-calling models.

    run_openrouter(user_msg, max_turns=4) -> {"final": "...", "tool_calls": [...]}
"""
from __future__ import annotations

import os
import sys
from typing import Any

from tools import TOOLS

MODEL = os.environ.get("OPENROUTER_MODEL", "deepseek/deepseek-v3")


def openrouter_tool_schemas() -> list[dict[str, Any]]:
    """Translate our internal tool schemas to OpenAI tool schema format."""
    out = []
    for _, schema in TOOLS.values():
        fn_schema = schema["function"]
        out.append({
            "type": "function",
            "function": {
                "name": fn_schema["name"],
                "description": fn_schema["description"],
                "parameters": fn_schema["parameters"],
            },
        })
    return out


def _client():
    api_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not api_key or api_key.startswith("sk-or-..."):
        print(
            "\n  OPENROUTER_API_KEY not set. Get one at "
            "https://openrouter.ai/keys"
            "\n  then add it to .env and try again.\n",
            file=sys.stderr,
        )
        sys.exit(1)
    from openai import OpenAI
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/ai-course",  # Optional, for rankings
            "X-Title": "AI Course Lab",  # Optional, for rankings
        },
    )


def run_openrouter(user_msg: str, max_turns: int = 4) -> dict[str, Any]:
    client = _client()
    schemas = openrouter_tool_schemas()
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_msg}]
    history: list[dict[str, Any]] = []

    for _ in range(max_turns):
        resp = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            tools=schemas,
            messages=messages,
        )
        
        choice = resp.choices[0]
        message = choice.message
        
        if message.tool_calls is None or len(message.tool_calls) == 0:
            return {"final": message.content or "", "tool_calls": history}
        
        messages.append({"role": "assistant", "content": message.content, "tool_calls": [
            {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
            for tc in message.tool_calls
        ]})
        
        for tc in message.tool_calls:
            import json
            fn, _ = TOOLS[tc.function.name]
            args = json.loads(tc.function.arguments)
            result = fn(**args)
            history.append({"name": tc.function.name, "args": args, "result": result})
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": str(result),
            })
        
        # Check if we should stop (no more tool calls needed)
        if choice.finish_reason != "tool_calls":
            text = message.content or ""
            return {"final": text, "tool_calls": history}

    return {"final": "(max turns reached)", "tool_calls": history}
