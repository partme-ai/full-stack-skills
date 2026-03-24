# Advanced Commands | 高级命令

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use advanced agent-browser commands.

### Key Concepts

- Snapshot command
- Eval command
- Screenshot and PDF
- Close command
- Command options

### Example: Snapshot

```bash
# Basic snapshot (accessibility tree with refs)
agent-browser snapshot

# Interactive snapshot
agent-browser snapshot -i

# Compact snapshot
agent-browser snapshot -c

# Snapshot with depth limit
agent-browser snapshot -d 2

# Snapshot specific element
agent-browser snapshot -s "main"

# Full snapshot
agent-browser snapshot --full

# Snapshot with JSON output
agent-browser snapshot --json
```

### Example: Eval

```bash
# Evaluate JavaScript
agent-browser eval "document.title"

# Evaluate with return value
agent-browser eval "document.querySelector('h1').textContent"

# Evaluate complex expression
agent-browser eval "Array.from(document.querySelectorAll('a')).map(a => a.href)"
```

### Example: Screenshot and PDF

```bash
# Take screenshot
agent-browser screenshot output.png

# Screenshot full page
agent-browser screenshot output.png --full

# Generate PDF
agent-browser pdf output.pdf

# PDF with options
agent-browser pdf output.pdf --format A4 --print-background
```

### Example: Close

```bash
# Close current page
agent-browser close

# Close all pages
agent-browser close --all
```

### Example: Snapshot Workflow

```bash
# 1. Open page
agent-browser open https://example.com

# 2. Get snapshot with refs
agent-browser snapshot -i --json

# 3. Use refs from snapshot
agent-browser click @e1
agent-browser fill @e2 "text"

# 4. Snapshot again after interaction
agent-browser snapshot --json
```

### Example: Eval Workflow

```bash
# Open page
agent-browser open https://example.com

# Extract data using eval
agent-browser eval "document.querySelectorAll('article').length"

# Get all links
agent-browser eval "Array.from(document.querySelectorAll('a')).map(a => ({text: a.textContent, href: a.href}))"

# Check if element exists
agent-browser eval "!!document.querySelector('.modal')"
```

### Key Points

- Use `snapshot` to get accessibility tree with refs
- Use `-i` for interactive snapshot selection
- Use `--json` for machine-readable output
- Use `eval` for custom JavaScript execution
- Use `screenshot` and `pdf` for capturing pages
- Always snapshot before interacting with elements
- Use refs from snapshot for reliable element selection
