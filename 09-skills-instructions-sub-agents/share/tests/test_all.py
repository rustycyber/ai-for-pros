"""Basic tests for the multi-agent system"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


def test_skill_md_exists():
    """Test that SKILL.md files exist"""
    skill_files = [
        Path(__file__).parent.parent.parent / "02-skills/skills/research/SKILL.md",
        Path(__file__).parent.parent.parent / "02-skills/skills/analysis/SKILL.md"
    ]
    
    for skill_file in skill_files:
        assert skill_file.exists(), f"SKILL.md not found: {skill_file}"
        content = skill_file.read_text()
        assert "Workflow" in content, f"SKILL.md missing workflow: {skill_file}"
        assert "Input" in content, f"SKILL.md missing input: {skill_file}"
        assert "Output" in content, f"SKILL.md missing output: {skill_file}"
    
    print("✅ All SKILL.md files exist with proper structure")


def test_agent_md_exists():
    """Test that AGENT.md files exist"""
    agent_files = [
        Path(__file__).parent.parent.parent / "04-subagents/agents/research/AGENT.md",
        Path(__file__).parent.parent.parent / "04-subagents/agents/writer/AGENT.md",
        Path(__file__).parent.parent.parent / "04-subagents/agents/orchestrator/AGENT.md"
    ]
    
    for agent_file in agent_files:
        assert agent_file.exists(), f"AGENT.md not found: {agent_file}"
        content = agent_file.read_text()
        assert "Purpose" in content, f"AGENT.md missing purpose: {agent_file}"
        assert "Capabilities" in content, f"AGENT.md missing capabilities: {agent_file}"
        assert "Handoffs" in content, f"AGENT.md missing handoffs: {agent_file}"
    
    print("✅ All AGENT.md files exist with proper structure")


def test_harness_configs_exist():
    """Test that AI harness configs exist"""
    config_files = [
        Path(__file__).parent.parent.parent / "06-ai-harness-loading/.claude/commands/research.md",
        Path(__file__).parent.parent.parent / "06-ai-harness-loading/.github/copilot-instructions.md",
        Path(__file__).parent.parent.parent / "06-ai-harness-loading/.opencode/instructions/research-agent.md",
        Path(__file__).parent.parent.parent / "06-ai-harness-loading/.opencode/skills/research.md"
    ]
    
    for config_file in config_files:
        assert config_file.exists(), f"Config file not found: {config_file}"
    
    print("✅ All AI harness config files exist")


def test_research_agent():
    """Test research agent loads and executes"""
    # Add 02-skills to path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "02-skills"))
    from skills.research.skill import research_skill
    
    result = research_skill("test topic", depth="quick")
    
    assert "topic" in result, "Result missing topic"
    # key_findings is the correct field name
    assert "key_findings" in result, "Result missing key_findings"
    assert "sources" in result, "Result missing sources"
    assert "confidence" in result, "Result missing confidence"
    
    print("✅ Research agent executes correctly")


def test_analysis_skill():
    """Test analysis skill loads and executes"""
    # Add 02-skills to path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "02-skills"))
    from skills.analysis.skill import analysis_skill
    
    result = analysis_skill("test data", analysis_type="summary")
    
    assert "analysis_type" in result, "Result missing analysis_type"
    assert "insights" in result, "Result missing insights"
    assert "confidence" in result, "Result missing confidence"
    
    print("✅ Analysis skill executes correctly")


if __name__ == "__main__":
    print("="*70)
    print(" RUNNING TESTS")
    print("="*70)
    
    test_skill_md_exists()
    test_agent_md_exists()
    test_harness_configs_exist()
    test_research_agent()
    test_analysis_skill()
    
    print("\n" + "="*70)
    print(" ALL TESTS PASSED ✅")
    print("="*70)
