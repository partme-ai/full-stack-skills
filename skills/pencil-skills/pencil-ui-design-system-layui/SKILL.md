---
name: pencil-ui-design-system-layui
description: "Initialize Layui design tokens and component overview frames in a Pencil .pen file. Use when the user mentions Pencil with Layui or layui-vue, needs to set up Layui color palette and typography variables, or wants to create component library frames for Button, Table, Form, Menu, and other Layui components."
license: Complete terms in LICENSE.txt
---


# Layui Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Layui" (or "layui-vue") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when:
- The user wants to initialize Layui tokens (primary, warm, danger colors) in a Pencil .pen file
- The user needs a component overview frame for Layui components in Pencil
- The user mentions "Pencil" together with "Layui", "layui-vue", or Layui-specific components (Table, Form, Menu, Tabs)
- An orchestrator skill (pencil-ui-designer) routes a Layui initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register Layui design tokens. Follow .pen file schema.

**Primary / Theme**
- `layui-primary`: `#1e9fff` (Layui default blue)
- `layui-normal`: `#1e9fff`
- `layui-warm`: `#ffb800`
- `layui-danger`: `#ff5722`

**Text & Border**
- `layui-text`: `#333333`
- `layui-border`: `#e6e6e6`

**Font & Radius**
- `layui-font-md`: `14px`
- `layui-radius`: `2px` (Layui default)

Fill from official Layui docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on Layui documentation:

1. **Basic (基础)**
   - Button, Form, Input, Textarea, Select, Checkbox, Radio, Switch
2. **Layout (布局)**
   - Container, Grid, Card
3. **Data (数据)**
   - Table, Tree, Pagination, Badge, Tag
4. **Feedback (反馈)**
   - Alert, Message, Modal, Drawer, Loading
5. **Navigation (导航)**
   - Menu, Tabs, Breadcrumb, Dropdown
6. **Other (其他)**
   - Icon, Divider, Timeline

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize Layui Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/app.pen",
    "replace": false,
    "variables": {
      "layui-primary": "#1e9fff",
      "layui-warm": "#ffb800",
      "layui-danger": "#ff5722",
      "layui-text": "#333333",
      "layui-border": "#e6e6e6",
      "layui-font-md": "14px",
      "layui-radius": "2px"
    }
  }
}
```

## Best Practices

- Verify token values against Layui official documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.
- Keep each `batch_design` call to maximum 25 operations; split by category if needed.

## Keywords

pencil, layui, layui-vue, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
