# Agent Mode Introduction | 代理模式介绍

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates agent mode in agent-browser for AI agent integration.

### Key Concepts

- What is agent mode
- JSON output format
- Machine-readable commands
- AI agent integration
- Agent mode benefits

### Example: Basic Agent Mode

```bash
# Enable JSON output for machine-readable format
agent-browser snapshot --json

# Output example:
# {
#   "type": "snapshot",
#   "refs": {
#     "@e1": {
#       "role": "button",
#       "name": "Submit",
#       "selector": "button.submit"
#     }
#   }
# }
```

### Example: JSON Output for Commands

```bash
# Get text with JSON output
agent-browser get text @e1 --json

# Output:
# {
#   "type": "text",
#   "value": "Submit",
#   "ref": "@e1"
# }

# Get attribute with JSON
agent-browser get attribute @e1 href --json

# Output:
# {
#   "type": "attribute",
#   "name": "href",
#   "value": "/login",
#   "ref": "@e1"
# }
```

### Example: Snapshot in Agent Mode

```bash
# Snapshot with JSON for AI parsing
agent-browser snapshot --json

# Compact JSON output
agent-browser snapshot -c --json

# Interactive snapshot with JSON
agent-browser snapshot -i --json
```

### Example: Complete Agent Mode Workflow

```bash
# 1. Open page
agent-browser open https://example.com --json

# 2. Get snapshot
agent-browser snapshot --json

# 3. Parse refs from JSON output
# AI agent identifies: @e1 = login button, @e2 = email input

# 4. Interact using refs
agent-browser fill @e2 "user@example.com" --json
agent-browser click @e1 --json

# 5. Verify result
agent-browser snapshot --json
```

### Example: Agent Mode with Session

```bash
# Start session
agent-browser open https://example.com --session agent-session --json

# Continue in same session
agent-browser snapshot --session agent-session --json
agent-browser click @e1 --session agent-session --json
agent-browser fill @e2 "text" --session agent-session --json
```

### Example: Error Handling in Agent Mode

```bash
# Commands return JSON errors
agent-browser click @e999 --json

# Output:
# {
#   "error": "Element not found",
#   "ref": "@e999",
#   "command": "click"
# }
```

### Key Points

- Agent mode uses `--json` flag for machine-readable output
- JSON output is essential for AI agent integration
- Snapshot with JSON provides structured refs
- All commands support `--json` flag
- Use sessions to maintain state across commands
- Error messages are also in JSON format
- Agent mode enables deterministic automation
