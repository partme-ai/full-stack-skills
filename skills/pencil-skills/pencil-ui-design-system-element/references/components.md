# Element Plus Design System Components

This reference defines the visual specifications for initializing Element Plus components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#409EFF` (Element Blue)
- **Border Radius**: `4px` (Base)
- **Font Size**: `14px`
- **Height**: `32px` (Default)

## 2. Component Specifications

### Button (`el-button`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#409EFF` (Primary)
  - Radius: `4px`
  - Padding: `8px 15px`
  - Height: `32px`
- **Content**: Text "Button" (White, 14px)

### Input (`el-input`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Stroke: `#dcdfe6` (1px)
  - Fill: `#ffffff`
  - Radius: `4px`
  - Height: `32px`
  - Padding: `1px 11px`
- **Content**: Text "Please input" (Gray #a8abb2, 14px)

### Card (`el-card`)
- **Structure**: Frame (AutoLayout: Vertical)
- **Visuals**:
  - Fill: `#ffffff`
  - Radius: `4px`
  - Stroke: `#e4e7ed` (1px)
  - Shadow: `Always/Hover`
- **Children**:
  - **Header**: Frame (Padding: 18px 20px, Border-Bottom: 1px solid #e4e7ed) -> Text "Card Title"
  - **Body**: Frame (Padding: 20px) -> Content Slot

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "el-button",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "height": 32,
    "cornerRadius": 4,
    "fills": [{"type": "SOLID", "color": "#409EFF"}],
    "children": [{"type": "text", "characters": "Button"}]
  }
}
```
