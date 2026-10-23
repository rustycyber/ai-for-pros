"""Demo: Skills in Action - Run this to see SKILL.md + skill.py working"""

import sys
from pathlib import Path

# Add skills to path for cross-platform compatibility
sys.path.insert(0, str(Path(__file__).parent))
# Add shared utilities
sys.path.insert(0, str(Path(__file__).parent.parent / "share"))

from skills.research.skill import research_skill, load_skill_definition
from skills.analysis.skill import analysis_skill
from demo_helpers import (
    section_header, subsection_header, pause, step_marker,
    show_result, show_key_takeaways, next_step
)
import json


section_header("DEMO: SKILLS IN ACTION")

pause("Press [Enter] to start Part 1: Research Skill...")

# ============================================================================
# PART 1: RESEARCH SKILL
# ============================================================================
section_header("PART 1: RESEARCH SKILL")

pause("Press [Enter] to view SKILL.MD definition...")

# Show SKILL.MD
print("\n📄 SKILL.MD (Natural Language Definition):")
print("-" * 70)
skill_md = load_skill_definition()
print(skill_md[:400] + "...(truncated)\n")

pause("Press [Enter] to execute research skill...")

step_marker(1, 2, "Executing Research Skill")
print("\n[EXECUTING] RESEARCH SKILL")
print("=" * 70)
result = research_skill("Python benefits", depth="quick")

pause("Press [Enter] to see structured output...")

print("\n📊 STRUCTURED OUTPUT:")
show_result(result)

pause("Press [Enter] to start Part 2: Analysis Skill...")

# ============================================================================
# PART 2: ANALYSIS SKILL
# ============================================================================
section_header("PART 2: ANALYSIS SKILL")

step_marker(2, 2, "Executing Analysis Skill")
result = analysis_skill(
    data="Python adoption grew 25% in 2024 with 10M new developers",
    analysis_type="summary"
)

pause("Press [Enter] to see analysis output...")

print("\n📊 STRUCTURED OUTPUT:")
show_result(result)

pause("Press [Enter] to see key takeaways...")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
show_key_takeaways([
    "SKILL.md: Declarative, natural language definition - describes workflow steps, defines input/output contracts, human-readable and machine-parseable",
    "skill.py: Python implementation - executes the workflow, uses multiple tools internally, returns structured output",
    "Skills are workflows, not single functions - multiple steps, multiple tools, decision making, structured output"
])

next_step("03-instructions/demo_instructions.py")
