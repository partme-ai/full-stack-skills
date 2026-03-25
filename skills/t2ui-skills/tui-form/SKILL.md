---
name: tui-form
description: "Generate and render a pixel-precise ASCII TUI Form component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a form in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

- Produce an ASCII Text UI (TUI) representation of **Form**.
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
  "id": "tui-form_1",
  "name": "Form",
  "type": "tui-form",
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
cmpBg=I(screen,{type:"rect",name:"Form/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Form/Text",content:"Form"})
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

Represent a form as an ordered list of fields inside `props`:

- `fields: Array<{ id: string, label: string, value: string, required?: boolean, placeholder?: string, error?: string, type?: "text" | "number" | "password" }>`
- `submitLabel?: string` (optional action hint)
- `readonly?: boolean` (disables editing; still allows navigation)

Rendering rules:
- One row per field, aligned as `Label: [ value ]`.
- Required fields show `*` after the label.
- A field error renders on the next line as `Error: ...` (truncate to width).

Interaction:
- `<up>/<down>` change active field
- `<enter>` edit/commit
- `<esc>` back

## Examples (Must include all output blocks)

### Example 1 — Minimal / default

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Form]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (default state)                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-form_ex1",
  "name": "Form",
  "type": "tui-form",
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
    { "id": "tui-form_ex1", "name": "Form", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Form/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Form/Text",content:"Form"})
U(cmpText,{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 2 — Styled / customized

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Form]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (custom style: strong border, increased padding)             │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-form_ex2",
  "name": "Form",
  "type": "tui-form",
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
    { "id": "tui-form_ex2", "name": "Form", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Form/Background"})
U(cmpBg,{x:24,y:24,width:342,height:104,fillColor:"#ffffff",strokeColor:"#111111",strokeThickness:2,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Form/Text",content:"Form"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 3 — Disabled / error / edge-case

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Form] Disabled                                           │
├──────────────────────────────────────────────────────────────┤
│ Error: Something went wrong…                                 │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-form_ex3",
  "name": "Form",
  "type": "tui-form",
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
    { "id": "tui-form_ex3", "name": "Form", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Form/Background"})
U(cmpBg,{x:24,y:24,width:342,height:112,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12,opacity:1})
cmpText=I(screen,{type:"text",name:"Form/Error",content:"Error: Something went wrong…"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#6b7280",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

### Example 4 — Two fields with required + validation

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Form]                                                      │
├──────────────────────────────────────────────────────────────┤
│ Username*: [ ada_lovelace________________________ ]          │
│ Email*:    [ ada@example.com______________________ ]         │
│ Error: Email must contain '@'                                │
├──────────────────────────────────────────────────────────────┤
│ Keys: <up>/<down> field  <enter> edit  <esc> back            │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-form_ex4",
  "name": "Form",
  "type": "tui-form",
  "bbox": { "topPx": 96, "leftPx": 24, "widthPx": 342, "heightPx": 152 },
  "zIndex": 1,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "wrap", "ellipsis": "…", "maxLines": 0 },
  "state": { "focused": true, "disabled": false, "loading": false, "error": "Email must contain '@'" },
  "hotkeys": ["<up>", "<down>", "<enter>", "<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "tui-form_ex4", "name": "Form", "bbox": { "topPx": 96, "leftPx": 24, "widthPx": 342, "heightPx": 152 }, "zIndex": 1 }
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
bg=I(screen,{type:"rect",name:"Form/Background"})
U(bg,{x:24,y:96,width:342,height:152,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
u=I(screen,{type:"text",name:"Form/Row1",content:"Username*: [ ada_lovelace ]"})
U(u,{x:40,y:120,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
e=I(screen,{type:"text",name:"Form/Row2",content:"Email*: [ ada@example.com ]"})
U(e,{x:40,y:144,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
err=I(screen,{type:"text",name:"Form/Error",content:"Error: Email must contain '@'"})
U(err,{x:40,y:168,width:310,height:20,textColor:"#ef4444",fontFamily:"Inter",fontSize:12,fontWeight:400})
```

## Component Summary Row (for page aggregation)

```text
| id | name | top | left | width | height | z | keyProps | state | hotkeys |
| tui-form | Form | 0 | 0 | 0 | 0 | 0 | keyProps=... | state=... | hotkeys=... |
```
