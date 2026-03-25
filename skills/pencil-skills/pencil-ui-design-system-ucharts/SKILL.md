---
name: pencil-ui-design-system-ucharts
description: "Initialize uCharts chart theme tokens and data visualization placeholder frames in a Pencil .pen file. Use when the user mentions Pencil with uCharts or qiun-data-charts, needs to set up chart series colors and axis tokens, or wants to create placeholder frames for Line, Bar, Pie, Radar, and other uCharts chart types."
license: Complete terms in LICENSE.txt
---


# uCharts Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "uCharts" (or "qiun-data-charts") or when orchestrating a Pencil design system initialization task for charts.

## When to use this skill

Use this skill when:
- The user wants to initialize uCharts chart theme tokens (series colors, axis, text) in a Pencil .pen file
- The user needs placeholder frames for uCharts chart types (Line, Area, Column, Bar, Pie, Ring, Radar)
- The user mentions "Pencil" together with "uCharts", "qiun-data-charts", or chart visualization components
- An orchestrator skill (pencil-ui-designer) routes a uCharts initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register uCharts-related design tokens (chart theme colors, font). Follow .pen file schema.

**Chart colors (series)**
- `ucharts-color-1`: `#1890ff`
- `ucharts-color-2`: `#52c41a`
- `ucharts-color-3`: `#faad14`
- `ucharts-color-4`: `#f5222d`
- `ucharts-color-5`: `#722ed1`

**Axis / grid**
- `ucharts-axis-color`: `#e8e8e8`
- `ucharts-text-color`: `#666666`
- `ucharts-font-size`: `12px`

Fill from uCharts theme docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Charts Overview" frame with placeholder sections for chart types (data-viz components):

1. **Basic Charts (基础图表)**
   - Line, Area, Column, Bar, Pie, Ring, Radar, Scatter
2. **Combined / Advanced (组合与进阶)**
   - Mix (mixed charts), Funnel, Candlestick, Heatmap, Gauge, WordCloud
3. **Containers (容器)**
   - Chart container placeholder, Legend placeholder

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize uCharts Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/dashboard.pen",
    "replace": false,
    "variables": {
      "ucharts-color-1": "#1890ff",
      "ucharts-color-2": "#52c41a",
      "ucharts-color-3": "#faad14",
      "ucharts-color-4": "#f5222d",
      "ucharts-axis-color": "#e8e8e8",
      "ucharts-text-color": "#666666",
      "ucharts-font-size": "12px"
    }
  }
}
```

## Best Practices

- Verify token values against uCharts theme documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Chart "components" here are placeholder frames for layout; actual chart config is code-side.
- Keep each `batch_design` call to maximum 25 operations.

## Keywords

pencil, ucharts, qiun-data-charts, chart, design system, init, variables, data visualization

## References

- `references/contract.md` – Design tokens and chart type naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Chart type specifications.
