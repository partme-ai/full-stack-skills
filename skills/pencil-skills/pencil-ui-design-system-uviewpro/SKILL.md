---
name: pencil-ui-design-system-uviewpro
description: "Initialize uView Pro design tokens and component overview frames in a Pencil .pen file. Use when the user mentions Pencil with uView Pro or uviewpro, needs to set up uView Pro color palette and typography variables, or wants to create component library frames for Button, Form, Tabs, Navbar, and other uView Pro components."
license: Complete terms in LICENSE.txt
---


# uView Pro Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "uView Pro" (or "uviewpro") or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when:
- The user wants to initialize uView Pro tokens (primary, error, warning, success colors) in a Pencil .pen file
- The user needs a component overview frame for uView Pro components in Pencil
- The user mentions "Pencil" together with "uView Pro", "uviewpro", or uView Pro-specific components (Button, Form, Tabs, Navbar)
- An orchestrator skill (pencil-ui-designer) routes a uView Pro initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register the following uView Pro design tokens. Follow .pen file schema; variable names are arbitrary strings.

**Primary Colors (Blue)**
- `u-type-primary`: `#2979ff`
- `u-type-primary-dark`: `#2b85e4`
- `u-type-primary-disabled`: `#a0cfff`
- `u-type-primary-light`: `#ecf5ff`

**Error Colors (Red)**
- `u-type-error`: `#fa3534`
- `u-type-error-dark`: `#dd6161`
- `u-type-error-disabled`: `#fab6b6`
- `u-type-error-light`: `#fef0f0`

**Warning Colors (Yellow)**
- `u-type-warning`: `#ff9900`
- `u-type-warning-dark`: `#f29100`
- `u-type-warning-disabled`: `#fcbd71`
- `u-type-warning-light`: `#fdf6ec`

**Success Colors (Green)**
- `u-type-success`: `#19be6b`
- `u-type-success-dark`: `#18b566`
- `u-type-success-disabled`: `#71d5a1`
- `u-type-success-light`: `#dbf1e1`

**Info Colors (Gray)**
- `u-type-info`: `#909399`
- `u-type-info-dark`: `#82848a`
- `u-type-info-disabled`: `#c8c9cc`
- `u-type-info-light`: `#f4f4f5`

**Text Colors**
- `u-main-color`: `#303133` (Main Text)
- `u-content-color`: `#606266` (Content Text)
- `u-tips-color`: `#909399` (Tips/Secondary)
- `u-light-color`: `#c0c4cc` (Placeholder)

**Background & Border**
- `u-bg-color`: `#f3f4f6`
- `u-border-color`: `#e4e7ed`

**Font Sizes (px)**
- `u-font-xs`: `12px` (24rpx)
- `u-font-sm`: `13px` (26rpx)
- `u-font-md`: `14px` (28rpx)
- `u-font-lg`: `15px` (30rpx)
- `u-font-xl`: `16px` (32rpx)

**Border Radius**
- `u-radius`: `4px` (8rpx)
- `u-radius-lg`: `8px` (16rpx)
- `u-radius-circle`: `9999px`

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame containing the following sections (Frames) based on uView Pro documentation:

1. **Basic Components (基础组件)**
   - Color, Icon, Image, Button, Layout, Cell, Badge, Tag, Text, Fab, Transition, TodoRootPortal, ConfigProvider
2. **Form Components (表单组件)**
   - Form, Input, Textarea, Calendar, Select, Keyboard, Picker, Rate, Search, NumberBox, Upload, VerificationCode, Field, Checkbox, Radio, Switch, Slider
3. **Data Components (数据组件)**
   - CircleProgress, LineProgress, Table, CountDown, CountTo
4. **Feedback Components (反馈组件)**
   - ActionSheet, AlertTips, Toast, NoticeBar, TopTips, Collapse, Popup, SwipeAction, Modal, FullScreen
5. **Layout Components (布局组件)**
   - Line, Card, Mask, NoNetwork, Grid, Swiper, TimeLine, Skeleton, Sticky, Waterfall, Divider
6. **Navigation Components (导航组件)**
   - Dropdown, Tabbar, BackTop, Navbar, Tabs, TabsSwiper, Subsection, IndexList, Steps, Empty, Link, Section, Pagination
7. **Other Components (其他组件)**
   - MessageInput, Loadmore, TodoReadMore, LazyLoad, Gap, Avatar, Loading, LoadingPopup, safeAreaInset

Organize component frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations; split by logical sections if needed.

### Example: Initialize uView Pro Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/app.pen",
    "replace": false,
    "variables": {
      "u-type-primary": "#2979ff",
      "u-type-error": "#fa3534",
      "u-type-warning": "#ff9900",
      "u-type-success": "#19be6b",
      "u-main-color": "#303133",
      "u-bg-color": "#f3f4f6",
      "u-border-color": "#e4e7ed",
      "u-font-md": "14px"
    }
  }
}
```

## Best Practices

- Always verify color values against the latest uView Pro documentation if unsure.
- Use `set_variables` with `replace: false` to merge into existing variables unless a full reset is requested.
- Organize component frames using Auto Layout for easy expansion.
- Keep each `batch_design` call to maximum 25 operations; split by category if needed.

## Keywords

pencil, uviewpro, uview pro, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN or usage.
- `references/components.md` – Component specifications.
