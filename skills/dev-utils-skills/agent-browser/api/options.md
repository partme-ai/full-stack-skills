# Options API | 选项 API

## API Reference

Complete options reference for agent-browser.

### Global Options

#### --session, -s

Use named session for state management.

**Example:**
```bash
agent-browser open https://example.com --session my-session
```

**Environment Variable:** `AGENT_BROWSER_SESSION`

#### --headers

Custom HTTP headers (JSON format).

**Example:**
```bash
agent-browser open https://example.com --headers '{"User-Agent": "MyBot"}'
```

**Environment Variable:** `AGENT_BROWSER_HEADERS`

#### --executable-path

Custom browser executable path.

**Example:**
```bash
agent-browser open https://example.com --executable-path /path/to/chromium
```

**Environment Variable:** `AGENT_BROWSER_EXECUTABLE_PATH`

#### --headed

Run in headed mode (visible browser).

**Example:**
```bash
agent-browser open https://example.com --headed
```

#### --cdp

Connect via Chrome DevTools Protocol.

**Example:**
```bash
agent-browser open https://example.com --cdp 9222
```

#### --json

JSON output format.

**Example:**
```bash
agent-browser snapshot --json
```

#### --debug

Enable debug output.

**Example:**
```bash
agent-browser open https://example.com --debug
```

### Snapshot Options

#### -i, --interactive

Interactive snapshot mode.

**Example:**
```bash
agent-browser snapshot -i
```

#### -c, --compact

Compact snapshot format.

**Example:**
```bash
agent-browser snapshot -c
```

#### -d, --depth

Limit snapshot depth.

**Example:**
```bash
agent-browser snapshot -d 2
```

#### -s, --selector

Filter by selector.

**Example:**
```bash
agent-browser snapshot -s "main"
```

#### --full, -f

Full snapshot with all details.

**Example:**
```bash
agent-browser snapshot --full
```

#### -n, --name

Filter by accessible name.

**Example:**
```bash
agent-browser snapshot -n "Submit"
```

#### --exact, -e

Exact name match.

**Example:**
```bash
agent-browser snapshot -n "Submit" --exact
```

### Command-Specific Options

#### --button

Mouse button for click (left, right, middle).

**Example:**
```bash
agent-browser click @e1 --button right
```

#### --to

Scroll to element.

**Example:**
```bash
agent-browser scroll --to @e1
```

#### --all

Close all pages.

**Example:**
```bash
agent-browser close --all
```

#### --format

PDF paper format.

**Example:**
```bash
agent-browser pdf output.pdf --format A4
```

#### --print-background

Print background in PDF.

**Example:**
```bash
agent-browser pdf output.pdf --print-background
```

### Environment Variables

- `AGENT_BROWSER_SESSION`: Default session name
- `AGENT_BROWSER_HEADERS`: Default headers (JSON)
- `AGENT_BROWSER_EXECUTABLE_PATH`: Default executable path

### Key Points

- Global options apply to all commands
- Snapshot options are specific to snapshot command
- Environment variables can set defaults
- Options can be combined
- Use `--json` for agent mode
- Use `--session` for state management
