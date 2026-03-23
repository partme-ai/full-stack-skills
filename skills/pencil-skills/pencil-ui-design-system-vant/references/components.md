# Vant 4 Design System Components

This reference defines the visual specifications for initializing Vant 4 components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#1989fa` (Vant Blue)
- **Border Radius**: `2px` (Small), `4px` (Medium)
- **Font Size**: `14px`
- **Height**: `44px` (Mobile Button)

## 2. Component Specifications

### Button (`van-button`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#1989fa` (Primary)
  - Radius: `4px` (Normal) or `999px` (Round)
  - Height: `44px` (Large/Normal)
- **Content**: Text "Button" (White, 14px)

### Cell (`van-cell`)
- **Structure**: Frame (AutoLayout: Horizontal, Space-Between)
- **Visuals**:
  - Fill: `#ffffff`
  - Padding: `10px 16px`
  - Border-Bottom: `1px solid #ebedf0`
- **Children**:
  - Left: Text "Title" (#323233)
  - Right: Text "Value" (#969799) + Icon (Optional)

### NavBar (`van-nav-bar`)
- **Structure**: Frame (AutoLayout: Horizontal, H: 46px)
- **Visuals**:
  - Fill: `#ffffff`
  - Border-Bottom: `1px solid #ebedf0`
- **Children**:
  - Left: Arrow Icon + Text "Back" (#1989fa)
  - Center: Text "Title" (Bold, 16px, #323233)
  - Right: Icon/Text

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "van-button",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "height": 44,
    "cornerRadius": 4,
    "fills": [{"type": "SOLID", "color": "#1989fa"}],
    "children": [{"type": "text", "characters": "Button"}]
  }
}
```
