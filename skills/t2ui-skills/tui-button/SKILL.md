---
name: tui-button
description: "Generate and render a pixel-precise ASCII TUI Button component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a button in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

- Produce an ASCII Text UI (TUI) representation of **Button**.
- Always output layout attributes (top/left/width/height, spacing, colors, typography, zIndex).
- Always output Pencil MCP–ready specs and a `batch_design` plan (≤25 operations per call).

## Workflow

1. **Parse input** — Read the input model JSON (widthCols, grid, props, state, style, typography, layout, hotkeys).
2. **Calculate layout** — Convert column/row positions to pixel coordinates using the grid (cellWidthPx=8, cellHeightPx=16).
3. **Render TUI_RENDER** — Build the monospace ASCII art with box-drawing characters, respecting widthCols.
4. **Build COMPONENT_SPEC** — Emit the JSON spec with bbox, style, typography, state, and hotkeys.
5. **Build PENCIL_SPEC** — Emit the canvas and component list for Pencil MCP.
6. **Plan PENCIL_BATCH_DESIGN** — Emit batch_design calls (max 25 ops per call) to create the design in Pencil.
7. **Validate** — Verify bbox dimensions in COMPONENT_SPEC match the TUI_RENDER grid; confirm batch ops stay within the 25-op limit.

## Input Model (Recommended)

```json
{
  "widthCols": 70,
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "props": {},
  "modelValue": null,
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "style": {
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#e5e7eb",
    "strokeThickness": 1,
    "cornerRadius": 12
  },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "layout": { "paddingPx": 16, "gapPx": 8 },
  "hotkeys": []
}
```

## Output Contract (Mandatory)

### OUTPUT: TUI_RENDER

```text
...monospace-only text...
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_1",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 0, "leftPx": 0, "widthPx": 0, "heightPx": 0 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" },
  "style": {
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#e5e7eb",
    "strokeThickness": 1,
    "cornerRadius": 12,
    "opacity": 1
  },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": []
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": []
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
cmpBg=I(screen,{type:"rect",name:"Button/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Button/Text",content:"Button"})
U(cmpText,{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

## Rendering Rules (Component-Level)

Follow the shared rules from `tui-front-ui`:
- No TAB characters.
- Do not exceed `widthCols`.
- Provide a header row, body area, and minimal hotkeys if interactive.
- `disabled=true` must suppress interaction hints.
- `loading=true` must show a stable placeholder.
- `error!=null` must be printed in a single line footer (truncated to width).

## Component Mapping (Actionable)

Model the button with these canonical fields inside `props`:
- `label: string` (required)
- `variant: "primary" | "secondary" | "danger" | "ghost"` (default `primary`)
- `size: "sm" | "md" | "lg"` (default `md`)
- `block: boolean` (full-width vs content-width)
- `iconLeft?: string`, `iconRight?: string` (render as ASCII glyphs)
- `loading: boolean` (prefer `state.loading`, but allow `props.loading` as override)
- `disabled: boolean` (prefer `state.disabled`, but allow `props.disabled` as override)
- `onClick: boolean` (whether to show click hints; for pure display, set false)

State and interaction rules:
- `disabled=true`: render label in muted color token; hide `<enter>` hint
- `loading=true`: replace label with `Loading...` (stable width); hide icon(s)
- Focus ring: if `state.focused=true`, render as `⟦ ... ⟧` wrapper or a stronger border

## Examples (Must include all output blocks)

### Example 1 — Minimal / default

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Button]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (default state)                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_ex1",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": []
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-button_ex1", "name": "Button", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }, "zIndex": 1 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
cmpBg=I(screen,{type:"rect",name:"Button/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Button/Text",content:"Button"})
U(cmpText,{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 2 — Styled / customized

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Button]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (custom style: strong border, increased padding)             │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_ex2",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 },
  "zIndex": 1,
  "layout": { "paddingPx": 20, "gapPx": 10, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#111111", "strokeThickness": 2, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 600, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": []
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-button_ex2", "name": "Button", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }, "zIndex": 1 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
cmpBg=I(screen,{type:"rect",name:"Button/Background"})
U(cmpBg,{x:24,y:24,width:342,height:104,fillColor:"#ffffff",strokeColor:"#111111",strokeThickness:2,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Button/Text",content:"Button"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 3 — Disabled / error / edge-case

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Button] Disabled                                           │
├──────────────────────────────────────────────────────────────┤
│ Error: Something went wrong…                                 │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_ex3",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#6b7280", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": false, "disabled": true, "loading": false, "error": "Something went wrong" },
  "hotkeys": []
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-button_ex3", "name": "Button", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }, "zIndex": 1 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
cmpBg=I(screen,{type:"rect",name:"Button/Background"})
U(cmpBg,{x:24,y:24,width:342,height:112,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12,opacity:1})
cmpText=I(screen,{type:"text",name:"Button/Error",content:"Error: Something went wrong…"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#6b7280",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

### Example 4 — Loading (stable label width)

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Button] Loading                                             │
├──────────────────────────────────────────────────────────────┤
│ ⟦  Loading...  ⟧                                             │
├──────────────────────────────────────────────────────────────┤
│ Keys: <esc> back                                             │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_ex4",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 120 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "center", "valign": "middle" },
  "style": { "fillColor": "#111111", "textColor": "#ffffff", "strokeColor": "#111111", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 600, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": true, "disabled": false, "loading": true, "error": null },
  "hotkeys": ["<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-button_ex4", "name": "Button", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 120 }, "zIndex": 1 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
btnBg=I(screen,{type:"rect",name:"Button/Background"})
U(btnBg,{x:24,y:24,width:342,height:56,fillColor:"#111111",strokeColor:"#111111",strokeThickness:1,cornerRadius:12})
btnText=I(screen,{type:"text",name:"Button/Text",content:"Loading..."})
U(btnText,{x:40,y:42,width:310,height:20,textColor:"#ffffff",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 5 — Icon + block button

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Button]                                                     │
├──────────────────────────────────────────────────────────────┤
│ [✓] Save changes                                             │
├──────────────────────────────────────────────────────────────┤
│ Keys: <enter> click  <esc> back                               │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-button_ex5",
  "name": "Button",
  "type": "tui-button",
  "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "middle" },
  "style": { "fillColor": "#111111", "textColor": "#ffffff", "strokeColor": "#111111", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 600, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": ["<enter>", "<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-button_ex5", "name": "Button", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }, "zIndex": 1 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Screen"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
btnBg=I(screen,{type:"rect",name:"Button/Background"})
U(btnBg,{x:24,y:24,width:342,height:56,fillColor:"#111111",strokeColor:"#111111",strokeThickness:1,cornerRadius:12})
btnText=I(screen,{type:"text",name:"Button/Text",content:"[✓] Save changes"})
U(btnText,{x:40,y:42,width:310,height:20,textColor:"#ffffff",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

## Component Summary Row (for page aggregation)

```text
| id | name | top | left | width | height | z | keyProps | state | hotkeys |
| tui-button | Button | 0 | 0 | 0 | 0 | 0 | keyProps=... | state=... | hotkeys=... |
```
