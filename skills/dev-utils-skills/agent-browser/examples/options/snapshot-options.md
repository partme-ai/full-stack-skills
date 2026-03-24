# Snapshot Options | 快照选项

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates snapshot-specific options in agent-browser.

### Key Concepts

- Interactive snapshot
- Compact format
- Depth limit
- Selector filter
- Full snapshot
- Name option
- Exact match

### Example: Interactive Snapshot

```bash
# Interactive mode for selecting elements
agent-browser snapshot -i

# Or long form
agent-browser snapshot --interactive

# Allows interactive element selection
```

### Example: Compact Format

```bash
# Compact snapshot output
agent-browser snapshot -c

# Or long form
agent-browser snapshot --compact

# More concise output format
```

### Example: Depth Limit

```bash
# Limit snapshot depth
agent-browser snapshot -d 2

# Or long form
agent-browser snapshot --depth 2

# Limits how deep the tree goes
```

### Example: Selector Filter

```bash
# Snapshot specific element and its children
agent-browser snapshot -s "main"

# Or long form
agent-browser snapshot --selector "main"

# Only snapshots matching selector
```

### Example: Full Snapshot

```bash
# Full snapshot (all details)
agent-browser snapshot --full

# Or short form
agent-browser snapshot -f

# Includes all element details
```

### Example: Name Option

```bash
# Snapshot with name filter
agent-browser snapshot -n "Submit"

# Or long form
agent-browser snapshot --name "Submit"

# Filters by accessible name
```

### Example: Exact Match

```bash
# Exact name match
agent-browser snapshot --name "Submit" --exact

# Or short form
agent-browser snapshot -n "Submit" -e

# Requires exact name match
```

### Example: Combining Snapshot Options

```bash
# Interactive, compact, with depth limit
agent-browser snapshot -i -c -d 2

# Full snapshot of specific selector
agent-browser snapshot --full -s "form"

# JSON output with compact format
agent-browser snapshot -c --json

# Interactive snapshot with JSON
agent-browser snapshot -i --json
```

### Example: Snapshot Workflow

```bash
# 1. Get full snapshot
agent-browser snapshot --full --json

# 2. Get compact snapshot for overview
agent-browser snapshot -c --json

# 3. Get snapshot of specific area
agent-browser snapshot -s "main" --json

# 4. Interactive snapshot to find element
agent-browser snapshot -i --json
```

### Key Points

- Use `-i` for interactive element selection
- Use `-c` for compact, concise output
- Use `-d` to limit tree depth
- Use `-s` to snapshot specific element
- Use `--full` for complete details
- Use `-n` to filter by name
- Use `--exact` for exact name matching
- Combine options as needed
- Always use `--json` in agent mode
