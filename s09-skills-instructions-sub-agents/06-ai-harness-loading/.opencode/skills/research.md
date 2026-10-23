---
name: research-skill
version: 1.0.0
type: skill
harness: opencode
description: Multi-step research workflow for OpenCode agents
workflow_type: multi_step
steps:
  - search
  - validate
  - extract
  - synthesize
  - output
tools_used:
  - web_search
  - scrape_url
  - validate_source
input_format: json
output_format: json
max_sources: 5
---

# Research Skill

## Description
Multi-step research workflow for OpenCode agents.

## Workflow
1. **Search**: Use web_search tool
2. **Validate**: Check source credibility
3. **Extract**: Scrape top sources
4. **Synthesize**: Combine findings
5. **Output**: Return structured data

## Input
```json
{
  "topic": "string",
  "depth": "quick|thorough"
}
```

## Output
```json
{
  "topic": "string",
  "summary": "string",
  "findings": ["array"],
  "sources": [{"url": "...", "credibility": "high"}],
  "confidence": "high|medium|low"
}
```

## Rules
- Max 5 sources
- Always include URLs
- Rate confidence accurately
