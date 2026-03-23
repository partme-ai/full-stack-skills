# ECharts Design System Components

This reference defines the visual specifications for initializing ECharts components in Pencil.

## 1. Design Tokens

- **Colors**: ECharts Default Theme
- **Font**: Sans-serif

## 2. Component Specifications

### Generic Chart Container
- **Structure**: Frame
- **Visuals**:
  - Size: 100% width, fixed height (e.g., 400px)
  - Background: Transparent or White
- **Content**: Placeholder Visual representing the chart type.

### Bar Chart
- **Visuals**: Series of rectangles aligned to bottom axis.

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "echarts-container",
  "spec": {
    "type": "frame",
    "name": "ECharts Container",
    "width": 400,
    "height": 300,
    "fills": [{"type": "SOLID", "color": "#FFFFFF"}],
    "stroke": [{"type": "SOLID", "color": "#EEEEEE"}],
    "children": [
      {"type": "text", "characters": "ECharts Visualization"}
    ]
  }
}
```
