"""Writer Agent Implementation"""
from typing import Dict
from pathlib import Path
import json


class WriterAgent:
    """Specialized Writer Agent with tools and skills"""
    
    def __init__(self):
        self.name = "writer_agent"
        self.agent_md = self.load_agent_definition()
        self.tools = self.load_tools()
    
    def load_agent_definition(self) -> str:
        """Load AGENT.md content"""
        agent_path = Path(__file__).parent / "AGENT.md"
        return agent_path.read_text()
    
    def load_tools(self) -> Dict:
        """Load agent's tools"""
        # Import tools from writer's local directory
        from pathlib import Path
        import importlib.util
        
        tools_path = Path(__file__).parent / "tools.py"
        spec = importlib.util.spec_from_file_location("writer_tools", tools_path)
        writer_tools = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(writer_tools)
        
        return {
            "format_document": writer_tools.format_document,
            "add_citations": writer_tools.add_citations
        }
    
    def execute(self, handoff_package: Dict) -> Dict:
        """Execute writing task"""
        print(f"\n[AGENT] Writer Agent executing...")
        print(f"  Agent: {self.name}")
        
        research_package = handoff_package.get("research_package", {})
        format_requirements = handoff_package.get("format_requirements", {})
        
        print(f"  Topic: {research_package.get('topic')}")
        print(f"  Style: {format_requirements.get('style')}")
        
        # Format document
        content = self.tools["format_document"](
            research_package,
            format_requirements
        )
        
        # Add citations
        citations = self.tools["add_citations"](
            research_package.get("sources", [])
        )
        
        result = {
            "title": f"Article about {research_package.get('topic', 'Unknown')}",
            "content": content,
            "word_count": len(content.split()),
            "citations": citations
        }
        
        return result


if __name__ == "__main__":
    print("="*70)
    print(" WRITER AGENT")
    print("="*70)
    
    agent = WriterAgent()
    
    # Show AGENT.md
    print("\n📄 AGENT.MD:")
    print("-" * 70)
    print(agent.agent_md[:400] + "...\n")
    
    # Simulate receiving handoff from Research Agent
    handoff_package = {
        "research_package": {
            "topic": "Python benefits",
            "findings": ["Easy to learn", "Versatile", "Large ecosystem"],
            "sources": [{"url": "https://python.org", "credibility": "high"}]
        },
        "format_requirements": {
            "style": "blog",
            "length": 300,
            "tone": "casual"
        }
    }
    
    result = agent.execute(handoff_package)
    
    print("\n📊 RESULT:")
    print(json.dumps(result, indent=2))
