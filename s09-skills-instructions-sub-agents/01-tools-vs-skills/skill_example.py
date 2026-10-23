"""Skill Example - Multi-Step Workflow Using Multiple Tools"""

def web_search(query: str) -> str:
    """Tool 1: Search the web"""
    return f"Search results for: {query}"


def scrape_url(url: str) -> str:
    """Tool 2: Extract content from URL"""
    return f"Content from {url}"


def summarize(text: str) -> str:
    """Tool 3: Summarize text"""
    return f"Summary: {text[:50]}..."


def research_skill(topic: str, depth: str = "quick") -> dict:
    """
    Skill: Multi-step research workflow.
    
    A skill combines multiple tools + reasoning steps.
    It's a workflow, not just a single function.
    """
    print(f"[SKILL] Starting research on: {topic}")
    
    # Step 1: Search
    print("  Step 1: Searching...")
    search_results = web_search(topic)
    
    # Step 2: Scrape top results
    print("  Step 2: Scraping content...")
    content = scrape_url("https://example.com/article")
    
    # Step 3: Summarize findings
    print("  Step 3: Summarizing...")
    summary = summarize(content)
    
    # Step 4: Structure output
    print("  Step 4: Structuring output...")
    result = {
        "topic": topic,
        "summary": summary,
        "sources": ["https://example.com"],
        "confidence": "high" if depth == "thorough" else "medium"
    }
    
    return result


if __name__ == "__main__":
    print("=== SKILL EXAMPLE ===")
    print("A skill is a multi-step workflow using multiple tools.\n")
    
    result = research_skill("Python benefits", depth="quick")
    
    print("\n=== SKILL OUTPUT ===")
    print(f"Type: {type(result)}")
    print(f"Content: {result}")
    
    print("\n\nDIFFERENCE:")
    print("Tool  = Single function, single purpose")
    print("Skill = Workflow that orchestrates multiple tools")
