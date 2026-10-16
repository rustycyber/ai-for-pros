---
name: analysis-skill
version: 1.0.0
type: skill
description: Multi-step workflow for analyzing data and extracting insights
workflow_type: multi_step
steps:
  - parse_data
  - analyze_patterns
  - extract_insights
  - generate_report
tools_used:
  - data_parser
  - pattern_analyzer
  - insight_generator
input_format: json
output_format: json
author: AI Course Workshop
---

# Analysis Skill

## Description
Multi-step workflow for analyzing data and extracting insights.

## Workflow Steps
1. **Parse Data** - Understand the input data structure
2. **Analyze Patterns** - Identify trends and patterns
3. **Extract Insights** - Generate key insights
4. **Generate Report** - Create structured analysis report

## Input
```json
{
  "data": "string or object - data to analyze",
  "analysis_type": "summary|trend|comparison|sentiment"
}
```

## Output
```json
{
  "analysis_type": "string",
  "summary": "string - brief analysis summary",
  "key_insights": ["array of strings"],
  "metrics": {
    "confidence": "high|medium|low",
    "data_quality": "high|medium|low"
  },
  "recommendations": ["array of strings"]
}
```

## Rules
- Always validate input data quality
- Provide confidence ratings
- Include actionable recommendations

## Example Execution

**Input**: `{"data": "Python adoption grew 25% in 2024", "analysis_type": "summary"}`

**Execution**:
1. Parse: Extract key metrics (25% growth, 2024)
2. Analyze: Identify trend (positive growth)
3. Generate insights: Strong momentum in Python ecosystem
4. Create report

**Output**:
```json
{
  "analysis_type": "summary",
  "summary": "Python shows strong growth momentum with 25% adoption increase in 2024",
  "key_insights": [
    "Significant growth trajectory",
    "Strong market momentum",
    "Increasing developer adoption"
  ],
  "metrics": {
    "confidence": "high",
    "data_quality": "high"
  },
  "recommendations": [
    "Continue monitoring growth trends",
    "Invest in Python ecosystem development"
  ]
}
```
