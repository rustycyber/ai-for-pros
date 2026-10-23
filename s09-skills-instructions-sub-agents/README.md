# S09: Skills, Instructions, Subagents & Handoffs

Learn how to build multi-agent systems with declarative definitions and handoff protocols.

## Setup

```bash
uv sync
```

## Running Demos (In Order)

```bash
# 1. Understand tools vs skills
uv run python 01-tools-vs-skills/comparison.py

# 2. See skills with SKILL.md
uv run python 02-skills/demo_skill.py

# 3. See instruction files
uv run python 03-instructions/demo_instructions.py

# 4. See subagents with AGENT.md
uv run python 04-subagents/demo_subagents.py

# 5. See handoffs in action
uv run python 05-handoffs/demo_handoffs.py

# 6. How AI harnesses load files
uv run python 06-ai-harness-loading/demo_harness_loading.py

# 7. Complete system
uv run python 07-complete-system/solution/main.py
```

## Testing with AI Harnesses

### OpenCode
```bash
cd 07-complete-system
opencode

# OpenCode automatically loads:
# - .opencode/instructions/ → Agent behaviors
# - .opencode/skills/ → Skill workflows

# Example: Research workflow
# The research agent instruction is loaded from:
# .opencode/instructions/research-agent.md
# Which references the skill from:
# .opencode/skills/research.md

# Just ask questions naturally:
# "Research Python benefits"
# OpenCode will use the research-agent instruction and research skill
```

### Claude Code CLI
```bash
cd 07-complete-system
claude

# Use slash commands defined in .claude/commands/
/research Python benefits           # Loads research AGENT.md + SKILL.md
/orchestrate Research FastAPI...     # Multi-agent handoff
```

### GitHub Copilot
```bash
# Open in VS Code with Copilot
# Copilot reads .github/copilot-instructions.md
# Suggests multi-agent patterns automatically
```

## Workshop Challenge

Implement the orchestrator in `07-complete-system/starter/main.py`

## Key Concepts

### SKILL.md
Declarative skill definition (natural language + structured format)
- Workflow steps
- Input/output contracts
- Rules and examples

### AGENT.md
Declarative agent definition
- Purpose and capabilities
- Tools and skills
- Behavior and rules
- **Handoff specifications**

### Handoffs
Agents delegating to other agents
- When to handoff
- Target agent
- Context packaging
- Handoff protocol

### AI Harness Loading
- **OpenCode** (Primary): `.opencode/instructions/` and `.opencode/skills/`
  - Instructions define agent behaviors (loaded automatically)
  - Skills define workflows (referenced by instructions)
  - Available throughout session without explicit commands
- **Claude Code**: `.claude/commands/` → Slash commands (`/research`, `/orchestrate`)
- **GitHub Copilot**: `.github/copilot-instructions.md` → Workspace context

## File Structure

```
├── 01-tools-vs-skills/      # Understanding basics
├── 02-skills/               # SKILL.md + skill.py
├── 03-instructions/          # Traditional instruction files
├── 04-subagents/             # AGENT.md + agent.py
├── 05-handoffs/              # Handoff protocol
├── 06-ai-harness-loading/    # How harnesses load files
└── 07-complete-system/       # Everything working together
    ├── starter/              # Your implementation
    ├── solution/             # Working example
    ├── .opencode/            # OpenCode config (primary)
    │   ├── instructions/     # Agent behaviors
    │   └── skills/           # Skill workflows
    ├── .claude/              # Claude Code config
    │   └── commands/         # Slash commands
    └── .github/              # GitHub Copilot config
```

## Tests & Eval

```bash
PYTHONPATH=. uv run pytest share/tests/
PYTHONPATH=. uv run python share/eval/run_eval.py
```
