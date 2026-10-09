# S8 Lab - Tools & Function Calling

Build 3 tools, wire them into an agent loop using OpenRouter with DeepSeek V3, and score them with a 20-input eval harness.

---

## Project Structure

```
├── share/                    # Shared infrastructure (agents, eval, tests)
│   ├── agents/               # OpenRouter agent with tool-use loop
│   ├── eval/                 # Evaluation harness + golden dataset
│   └── tests/                # Acceptance tests (for both starter & solution)
├── starter/                  # Skeleton tools (first commit)
│   └── tools/                # Empty tool shells to implement
└── solution/                 # Full implementation (second commit)
    └── tools/                # Complete tool implementations
```

**What's where:**
- `share/agents/` - OpenRouter agent with tool-use loop
- `share/eval/` - 20-input eval harness + golden outputs
- `share/tests/` - Acceptance tests for tools (tests both starter & solution)
- `starter/tools/` - skeleton tools with schemas (NotImplementedError)
- `solution/tools/` - complete tool implementations

---

## Tools to Build

| Tool | Description | Parameters |
|------|-------------|------------|
| `flight_status` | Look up airline flight status | `flight_no`, `date` |
| `currency_convert` | Convert between currencies | `amount`, `from_ccy`, `to_ccy` |
| `weather_now` | Get current weather for a city | `city` |

All three are pure Python functions exposed as tools via JSON schema.

---

## Setup

```bash
cd labs/s08-tools-function-calling

# 1. Add your OpenRouter API key to .env
# Edit .env and add your key from https://openrouter.ai/keys
# (The .env file is committed with OPENROUTER_MODEL already set)

# 2. Install dependencies (creates .venv automatically)
uv sync
```

---

## Running Tests

```bash
# Test starter (will fail - NotImplementedError)
PYTHONPATH=starter uv run pytest share/tests/

# Test solution (should pass)
PYTHONPATH=solution uv run pytest share/tests/
```

---

## Running the Eval

```bash
# Run all 20 eval cases with solution (requires OPENROUTER_API_KEY)
PYTHONPATH=solution uv run python share/eval/run_eval.py

# Run against starter (will fail - NotImplementedError)
PYTHONPATH=starter uv run python share/eval/run_eval.py --n 1

# Run specific tool
PYTHONPATH=solution uv run python share/eval/run_eval.py --tool flight_status

# Run first N cases
PYTHONPATH=solution uv run python share/eval/run_eval.py --n 5
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Required for eval |
| `OPENROUTER_MODEL` | Model to use | `deepseek/deepseek-chat` |

### Alternative Models

```bash
# Use Claude 3.5 Sonnet
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet uv run python share/eval/run_eval.py

# Use GPT-4o
OPENROUTER_MODEL=openai/gpt-4o uv run python share/eval/run_eval.py
```

---

## Learning Objectives

1. Understand JSON schema for tool definitions
2. Build deterministic mock tools for testing
3. Wire tools into an agent loop
4. Evaluate tool-calling accuracy with a golden dataset

---

## Watch-Along Guide

### What you're seeing
1. Each tool has THREE pieces: implementation, JSON schema, and a row in the eval harness. Watch all three move together.
2. The agent loop is short: ask Claude, intercept any `tool_use` block, run the Python tool, feed the result back, repeat until Claude returns a final text reply.
3. The eval harness runs 20 inputs through the agent, scores the raw answer against a golden, and prints a pass/fail rate.

### When to use this pattern
- Anywhere your LLM needs to read or write a system of record.
- Internal APIs: wrap them as tools, not as raw HTTP from the prompt.
- Don't model UI affordances as tools; model business actions.

---

## Strategic Reflections

### Why this matters
Tools are the LLM's hands. The wrong tool surface ships bugs; the right one ships features.

### Design Decisions

1. **Tool granularity**: one mega-tool with 30 params or 6 focused tools? 
   - Focused tools are easier for models to pick correctly
   - They cost more tokens in the schema
   - Pick focused for accuracy

2. **Read vs write split**: keep write tools behind a "confirm" wrapper. 
   - The lab's structure puts each tool through an evaluator before any side effect lands.

3. **Versioning**: tool schemas change. 
   - Pin the version in the schema name (`flight_status_v2`) and migrate explicitly.

### Cost/Latency Profile
Each tool round-trips the model + one HTTP call. For latency-sensitive paths, cache aggressively and consider co-locating tool servers with the model API endpoint.

### Watch out for
- **Hallucinated parameters** when the tool name is too generic
- **Tools that return giant payloads** (>4KB) - trim or paginate before feeding back to the model
- **Auth**: tool calls happen server-side, but a tool that calls a user-scoped API still needs the user's identity
