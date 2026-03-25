---
name: pencil-ui-design-system-element
description: "Initialize Element Plus design tokens and component overview frames in a Pencil .pen file. Use when the user mentions Pencil with Element Plus or Element UI, needs to set up Element color palette and typography variables, or wants to create component library frames for Button, Table, Form, Dialog, and other Element components."
license: Complete terms in LICENSE.txt
---


# Element Plus Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Element" (or "Element Plus") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when:
- The user wants to initialize Element Plus tokens (primary, success, warning, danger colors) in a Pencil .pen file
- The user needs a component overview frame for Element Plus components in Pencil
- The user mentions "Pencil" together with "Element", "Element Plus", or Element-specific components (Table, Form, Dialog, Menu)
- An orchestrator skill (pencil-ui-designer) routes an Element Plus initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register Element Plus design tokens. Follow .pen file schema.

**Primary / Semantic**
- `el-color-primary`: `#409eff`
- `el-color-success`: `#67c23a`
- `el-color-warning`: `#e6a23c`
- `el-color-danger`: `#f56c6c`
- `el-color-info`: `#909399`

**Text & Border**
- `el-text-color-primary`: `#303133`
- `el-text-color-regular`: `#606266`
- `el-text-color-secondary`: `#909399`
- `el-border-color`: `#dcdfe6`
- `el-border-radius-base`: `4px`

**Font**
- `el-font-size-base`: `14px`

Fill from Element Plus theme docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on Element Plus documentation:

1. **Basic (基础)**
   - Button, Link, Icon
2. **Layout (布局)**
   - Container, Grid, Divider
3. **Form (表单)**
   - Radio, Checkbox, Input, InputNumber, Select, Cascader, Switch, Slider, TimePicker, DatePicker, DateTimePicker, Form, Upload, Rate
4. **Data (数据)**
   - Table, Tag, Progress, Tree, Pagination, Avatar, Skeleton, Empty
5. **Navigation (导航)**
   - Menu, Tabs, Breadcrumb, PageHeader, Dropdown, Steps
6. **Feedback (反馈)**
   - Alert, Loading, Message, MessageBox, Notification, Dialog, Drawer, Popover, Tooltip

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize Element Plus Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/app.pen",
    "replace": false,
    "variables": {
      "el-color-primary": "#409eff",
      "el-color-success": "#67c23a",
      "el-color-warning": "#e6a23c",
      "el-color-danger": "#f56c6c",
      "el-text-color-primary": "#303133",
      "el-border-color": "#dcdfe6",
      "el-font-size-base": "14px"
    }
  }
}
```

## Best Practices

- Verify token values against Element Plus theme documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.
- Keep each `batch_design` call to maximum 25 operations; split by category if needed.

## Keywords

pencil, element, element plus, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
