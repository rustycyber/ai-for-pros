"""Writer Agent Tools - Specialized tools for content creation"""


def format_document(research_package: dict, format_requirements: dict) -> str:
    """Tool: Format research findings into structured content"""
    topic = research_package.get("topic", "Unknown")
    findings = research_package.get("findings", [])
    style = format_requirements.get("style", "summary")
    tone = format_requirements.get("tone", "neutral")
    
    # Simulated content generation
    content = f"""
{topic.title()}

Introduction:
{' '.join(findings[:2])}

Key Points:
{chr(10).join(f'- {finding}' for finding in findings)}

Conclusion:
{findings[0] if findings else 'No findings available'}
    """.strip()
    
    return content


def add_citations(sources: list) -> list:
    """Tool: Extract citation URLs from sources"""
    return [source.get("url") for source in sources if "url" in source]
