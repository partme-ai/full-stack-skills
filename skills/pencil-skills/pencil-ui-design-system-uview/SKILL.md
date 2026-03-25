---
name: pencil-ui-design-system-uview
description: "Initialize uView 2.x design tokens and component overview frames in a Pencil .pen file. Use when the user mentions Pencil with uView 2.x (not uView Pro), needs to set up uView color palette and typography variables, or wants to create component library frames for Button, Form, Cell, Tabs, and other uView components."
license: Complete terms in LICENSE.txt
---


# uView Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "uView" (2.x, not uView Pro) or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when:
- The user wants to initialize uView 2.x tokens (primary, success, warning, error colors) in a Pencil .pen file
- The user needs a component overview frame for uView 2.x components in Pencil
- The user mentions "Pencil" together with "uView" (2.x, not Pro) or uView-specific components (Button, Cell, Tabs, Navbar)
- An orchestrator skill (pencil-ui-designer) routes a uView 2.x initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register uView 2.x design tokens. Follow .pen file schema.

**Primary / Semantic**
- `u-type-primary`: `#3c9cff`
- `u-type-success`: `#5ac725`
- `u-type-warning`: `#f9ae3d`
- `u-type-error`: `#f56c6c`
- `u-type-info`: `#909399`

**Text & Border**
- `u-main-color`: `#303133`
- `u-content-color`: `#606266`
- `u-tips-color`: `#909399`
- `u-border-color`: `#e4e7ed`
- `u-radius`: `4px`

**Font**
- `u-font-size-base`: `14px` (28rpx)

Fill from uView 2.x docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on uView 2.x documentation:

1. **Basic (基础)**
   - Icon, Button, Layout, Cell, Badge, Tag
2. **Form (表单)**
   - Form, Input, Textarea, Radio, Checkbox, Switch, Rate, Upload, Picker, Select, DatetimePicker, Search, NumberBox, CodeInput
3. **Data (数据)**
   - Table, List, Calendar, CountDown, CountTo, Progress, CircleProgress
4. **Feedback (反馈)**
   - ActionSheet, Modal, Toast, Notify, SwipeAction, Collapse, Popup
5. **Layout (布局)**
   - Grid, Divider, Sticky, IndexList, Swiper, Waterfall
6. **Navigation (导航)**
   - Navbar, Tabbar, Tabs, BackTop, Link, Section

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize uView 2.x Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/app.pen",
    "replace": false,
    "variables": {
      "u-type-primary": "#3c9cff",
      "u-type-success": "#5ac725",
      "u-type-warning": "#f9ae3d",
      "u-type-error": "#f56c6c",
      "u-main-color": "#303133",
      "u-border-color": "#e4e7ed",
      "u-font-size-base": "14px"
    }
  }
}
```

## Best Practices

- Verify token values against uView 2.x documentation (distinct from uView Pro).
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.
- Keep each `batch_design` call to maximum 25 operations; split by category if needed.

## Keywords

pencil, uview, uview 2, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
