# Ant Design System Components

This reference defines the visual specifications for initializing Ant Design components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#1677ff` (Antd Blue)
- **Border Radius**: `6px` (v5 Default)
- **Font Size**: `14px`
- **Height**: `32px` (Standard Input/Button)

## 2. Component Specifications

### Button (`a-button`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#1677ff` (Primary)
  - Radius: `6px`
  - Padding: `4px 15px`
  - Height: `32px`
- **Content**: Text "Button" (White, 14px)

### Input (`a-input`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Stroke: `#d9d9d9` (1px)
  - Fill: `#ffffff`
  - Radius: `6px`
  - Height: `32px`
  - Padding: `4px 11px`
- **Content**: Text "Please input" (Gray #bfbfbf, 14px)

### Card (`a-card`)
- **Structure**: Frame (AutoLayout: Vertical)
- **Visuals**:
  - Fill: `#ffffff`
  - Radius: `8px`
  - Stroke: `#f0f0f0` (1px)
- **Children**:
  - **Header**: Frame (H: 56px, Border-Bottom: 1px solid #f0f0f0, Padding: 0 24px) -> Text "Card Title"
  - **Body**: Frame (Padding: 24px) -> Content Slot

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "a-button",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "height": 32,
    "cornerRadius": 6,
    "fills": [{"type": "SOLID", "color": "#1677ff"}],
    "children": [{"type": "text", "characters": "Button"}]
  }
}
```
