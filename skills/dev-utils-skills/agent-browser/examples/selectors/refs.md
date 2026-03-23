# Refs | 引用

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use refs for element selection in agent-browser.

### Key Concepts

- What are refs
- Getting refs from snapshot
- Using refs in commands
- Refs advantages
- Refs workflow

### Example: Getting Refs from Snapshot

```bash
# Get snapshot with refs
agent-browser snapshot

# Output example:
# @e1 button "Submit"
# @e2 input[name="email"]
# @e3 a[href="/login"]
```

### Example: Using Refs in Commands

```bash
# Click using ref
agent-browser click @e1

# Fill using ref
agent-browser fill @e2 "user@example.com"

# Get text using ref
agent-browser get text @e3

# Multiple refs
agent-browser click @e1
agent-browser fill @e2 "text"
agent-browser click @e3
```

### Example: Interactive Snapshot for Refs

```bash
# Interactive snapshot to select element and get ref
agent-browser snapshot -i

# This allows you to interactively select elements and see their refs
```

### Example: Refs with JSON Output

```bash
# Get snapshot as JSON with refs
agent-browser snapshot --json

# Output example:
# {
#   "refs": {
#     "@e1": {
#       "role": "button",
#       "name": "Submit",
#       "selector": "button.submit"
#     },
#     "@e2": {
#       "role": "textbox",
#       "name": "Email",
#       "selector": "input[name='email']"
#     }
#   }
# }
```

### Example: Complete Refs Workflow

```bash
# 1. Open page
agent-browser open https://example.com

# 2. Get snapshot with refs
agent-browser snapshot --json > snapshot.json

# 3. Parse refs from JSON (in your script)
# @e1 = submit button
# @e2 = email input
# @e3 = password input

# 4. Use refs for interaction
agent-browser fill @e2 "user@example.com" --session login
agent-browser fill @e3 "password123" --session login
agent-browser click @e1 --session login
```

### Example: Refs Advantages

```bash
# Refs are deterministic - same element always gets same ref
agent-browser snapshot
# @e1 button "Login"

# Even if page structure changes, ref points to same element
agent-browser click @e1  # Always clicks the Login button

# Traditional selector might break:
agent-browser click "button.login"  # Might not work if class changes
```

### Key Points

- Refs are deterministic identifiers (@e1, @e2, etc.)
- Get refs from `snapshot` command
- Refs are AI-friendly and stable
- Use `--json` flag for machine-readable refs
- Refs work better than CSS selectors for dynamic pages
- Always snapshot before using refs
- Refs persist within a session
