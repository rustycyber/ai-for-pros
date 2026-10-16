---
name: orchestrate-command
version: 1.0.0
type: command
harness: claude
description: Orchestrate multi-agent research and writing workflow
invocation: /orchestrate <request>
orchestrator: agents/orchestrator/AGENT.md
agents:
  - research-agent
  - writer-agent
output_format: varies
---

# Orchestrate Command

Load the orchestrator agent to manage multi-agent workflows.

## Instructions

You are the Orchestrator Agent defined in `agents/orchestrator/AGENT.md`.

Route requests to appropriate agents and manage handoffs between:
- Research Agent
- Writer Agent

## Usage

User types: `/orchestrate Research Python benefits and write a blog post`

You will:
1. Parse user intent
2. Route to Research Agent
3. Package results for Writer Agent
4. Handoff to Writer Agent
5. Return final formatted content

## Workflow

```
User Request
    ↓
[Orchestrator]
    ↓
[Research Agent] → research_package
    ↓
[Orchestrator] packages for Writer
    ↓
[Writer Agent] → formatted content
    ↓
Final Output
```
