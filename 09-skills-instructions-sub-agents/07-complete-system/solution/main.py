"""Complete System: Multi-agent orchestration with skills, instructions, and handoffs"""

import sys
from pathlib import Path
import json

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "04-subagents"))

from agents.research.agent import ResearchAgent
from agents.writer.agent import WriterAgent


print("="*70)
print(" COMPLETE MULTI-AGENT SYSTEM")
print("="*70)
print("""
This system demonstrates:
✅ SKILL.md files (declarative skill definitions)
✅ AGENT.md files (declarative agent definitions)
✅ Handoffs (agents delegating to other agents)
✅ AI Harness configs (Claude, GitHub Copilot, OpenCode)
""")


class CompleteOrchestrator:
    """Orchestrator managing multi-agent workflows"""
    
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
        self.workflow_history = []
    
    def parse_intent(self, user_request: str) -> dict:
        """Parse user request to determine workflow needs"""
        user_lower = user_request.lower()
        
        intent = {
            "needs_research": any(word in user_lower for word in ["research", "find", "investigate", "look up"]),
            "needs_writing": any(word in user_lower for word in ["write", "draft", "create", "blog", "article", "summary"]),
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
        elif intent["needs_writing"]:
            intent["format_requirements"] = {"style": "summary", "length": 300, "tone": "neutral"}
        
        return intent
    
    def execute(self, user_request: str) -> dict:
        """Execute complete multi-agent workflow"""
        
        print(f"\n{'='*70}")
        print(f" USER REQUEST: {user_request}")
        print("="*70)
        
        # Parse intent
        print("\n[STEP 1] Parsing Intent...")
        intent = self.parse_intent(user_request)
        print(f"  Needs Research: {intent['needs_research']}")
        print(f"  Needs Writing: {intent['needs_writing']}")
        print(f"  Topic: {intent['topic']}")
        if intent['format_requirements']:
            print(f"  Format: {intent['format_requirements']}")
        
        result = {}
        
        # Research Phase
        if intent["needs_research"]:
            print(f"\n[STEP 2] Research Phase...")
            print(f"  Handoff to: Research Agent")
            
            research_result = self.research_agent.execute(
                topic=intent["topic"],
                depth="quick"
            )
            
            print(f"\n  Research Complete:")
            print(f"    Findings: {len(research_result.get('findings', []))} found")
            print(f"    Sources: {len(research_result.get('sources', []))} cited")
            print(f"    Confidence: {research_result.get('confidence')}")
            
            # Writing Phase
            if intent["needs_writing"]:
                print(f"\n[STEP 3] Handoff to Writer Agent...")
                
                handoff_package = {
                    "research_package": research_result,
                    "format_requirements": intent["format_requirements"]
                }
                
                print(f"  Packaging Context:")
                print(f"    Research findings: {len(research_result.get('findings', []))}")
                print(f"    Format: {intent['format_requirements'].get('style')}")
                
                writer_result = self.writer_agent.execute(handoff_package)
                
                print(f"\n  Writing Complete:")
                print(f"    Word count: {writer_result.get('word_count')}")
                print(f"    Citations: {len(writer_result.get('citations', []))}")
                
                result = writer_result
            else:
                result = research_result
        else:
            result = {"error": "Could not determine intent from request"}
        
        # Record workflow
        self.workflow_history.append({
            "request": user_request,
            "intent": intent,
            "result": result
        })
        
        print(f"\n[STEP 4] Returning Result...")
        return result
    
    def get_workflow_history(self) -> list:
        """Get all executed workflows"""
        return self.workflow_history


if __name__ == "__main__":
    orchestrator = CompleteOrchestrator()
    
    # Test Case 1: Research + Write
    print("\n" + "="*70)
    print(" TEST CASE 1: Research + Write")
    print("="*70)
    
    result1 = orchestrator.execute("Research Python benefits and write a blog post")
    
    print("\n" + "="*70)
    print(" FINAL RESULT")
    print("="*70)
    print(json.dumps(result1, indent=2))
    
    # Test Case 2: Research Only
    print("\n\n" + "="*70)
    print(" TEST CASE 2: Research Only")
    print("="*70)
    
    result2 = orchestrator.execute("Research FastAPI features")
    
    print("\n" + "="*70)
    print(" FINAL RESULT")
    print("="*70)
    print(json.dumps(result2, indent=2))
    
    # Show workflow history
    print("\n\n" + "="*70)
    print(" WORKFLOW HISTORY")
    print("="*70)
    print(f"Total workflows executed: {len(orchestrator.get_workflow_history())}")
    for i, workflow in enumerate(orchestrator.get_workflow_history(), 1):
        print(f"\n{i}. Request: {workflow['request']}")
        if 'title' in workflow['result']:
            print(f"   Output: {workflow['result']['title']}")
        elif 'topic' in workflow['result']:
            print(f"   Output: Research on {workflow['result']['topic']}")
    
    print("\n" + "="*70)
    print(" SYSTEM COMPLETE!")
    print("="*70)
    print("""
This complete system demonstrates:

✅ SKILL.md Files (skills/research/SKILL.md)
   - Declarative skill definitions
   - Workflow steps in natural language
   - Used by: Research Agent

✅ AGENT.md Files (agents/.../AGENT.md)
   - Declarative agent definitions
   - Purpose, tools, skills, behavior
   - Handoff specifications

✅ Handoffs (defined in AGENT.md)
   - Research Agent → Writer Agent
   - Context packaging
   - Handoff protocol

✅ AI Harness Configs
   - .claude/commands/ (Claude Code)
   - .github/copilot-instructions.md (GitHub Copilot)
   - .opencode/instructions/ and .opencode/skills/ (OpenCode)

Ready for production use!
""")
