# uCharts Design System Components

This reference defines the visual specifications for initializing uCharts components in Pencil.

## 1. Design Tokens

- **Colors**: uCharts Default Palette (Blue, Cyan, Orange...)
- **Font**: System Default

## 2. Component Specifications

### Line Chart (`qiun-data-charts type="line"`)
- **Structure**: Frame (Container)
- **Visuals**:
  - Placeholder Rect (Gray/White)
  - Mock Data Lines (Vector Paths)
  - Axis Labels (Text)
  - Legend (Bottom/Top)

### Column Chart (`type="column"`)
- **Structure**: Frame
- **Visuals**:
  - Vertical Bars (Rectangles)
  - Axis Lines

### Pie Chart (`type="pie"`)
- **Structure**: Frame
- **Visuals**:
  - Circle (Slices)
  - Legend

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "chart-line",
  "spec": {
    "type": "frame",
    "name": "Line Chart Placeholder",
    "width": 300,
    "height": 200,
    "fills": [{"type": "SOLID", "color": "#F0F0F0"}],
    "children": [
      {"type": "text", "characters": "Line Chart (uCharts)"}
    ]
  }
}
```
