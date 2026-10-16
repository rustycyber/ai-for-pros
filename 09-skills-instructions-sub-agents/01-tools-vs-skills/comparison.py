"""Side-by-Side Comparison: Tool vs Skill"""

from tool_example import web_search
from skill_example import research_skill

print("="*70)
print(" TOOLS vs SKILLS - SIDE BY SIDE COMPARISON")
print("="*70)

print("\n" + "="*70)
print(" EXAMPLE 1: USING A TOOL")
print("="*70)
print("\nTOOL: web_search()")
print("PURPOSE: Does ONE thing - search the web")
print("\nCode:")
print("  result = web_search('Python benefits')")
print("\nExecution:")
result = web_search("Python benefits")
print(f"  {result}")
print("\nObservation: Single call. Single result. Done.")

print("\n" + "="*70)
print(" EXAMPLE 2: USING A SKILL")
print("="*70)
print("\nSKILL: research_skill()")
print("PURPOSE: complete workflow - search, scrape, summarize, structure")
print("\nCode:")
print("  result = research_skill('Python benefits', depth='quick')")
print("\nExecution:")
result = research_skill("Python benefits", depth="quick")
print(f"\n  {result}")
print("\nObservation: Multiple steps. Multiple tools. Structured output.")

print("\n" + "="*70)
print(" KEY DIFFERENCES")
print("="*70)

comparison = """
┌─────────────────────┬──────────────────┬─────────────────────┐
│ Aspect               │ Tool             │ Skill               │
├─────────────────────┼──────────────────┼─────────────────────┤
│ Scope                │ Single function  │ Multi-step workflow │
│ Complexity           │ Simple           │ Complex             │
│ Tools Used           │ 0 (it IS a tool) │ Multiple tools      │
│ Steps                │ 1                │ Multiple            │
│ Decision Making      │ None             │ Yes                 │
│ Output               │ Raw result       │ Structured data     │
│ Example              │ web_search()     │ research_skill()    │
│ Analogy              │ Hammer           │ Building a house    │
└─────────────────────┴──────────────────┴─────────────────────┘
"""
print(comparison)

print("\n" + "="*70)
print(" WHEN TO USE WHAT?")
print("="*70)
print("""
Use TOOLS when:
  ✅ Single, atomic action
  ✅ No decision making needed
  ✅ Example: calculate(), search(), save()

Use SKILLS when:
  ✅ Multi-step workflow
  ✅ Need to orchestrate multiple tools
  ✅ Need reasoning/decision making
  ✅ Example: research(), analyze(), generate_report()
""")

print("="*70)
print(" RUN THIS:")
print("   python tool_example.py    # See tool in action")
print("   python skill_example.py    # See skill in action")
print("="*70)
