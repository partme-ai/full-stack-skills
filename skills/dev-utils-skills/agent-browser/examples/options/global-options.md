# Global Options | 全局选项

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates global options available in agent-browser.

### Key Concepts

- Session management
- Headers configuration
- Headed/headless mode
- Executable path
- CDP integration
- Debug mode
- JSON output

### Example: Session Management

```bash
# Create named session
agent-browser open https://example.com --session my-session

# Use session in subsequent commands
agent-browser click @e1 --session my-session
agent-browser fill @e2 "text" --session my-session

# Session maintains browser state
```

### Example: Headers Configuration

```bash
# Set custom headers
agent-browser open https://example.com --headers '{"User-Agent": "MyBot/1.0"}'

# Or use environment variable
export AGENT_BROWSER_HEADERS='{"User-Agent": "MyBot/1.0"}'
agent-browser open https://example.com
```

### Example: Headed Mode

```bash
# Run in headed mode (visible browser)
agent-browser open https://example.com --headed

# Useful for debugging
agent-browser snapshot --headed
agent-browser click @e1 --headed
```

### Example: Executable Path

```bash
# Use custom browser executable
agent-browser open https://example.com --executable-path /path/to/chromium

# Or use environment variable
export AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium
agent-browser open https://example.com
```

### Example: CDP Integration

```bash
# Connect to existing Chrome via CDP
agent-browser open https://example.com --cdp 9222

# Use with Chrome running with remote debugging
# chrome --remote-debugging-port=9222
```

### Example: Debug Mode

```bash
# Enable debug output
agent-browser open https://example.com --debug

# Debug shows detailed information
agent-browser snapshot --debug
```

### Example: JSON Output

```bash
# Get JSON output for all commands
agent-browser open https://example.com --json
agent-browser snapshot --json
agent-browser click @e1 --json
agent-browser get text @e1 --json
```

### Example: Combining Options

```bash
# Use multiple options together
agent-browser open https://example.com \
  --session my-task \
  --headed \
  --headers '{"User-Agent": "MyBot"}' \
  --json

# All subsequent commands can use session
agent-browser snapshot --session my-task --json
agent-browser click @e1 --session my-task --json
```

### Example: Environment Variables

```bash
# Set session via environment
export AGENT_BROWSER_SESSION=my-session
agent-browser open https://example.com
agent-browser click @e1  # Uses my-session automatically

# Set executable path
export AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium

# Set headers
export AGENT_BROWSER_HEADERS='{"User-Agent": "MyBot"}'
```

### Key Points

- Use `--session` to maintain state across commands
- Use `--headers` for custom HTTP headers
- Use `--headed` for visible browser (debugging)
- Use `--executable-path` for custom browser
- Use `--cdp` for Chrome DevTools Protocol
- Use `--debug` for detailed output
- Use `--json` for machine-readable output
- Options can be set via environment variables
