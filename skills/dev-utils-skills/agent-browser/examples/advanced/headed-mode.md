# Headed Mode | 有界面模式

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to run agent-browser in headed mode (visible browser window) for debugging.

### Key Concepts

- Running browser in visible mode
- Debugging browser automation
- Visual verification of actions
- Headless vs headed mode

### Example: Basic Headed Mode

```bash
# Open browser in visible mode
agent-browser open example.com --headed

# All subsequent commands will use the visible browser
agent-browser snapshot
agent-browser click @e1
agent-browser fill @e2 "test"
```

### Example: Debugging Workflow

```bash
# Start with visible browser for debugging
agent-browser open example.com --headed

# Take snapshot to see what's available
agent-browser snapshot -i

# Interact and watch the browser
agent-browser click @e2
agent-browser fill @e3 "test@example.com"

# Take screenshot to verify
agent-browser screenshot debug.png

# Close when done
agent-browser close
```

### Example: Switching Between Headed and Headless

```bash
# Debug with visible browser
agent-browser open example.com --headed
agent-browser snapshot -i
agent-browser click @e1

# Switch to headless for production
agent-browser close
agent-browser open example.com  # Headless by default
agent-browser click @e1
```

### Key Points

- Use `--headed` flag to show browser window
- Useful for debugging and visual verification
- Headless mode is default (faster, no UI)
- Headed mode is slower but allows visual inspection
- Use headed mode during development, headless for production
