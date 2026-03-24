# uView Pro Design System Components

This reference defines the visual specifications for initializing uView Pro components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#3c9cff`
- **Border Radius**: `8rpx` (approx 4px)
- **Font Size**: `28rpx` (approx 14px)
- **Prefix**: `up-`

## 2. Component Specifications

### Button (`up-button`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#3c9cff`
  - Radius: `4px`
  - Height: `40px`
- **Content**: Text "Button" (White)

### Search (`up-search`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#f2f2f2` (Bg)
  - Radius: `100px` (Round)
  - Height: `34px`
- **Children**: Search Icon + Text "Keyword"

### Grid (`up-grid`)
- **Structure**: Frame (Grid Layout or AutoLayout Wrap)
- **Children**: `up-grid-item` (Icon + Text Vertical Stack)

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "up-button",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "height": 40,
    "cornerRadius": 4,
    "fills": [{"type": "SOLID", "color": "#3c9cff"}],
    "children": [{"type": "text", "characters": "Button"}]
  }
}
```
