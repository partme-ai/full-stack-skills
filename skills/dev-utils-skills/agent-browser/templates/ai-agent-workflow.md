# AI Agent Workflow Template | AI 代理工作流模板

## Template

Complete AI agent workflow using agent-browser with JSON output.

```bash
#!/bin/bash

SESSION="agent-task"

# Step 1: Open page
agent-browser open https://example.com/login --session $SESSION --json

# Step 2: Get snapshot with refs (JSON)
agent-browser snapshot --json --session $SESSION > snapshot1.json

# Step 3: AI agent parses snapshot1.json
# Identifies: @e1 = email input, @e2 = password input, @e3 = login button

# Step 4: Fill form
agent-browser fill @e1 "user@example.com" --session $SESSION --json
agent-browser fill @e2 "password123" --session $SESSION --json

# Step 5: Submit
agent-browser click @e3 --session $SESSION --json

# Step 6: Verify page changed
agent-browser snapshot --json --session $SESSION > snapshot2.json

# Step 7: AI agent analyzes snapshot2.json
# Identifies new refs: @e4 = dashboard link, @e5 = settings button

# Step 8: Continue interaction
agent-browser click @e4 --session $SESSION --json
agent-browser snapshot --json --session $SESSION > snapshot3.json
```

## Python Integration Example

```python
import subprocess
import json

def agent_browser(command):
    result = subprocess.run(
        f"agent-browser {command} --json",
        shell=True,
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

# Workflow
session = "my-task"

# Open page
agent_browser(f"open https://example.com --session {session}")

# Get snapshot
snapshot = agent_browser(f"snapshot --json --session {session}")
refs = snapshot.get("refs", {})

# Interact
agent_browser(f"fill {refs['@e1']['ref']} user@example.com --session {session}")
agent_browser(f"fill {refs['@e2']['ref']} password --session {session}")
agent_browser(f"click {refs['@e3']['ref']} --session {session}")

# Verify
new_snapshot = agent_browser(f"snapshot --json --session {session}")
```

## Usage

1. Install agent-browser: `npm install -g agent-browser && agent-browser install`
2. Use the template workflow
3. Parse JSON output in your agent code
4. Use refs for element interaction
5. Snapshot after each page change

## Key Points

- Always use `--json` for machine-readable output
- Use `--session` to maintain state
- Snapshot before and after interactions
- Parse JSON to extract refs
- Use refs for reliable element selection
- Follow: open → snapshot → interact → snapshot pattern
