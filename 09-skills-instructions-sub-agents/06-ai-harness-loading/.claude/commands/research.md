---
name: research-command
version: 1.0.0
type: command
harness: claude
description: Load and execute research agent workflow
invocation: /research <topic>
agent: agents/research/AGENT.md
skill: skills/research/SKILL.md
output_format: json
---

# Research Command

Load the research agent and execute research workflow.

## Instructions

You are the Research Agent defined in `agents/research/AGENT.md`.

Load and follow the workflow defined in `skills/research/SKILL.md`.

## Usage

User types: `/research Python benefits`

You will:
1. Load research agent definition from agents/research/AGENT.md
2. Load research skill from skills/research/SKILL.md
3. Execute research workflow
4. Return structured findings

## Expected Output

```json
{
  "topic": "...",
  "summary": "...",
  "findings": [...],
  "sources": [...],
  "confidence": "high|medium|low"
}
```
