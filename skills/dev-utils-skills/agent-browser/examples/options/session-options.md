# Session Options | 会话选项

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates session management options in agent-browser.

### Key Concepts

- Creating sessions
- Using sessions
- Session state
- Session persistence
- Environment variables

### Example: Creating Sessions

```bash
# Create session on open
agent-browser open https://example.com --session my-session

# Session is created and maintained
```

### Example: Using Sessions

```bash
# All commands can use the session
agent-browser open https://example.com --session task1
agent-browser snapshot --session task1
agent-browser click @e1 --session task1
agent-browser fill @e2 "text" --session task1
agent-browser click @e3 --session task1
```

### Example: Session State

```bash
# Session maintains browser state
agent-browser open https://example.com --session login
agent-browser fill @e1 "user@example.com" --session login
agent-browser fill @e2 "password" --session login
agent-browser click @e3 --session login

# Now logged in, continue in same session
agent-browser snapshot --session login
agent-browser click @e4 --session login
```

### Example: Multiple Sessions

```bash
# Create multiple independent sessions
agent-browser open https://site1.com --session session1
agent-browser open https://site2.com --session session2

# Work with each independently
agent-browser snapshot --session session1
agent-browser snapshot --session session2
```

### Example: Environment Variable

```bash
# Set session via environment variable
export AGENT_BROWSER_SESSION=my-session

# Commands automatically use session
agent-browser open https://example.com
agent-browser snapshot
agent-browser click @e1
```

### Example: Session with JSON

```bash
# Session with JSON output
agent-browser open https://example.com --session task1 --json
agent-browser snapshot --session task1 --json
agent-browser click @e1 --session task1 --json
```

### Example: Session Workflow

```bash
# Complete workflow with session
agent-browser open https://example.com/login --session login-task --json

# Step 1: Analyze page
agent-browser snapshot --session login-task --json

# Step 2: Fill form
agent-browser fill @e1 "user@example.com" --session login-task --json
agent-browser fill @e2 "password" --session login-task --json

# Step 3: Submit
agent-browser click @e3 --session login-task --json

# Step 4: Verify
agent-browser snapshot --session login-task --json

# Step 5: Continue
agent-browser click @e4 --session login-task --json
```

### Key Points

- Use `--session <name>` to create/maintain sessions
- Sessions preserve browser state
- All commands can use `--session`
- Multiple sessions can run independently
- Set session via environment variable
- Sessions work with JSON output
- Sessions maintain cookies and state
- Use sessions for multi-step workflows
