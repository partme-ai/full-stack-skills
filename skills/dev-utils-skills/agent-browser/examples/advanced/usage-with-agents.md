# Usage with AI Agents | 与 AI 智能体一起使用

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to integrate agent-browser with AI agents.

### Key Concepts

- Integration with AI agents
- Just ask the agent approach
- AGENTS.md / CLAUDE.md instructions
- Claude Code skill
- Optimal workflow patterns

### Example: Just Ask the Agent

The simplest approach - just tell your agent to use it:

```
Use agent-browser to test the login flow. Run agent-browser --help to see available commands.
```

The `--help` output is comprehensive and most agents can figure it out from there.

### Example: AGENTS.md / CLAUDE.md

For more consistent results, add to your project or global instructions file:

```markdown
## Browser Automation

Use `agent-browser` for web automation. Run `agent-browser --help` for all commands.

Core workflow:
1. `agent-browser open <url>` - Navigate to page
2. `agent-browser snapshot -i` - Get interactive elements with refs (@e1, @e2)
3. `agent-browser click @e1` / `fill @e2 "text"` - Interact using refs
4. Re-snapshot after page changes
```

### Example: Claude Code Skill

For Claude Code, a skill provides richer context:

**Option 1: Copy from node_modules**
```bash
cp -r node_modules/agent-browser/skills/agent-browser .claude/skills/
```

**Option 2: Download directly**
```bash
mkdir -p .claude/skills/agent-browser
curl -o .claude/skills/agent-browser/SKILL.md \
  https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/SKILL.md
```

### Example: Optimal AI Workflow

```bash
# 1. Navigate and get snapshot
agent-browser open example.com
agent-browser snapshot -i --json   # AI parses tree and refs

# 2. AI identifies target refs from snapshot
# 3. Execute actions using refs
agent-browser click @e2
agent-browser fill @e3 "input text"

# 4. Get new snapshot if page changed
agent-browser snapshot -i --json
```

### Example: Integration Patterns

**Pattern 1: Simple Automation**
```bash
# Agent executes commands sequentially
agent-browser open example.com
agent-browser snapshot -i
agent-browser click @e1
agent-browser fill @e2 "value"
agent-browser click @e3
```

**Pattern 2: With Error Handling**
```bash
# Agent checks for errors
agent-browser open example.com || echo "Failed to open"
agent-browser snapshot -i || echo "Failed to snapshot"
agent-browser click @e1 || echo "Failed to click"
```

**Pattern 3: With JSON Output**
```bash
# Agent parses JSON responses
agent-browser snapshot -i --json | jq '.data.refs'
agent-browser get text @e1 --json | jq '.data'
```

### Key Points

- Just ask the agent - simplest approach
- Add instructions to AGENTS.md / CLAUDE.md for consistency
- Use Claude Code skill for richer context
- Follow optimal workflow: snapshot → identify refs → interact → re-snapshot
- Use `--json` flag for machine-readable output
- Combine with error handling for robust automation
