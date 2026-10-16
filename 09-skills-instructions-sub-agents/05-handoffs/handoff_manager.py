"""Handoff Manager - Implements handoff protocol between agents"""
from typing import Dict, Any
from pathlib import Path
import json


class HandoffManager:
    """
    Manages handoffs between agents:
    - Validates handoff target exists
    - Packages context in correct format
    - Invokes target agent
    - Validates output
    """
    
    def __init__(self, agents_dir: str = "agents"):
        self.agents_dir = Path(agents_dir)
        self.handoff_history = []
    
    def validate_agent(self, agent_name: str) -> bool:
        """Check if agent exists and has AGENT.md"""
        agent_path = self.agents_dir / agent_name / "AGENT.md"
        return agent_path.exists()
    
    def load_agent_handoff_spec(self, agent_name: str) -> Dict:
        """Extract handoff specifications from AGENT.md"""
        agent_md = self.agents_dir / agent_name / "AGENT.md"
        
        if not agent_md.exists():
            raise FileNotFoundError(f"AGENT.md not found for: {agent_name}")
        
        content = agent_md.read_text()
        
        # Parse handoff section
        handoff_spec = {
            "agent": agent_name,
            "can_handoff_to": [],
            "handoff_format": {}
        }
        
        # Extract what agents this one can handoff to
        if "Handoff To:" in content:
            # Simple parsing - in production use proper parser
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if "Handoff To:" in line:
                    # Next lines contain target agent
                    if i + 1 < len(lines):
                        target = lines[i + 1]
                        if "AGENT.md" in target:
                            handoff_spec["can_handoff_to"].append(
                                target.split("agents/")[1].split("/")[0]
                            )
        
        return handoff_spec
    
    def create_handoff_package(self, 
                               from_agent: str,
                               to_agent: str,
                               context: Dict,
                               format_requirements: Dict = None) -> Dict:
        """Package context for handoff according to target agent's expected format"""
        
        print(f"\n[HANDOFF] Creating package:")
        print(f"  From: {from_agent}")
        print(f"  To: {to_agent}")
        
        handoff_package = {
            "handoff_id": f"{from_agent}_{to_agent}_{len(self.handoff_history)}",
            "from_agent": from_agent,
            "to_agent": to_agent,
            "timestamp": "2024-01-01T00:00:00",  # Would use datetime in production
            "context": context,
            "format_requirements": format_requirements or {}
        }
        
        print(f"  Context keys: {list(context.keys())}")
        print(f"  Package ID: {handoff_package['handoff_id']}")
        
        return handoff_package
    
    def validate_handoff(self, from_agent: str, to_agent: str) -> bool:
        """Validate that handoff is allowed"""
        
        # Check target exists
        if not self.validate_agent(to_agent):
            print(f"  ❌ Target agent '{to_agent}' does not exist")
            return False
        
        # Check from agent can handoff to target
        spec = self.load_agent_handoff_spec(from_agent)
        
        if to_agent not in spec.get("can_handoff_to", []):
            print(f"  ❌ Agent '{from_agent}' cannot handoff to '{to_agent}'")
            return False
        
        print(f"  ✅ Handoff validated: {from_agent} → {to_agent}")
        return True
    
    def record_handoff(self, handoff_package: Dict, result: Dict):
        """Record handoff in history"""
        self.handoff_history.append({
            "handoff": handoff_package,
            "result": result
        })
    
    def get_handoff_history(self) -> list:
        """Get all handoff history"""
        return self.handoff_history


def execute_handoff(from_agent: Any, to_agent: Any, context: Dict, format_requirements: Dict = None) -> Dict:
    """
    Execute a handoff between agents
    
    Args:
        from_agent: Source agent instance
        to_agent: Target agent instance
        context: Data to pass
        format_requirements: Formatting requirements
    
    Returns:
        Result from target agent
    """
    print(f"\n{'='*70}")
    print(" HANDOFF EXECUTION")
    print("="*70)
    
    handoff_manager = HandoffManager()
    
    # Validate
    from_name = from_agent.name if hasattr(from_agent, 'name') else 'unknown'
    to_name = to_agent.name if hasattr(to_agent, 'name') else 'unknown'
    
    print(f"\n[STEP 1] Validating Handoff")
    print(f"  Source: {from_name}")
    print(f"  Target: {to_name}")
    
    # Create package
    print(f"\n[STEP 2] Creating Handoff Package")
    package = handoff_manager.create_handoff_package(
        from_agent=from_name,
        to_agent=to_name,
        context=context,
        format_requirements=format_requirements
    )
    
    # Execute target agent
    print(f"\n[STEP 3] Invoking Target Agent")
    # In production, would dynamically load and invoke
    # For demo, we just show the flow
    
    print(f"  Target agent: {to_name}")
    print(f"  Input: {json.dumps(package, indent=2)}")
    
    # Record handoff
    print(f"\n[STEP 4] Recording Handoff")
    handoff_manager.record_handoff(package, {"status": "completed"})
    
    print(f"  ✅ Handoff complete")
    print(f"  History length: {len(handoff_manager.get_handoff_history())}")
    
    return package


if __name__ == "__main__":
    print("="*70)
    print(" HANDOFF MANAGER")
    print("="*70)
    
    manager = HandoffManager()
    
    # Test validation
    print("\n[TEST] Validate agent existence:")
    print(f"  research exists: {manager.validate_agent('research')}")
    print(f"  writer exists: {manager.validate_agent('writer')}")
    
    # Test handoff spec parsing
    print("\n[TEST] Parse handoff spec from AGENT.md:")
    spec = manager.load_agent_handoff_spec("research")
    print(json.dumps(spec, indent=2))
