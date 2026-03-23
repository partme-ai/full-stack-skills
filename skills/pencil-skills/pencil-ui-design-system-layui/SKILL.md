---
name: pencil-ui-design-system-layui
description: Initialize Layui. design system components in Pencil variables and component overview.
license: Complete terms in LICENSE.txt
---


# Layui Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Layui" (or "layui-vue") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when you need to initialize a new design system based on Layui specifications, specifically to set up the global color palette and create the initial component library frames in a .pen file.

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

## Best Practices

- Verify token values against Layui official documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.

## Keywords

pencil, layui, layui-vue, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
