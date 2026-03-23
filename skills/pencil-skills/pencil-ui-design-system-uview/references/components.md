# uView 2.0 Design System Components

This reference defines the visual specifications for initializing uView 2.0 components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#3c9cff`
- **Border Radius**: `4px`
- **Font Size**: `14px` (28rpx)
- **Background**: `#f3f4f6`

## 2. Component Specifications

### Button (`u-button`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#3c9cff` (Primary)
  - Radius: `4px`
  - Height: `40px` (Default)
- **Content**: Text "Button" (White, 14px)

### Input (`u--input`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Stroke: `#dadbde`
  - Fill: `#ffffff`
  - Radius: `4px`
  - Height: `36px`
  - Padding: `0 9px`
- **Content**: Text "Please input" (#c0c4cc)

### Cell (`u-cell`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#ffffff`
  - Padding: `10px 15px`
  - Border-Bottom: `1px solid #dadbde`
- **Children**: Icon + Title + Value + Arrow

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "u-button",
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
