---
name: pencil-ui-design-system-antd
description: "Initialize Ant Design (antd) design tokens and component overview frames in a Pencil .pen file. Use when the user mentions Pencil with Ant Design or antd, needs to set up antd color palette and typography variables, or wants to create component library frames for Button, Form, Table, Modal, and other antd components."
license: Complete terms in LICENSE.txt
---

# Ant Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Ant Design" (or "antd") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when:
- The user wants to initialize Ant Design tokens (colors, typography, radius) in a Pencil .pen file
- The user needs a component overview frame for antd components in Pencil
- The user mentions "Pencil" together with "Ant Design", "antd", or antd-specific components (Button, Table, Modal, Form)
- An orchestrator skill (pencil-ui-designer) routes an antd initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register Ant Design design tokens. Follow .pen file schema.

**Primary / Semantic**
- `ant-primary`: `#1677ff`
- `ant-primary-hover`: `#4096ff`
- `ant-success`: `#52c41a`
- `ant-warning`: `#faad14`
- `ant-error`: `#ff4d4f`
- `ant-info`: `#1677ff`

**Neutral / Text**
- `ant-text`: `#000000e0`
- `ant-text-secondary`: `#00000073`
- `ant-border`: `#d9d9d9`
- `ant-bg`: `#ffffff`

**Font & Radius**
- `ant-font-size-base`: `14px`
- `ant-border-radius`: `6px`

Fill from Ant Design token docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on Ant Design documentation:

1. **General (通用)**
   - Button, Icon, Typography
2. **Layout (布局)**
   - Grid, Divider, Space
3. **Navigation (导航)**
   - Affix, Breadcrumb, Dropdown, Menu, Pagination, Steps, Tabs
4. **Data Entry (数据录入)**
   - AutoComplete, Cascader, Checkbox, DatePicker, Form, Input, InputNumber, Radio, Rate, Select, Slider, Switch, TimePicker, Transfer, Upload
5. **Data Display (数据展示)**
   - Avatar, Badge, Calendar, Card, Carousel, Collapse, Descriptions, Empty, Image, List, Popover, Statistic, Table, Tabs, Tag, Timeline, Tooltip, Tree
6. **Feedback (反馈)**
   - Alert, Drawer, Message, Modal, Notification, Progress, Result, Skeleton, Spin

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize Ant Design Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/app.pen",
    "replace": false,
    "variables": {
      "ant-primary": "#1677ff",
      "ant-success": "#52c41a",
      "ant-warning": "#faad14",
      "ant-error": "#ff4d4f",
      "ant-text": "#000000e0",
      "ant-border": "#d9d9d9",
      "ant-font-size-base": "14px",
      "ant-border-radius": "6px"
    }
  }
}
```

## Best Practices

- Verify token values against Ant Design token documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.
- Keep each `batch_design` call to maximum 25 operations; split by category if needed.

## Keywords

pencil, antd, ant design, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
