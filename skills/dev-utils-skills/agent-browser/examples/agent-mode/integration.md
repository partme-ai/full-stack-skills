# Agent Integration | 代理集成

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to integrate agent-browser with AI agents.

### Key Concepts

- Integrating with Claude
- Integrating with Cursor
- Integrating with Copilot
- Integrating with OpenAI
- Integrating with Gemini
- Adding to agent skills

### Example: Claude Integration

```bash
# Add to Claude's skills/AGENTS.md or similar
# agent-browser: Browser automation CLI for AI agents
# - Use snapshot --json to get page state
# - Use refs (@e1, @e2) for element selection
# - Use --session to maintain state
```

### Example: Cursor Integration

```bash
# Configure Cursor to use agent-browser
# Add agent-browser commands to Cursor's tool set
# Use JSON output for structured responses
```

### Example: Basic Integration Pattern

```javascript
// Example: Node.js integration
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

async function agentBrowserCommand(command) {
  try {
    const { stdout, stderr } = await execPromise(
      `agent-browser ${command} --json`
    );
    return JSON.parse(stdout);
  } catch (error) {
    return { error: error.message };
  }
}

// Usage
const snapshot = await agentBrowserCommand('snapshot --session my-task');
const refs = snapshot.refs;
await agentBrowserCommand(`click ${refs['@e1'].ref} --session my-task`);
```

### Example: Python Integration

```python
import subprocess
import json

def agent_browser_command(command):
    try:
        result = subprocess.run(
            f"agent-browser {command} --json",
            shell=True,
            capture_output=True,
            text=True
        )
        return json.loads(result.stdout)
    except Exception as e:
        return {"error": str(e)}

# Usage
snapshot = agent_browser_command("snapshot --session my-task")
refs = snapshot.get("refs", {})
agent_browser_command(f"click {refs['@e1']['ref']} --session my-task")
```

### Example: Agent Skill Definition

```markdown
## agent-browser

Browser automation CLI tool for AI agents.

### Commands:
- `agent-browser open <url>` - Navigate to URL
- `agent-browser snapshot --json` - Get page snapshot with refs
- `agent-browser click <ref>` - Click element by ref
- `agent-browser fill <ref> <text>` - Fill input by ref

### Workflow:
1. Open page: `agent-browser open <url> --session <name> --json`
2. Snapshot: `agent-browser snapshot --json --session <name>`
3. Interact: Use refs from snapshot
4. Verify: Snapshot again after changes
```

### Example: Agent Workflow Integration

```bash
# Agent receives task: "Login to example.com"

# Step 1: Agent executes
agent-browser open https://example.com/login --session task1 --json

# Step 2: Agent gets snapshot
agent-browser snapshot --json --session task1

# Step 3: Agent parses JSON, identifies:
# - @e1 = email input
# - @e2 = password input  
# - @e3 = login button

# Step 4: Agent fills form
agent-browser fill @e1 "user@example.com" --session task1 --json
agent-browser fill @e2 "password" --session task1 --json

# Step 5: Agent submits
agent-browser click @e3 --session task1 --json

# Step 6: Agent verifies
agent-browser snapshot --json --session task1
```

### Key Points

- Integrate via command-line interface
- Use `--json` for structured output
- Parse JSON responses in your agent code
- Use sessions for state management
- Follow standard workflow pattern
- Handle errors appropriately
- Document agent-browser in agent skills
- Use refs for reliable element selection
