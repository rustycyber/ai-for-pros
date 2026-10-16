---
name: research-skill
version: 1.0.0
type: skill
description: Multi-step workflow for researching any topic and returning structured findings
workflow_type: multi_step
steps:
  - understand
  - search
  - evaluate
  - extract
  - synthesize
  - cite
tools_used:
  - web_search
  - scrape_url
  - validate_source
input_format: json
output_format: json
max_sources: 5
author: AI Course Workshop
---

# Research Skill

## Description
Multi-step workflow for researching any topic and returning structured findings.

## Workflow Steps
1. **Understand** - Parse the research question/topic
2. **Search** - Use web_search tool to find relevant sources
3. **Evaluate** - Validate source credibility (high/medium/low)
4. **Extract** - Scrape top 3-5 sources for key information
5. **Synthesize** - Combine findings into structured output
6. **Cite** - Format all sources with credibility scores

## Input
```json
{
  "topic": "string - what to research",
  "depth": "quick|thorough"
}
```

## Output
```json
{
  "topic": "string",
  "summary": "string - 2-3 sentence overview",
  "key_findings": ["array of strings"],
  "sources": [
    {
      "url": "string",
      "title": "string",
      "credibility": "high|medium|low",
      "relevance": "string - why this source matters"
    }
  ],
  "confidence": "high|medium|low"
}
```

## Rules
- Maximum 5 sources
- Never use sources older than 2 years (unless historical topic)
- Always include source URLs
- If no good sources found, return confidence: "low"

## Example Execution

**Input**: `{"topic": "Python benefits", "depth": "quick"}`

**Execution**:
1. Search: "Python programming benefits"
2. Find 5 results → Validate credibility
3. Scrape top 3 URLs
4. Extract key points from each
5. Synthesize into findings array
6. Return structured JSON

**Output**:
```json
{
  "topic": "Python benefits",
  "summary": "Python offers simplicity, versatility, and strong community support.",
  "key_findings": [
    "Easy to learn with simple syntax",
    "Versatile - web, data science, automation",
    "Large ecosystem of libraries"
  ],
  "sources": [
    {
      "url": "https://python.org",
      "title": "Why Python",
      "credibility": "high",
      "relevance": "Official source"
    }
  ],
  "confidence": "high"
}
```
