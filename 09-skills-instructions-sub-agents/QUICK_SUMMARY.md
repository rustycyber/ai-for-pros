# S09 Complete Structure Summary

## What Was Created

```
09-skills-instructions-sub-agents/
│
├── 📁 01-tools-vs-skills/         # Lesson 1: Fundamentals
│   ├── tool_example.py            # Single-purpose function
│   ├── skill_example.py           # Multi-step workflow
│   └── comparison.py              # Side-by-side demo
│
├── 📁 02-skills/                  # Lesson 2: Skills
│   ├── 📁 skills/
│   │   ├── 📁 research/
│   │   │   ├── SKILL.md           # ✨ Declarative definition
│   │   │   └── skill.py           # Python implementation
│   │   └── 📁 analysis/
│   │       ├── SKILL.md
│   │       └── skill.py
│   └── demo_skill.py
│
├── 📁 03-instructions/            # Lesson 3: Instructions
│   ├── 📁 instructions/
│   │   ├── research_agent.md      # Traditional approach
│   │   └── writer_agent.md
│   └── demo_instructions.py
│
├── 📁 04-subagents/               # Lesson 4: Subagents
│   ├── 📁 agents/
│   │   ├── 📁 research/
│   │   │   ├── AGENT.md           # ✨ Declarative agent def + handoffs
│   │   │   ├── agent.py
│   │   │   └── tools.py
│   │   ├── 📁 writer/
│   │   │   ├── AGENT.md           # ✨ Includes handoff logic
│   │   │   ├── agent.py
│   │   │   └── tools.py
│   │   └── 📁 orchestrator/
│   │       ├── AGENT.md           # ✨ Routing logic + handoffs
│   │       └── orchestrator.py
│   └── demo_subagents.py
│
├── 📁 05-handoffs/                # Lesson 5: Handoff Protocol
│   ├── handoff_manager.py        # Context packaging
│   └── demo_handoffs.py
│
├── 📁 06-ai-harness-loading/      # Lesson 6: AI Tool Integration
│   ├── 📁 .claude/                # Claude Code CLI
│   │   └── 📁 commands/
│   │       ├── research.md        # /research command
│   │       └── orchestrate.md     # /orchestrate command
│   ├── 📁 .github/                # GitHub Copilot
│   │   └── copilot-instructions.md
│   ├── 📁 .opencode/              # OpenCode
│   │   ├── 📁 instructions/
│   │   │   ├── research-agent.md
│   │   │   └── writer-agent.md
│   │   └── 📁 skills/
│   │       ├── research.md
│   │       └── writing.md
│   └── demo_harness_loading.py
│
├── 📁 07-complete-system/         # Lesson 7: Everything Together
│   ├── 📁 starter/
│   │   └── main.py                # Workshop challenge
│   ├── 📁 solution/
│   │   └── main.py                # Working implementation
│   ├── 📁 .claude/                # Claude Code configs
│   ├── 📁 .github/                # GitHub Copilot configs
│   └── 📁 .opencode/              # OpenCode configs
│
├── 📁 share/
│   ├── demo_helpers.py           # Reusable interactive utilities
│   ├── 📁 eval/
│   │   ├── golden_dataset.json    # 5 test cases
│   │   └── run_eval.py
│   └── 📁 tests/
│       └── test_all.py           # Fixed field assertions
│
├── README.md
├── pyproject.toml
└── .env.example
```

## Key Files Created

### SKILL.md Files (2)
- ✅ `02-skills/skills/research/SKILL.md`
- ✅ `02-skills/skills/analysis/SKILL.md`

### AGENT.md Files (3)
- ✅ `04-subagents/agents/research/AGENT.md` (includes handoff logic)
- ✅ `04-subagents/agents/writer/AGENT.md` (includes handoff logic)
- ✅ `04-subagents/agents/orchestrator/AGENT.md` (routing + handoffs)

### AI Harness Configs (All 3)
- ✅ `.claude/commands/research.md`
- ✅ `.claude/commands/orchestrate.md`
- ✅ `.github/copilot-instructions.md`
- ✅ `.opencode/instructions/research-agent.md`
- ✅ `.opencode/instructions/writer-agent.md`
- ✅ `.opencode/skills/research.md`
- ✅ `.opencode/skills/writing.md`

### Python Implementations
- ✅ Skills: research_skill, analysis_skill
- ✅ Agents: research_agent, writer_agent, orchestrator
- ✅ Tools: web_search, scrape_url, validate_source, format_document, add_citations
- ✅ Handoff manager with validation and recording
- ✅ Demo helpers: Interactive step-by-step execution with graceful fallback

### Demos (7)
1. ✅ Tools vs Skills comparison
2. ✅ Skills in action
3. ✅ Instruction files loading
4. ✅ Subagents working
5. ✅ Handoffs demonstration
6. ✅ AI harness loading
7. ✅ Complete system

### Tests & Eval
- ✅ 5 test cases in golden dataset
- ✅ Test suite for SKILL.md, AGENT.md, harness configs (field names fixed)
- ✅ Evaluation harness
- ✅ PyYAML dependency added to pyproject.toml

## What Professionals Learn

### 1. Tools vs Skills
- Single function vs multi-step workflow
- When to use each

### 2. SKILL.md Pattern
- Declarative skill definitions
- Natural language + structured format
- Input/output contracts
- Workflow steps

### 3. AGENT.md Pattern
- Declarative agent definitions
- Purpose, tools, skills, behavior
- **Handoff specifications**

### 4. Handoffs
- Defined in AGENT.md files
- Context packaging
- Validation and recording
- Agent-to-agent delegation

### 5. AI Harness Integration
- Claude Code: `.claude/commands/`
- GitHub Copilot: `.github/copilot-instructions.md`
- OpenCode: `.opencode/instructions/` and `.opencode/skills/`
- All three autoload AGENT.md and SKILL.md

### 6. Complete System
- Multi-agent orchestration
- Research → Writer handoff
- Context preservation
- Works across all AI tools

## Running the Course

```bash
cd 09-skills-instructions-sub-agents

# Run lessons in order (use uv, not pip)
uv run python 01-tools-vs-skills/comparison.py
uv run python 02-skills/demo_skill.py
uv run python 03-instructions/demo_instructions.py
uv run python 04-subagents/demo_subagents.py
uv run python 05-handoffs/demo_handoffs.py
uv run python 06-ai-harness-loading/demo_harness_loading.py
uv run python 07-complete-system/solution/main.py

# Run tests
PYTHONPATH=. uv run pytest share/tests/ -v
```

## Production Ready Patterns

✅ All files needed for real multi-agent systems  
✅ Works with OpenCode, Claude Code, GitHub Copilot  
✅ OpenCode auto-loads `.opencode/instructions/` (agent behaviors) and `.opencode/skills/` (workflows)  
✅ Declarative definitions (SKILL.md, AGENT.md)  
✅ Standardized YAML front matter format  
✅ Handoff logic in agent definitions  
✅ Context preservation  
✅ Validation and testing  
✅ Interactive demos with graceful non-interactive fallback  

---

**Total Files Created**: 50+ files  
**Total Directories**: 21  
**All Demos Working**: ✅  
**AI Harness Configs**: All 3 major tools  
**Production Ready**: ✅
