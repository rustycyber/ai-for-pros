"""Demo: Handoffs in Action - See orchestrator manage agent handoffs"""

import sys
from pathlib import Path

# Cross-platform path setup
sys.path.insert(0, str(Path(__file__).parent.parent / "04-subagents"))
sys.path.insert(0, str(Path(__file__).parent.parent / "share"))

from agents.research.agent import ResearchAgent
from agents.writer.agent import WriterAgent
from agents.orchestrator.orchestrator import OrchestratorAgent
from handoff_manager import HandoffManager
from demo_helpers import (
    section_header, subsection_header, pause, step_marker,
    show_result, show_key_takeaways, next_step
)
import json


section_header("DEMO: HANDOFFS IN ACTION")

subsection_header("WHAT IS A HANDOFF?")
print("""
A handoff is when one agent delegates work to another agent:

1. ✅ Validated - Target agent must exist
2. 📦 Packaged - Context wrapped in expected format
3. 🔄 Transferred - Control passed to target agent
4. 📝 Recorded - Handoff tracked in history
5. ↩️ Returned - Results come back to source

Defined in AGENT.md files under 'Handoffs' section.
""")

pause("Press [Enter] to start Example 1...")

# ============================================================================
# EXAMPLE 1: RESEARCH → WRITER HANDOFF
# ============================================================================
section_header("EXAMPLE 1: RESEARCH → WRITER HANDOFF")

pause("Press [Enter] to initialize agents...")

# Initialize agents
research_agent = ResearchAgent()
writer_agent = WriterAgent()
handoff_manager = HandoffManager()

step_marker(1, 3, "Research Agent executes")
print("\n[1] Research Agent executes...")
research_result = research_agent.execute("Python benefits", depth="quick")

pause("Press [Enter] to see research output...")

print("\nResearch output:")
output_str = json.dumps(research_result, indent=2)
print(output_str[:300] + "...\n")

pause("Press [Enter] to package for handoff...")

step_marker(2, 3, "Packaging for handoff")
print("\n[2] Packaging for handoff...")
handoff_package = {
    "research_package": research_result,
    "format_requirements": {
        "style": "blog",
        "length": 300,
        "tone": "casual"
    }
}
print(f"Package keys: {list(handoff_package.keys())}")
print(f"  research_package keys: {list(handoff_package['research_package'].keys())}")
print(f"  format_requirements: {handoff_package['format_requirements']}")

pause("Press [Enter] to handoff to Writer Agent...")

step_marker(3, 3, "Handoff to Writer Agent")
print("\n[3] Handoff to Writer Agent...")
writer_result = writer_agent.execute(handoff_package)

pause("Press [Enter] to see writer output...")

print("\nWriter output:")
show_result(writer_result)

pause("Press [Enter] to start Example 2: Orchestrator...")

# ============================================================================
# EXAMPLE 2: ORCHESTRATOR MANAGING HANDOFFS
# ============================================================================
section_header("EXAMPLE 2: ORCHESTRATOR MANAGING HANDOFFS")

pause("Press [Enter] to initialize orchestrator...")

orchestrator = OrchestratorAgent()

print("\n[ORCHESTRATOR] User request: 'Research FastAPI and write a summary'")
print("\nOrchestrator will:")
print("  1. Parse intent → needs_research=True, needs_writing=True")
print("  2. Handoff to Research Agent")
print("  3. Wait for research_package")
print("  4. Package context for Writer Agent")
print("  5. Handoff to Writer Agent")
print("  6. Return final result")

pause("Press [Enter] to execute orchestrated workflow...")

result = orchestrator.execute("Research FastAPI and write a summary")

pause("Press [Enter] to see final result...")

section_header("FINAL RESULT")
show_result(result)

pause("Press [Enter] to see handoff protocol...")

# ============================================================================
# HANDOFF PROTOCOL
# ============================================================================
section_header("HANDOFF PROTOCOL")

print("""
┌─────────────────────────────────────────────────────────────┐
│                    HANDOFF WORKFLOW                          │
└─────────────────────────────────────────────────────────────┘

[Research Agent]                    [Writer Agent]
       │                                  │
       │ 1. Complete research             │
       │ 2. Validate can handoff          │
       │                                  │
       ├──────── HANDOFF ────────────────>│
       │                                  │
       │ Package:                         │
       │  {                               │
       │    research_package: {...},      │
       │    format_requirements: {...}    │
       │  }                               │
       │                                  │
       │                         3. Receive package
       │                         4. Execute writing
       │                         5. Return result
       │                                  │
       │<─────── RESULT ──────────────────┤
       │                                  │
       │ 6. Return to user                │

Handoff defined in AGENT.md:
  ## Handoffs
  
  ### When to Hand Off
  After completing research, hand off to Writer Agent if:
  - User requested formatted output
  
  ### Handoff To: Writer Agent
  - Agent: agents/writer/AGENT.md
  - Package: {research_package, format_requirements}
""")

pause("Press [Enter] to see key takeaways...")

show_key_takeaways([
    "Handoffs are defined in AGENT.md files - when to handoff, target agent, context format",
    "Handoff Manager validates and tracks - target exists, package format correct, history recorded",
    "Orchestrator coordinates handoffs - routes requests, manages workflow, returns final result",
    "Context is preserved - research findings passed to Writer, format requirements included, sources cited throughout"
])

next_step("06-ai-harness-loading/demo_harness_loading.py")
