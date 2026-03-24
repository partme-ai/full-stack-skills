# Layui Design Contract (Layui-Vue)

This reference contains:

- Hard constraints prefix (paste-ready)
- Layout invariants for beautify mode
- Component snippets (Layui look & feel)

---

## Trigger Keywords

Use this contract when the request mentions **Stitch** and any of the following keywords:

- `layui`
- `layui-vue`

---

## Hard Constraints (Must Follow)

### Color Tokens (Layui-Vue theme)

Only use this palette. Do not introduce new brand colors:

- Brand
  - `primary`: `#16baaa` (Cyan-Green)
  - `secondary`: `#16b777`
  - `classic-blue`: `#1E9FFF`
  - `nav-bg`: `#393D49`
- Functional
  - `info`: `#31BDEC`
  - `success`: `#16b777`
  - `warning`: `#FFB800`
  - `error`: `#FF5722` (Danger)
- Neutrals
  - `text-main`: `#333333`
  - `text-regular`: `#666666`
  - `text-secondary`: `#999999`
  - `border`: `#e2e2e2` / `#eeeeee`
  - `bg-page`: `#f2f2f2`
  - `bg-white`: `#ffffff`

Forbidden:
- No gradients as default style.
- No rounded-xl buttons (Layui uses small radius 2px or 4px).

### Type Scale

Only use these font sizes (px): `12, 14, 16, 18, 20, 24, 30`.

Font weights:
- Titles: 500 (Layui tends to be lighter than Material)
- Body: 400

### Spacing Scale

Only use spacing (px): `5, 10, 15, 20, 30`. (Layui typically uses 10/15px grid).

### Radius + Border + Shadow

Radius:
- Small: `2px` (Classic Layui feel)
- Medium: `4px`
- Do NOT use large radius (8px/12px) unless explicitly requested.

Borders:
- Color: `#e2e2e2`
- Default width: 1px solid.

Shadows:
- Very subtle or flat.

---

## Beautify Mode (Layout-Locked)

Paste snippet:

```text
Layout invariants (must follow):
- Preserve the existing layout and alignment.
- Keep the logo placement and alignment exactly as-is.
- Do not add/remove/reorder sections; only polish spacing/typography/colors/radius within Layui constraints.
```

---

## Component Snippets (Layui Look & Feel)

### Button (layui-btn)

```text
Buttons (layui-btn style):
- Height: 38px (normal), 30px (small), 44px (large).
- Radius: 2px.
- Primary: bg #16baaa, text white.
- Danger: bg #FF5722, text white.
- Normal: bg white, border #e2e2e2, text #333.
```

### Input (layui-input)

```text
Inputs (layui-input style):
- Height: 38px.
- Border: 1px solid #e2e2e2.
- Radius: 2px.
- Focus: border #16baaa, subtle shadow.
- Placeholder: #cccccc.
```

### Card (layui-card)

```text
Cards (layui-card style):
- Bg: white.
- Header: height 42px, border-bottom 1px solid #f6f6f6, text #333, font-size 14px/16px.
- Body: padding 10px 15px.
- Radius: 2px.
```

### Table (layui-table)

```text
Table (layui-table style):
- Header bg: #f2f2f2.
- Border: 1px solid #e2e2e2.
- Row hover: #f8f8f8.
- Text: 14px #666.
```

### Other Components
```text
- PageHeader: <lay-page-header content="Detail" @back="onBack" />
- Result: <lay-result status="success" title="Success" describe="Check details" />
- Skeleton: <lay-skeleton :rows="4" />
- Timeline: <lay-timeline><lay-timeline-item title="Step 1">...</lay-timeline-item></lay-timeline>
- Space: <lay-space direction="vertical" size="md">...</lay-space> (For layout gaps)
```

---

## Stitch Prompt Prefix (paste-ready)

```text
Hard constraints (Layui-Vue style, must follow):
1) Colors: ONLY use this palette:
   - Primary: #16baaa (Cyan-Green)
   - Success: #16b777, Warning: #FFB800, Danger: #FF5722, Info: #31BDEC
   - Nav: #393D49
   - Neutrals: Text #333/#666/#999; Border #e2e2e2; Bg #f2f2f2
2) Radius: STRICTLY use 2px or 4px. No large rounded corners (8px+).
3) Typography: 14px base size. Titles font-weight 500.
4) Components:
   - Buttons: Height 38px, Radius 2px.
   - Inputs: Height 38px, Border #e2e2e2.
   - Cards: White bg, Header border-bottom #f6f6f6.
5) Spacing: Use 10px / 15px grid system.
6) Style: Minimalist, Flat, Clean, "Classic Design".
```

---

## Selector JSON (Fixed Schema)

```json
{
  "version": "CONTRACT_SELECTION_JSON_V1",
  "designSystem": "layui-vue",
  "mode": "selector",
  "contracts": {
    "include": [
      "hard-constraints",
      "layout-invariants",
      "components:layui-btn",
      "components:layui-input",
      "components:layui-card",
      "components:layui-table"
    ]
  },
  "states": {
    "include": [
      "error",
      "success",
      "disabled",
      "focus"
    ]
  }
}
```
