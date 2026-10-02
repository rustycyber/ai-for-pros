import json

def add_numbers(a: float, b: float) -> str:
    """Executes deterministic addition on the host machine."""
    print(f"\n[HOST EXECUTION] Running local Python code: add_numbers(a={a}, b={b})")
    return str(a + b)

# Dictionary mapping tool names to actual python callables
TOOL_REGISTRY = {
    "add_numbers": add_numbers
}

# OpenAI / OpenRouter Tool Definition Standard
OPENAI_TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "add_numbers",
            "description": "Adds two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "The first number"},
                    "b": {"type": "number", "description": "The second number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]
