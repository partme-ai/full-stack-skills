# Layui Design System Components

This reference defines the visual specifications for initializing Layui components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#16baaa` (Cyan-Green)
- **Border Radius**: `2px` (Small/Sharp)
- **Font Size**: `14px`
- **Height**: `38px` (Standard Input/Button)

## 2. Component Specifications

### Button (`layui-btn`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#16baaa` (Primary)
  - Radius: `2px`
  - Padding: `0 18px`
  - Height: `38px`
- **Content**: Text "Button" (White, 14px)

### Input (`layui-input`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Stroke: `#e2e2e2` (1px)
  - Fill: `#ffffff`
  - Radius: `2px`
  - Height: `38px`
  - Padding: `0 10px`
- **Content**: Text "Please input" (Gray #cccccc, 14px)

### Card (`layui-card`)
- **Structure**: Frame (AutoLayout: Vertical)
- **Visuals**:
  - Fill: `#ffffff`
  - Radius: `2px`
  - Shadow: `0 1px 2px 0 rgba(0,0,0,.05)`
- **Children**:
  - **Header**: Frame (H: 42px, Border-Bottom: 1px solid #f6f6f6) -> Text "Card Title"
  - **Body**: Frame (Padding: 10px 15px) -> Content Slot

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "layui-btn",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "primaryAxisAlignItems": "CENTER",
    "counterAxisAlignItems": "CENTER",
    "fills": [{"type": "SOLID", "color": "#16baaa"}],
    "cornerRadius": 2,
    "height": 38,
    "children": [{"type": "text", "characters": "Button", "fills": [{"type": "SOLID", "color": "#FFFFFF"}]}]
  }
}
```
