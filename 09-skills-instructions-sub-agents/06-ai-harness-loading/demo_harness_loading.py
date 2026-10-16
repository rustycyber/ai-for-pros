"""Demo: How AI Harnesses Load AGENT.md and SKILL.md Files"""

import sys
from pathlib import Path

# Cross-platform path setup
sys.path.insert(0, str(Path(__file__).parent.parent / "share"))

from demo_helpers import (
    section_header, subsection_header, pause, step_marker,
    show_key_takeaways, next_step
)
import json


section_header("HOW AI HARNESSES LOAD AGENT.MD & SKILL.MD FILES")

pause("Press [Enter] to start with Claude Code CLI...")

# ============================================================================
# 1. CLAUDE CODE CLI
# ============================================================================
section_header("1. CLAUDE CODE CLI (.claude/)")

pause("Press [Enter] to view directory structure...")

print("\nDirectory: .claude/")
print("  ├── commands/")
print("  │   ├── research.md       # /research command")
print("  │   └── orchestrate.md    # /orchestrate command")
print("  └── settings.json         # Claude configuration")

pause("Press [Enter] to view research.md command...")

print("\n📄 Command: research.md")
print("-" * 70)
# Resolve path cross-platform
script_dir = Path(__file__).parent.resolve()
claude_command_path = script_dir / ".claude" / "commands" / "research.md"
claude_command = claude_command_path.read_text()
print(claude_command[:300] + "...\n")

pause("Press [Enter] to see how Claude loads...")

print("✅ Claude Code loads:")
print("  - Commands from .claude/commands/*.md")
print("  - Each command references AGENT.md & SKILL.md")
print("  - User invokes: /research <topic>")
print("  - Claude executes workflow from definitions")

pause("Press [Enter] to continue with GitHub Copilot...")

# ============================================================================
# 2. GITHUB COPILOT
# ============================================================================
section_header("2. GITHUB COPILOT (.github/)")

print("\nDirectory: .github/")
print("  └── copilot-instructions.md     # Workspace instructions")

pause("Press [Enter] to view copilot-instructions.md...")

print("\n📄 File: copilot-instructions.md")
print("-" * 70)
copilot_inst_path = script_dir / ".github" / "copilot-instructions.md"
copilot_inst = copilot_inst_path.read_text()
print(copilot_inst[:400] + "...\n")

pause("Press [Enter] to see how Copilot loads...")

print("✅ GitHub Copilot loads:")
print("  - Workspace instructions from .github/copilot-instructions.md")
print("  - References AGENT.md files in workspace")
print("  - Uses definitions as context for suggestions")
print("  - Suggests multi-agent patterns when appropriate")

pause("Press [Enter] to continue with OpenCode...")

# ============================================================================
# 3. OPENCODE
# ============================================================================
section_header("3. OPENCODE (.opencode/)")

pause("Press [Enter] to view directory structure...")

print("\nDirectory: .opencode/")
print("  ├── instructions/")
print("  │   ├── research-agent.md  # Research agent behavior")
print("  │   └── writer-agent.md   # Writer agent behavior")
print("  └── skills/")
print("      ├── research.md       # Research skill workflow")
print("      └── writing.md        # Writing skill workflow")

pause("Press [Enter] to view research-agent.md...")

print("\n📄 Instructions: research-agent.md")
print("-" * 70)
opencode_inst_path = script_dir / ".opencode" / "instructions" / "research-agent.md"
opencode_inst = opencode_inst_path.read_text()
print(opencode_inst[:300] + "...\n")

pause("Press [Enter] to view research.md skill...")

print("📄 Skill: research.md")
print("-" * 70)
opencode_skill_path = script_dir / ".opencode" / "skills" / "research.md"
opencode_skill = opencode_skill_path.read_text()
print(opencode_skill[:300] + "...\n")

pause("Press [Enter] to see how OpenCode loads...")

print("✅ OpenCode loads:")
print("  - Instructions from .opencode/instructions/*.md")
print("  - Skills from .opencode/skills/*.md")
print("  - Agent definitions at session start")
print("  - Available throughout conversation")

pause("Press [Enter] to see comparison...")

# ============================================================================
# COMPARISON TABLE
# ============================================================================
section_header("COMPARISON: HOW EACH HARNESS LOADS")

comparison = """
┌─────────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Harness         │ Directory       │ What Loads       │ How Used        │
├─────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ Claude Code     │ .claude/        │ Commands (.md)   │ User types      │
│                 │                 │ → AGENT.md       │ /command        │
│                 │                 │ → SKILL.md       │                 │
├─────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ GitHub Copilot  │ .github/        │ copilot-         │ Context for     │
│                 │                 │ instructions.md  │ code            │
│                 │                 │ → AGENT.md refs  │ suggestions     │
├─────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ OpenCode        │ .opencode/      │ instructions/    │ Loaded at       │
│                 │                 │ → AGENT.md       │ session start   │
│                 │                 │ skills/          │ Available       │
│                 │                 │ → SKILL.md       │ throughout      │
└─────────────────┴─────────────────┴──────────────────┴─────────────────┘
"""
print(comparison)

pause("Press [Enter] to see practical usage...")

# ============================================================================
# PRACTICAL USAGE
# ============================================================================
section_header("PRACTICAL USAGE")

print("""
# Claude Code CLI
cd 06-ai-harness-loading
claude
> /research Python benefits           # Loads research.md → AGENT.md + SKILL.md
> /orchestrate Research FastAPI...     # Multi-agent handoff

# GitHub Copilot
# Open in VS Code with Copilot
# Copilot reads .github/copilot-instructions.md
# Suggests code based on AGENT.md and SKILL.md definitions

# OpenCode
opencode
# Automatically loads .opencode/instructions and .opencode/skills
# Agents and skills available in conversation
""")

pause("Press [Enter] to see key takeaways...")

show_key_takeaways([
    "AGENT.md and SKILL.md are declarative definitions - human-readable, machine-parseable, define behavior",
    "Each AI harness has its own loading mechanism - Claude Code: Commands, GitHub Copilot: Workspace instructions, OpenCode: Dedicated dirs",
    "Place files in correct locations - .claude/commands/*.md, .github/copilot-instructions.md, .opencode/instructions/*.md and .opencode/skills/*.md",
    "All harnesses preserve context and handoffs - Research findings passed to Writer, sources tracked, handoffs recorded",
    "Production pattern - AGENT.md defines agents, SKILL.md defines skills, Orchestrator manages handoffs, works across all major AI tools"
])

next_step("07-complete-system/solution/main.py")
