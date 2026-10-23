"""Research Agent Implementation"""
from typing import Dict, List
from pathlib import Path
import json


class ResearchAgent:
    """Specialized Research Agent with tools and skills"""
    
    def __init__(self):
        self.name = "research_agent"
        self.agent_md = self.load_agent_definition()
        self.tools = self.load_tools()
        self.skills = self.load_skills()
    
    def load_agent_definition(self) -> str:
        """Load AGENT.md content"""
        agent_path = Path(__file__).parent / "AGENT.md"
        return agent_path.read_text()
    
    def load_tools(self) -> Dict:
        """Load agent's tools"""
        # Import tools from research's local directory
        from pathlib import Path
        import importlib.util
        
        tools_path = Path(__file__).parent / "tools.py"
        spec = importlib.util.spec_from_file_location("research_tools", tools_path)
        research_tools = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(research_tools)
        
        return {
            "web_search": research_tools.web_search,
            "scrape_url": research_tools.scrape_url,
            "validate_source": research_tools.validate_source
        }
    
    def load_skills(self) -> Dict:
        """Load agent's skills"""
        # Import skill with proper path
        import sys
        from pathlib import Path
        skill_path = Path(__file__).parent.parent.parent.parent / "02-skills"
        sys.path.insert(0, str(skill_path))
        from skills.research.skill import research_skill
        return {
            "research_skill": research_skill
        }
    
    def execute(self, topic: str, depth: str = "quick") -> Dict:
        """Execute research task"""
        print(f"\n[AGENT] Research Agent executing...")
        print(f"  Agent: {self.name}")
        print(f"  Task: Research '{topic}'")
        
        # Use research_skill
        result = self.skills["research_skill"](topic, depth)
        
        return result
    
    def prepare_handoff(self, result: Dict, format_requirements: Dict = None) -> Dict:
        """Package result for handoff to Writer Agent"""
        handoff_package = {
            "research_package": result,
            "format_requirements": format_requirements or {
                "style": "summary",
                "length": 300,
                "tone": "neutral"
            }
        }
        return handoff_package


if __name__ == "__main__":
    print("="*70)
    print(" RESEARCH AGENT")
    print("="*70)
    
    agent = ResearchAgent()
    
    # Show AGENT.md
    print("\n📄 AGENT.MD:")
    print("-" * 70)
    print(agent.agent_md[:400] + "...\n")
    
    # Execute
    result = agent.execute("Python benefits", depth="quick")
    
    print("\n📊 RESULT:")
    print(json.dumps(result, indent=2))
