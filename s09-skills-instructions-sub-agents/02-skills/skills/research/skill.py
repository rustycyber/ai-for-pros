"""Research Skill Implementation - Multi-step workflow"""
from typing import Dict, List


def web_search(query: str) -> List[Dict]:
    """Tool: Search the web"""
    # Simulated search results
    return [
        {"url": "https://python.org", "title": "Why Python", "credibility": "high"},
        {"url": "https://realpython.com", "title": "Python Benefits", "credibility": "high"},
        {"url": "https://example.com/python", "title": "Python Guide", "credibility": "medium"},
    ]


def scrape_url(url: str) -> str:
    """Tool: Extract content from URL"""
    # Simulated content
    return f"Content from {url}: Python is versatile and easy to learn."


def synthesize(content_list: List[str], topic: str) -> Dict:
    """Tool: Synthesize multiple content pieces into findings"""
    findings = [
        f"Key insight 1 about {topic}",
        f"Key insight 2 about {topic}",
        f"Key insight 3 about {topic}",
    ]
    return findings


def research_skill(topic: str, depth: str = "quick") -> Dict:
    """
    SKILL: Research Workflow
    
    Executing multi-step research process:
    1. Understand topic
    2. Search for sources
    3. Evaluate credibility
    4. Extract content
    5. Synthesize findings
    6. Return structured output
    """
    print(f"\n[SKILL] Executing: research_skill")
    print(f"  Input: topic='{topic}', depth='{depth}'")
    
    # Step 1 & 2: Search
    print("\n  Step 1-2: Searching...")
    sources = web_search(topic)
    print(f"    Found {len(sources)} sources")
    
    # Step 3: Evaluate (already in simulated data)
    print("\n  Step 3: Evaluating credibility...")
    valid_sources = [s for s in sources if s["credibility"] in ["high", "medium"]]
    print(f"    {len(valid_sources)} valid sources")
    
    # Step 4: Extract content
    print("\n  Step 4: Extracting content...")
    max_sources = 3 if depth == "quick" else 5
    scraped_content = []
    for source in valid_sources[:max_sources]:
        content = scrape_url(source["url"])
        scraped_content.append(content)
        print(f"    Scraped: {source['url']}")
    
    # Step 5: Synthesize
    print("\n  Step 5: Synthesizing findings...")
    key_findings = synthesize(scraped_content, topic)
    
    # Step 6: Structure output
    print("\n  Step 6: Structuring output...")
    result = {
        "topic": topic,
        "summary": f"{topic} offers multiple benefits and applications.",
        "key_findings": key_findings,
        "sources": valid_sources[:max_sources],
        "confidence": "high" if depth == "thorough" else "medium"
    }
    
    print(f"\n  ✅ Skill complete!")
    return result


def load_skill_definition() -> str:
    """Load SKILL.md content"""
    from pathlib import Path
    skill_md = Path(__file__).parent / "SKILL.md"
    return skill_md.read_text()


if __name__ == "__main__":
    print("="*70)
    print(" RESEARCH SKILL EXECUTION")
    print("="*70)
    
    # Show SKILL.md
    print("\n📚 SKILL.MD DEFINITION:")
    print("-" * 70)
    skill_def = load_skill_definition()
    print(skill_def[:500] + "...\n")
    
    # Execute skill
    print("="*70)
    print(" EXECUTING SKILL")
    print("="*70)
    result = research_skill("Python benefits", depth="quick")
    
    print("\n" + "="*70)
    print(" RESULT")
    print("="*70)
    import json
    print(json.dumps(result, indent=2))
