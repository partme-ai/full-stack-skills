---
name: tui-table
description: "Generate and render a pixel-precise ASCII TUI Table component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a table in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

- Produce an ASCII Text UI (TUI) representation of **Table**.
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
  "id": "tui-table_1",
  "name": "Table",
  "type": "tui-table",
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
cmpBg=I(screen,{type:"rect",name:"Table/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Table/Text",content:"Table"})
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

Canonical `props` for a table:
- `columns: Array<{ key: string, title: string, widthCols?: number, align?: "left" | "right" | "center" }>`
- `rows: Array<Record<string, string | number>>`
- `rowKey?: string`
- `sortable?: boolean`
- `sort?: { key: string, dir: "asc" | "desc" }`
- `emptyText?: string`

Rendering rules:
- Fixed-width columns; if total exceeds `widthCols`, truncate cell text with `…`.
- Header shows sort indicator when `sort` is present: `↑` or `↓`.
- Show row striping only if explicitly requested (default off to keep output stable).

Interaction hints:
- `<up>/<down>` row, `<left>/<right>` column (optional), `<enter>` select.

## Examples (Must include all output blocks)

### Example 1 — Minimal / default

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Table]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (default state)                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-table_ex1",
  "name": "Table",
  "type": "tui-table",
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
    { "id": "tui-table_ex1", "name": "Table", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 96 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Table/Background"})
U(cmpBg,{x:24,y:24,width:342,height:96,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Table/Text",content:"Table"})
U(cmpText,{x:40,y:56,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 2 — Styled / customized

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Table]                                                    │
├──────────────────────────────────────────────────────────────┤
│ (custom style: strong border, increased padding)             │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-table_ex2",
  "name": "Table",
  "type": "tui-table",
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
    { "id": "tui-table_ex2", "name": "Table", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 104 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Table/Background"})
U(cmpBg,{x:24,y:24,width:342,height:104,fillColor:"#ffffff",strokeColor:"#111111",strokeThickness:2,cornerRadius:12})
cmpText=I(screen,{type:"text",name:"Table/Text",content:"Table"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

### Example 3 — Disabled / error / edge-case

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Table] Disabled                                           │
├──────────────────────────────────────────────────────────────┤
│ Error: Something went wrong…                                 │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-table_ex3",
  "name": "Table",
  "type": "tui-table",
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
    { "id": "tui-table_ex3", "name": "Table", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 112 }, "zIndex": 1 }
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
cmpBg=I(screen,{type:"rect",name:"Table/Background"})
U(cmpBg,{x:24,y:24,width:342,height:112,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12,opacity:1})
cmpText=I(screen,{type:"text",name:"Table/Error",content:"Error: Something went wrong…"})
U(cmpText,{x:40,y:60,width:310,height:20,textColor:"#6b7280",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

### Example 4 — Sorted table with overflow truncation

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Table]                                                     │
├──────────────────────────────────────────────────────────────┤
│ Name ↑               | Role        | Last login              │
│ Ada Lovelace         | Engineer    | 2026-01-30 12:43         │
│ Grace Hopper         | Admiral     | 2026-01-29 09:10         │
│ A very very long na… | Analyst     | 2026-01-28 20:01         │
├──────────────────────────────────────────────────────────────┤
│ Keys: <up>/<down> row  <enter> select  <esc> back            │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "tui-table_ex4",
  "name": "Table",
  "type": "tui-table",
  "bbox": { "topPx": 120, "leftPx": 24, "widthPx": 342, "heightPx": 200 },
  "zIndex": 1,
  "layout": { "paddingPx": 12, "gapPx": 0, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 12, "fontWeight": 400, "lineHeight": 18 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": true, "disabled": false, "loading": false, "error": null },
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
    { "id": "tui-table_ex4", "name": "Table", "bbox": { "topPx": 120, "leftPx": 24, "widthPx": 342, "heightPx": 200 }, "zIndex": 1 }
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
bg=I(screen,{type:"rect",name:"Table/Background"})
U(bg,{x:24,y:120,width:342,height:200,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
header=I(screen,{type:"text",name:"Table/Header",content:"Name ↑ | Role | Last login"})
U(header,{x:40,y:140,width:310,height:18,textColor:"#111111",fontFamily:"Inter",fontSize:12,fontWeight:600})
row1=I(screen,{type:"text",name:"Table/Row1",content:"Ada Lovelace | Engineer | 2026-01-30 12:43"})
U(row1,{x:40,y:162,width:310,height:18,textColor:"#111111",fontFamily:"Inter",fontSize:12,fontWeight:400})
row2=I(screen,{type:"text",name:"Table/Row2",content:"Grace Hopper | Admiral | 2026-01-29 09:10"})
U(row2,{x:40,y:182,width:310,height:18,textColor:"#111111",fontFamily:"Inter",fontSize:12,fontWeight:400})
row3=I(screen,{type:"text",name:"Table/Row3",content:"A very very long na… | Analyst | 2026-01-28 20:01"})
U(row3,{x:40,y:202,width:310,height:18,textColor:"#111111",fontFamily:"Inter",fontSize:12,fontWeight:400})
```

## Component Summary Row (for page aggregation)

```text
| id | name | top | left | width | height | z | keyProps | state | hotkeys |
| tui-table | Table | 0 | 0 | 0 | 0 | 0 | keyProps=... | state=... | hotkeys=... |
```
