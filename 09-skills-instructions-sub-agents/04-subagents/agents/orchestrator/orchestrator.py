"""Orchestrator Agent - Routes and manages handoffs"""
from typing import Dict
from pathlib import Path
import json
import sys

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.research.agent import ResearchAgent
from agents.writer.agent import WriterAgent


class OrchestratorAgent:
    """Orchestrator that routes requests and manages handoffs"""
    
    def __init__(self):
        self.name = "orchestrator_agent"
        self.agent_md = self.load_agent_definition()
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
    
    def load_agent_definition(self) -> str:
        """Load AGENT.md content"""
        agent_path = Path(__file__).parent / "AGENT.md"
        return agent_path.read_text()
    
    def parse_intent(self, user_request: str) -> Dict:
        """Parse user request to determine routing"""
        user_lower = user_request.lower()
        
        intent = {
            "needs_research": "research" in user_lower or "find" in user_lower,
            "needs_writing": "write" in user_lower or "draft" in user_lower or "create" in user_lower,
            "topic": user_request,
            "format_requirements": {}
        }
        
        # Detect format
        if "blog" in user_lower:
            intent["format_requirements"] = {"style": "blog", "length": 500, "tone": "casual"}
        elif "summary" in user_lower:
            intent["format_requirements"] = {"style": "summary", "length": 300, "tone": "neutral"}
        elif "article" in user_lower:
            intent["format_requirements"] = {"style": "article", "length": 800, "tone": "formal"}
        else:
            intent["format_requirements"] = {"style": "summary", "length": 300, "tone": "neutral"}
        
        return intent
    
    def execute(self, user_request: str) -> Dict:
        """Execute orchestrated workflow"""
        print(f"\n[ORCHESTRATOR] Parsing request...")
        intent = self.parse_intent(user_request)
        
        print(f"  Needs Research: {intent['needs_research']}")
        print(f"  Needs Writing: {intent['needs_writing']}")
        print(f"  Topic: {intent['topic']}")
        print(f"  Format: {intent['format_requirements'].get('style')}")
        
        result = {}
        
        # Step 1: Research if needed
        if intent["needs_research"]:
            print(f"\n[ORCHESTRATOR] Handoff to Research Agent...")
            research_result = self.research_agent.execute(
                topic=intent["topic"],
                depth="quick"
            )
            
            # Step 2: Write if needed
            if intent["needs_writing"]:
                print(f"\n[ORCHESTRATOR] Packaging for Writer Agent...")
                handoff_package = self.package_for_handoff(
                    research_result,
                    intent["format_requirements"]
                )
                
                print(f"\n[ORCHESTRATOR] Handoff to Writer Agent...")
                writer_result = self.writer_agent.execute(handoff_package)
                
                result = writer_result
            else:
                result = research_result
        else:
            result = {"error": "Could not determine intent"}
        
        print(f"\n[ORCHESTRATOR] Returning result...")
        return result
    
    def package_for_handoff(self, research_result: Dict, format_requirements: Dict) -> Dict:
        """Package research results for handoff"""
        return {
            "research_package": research_result,
            "format_requirements": format_requirements
        }


if __name__ == "__main__":
    print("="*70)
    print(" ORCHESTRATOR AGENT")
    print("="*70)
    
    orchestrator = OrchestratorAgent()
    
    print("\n📄 AGENT.MD:")
    print("-" * 70)
    print(orchestrator.agent_md[:400] + "...\n")
    
    # Test orchestration
    user_request = "Research Python benefits and write a blog post"
    
    print(f"\n{'='*70}")
    print(f" USER REQUEST: {user_request}")
    print("="*70)
    
    result = orchestrator.execute(user_request)
    
    print("\n" + "="*70)
    print(" FINAL RESULT")
    print("="*70)
    print(json.dumps(result, indent=2))
