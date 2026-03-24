---
name: pencil-ui-design-system-bootstrap
description: Initialize Bootstrap. design system components in Pencil variables and component overview.
license: Complete terms in LICENSE.txt
---


# Bootstrap Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "Bootstrap" or when orchestrating a Pencil design system initialization task.

## When to use this skill

Use this skill when you need to initialize a new design system based on Bootstrap specifications, specifically to set up the global color palette and create the initial component library frames in a .pen file.

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register Bootstrap design tokens. Follow .pen file schema.

**Primary / Semantic**
- `bs-primary`: `#0d6efd`
- `bs-secondary`: `#6c757d`
- `bs-success`: `#198754`
- `bs-danger`: `#dc3545`
- `bs-warning`: `#ffc107`
- `bs-info`: `#0dcaf0`
- `bs-light`: `#f8f9fa`
- `bs-dark`: `#212529`

**Body & Border**
- `bs-body-color`: `#212529`
- `bs-border-color`: `#dee2e6`
- `bs-border-radius`: `0.375rem` (6px)

**Font**
- `bs-font-size-base`: `1rem` (16px)

Fill from Bootstrap Sass variables / CSS variables if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Components Overview" frame with sections based on Bootstrap documentation:

1. **Layout**
   - Container, Grid, Stack
2. **Content**
   - Typography, Images, Tables
3. **Forms**
   - Form, Input, Select, Checkbox, Radio, Switch, Range
4. **Components**
   - Accordion, Alert, Badge, Breadcrumb, Buttons, Button group, Card, Carousel, Close button, Collapse, Dropdowns, List group, Modal, Navbar, Offcanvas, Pagination, Placeholders, Popovers, Progress, Scrollspy, Spinners, Toasts, Tooltips
5. **Utilities**
   - Borders, Colors, Display, Flex, Float, Spacing

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

## Best Practices

- Verify token values against Bootstrap docs (Sass/CSS variables).
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Use Auto Layout for component overview frames.

## Keywords

pencil, bootstrap, design system, init, variables, components

## References

- `references/contract.md` – Design tokens and component naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Component specifications.
