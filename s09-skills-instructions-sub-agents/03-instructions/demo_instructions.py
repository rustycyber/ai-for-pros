"""Demo: Instruction Files - How agents load and use instructions"""

import sys
from pathlib import Path

# Add parent to path for shared utilities
sys.path.insert(0, str(Path(__file__).parent.parent / "share"))

from demo_helpers import (
    section_header, subsection_header, pause, step_marker, 
    show_result, show_key_takeaways, next_step, python_cmd
)
import json

# Resolve paths cross-platform (works in both macOS and Windows)
script_dir = Path(__file__).parent.resolve()
instructions_dir = script_dir / "instructions"


section_header("DEMO: INSTRUCTION FILES")

section_header("WHAT IS AN INSTRUCTION FILE?")
print("""
Instruction files are natural language prompts that define:
- Agent's role and identity
- Capabilities and style
- Rules and constraints
- Input/output formats
- Examples of desired behavior

They are loaded as system prompts to shape agent behavior.
""")

pause("Press [Enter] to see how to load instruction files...")

section_header("LOADING INSTRUCTION FILES")

# Load research instructions with robust path handling
research_instructions_path = instructions_dir / "research_agent.md"
research_instructions = research_instructions_path.read_text()

print(f"\n📄 RESEARCH AGENT INSTRUCTIONS:")
print("-" * 70)
print(research_instructions[:500] + "...\n")

pause("Press [Enter] to load writer agent instructions...")

# Load writer instructions
writer_instructions_path = instructions_dir / "writer_agent.md"
writer_instructions = writer_instructions_path.read_text()

print("=" * 70)
print(" WRITER AGENT INSTRUCTIONS:")
print("-" * 70)
print(writer_instructions[:500] + "...\n")

pause("Press [Enter] to see usage example...")

section_header("USING INSTRUCTIONS IN CODE")

code_example = '''
# Load instructions as system prompt
from pathlib import Path

research_instructions = Path("instructions/research_agent.md").read_text()

# Use with any LLM
messages = [
    {"role": "system", "content": research_instructions},
    {"role": "user", "content": "Research Python benefits"}
]

# Send to Claude, GPT, or any model
response = llm.chat(messages)
'''

print("\nExample Code:")
print(code_example)

pause("Press [Enter] to see simulation with instructions...")

section_header("SIMULATING AGENT WITH INSTRUCTIONS")

# Simulate a research agent using instructions
print("\n[AGENT] Research Agent initialized")
print(f"[AGENT] Loaded instructions from: instructions/research_agent.md")
print(f"[AGENT] Instructions length: {len(research_instructions)} characters")
print(f"[AGENT] Instructions parsed into:")
print(f"  - Role: Research specialist")
print(f"  - Rules: {research_instructions.count('## Rules')}")
print(f"  - Output format defined: {research_instructions.count('Output Format')}")

pause("Press [Enter] to process user request...")

print("\n[AGENT] Processing user request...")
print("  User: 'Research Python benefits'")

# Simulated output following instructions
simulated_output = {
    "topic": "Python benefits",
    "summary": "Python offers simplicity, versatility, and strong community support.",
    "findings": [
        "Easy to learn with clean syntax",
        "Versatile - web, data science, AI, automation",
        "Large ecosystem with 300k+ packages"
    ],
    "sources": [
        {"url": "https://python.org", "credibility": "high"},
        {"url": "https://realpython.com", "credibility": "high"}
    ],
    "confidence": "high"
}

print("\n[AGENT] Output (following instruction format):")
show_result(simulated_output)

pause("Press [Enter] to see key takeaways...")

show_key_takeaways([
    "Instruction files are plain text/markdown prompts",
    "Define agent behavior declaratively",
    "Loaded as system prompts at runtime",
    "Shape: Role, Rules, Style, Examples, Output formats",
    "Used by: Research Agent, Writer Agent, any specialized agent"
])

next_step("04-subagents/demo_subagents.py")
