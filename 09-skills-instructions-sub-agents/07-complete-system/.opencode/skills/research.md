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
