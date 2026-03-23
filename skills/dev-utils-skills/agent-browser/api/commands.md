# Commands API | 命令 API

## API Reference

Complete command reference for agent-browser CLI.

### Navigation Commands

#### open, goto, navigate

Navigate to a URL.

**Syntax:**
```bash
agent-browser open <url> [options]
```

**Options:**
- `--session <name>`: Use named session
- `--headers <json>`: Custom HTTP headers
- `--headed`: Run in headed mode
- `--json`: JSON output

**Example:**
```bash
agent-browser open https://example.com --session my-session --json
```

### Interaction Commands

#### click

Click an element.

**Syntax:**
```bash
agent-browser click <selector> [options]
```

**Options:**
- `--session <name>`: Use named session
- `--button <button>`: Mouse button (left, right, middle)
- `--json`: JSON output

**Example:**
```bash
agent-browser click @e1 --session my-session --json
```

#### dblclick

Double-click an element.

**Syntax:**
```bash
agent-browser dblclick <selector> [options]
```

**Example:**
```bash
agent-browser dblclick @e1
```

### Input Commands

#### type

Type text into an element.

**Syntax:**
```bash
agent-browser type <selector> <text> [options]
```

**Example:**
```bash
agent-browser type @e1 "Hello World"
```

#### fill

Fill an input field.

**Syntax:**
```bash
agent-browser fill <selector> <text> [options]
```

**Example:**
```bash
agent-browser fill @e1 "user@example.com"
```

#### press

Press a key.

**Syntax:**
```bash
agent-browser press <selector> <key> [options]
```

**Example:**
```bash
agent-browser press @e1 Enter
```

#### keydown, keyup

Key down/up events.

**Syntax:**
```bash
agent-browser keydown <selector> <key> [options]
agent-browser keyup <selector> <key> [options]
```

### Form Commands

#### focus

Focus an element.

**Syntax:**
```bash
agent-browser focus <selector> [options]
```

#### select

Select an option.

**Syntax:**
```bash
agent-browser select <selector> <value> [options]
```

#### check, uncheck

Check/uncheck a checkbox.

**Syntax:**
```bash
agent-browser check <selector> [options]
agent-browser uncheck <selector> [options]
```

### Mouse Commands

#### hover

Hover over an element.

**Syntax:**
```bash
agent-browser hover <selector> [options]
```

#### scroll

Scroll element or page.

**Syntax:**
```bash
agent-browser scroll <selector> [options]
agent-browser scroll --to <selector> [options]
```

### Information Commands

#### get text

Get text content.

**Syntax:**
```bash
agent-browser get text <selector> [options]
```

#### get attribute

Get attribute value.

**Syntax:**
```bash
agent-browser get attribute <selector> <name> [options]
```

#### get property

Get property value.

**Syntax:**
```bash
agent-browser get property <selector> <name> [options]
```

### Advanced Commands

#### snapshot

Get accessibility tree with refs.

**Syntax:**
```bash
agent-browser snapshot [options]
```

**Options:**
- `-i, --interactive`: Interactive mode
- `-c, --compact`: Compact format
- `-d, --depth <n>`: Depth limit
- `-s, --selector <sel>`: Filter by selector
- `--full, -f`: Full snapshot
- `-n, --name <name>`: Filter by name
- `--exact, -e`: Exact name match
- `--json`: JSON output

**Example:**
```bash
agent-browser snapshot -i --json --session my-session
```

#### eval

Evaluate JavaScript.

**Syntax:**
```bash
agent-browser eval <expression> [options]
```

**Example:**
```bash
agent-browser eval "document.title"
```

#### screenshot

Take screenshot.

**Syntax:**
```bash
agent-browser screenshot <path> [options]
```

**Options:**
- `--full`: Full page screenshot

#### pdf

Generate PDF.

**Syntax:**
```bash
agent-browser pdf <path> [options]
```

**Options:**
- `--format <format>`: Paper format
- `--print-background`: Print background

#### close

Close page or browser.

**Syntax:**
```bash
agent-browser close [options]
```

**Options:**
- `--all`: Close all pages

### Common Options

All commands support:
- `--session <name>`: Use named session
- `--json`: JSON output
- `--headed`: Headed mode
- `--debug`: Debug output

### Key Points

- All commands support `--session` for state management
- Use `--json` for machine-readable output
- Commands automatically wait for navigation
- Use refs (@e1, @e2) for reliable selection
- Commands return appropriate exit codes
