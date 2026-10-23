---
name: writing-skill
version: 1.0.0
type: skill
harness: opencode
description: Multi-step content creation workflow for OpenCode agents
workflow_type: multi_step
steps:
  - analyze_requirements
  - structure_content
  - draft_content
  - add_citations
  - format_output
tools_used:
  - format_document
  - add_citations
input_format: json
output_format: json
---

# Writing Skill

## Description
Multi-step content creation workflow for OpenCode agents.

## Workflow
1. **Analyze Requirements**: Parse format requirements and research package
2. **Structure Content**: Create outline based on style
3. **Draft Content**: Write content following specifications
4. **Add Citations**: Insert proper citations
5. **Format Output**: Apply final formatting

## Input
```json
{
  "research_package": {
    "topic": "string",
    "findings": ["array"],
    "sources": ["array"]
  },
  "format_requirements": {
    "style": "blog|article|summary|report",
    "length": "number",
    "tone": "formal|casual|technical"
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
- Always use provided research findings
- Match format requirements exactly
- Include proper citations
- Never fabricate information
