---
name: pencil-ui-design-system-echarts
description: "Initialize ECharts chart theme tokens and data visualization placeholder frames in a Pencil .pen file. Use when the user mentions Pencil with ECharts, needs to set up chart color palette and axis tokens, or wants to create placeholder frames for Line, Bar, Pie, Radar, and other ECharts chart types."
license: Complete terms in LICENSE.txt
---


# ECharts Design System Initializer

**Constraint**: Only use this skill when the user explicitly mentions "Pencil" and "ECharts" or when orchestrating a Pencil design system initialization task for charts.

## When to use this skill

Use this skill when:
- The user wants to initialize ECharts chart theme tokens (colors, axis, text) in a Pencil .pen file
- The user needs placeholder frames for ECharts chart types (Line, Bar, Pie, Scatter, Radar, Gauge)
- The user mentions "Pencil" together with "ECharts" or chart visualization components
- An orchestrator skill (pencil-ui-designer) routes an ECharts initialization request

## How to use this skill

This skill outputs a PENCIL_PLAN. The Agent then calls Pencil MCP tools in order: `open_document`, `set_variables`, `batch_design`, optionally `get_screenshot`.

### Step 1: Initialize Variables (set_variables)

Use `mcp__pencil__set_variables` to register ECharts-related design tokens (chart theme colors, font). Follow .pen file schema.

**Chart colors (palette)**
- `echarts-color-1`: `#5470c6`
- `echarts-color-2`: `#91cc75`
- `echarts-color-3`: `#fac858`
- `echarts-color-4`: `#ee6666`
- `echarts-color-5`: `#73c0de`

**Axis / grid / text**
- `echarts-axis-line-color`: `#6e7079`
- `echarts-split-line-color`: `#e0e6f1`
- `echarts-text-color`: `#6e7079`
- `echarts-font-size`: `12px`

Fill from ECharts theme docs if more tokens are needed.

### Step 2: Create Component Overview Structure (batch_design)

Use `mcp__pencil__batch_design` to create a "Charts Overview" frame with placeholder sections for chart types (data-viz components):

1. **Basic Charts (基础图表)**
   - Line, Bar, Pie, Scatter, Radar, Gauge
2. **Complex Charts (复杂图表)**
   - Candlestick, Heatmap, Tree, Treemap, Sunburst, Parallel, Sankey, Funnel, PictorialBar
3. **Containers (容器)**
   - Chart container placeholder, Legend placeholder, Grid placeholder

Organize frames using Auto Layout. Keep each `batch_design` call to maximum 25 operations.

### Example: Initialize ECharts Variables

```json
{
  "name": "set_variables",
  "arguments": {
    "filePath": "designs/dashboard.pen",
    "replace": false,
    "variables": {
      "echarts-color-1": "#5470c6",
      "echarts-color-2": "#91cc75",
      "echarts-color-3": "#fac858",
      "echarts-color-4": "#ee6666",
      "echarts-axis-line-color": "#6e7079",
      "echarts-text-color": "#6e7079",
      "echarts-font-size": "12px"
    }
  }
}
```

## Best Practices

- Verify token values against ECharts theme documentation.
- Use `set_variables` with `replace: false` unless a full reset is requested.
- Chart "components" here are placeholder frames for layout; actual chart config is code-side.
- Keep each `batch_design` call to maximum 25 operations.

## Keywords

pencil, echarts, chart, design system, init, variables, data visualization

## References

- `references/contract.md` – Design tokens and chart type naming.
- `references/official.md` – Link to official documentation.
- `references/examples.md` – Example PENCIL_PLAN.
- `references/components.md` – Chart type specifications.
