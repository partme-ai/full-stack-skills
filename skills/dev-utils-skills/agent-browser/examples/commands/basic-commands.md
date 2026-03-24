# Basic Commands | 基础命令

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use basic agent-browser commands.

### Key Concepts

- Navigation commands
- Interaction commands
- Input commands
- Form commands
- Mouse commands

### Example: Navigation

```bash
# Open a URL (aliases: goto, navigate)
agent-browser open https://example.com

# Open with session
agent-browser open https://example.com --session my-session
```

### Example: Clicking Elements

```bash
# Click an element using ref
agent-browser click @e1

# Click using CSS selector
agent-browser click button.submit

# Click using XPath
agent-browser click "//button[@type='submit']"

# Double-click
agent-browser dblclick @e2

# Right-click
agent-browser click @e3 --button right
```

### Example: Typing and Filling

```bash
# Type text into an element
agent-browser type @e1 "Hello World"

# Fill an input field
agent-browser fill @e2 "username@example.com"

# Press a key
agent-browser press @e1 Enter

# Key down
agent-browser keydown @e1 Control

# Key up
agent-browser keyup @e1 Control
```

### Example: Form Interactions

```bash
# Focus an element
agent-browser focus @e1

# Select an option
agent-browser select @e1 "Option 1"

# Check a checkbox
agent-browser check @e1

# Uncheck a checkbox
agent-browser uncheck @e1
```

### Example: Mouse Actions

```bash
# Hover over an element
agent-browser hover @e1

# Scroll
agent-browser scroll @e1

# Scroll to element
agent-browser scroll @e1 --to
```

### Example: Getting Element Information

```bash
# Get text content
agent-browser get text @e1

# Get attribute
agent-browser get attribute @e1 href

# Get property
agent-browser get property @e1 value
```

### Example: Command Chaining

```bash
# Open page, then click
agent-browser open https://example.com && agent-browser click @e1

# Using session for state
agent-browser open https://example.com --session test
agent-browser click @e1 --session test
agent-browser fill @e2 "text" --session test
```

### Key Points

- Use `open` to navigate to URLs
- Use refs (@e1, @e2) for deterministic selection
- Commands automatically wait for navigation
- Use `--session` to maintain state
- Commands support CSS selectors, XPath, and semantic locators
- All commands return appropriate exit codes
