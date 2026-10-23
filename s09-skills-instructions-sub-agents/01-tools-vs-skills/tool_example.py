"""Simple Tool Example - Single Purpose Function"""

def web_search(query: str) -> str:
    """
    Single-purpose tool: Search the web.
    Takes input -> Returns output -> Done.
    """
    # Simulated search results
    results = [
        f"Result 1 for: {query}",
        f"Result 2 for: {query}",
        f"Result 3 for: {query}"
    ]
    return "\n".join(results)


if __name__ == "__main__":
    print("=== TOOL EXAMPLE ===")
    print("A tool is a single function that does ONE thing.\n")
    
    result = web_search("Python benefits")
    print(f"Input: 'Python benefits'")
    print(f"Output:\n{result}")
    print("\nThat's it. One function call. One result.")
