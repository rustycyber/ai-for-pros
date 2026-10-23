# Writing Skill

## Description
Content creation workflow for OpenCode agents.

## Workflow
1. **Parse**: Receive research_package
2. **Structure**: Organize content outline
3. **Draft**: Write content following format
4. **Cite**: Add citations from sources
5. **Output**: Return formatted content

## Input
```json
{
  "research_package": {
    "topic": "string",
    "findings": ["array"],
    "sources": ["array"]
  },
  "format_requirements": {
    "style": "blog|article|summary",
    "length": "number",
    "tone": "formal|casual|neutral"
  }
}
```

## Output
```json
{
  "title": "string",
  "content": "string",
  "word_count": "number",
  "citations": ["array"]
}
```

## Rules
- Always use provided research
- Match style and tone
- Include all citations
