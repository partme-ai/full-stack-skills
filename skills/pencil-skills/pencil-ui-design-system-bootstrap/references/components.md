# Bootstrap Design System Components

This reference defines the visual specifications for initializing Bootstrap components in Pencil.

## 1. Design Tokens

- **Primary Color**: `#0d6efd`
- **Border Radius**: `0.375rem` (6px)
- **Font Size**: `1rem` (16px)
- **Spacing**: `1rem` (16px base)

## 2. Component Specifications

### Button (`btn-primary`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Fill: `#0d6efd`
  - Radius: `6px`
  - Padding: `6px 12px`
- **Content**: Text "Button" (White, 16px)

### Card (`card`)
- **Structure**: Frame (AutoLayout: Vertical)
- **Visuals**:
  - Fill: `#ffffff`
  - Stroke: `#dee2e6` (1px)
  - Radius: `6px`
- **Children**:
  - Image (Optional)
  - Body (Frame, Padding 16px)
    - Title (H5, Bold)
    - Text (P)
    - Button

### Form Control (`form-control`)
- **Structure**: Frame (AutoLayout: Horizontal)
- **Visuals**:
  - Stroke: `#dee2e6`
  - Radius: `6px`
  - Height: `38px`
  - Padding: `6px 12px`
- **Content**: Text "Placeholder" (#6c757d)

## 3. Initialization Actions (JSON Template)

```json
{
  "type": "draw_component",
  "name": "btn-primary",
  "spec": {
    "type": "frame",
    "layoutMode": "HORIZONTAL",
    "padding": {"top": 6, "bottom": 6, "left": 12, "right": 12},
    "cornerRadius": 6,
    "fills": [{"type": "SOLID", "color": "#0d6efd"}],
    "children": [{"type": "text", "characters": "Button"}]
  }
}
```
