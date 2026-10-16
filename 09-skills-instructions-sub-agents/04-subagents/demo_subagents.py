"""Demo: Subagents in Action - Run this to see all agents working"""

import sys
from pathlib import Path

# Add to path for cross-platform compatibility
sys.path.insert(0, str(Path(__file__).parent))
# Add shared utilities
sys.path.insert(0, str(Path(__file__).parent.parent / "share"))

from agents.research.agent import ResearchAgent
from agents.writer.agent import WriterAgent
from agents.orchestrator.orchestrator import OrchestratorAgent
from demo_helpers import (
    section_header, subsection_header, pause, step_marker,
    show_result, show_key_takeaways, next_step
)
import json


section_header("DEMO: SUBAGENTS IN ACTION")

pause("Press [Enter] to start Part 1: Research Agent...")

# ============================================================================
# PART 1: RESEARCH AGENT
# ============================================================================
section_header("PART 1: RESEARCH AGENT (Independent)")

print("\n📄 AGENT.MD loaded:")
research_agent = ResearchAgent()
print(f"  Length: {len(research_agent.agent_md)} characters")
print(f"  Contains 'Handoffs' section: {'Handoffs' in research_agent.agent_md}")

pause("Press [Enter] to execute Research Agent standalone...")

step_marker(1, 3, "Executing Research Agent")
print("\n[EXECUTING] Research Agent standalone...")
result = research_agent.execute("Python benefits", depth="quick")

pause("Press [Enter] to see research results...")

print("\n📊 Result:")
show_result(result)

pause("Press [Enter] to start Part 2: Writer Agent...")

# ============================================================================
# PART 2: WRITER AGENT
# ============================================================================
section_header("PART 2: WRITER AGENT (Independent)")

print("\n📄 AGENT.MD loaded:")
writer_agent = WriterAgent()
print(f"  Length: {len(writer_agent.agent_md)} characters")
print(f"  Contains 'Receives Handoffs From': {'Receives Handoffs From' in writer_agent.agent_md}")

pause("Press [Enter] to simulate handoff package...")

# Simulate handoff package
handoff = {
    "research_package": result,
    "format_requirements": {"style": "blog", "length": 300, "tone": "casual"}
}

step_marker(2, 3, "Executing Writer Agent with handoff package")
print("\n[EXECUTING] Writer Agent with handoff package...")
print(f"\nHandoff Package:")
print(f"  research_package keys: {list(handoff['research_package'].keys())}")
print(f"  format_requirements: {handoff['format_requirements']}")

pause("Press [Enter] to see writer results...")

writer_result = writer_agent.execute(handoff)
print("\n📊 Result:")
show_result(writer_result)

pause("Press [Enter] to start Part 3: Orchestrator...")

# ============================================================================
# PART 3: ORCHESTRATOR
# ============================================================================
section_header("PART 3: ORCHESTRATOR (Managing Handoffs)")

print("\n📄 ORCHESTRATOR AGENT.MD loaded:")
orchestrator = OrchestratorAgent()
print(f"  Length: {len(orchestrator.agent_md)} characters")
print(f"  Contains 'Routing Logic': {'Routing Logic' in orchestrator.agent_md}")
print(f"  Contains 'Handoff Protocol': {'Handoff Protocol' in orchestrator.agent_md}")

pause("Press [Enter] to execute full workflow...")

step_marker(3, 3, "Full workflow: Research → Handoff → Write")
print("\n[EXECUTING] Full workflow: Research → Handoff → Write")
user_request = "Research Python benefits and write a summary"
print(f"\nUser Request: '{user_request}'")

pause("Press [Enter] to see orchestrator execute...")

final_result = orchestrator.execute(user_request)

pause("Press [Enter] to see final results...")

print("\n📊 Final Result:")
show_result(final_result)

pause("Press [Enter] to see key takeaways...")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
show_key_takeaways([
    "Each agent has AGENT.md defining Purpose, Capabilities, Tools, Skills, Behavior, Rules, Handoffs, Output format",
    "Research Agent: Specialized in information gathering, has research_skill + tools, can handoff to Writer",
    "Writer Agent: Specialized in content creation, has writing tools, receives handoffs from Research Agent",
    "Orchestrator Agent: Routes requests, packages context, manages multi-agent workflows, has no tools",
    "Handoffs are defined in AGENT.md files: when to handoff, what agent, what context to package"
])

next_step("05-handoffs/demo_handoffs.py")
