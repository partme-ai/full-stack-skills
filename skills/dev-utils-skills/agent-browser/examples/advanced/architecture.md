# Architecture | 架构

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example explains the architecture of agent-browser.

### Key Concepts

- Client-daemon architecture
- Rust CLI (fast native binary)
- Node.js daemon
- Fallback mechanism
- Browser engine (Chromium, Firefox, WebKit)

### Architecture Overview

agent-browser uses a client-daemon architecture:

1. **Rust CLI** (fast native binary)
   - Parses commands
   - Communicates with daemon
   - Fast startup and execution

2. **Node.js Daemon**
   - Manages Playwright browser instance
   - Handles browser automation
   - Persists between commands for fast subsequent operations

3. **Fallback**
   - If native binary unavailable, uses Node.js directly
   - Ensures compatibility across platforms

### Daemon Lifecycle

```bash
# First command starts daemon automatically
agent-browser open example.com  # Daemon starts here

# Subsequent commands reuse daemon (fast)
agent-browser snapshot           # Reuses existing daemon
agent-browser click @e1         # Reuses existing daemon

# Daemon persists until explicitly closed
agent-browser close              # Daemon stops
```

### Browser Engine

- **Default**: Chromium (bundled with Playwright)
- **Also supports**: Firefox and WebKit via Playwright protocol
- **Custom**: Can use custom executable via `--executable-path`

### Performance Benefits

- **Fast startup**: Native Rust binary parses commands quickly
- **Persistent daemon**: Browser instance reused between commands
- **Efficient communication**: Client-daemon model reduces overhead
- **Fallback support**: Node.js fallback ensures compatibility

### Key Points

- Client-daemon architecture for performance
- Rust CLI for fast command parsing
- Node.js daemon manages browser instance
- Daemon persists between commands (fast)
- Fallback to Node.js if native binary unavailable
- Supports Chromium (default), Firefox, and WebKit
