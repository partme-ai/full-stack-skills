---
name: tui-modal
description: "Generate and render a pixel-precise ASCII TUI Modal component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a modal in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

- Produce an ASCII Text UI (TUI) representation of **Modal**.
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
  "id": "tui-modal_1",
  "name": "Modal",
  "type": "tui-modal",
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
cmpBg=I(screen,{type:"rect",name:"Modal/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Modal/Text",content:"Modal"})
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

Canonical `props` for a modal dialog:
- `title: string`
- `body: string` (can be multi-line; wrap inside the modal width)
- `primaryAction: { label: string }`
- `secondaryAction?: { label: string }`
- `variant?: "default" | "danger"`
- `closeOnEsc?: boolean` (default true)
- `maskClosable?: boolean` (default false)

Layout rules:
- Modal is an overlay: it should have higher `zIndex` than the page content (e.g. 100).
- The modal is centered within the screen frame.

Interaction:
- `<enter>` triggers primary action (unless disabled/loading)
- `<esc>` closes when `closeOnEsc=true`

## Examples (Must include all output blocks)

### Example 1 — Minimal / default

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Modal]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (default state)                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-modal_ex1",
  "name": "Modal",
  "type": "tui-modal",
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
    { "id": "tui-modal_ex1", "name": "Modal", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Modal/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Modal/Text",content:"Modal"})
U(cmpText,{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 2 — Styled / customized

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Modal]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (custom style: strong border, increased padding)             │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-modal_ex2",
  "name": "Modal",
  "type": "tui-modal",
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
    { "id": "tui-modal_ex2", "name": "Modal", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Modal/Background"})
U(cmpBg,{x:24,y:24,width:342,height:104,fillColor:"#ffffff",strokeColor:"#111111",strokeThickness:2,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Modal/Text",content:"Modal"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 3 — Disabled / error / edge-case

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Modal] Disabled                                           │
├──────────────────────────────────────────────────────────────┤
│ Error: Something went wrong…                                 │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-modal_ex3",
  "name": "Modal",
  "type": "tui-modal",
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
    { "id": "tui-modal_ex3", "name": "Modal", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Modal/Background"})
U(cmpBg,{x:24,y:24,width:342,height:112,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12,opacity:1})
cmpText=I(screen,{type:"text",name:"Modal/Error",content:"Error: Something went wrong…"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#6b7280",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

### Example 4 — Confirmation modal with 2 actions

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Modal]                                                     │
├──────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ Delete item?                                             │ │
│ │ This action cannot be undone.                            │ │
│ │                                                          │ │
│ │ [Cancel]                              [Delete]           │ │
│ └──────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│ Keys: <left>/<right> switch  <enter> confirm  <esc> close     │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-modal_ex4",
  "name": "Modal",
  "type": "tui-modal",
  "bbox": { "topPx": 192, "leftPx": 24, "widthPx": 342, "heightPx": 220 },
  "zIndex": 100,
  "layout": { "paddingPx": 16, "gapPx": 12, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "wrap", "ellipsis": "…", "maxLines": 0 },
  "state": { "focused": true, "disabled": false, "loading": false, "error": null },
  "hotkeys": ["<left>", "<right>", "<enter>", "<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-modal_ex4", "name": "Modal", "bbox": { "topPx": 192, "leftPx": 24, "widthPx": 342, "heightPx": 220 }, "zIndex": 100 }
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
overlay=I(screen,{type:"rect",name:"Modal/Overlay"})
U(overlay,{x:0,y:0,width:390,height:844,fillColor:"#000000",opacity:0.35})
modalBg=I(screen,{type:"rect",name:"Modal/Background"})
U(modalBg,{x:24,y:192,width:342,height:220,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
title=I(screen,{type:"text",name:"Modal/Title",content:"Delete item?"})
U(title,{x:40,y:212,width:310,height:24,textColor:"#111111",fontFamily:"Inter",fontSize:16,fontWeight:600})
body=I(screen,{type:"text",name:"Modal/Body",content:"This action cannot be undone."})
U(body,{x:40,y:244,width:310,height:40,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
cancel=I(screen,{type:"rect",name:"Modal/Cancel"})
U(cancel,{x:40,y:352,width:120,height:40,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:10})
cancelText=I(screen,{type:"text",name:"Modal/CancelText",content:"Cancel"})
U(cancelText,{x:64,y:362,width:90,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
del=I(screen,{type:"rect",name:"Modal/Delete"})
U(del,{x:230,y:352,width:120,height:40,fillColor:"#ef4444",strokeColor:"#ef4444",strokeThickness:1,cornerRadius:10})
delText=I(screen,{type:"text",name:"Modal/DeleteText",content:"Delete"})
U(delText,{x:258,y:362,width:90,height:20,textColor:"#ffffff",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

## Component Summary Row (for page aggregation)

```text
| id | name | top | left | width | height | z | keyProps | state | hotkeys |
| tui-modal | Modal | 0 | 0 | 0 | 0 | 0 | keyProps=... | state=... | hotkeys=... |
```
