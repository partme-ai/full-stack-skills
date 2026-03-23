# Quick Start | 快速开始

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates the quick start workflow with agent-browser.

### Key Concepts

- Basic workflow
- Using refs
- Traditional selectors
- Common commands

### Example: Basic Workflow

```bash
# 1. Open a page
agent-browser open example.com

# 2. Get snapshot with refs
agent-browser snapshot
# Output:
# - heading "Example Domain" [ref=e1] [level=1]
# - button "Submit" [ref=e2]
# - textbox "Email" [ref=e3]
# - link "Learn more" [ref=e4]

# 3. Click by ref from snapshot
agent-browser click @e2

# 4. Fill by ref
agent-browser fill @e3 "test@example.com"

# 5. Get text by ref
agent-browser get text @e1

# 6. Take screenshot
agent-browser screenshot page.png

# 7. Close browser
agent-browser close
```

### Example: Traditional Selectors

```bash
# Using CSS selectors
agent-browser click "#submit"
agent-browser fill "#email" "test@example.com"

# Using semantic locators
agent-browser find role button click --name "Submit"
```

### Example: Complete Workflow

```bash
# Navigate
agent-browser open example.com

# Get snapshot
agent-browser snapshot

# Interact using refs
agent-browser click @e2
agent-browser fill @e3 "test@example.com"
agent-browser get text @e1

# Capture
agent-browser screenshot page.png

# Close
agent-browser close
```

### Key Points

- Start with `open` to navigate
- Use `snapshot` to get refs
- Use refs (@e1, @e2) for interaction
- Use traditional selectors as fallback
- Always close when done
