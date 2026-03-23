---
name: pencil-ui-design-system-vant
description: Initialize Vant. design system components in Pencil variables and component overview.
license: Complete terms in LICENSE.txt
---


# Vant Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Vant" (or "Vant 4") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when you need to initialize a new design system based on Vant specifications, specifically to set up the global color palette and create the initial component library frames in a .pen file.

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register Vant design tokens. Follow .pen file schema.

**Primary / Semantic**
- `van-primary-color`: `#1989fa`
- `van-success-color`: `#07c160`
- `van-warning-color`: `#ff976a`
- `van-danger-color`: `#ee0a24`
- `van-gray-color`: `#323233`

**Text & Border**
- `van-text-color`: `#323233`
- `van-text-color-2`: `#646566`
- `van-text-color-3`: `#969799`
- `van-border-color`: `#ebedf0`
- `van-border-radius`: `4px`

**Font**
- `van-font-size-md`: `14px`

Fill from Vant theme docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on Vant documentation:

1. **Basic (基础)**
   - Button, Cell, Icon, Image, Layout, Popup, Space, ConfigProvider
2. **Form (表单)**
   - Calendar, Cascader, Checkbox, DatetimePicker, Field, Form, NumberKeyboard, PasswordInput, Picker, Radio, Rate, Search, Slider, Stepper, Switch, Upload
3. **Feedback (反馈)**
   - ActionSheet, Dialog, DropdownMenu, Loading, Notify, Overlay, ShareSheet, SwipeCell, Toast
4. **Display (展示)**
   - Badge, Circle, Collapse, CountDown, Divider, Empty, ImagePreview, Laziness, List, NoticeBar, Progress, Skeleton, Steps, Sticky, Swipe, Tag
5. **Navigation (导航)**
   - ActionBar, Grid, IndexBar, NavBar, Pagination, Sidebar, Tab, Tabbar, TreeSelect

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

## Best Practices

- Verify token values against Vant theme documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.

## Keywords

pencil, vant, vant 4, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
