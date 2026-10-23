# GitHub Copilot Instructions

This workspace has specialized agents and skills defined in AGENT.md and SKILL.md files.

## Agent System

### Research Agent
File: `agents/research/AGENT.md`
- Role: Information gathering and validation
- Tools: web_search, scrape_url, validate_source
- Skills: research_skill
- Can handoff to: Writer Agent

### Writer Agent
File: `agents/writer/AGENT.md`  
- Role: Content creation and formatting
- Tools: format_document, add_citations
- Receives handoffs from: Research Agent

### Orchestrator Agent
File: `agents/orchestrator/AGENT.md`
- Role: Route requests, manage handoffs
- Routes to: Research Agent, Writer Agent

## Skills

### Research Skill
File: `skills/research/SKILL.md`
- Workflow: search → evaluate → extract → synthesize
- Input: topic, depth
- Output: structured findings with sources

### Analysis Skill
File: `skills/analysis/SKILL.md`
- Workflow: parse → process → extract → structure
- Input: data, analysis_type
- Output: insights and metrics

## Handoff Protocol

When implementing multi-agent workflows:

### Orchestrator Pattern

```python
# Step 1: Research Phase
research_findings = research_agent.execute(topic="Python benefits")

# Step 2: Package for Handoff
handoff_package = {
    "research_package": research_findings,
    "format_requirements": {"style": "blog", "length": 500}
}

# Step 3: Writing Phase
final_output = writer_agent.execute(handoff_package)
```

## Usage Guidelines

When generating code suggestions:

1. **Check AGENT.md files** for agent definitions
2. **Load SKILL.md files** for workflow specifications
3. **Follow handoff protocol** when connecting agents
4. **Preserve context** in handoff packages
5. **Include citations** from sources

## Example Workflow

User comment: "Research FastAPI and write a summary"

Copilot should suggest:

```python
from agents.orchestrator.orchestrator import OrchestratorAgent

orchestrator = OrchestratorAgent()
result = orchestrator.execute("Research FastAPI and write a summary")
```

The orchestrator will:
- Parse intent
- Handoff to Research Agent
- Package results
- Handoff to Writer Agent
- Return final output
