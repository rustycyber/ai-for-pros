"""Starter: Implement the orchestrator for a complete multi-agent system

TODO: Implement the orchestration logic
1. Parse user request to determine intent
2. Route to appropriate agents
3. Manage handoffs
4. Return final result
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.research.agent import ResearchAgent
from agents.writer.agent import WriterAgent


class Orchestrator:
    """TODO: Implement orchestration logic"""
    
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writer_agent = WriterAgent()
        # TODO: Add any other initialization
    
    def parse_intent(self, user_request: str):
        """TODO: Parse user request"""
        # Hint: Check for keywords like "research", "write", "blog", "summary"
        pass
    
    def execute(self, user_request: str):
        """TODO: Execute multi-agent workflow"""
        # Hint: 
        # 1. Parse intent
        # 2. If research needed: execute research agent
        # 3. If writing needed: execute writer agent with handoff
        # 4. Return result
        pass


if __name__ == "__main__":
    orchestrator = Orchestrator()
    
    # Test case 1: Research only
    result = orchestrator.execute("Research Python benefits")
    print(result)
    
    # Test case 2: Research + Write
    result = orchestrator.execute("Research FastAPI and write a blog post")
    print(result)
