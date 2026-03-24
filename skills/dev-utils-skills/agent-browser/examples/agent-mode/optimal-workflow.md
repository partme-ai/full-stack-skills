# Optimal AI Workflow | 最优 AI 工作流

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates the optimal workflow for AI agents using agent-browser.

### Key Concepts

- Standard workflow steps
- Snapshot-first approach
- Ref-based interaction
- State management
- Error recovery

### Example: Standard Workflow

```bash
# Step 1: Open the page
agent-browser open https://example.com --session my-task --json

# Step 2: Get snapshot with refs
agent-browser snapshot -i --json --session my-task

# Step 3: AI agent parses snapshot JSON
# Identifies available elements and their refs:
# @e1 = login button
# @e2 = email input
# @e3 = password input

# Step 4: Interact using refs
agent-browser fill @e2 "user@example.com" --session my-task --json
agent-browser fill @e3 "password123" --session my-task --json
agent-browser click @e1 --session my-task --json

# Step 5: Verify page changed (snapshot again)
agent-browser snapshot --json --session my-task

# Step 6: Continue with new refs from updated snapshot
agent-browser click @e4 --session my-task --json
```

### Example: Snapshot-First Pattern

```bash
# Always snapshot before interaction
agent-browser snapshot --json > current-state.json

# AI agent analyzes snapshot
# Decides next action based on available refs

# Execute action
agent-browser click @e1 --json

# Snapshot again to verify
agent-browser snapshot --json > new-state.json
```

### Example: Ref-Based Interaction

```bash
# Get refs
agent-browser snapshot --json

# Use refs (deterministic)
agent-browser click @e1 --json
agent-browser fill @e2 "text" --json
agent-browser click @e3 --json

# Refs are stable and reliable
```

### Example: State Management with Sessions

```bash
# Create session
agent-browser open https://example.com --session task1 --json

# All subsequent commands use same session
agent-browser snapshot --session task1 --json
agent-browser click @e1 --session task1 --json
agent-browser fill @e2 "text" --session task1 --json

# Session maintains browser state
```

### Example: Error Recovery

```bash
# Try action
agent-browser click @e1 --json

# If error, snapshot again
agent-browser snapshot --json

# Get updated refs
# Retry with new refs
agent-browser click @e2 --json
```

### Example: Complete Task Workflow

```bash
# 1. Initialize
agent-browser open https://example.com/login --session login-task --json

# 2. Analyze page
agent-browser snapshot --json --session login-task > page1.json

# 3. Fill form
agent-browser fill @e2 "user@example.com" --session login-task --json
agent-browser fill @e3 "password" --session login-task --json

# 4. Submit
agent-browser click @e1 --session login-task --json

# 5. Verify success
agent-browser snapshot --json --session login-task > page2.json

# 6. Continue if needed
agent-browser click @e4 --session login-task --json
```

### Key Points

- Always start with `open` command
- Always `snapshot` before interacting
- Use refs from snapshot for interaction
- Use `--session` to maintain state
- Snapshot again after page changes
- Use `--json` for machine-readable output
- Handle errors by re-snapshotting
- Follow: open → snapshot → interact → snapshot pattern
