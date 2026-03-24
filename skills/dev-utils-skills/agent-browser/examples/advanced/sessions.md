# Sessions | 会话管理

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to manage multiple isolated browser sessions with agent-browser.

### Key Concepts

- Multiple isolated browser instances
- Session management via `--session` flag or environment variable
- Listing and managing active sessions
- Session isolation (cookies, storage, history, auth state)

### Example: Using Named Sessions

```bash
# Start session 1
agent-browser --session agent1 open site-a.com
agent-browser --session agent1 click "#button"

# Start session 2 (isolated from session 1)
agent-browser --session agent2 open site-b.com
agent-browser --session agent2 fill "#input" "value"

# Each session has its own:
# - Browser instance
# - Cookies and storage
# - Navigation history
# - Authentication state
```

### Example: Using Environment Variable

```bash
# Set session via environment variable
export AGENT_BROWSER_SESSION=agent1
agent-browser open example.com
agent-browser click "#btn"

# Switch to different session
export AGENT_BROWSER_SESSION=agent2
agent-browser open other-site.com
```

### Example: Listing Active Sessions

```bash
# List all active sessions
agent-browser session list

# Output:
# Active sessions:
# -> default
#    agent1
#    agent2
```

### Example: Show Current Session

```bash
# Show current session name
agent-browser session

# Output:
# Current session: agent1
```

### Example: Session Isolation

```bash
# Session 1: Login to site A
agent-browser --session user1 open site-a.com
agent-browser --session user1 fill "#email" "user1@example.com"
agent-browser --session user1 fill "#password" "pass1"
agent-browser --session user1 click "#login"

# Session 2: Login to site A with different user (isolated)
agent-browser --session user2 open site-a.com
agent-browser --session user2 fill "#email" "user2@example.com"
agent-browser --session user2 fill "#password" "pass2"
agent-browser --session user2 click "#login"

# Each session maintains its own authentication state
```

### Key Points

- Use `--session <name>` to create isolated browser sessions
- Each session has its own browser instance, cookies, storage, and history
- Use `AGENT_BROWSER_SESSION` environment variable for convenience
- List active sessions with `agent-browser session list`
- Sessions persist until browser is closed
