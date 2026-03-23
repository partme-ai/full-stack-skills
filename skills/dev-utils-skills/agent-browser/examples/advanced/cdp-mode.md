# CDP Mode | Chrome DevTools Protocol 模式

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to connect to an existing browser via Chrome DevTools Protocol (CDP).

### Key Concepts

- Connecting to existing browsers via CDP
- Controlling Electron apps
- Remote debugging
- WebView2 applications
- CDP endpoint connection

### Example: Connect Once

```bash
# Start Chrome with remote debugging
# google-chrome --remote-debugging-port=9222

# Connect once
agent-browser connect 9222

# Run commands without --cdp flag
agent-browser snapshot
agent-browser tab
agent-browser click @e1
agent-browser close
```

### Example: Pass CDP on Each Command

```bash
# Start Chrome with remote debugging
# google-chrome --remote-debugging-port=9222

# Pass --cdp on each command
agent-browser --cdp 9222 snapshot
agent-browser --cdp 9222 tab
agent-browser --cdp 9222 click @e1
```

### Example: Electron App

```bash
# Start Electron app with remote debugging
# electron --remote-debugging-port=9222

# Connect and control
agent-browser connect 9222
agent-browser snapshot -i
agent-browser click @e1
```

### Example: WebView2 Application

```bash
# Start WebView2 app with remote debugging enabled
# (depends on application configuration)

# Connect via CDP
agent-browser connect 9222
agent-browser snapshot
agent-browser click @e1
```

### Example: Chrome/Chromium Instance

```bash
# Start Chrome with remote debugging
# google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug

# Connect and automate
agent-browser connect 9222
agent-browser open example.com
agent-browser snapshot -i
agent-browser click @e2
```

### Key Points

- Use `connect <port>` to connect once, or `--cdp <port>` on each command
- Enables control of Electron apps, Chrome instances, WebView2 apps
- Any browser exposing a CDP endpoint can be controlled
- Useful for debugging and testing existing browser instances
- After `connect`, subsequent commands don't need `--cdp` flag
