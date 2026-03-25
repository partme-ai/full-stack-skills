---
name: tui-front-ui
description: "Generate and render a pixel-precise ASCII TUI Front UI Framework component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a front UI in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

Produce TUI designs that are accurate enough to be treated like product design artifacts:
- Render a copy-pastable ASCII TUI.
- Output a complete layout/spec block with geometry and style tokens.
- Output a Pencil MCP–ready plan: JSON spec + `batch_design` operations (chunked to ≤25 ops).

## Workflow

1. **Parse input** — Read the input model JSON (widthCols, grid, props, state, style, typography, layout, hotkeys).
2. **Calculate layout** — Convert column/row positions to pixel coordinates using the grid (cellWidthPx=8, cellHeightPx=16).
3. **Render TUI_RENDER** — Build the monospace ASCII art with box-drawing characters, respecting widthCols.
4. **Build COMPONENT_SPEC** — Emit the JSON spec with bbox, style, typography, state, and hotkeys.
5. **Build PENCIL_SPEC** — Emit the canvas and component list for Pencil MCP.
6. **Plan PENCIL_BATCH_DESIGN** — Emit batch_design calls (max 25 ops per call) to create the design in Pencil.
7. **Validate** — Verify bbox dimensions in COMPONENT_SPEC match the TUI_RENDER grid; confirm batch ops stay within the 25-op limit.

## Output Contract (Mandatory)

For any request, output these blocks in this order:

### OUTPUT: TUI_RENDER

```text
...monospace-only text...
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "cmp_x",
  "name": "ComponentName",
  "type": "tui-component",
  "bbox": { "topPx": 0, "leftPx": 0, "widthPx": 0, "heightPx": 0 },
  "zIndex": 0,
  "layout": { "paddingPx": 0, "gapPx": 0, "align": "left", "valign": "top" },
  "style": {
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#dddddd",
    "strokeThickness": 1,
    "cornerRadius": 8,
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
...up to 25 ops...
```

## Rendering Rules (Strict)

### 1) Character grid and pixel mapping

- Use a grid (rows/cols) for the ASCII layout.
- Default mapping:
  - `grid.cellWidthPx = 8`
  - `grid.cellHeightPx = 16`
- Convert:
  - `leftPx = col * cellWidthPx`
  - `topPx = row * cellHeightPx`
  - `widthPx = cols * cellWidthPx`
  - `heightPx = rows * cellHeightPx`

### 2) Width / truncation / wrapping

- Never output TAB characters.
- Hard max line length: `pageWidthCols`.
- Overflow policies:
  - `truncate`: cut and append `…`
  - `wrap`: break lines and keep indentation
  - `clip`: cut without `…` (avoid unless required)

### 3) Frames, borders, and box-drawing

- Preferred frame set:
  - Corners: `┌ ┐ └ ┘`
  - Lines: `─ │`
  - Intersections: `├ ┤ ┬ ┴ ┼`
- Default component chrome:
  - Header row: `[Title]` + state tags (e.g., `Disabled`, `Loading`)
  - Body region: content
  - Footer row (optional): `Keys: ...`

### 4) Color output policy

- Default: do not emit ANSI colors unless explicitly requested by the user.
- If coloring is requested:
  - Emit ANSI TrueColor sequences.
  - Provide a `noColor` switch and honor `NO_COLOR=1` as a hard disable.
- In `COMPONENT_SPEC` and `PENCIL_SPEC`, always represent colors as hex.

### 5) Interaction hints

- Hotkeys must be minimal and consistent.
- Use this canonical set when applicable:
  - Navigation: `<up>/<down>/<left>/<right>`
  - Confirm: `<enter>`
  - Back: `<esc>`
  - Focus: `<tab>`

## Pencil MCP Execution Playbook (Always include)

1. Call `get_editor_state(include_schema=false)` to find the active `.pen` file and selection.
2. If there is no active document: `open_document("new")`.
3. Use `batch_design(filePath, operations)` to apply `PENCIL_BATCH_DESIGN`.
   - Keep each call ≤ 25 operations.
   - Never reuse binding names across different calls.
4. Validate layout: `snapshot_layout(filePath, maxDepth=2, problemsOnly=true)`.
5. Visual check: `get_screenshot(filePath, nodeId)` for the page frame.

Important: the exact positioning property names may differ by schema (e.g. `x/y` vs `left/top`). If unknown, retrieve guidelines first (e.g., `get_guidelines(topic="design-system")`) and adapt the update keys in `U(...)` accordingly.

## Example 1 — Single card with title and body

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Card]                                                      │
├──────────────────────────────────────────────────────────────┤
│ Title: Account Overview                                     │
│ Balance: $2,340.18                                          │
│ Status: Active                                              │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "cmp_card_1",
  "name": "Card",
  "type": "tui-card",
  "bbox": { "topPx": 48, "leftPx": 24, "widthPx": 342, "heightPx": 160 },
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
  "overflow": { "mode": "wrap", "ellipsis": "…", "maxLines": 4 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": []
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [
    {
      "id": "node_screen",
      "type": "frame",
      "name": "Screen",
      "topPx": 0,
      "leftPx": 0,
      "widthPx": 390,
      "heightPx": 844,
      "style": { "fillColor": "#ffffff" },
      "children": ["node_card_bg", "node_card_title", "node_card_body"]
    },
    {
      "id": "node_card_bg",
      "type": "rect",
      "name": "Card/Background",
      "topPx": 48,
      "leftPx": 24,
      "widthPx": 342,
      "heightPx": 160,
      "style": { "fillColor": "#ffffff", "strokeColor": "#e5e7eb", "strokeThickness": 1, "cornerRadius": 12 }
    },
    {
      "id": "node_card_title",
      "type": "text",
      "name": "Card/Title",
      "topPx": 64,
      "leftPx": 40,
      "widthPx": 310,
      "heightPx": 24,
      "text": "Account Overview",
      "style": { "textColor": "#111111" },
      "typography": { "fontFamily": "Inter", "fontSize": 16, "fontWeight": 600, "lineHeight": 24 }
    },
    {
      "id": "node_card_body",
      "type": "text",
      "name": "Card/Body",
      "topPx": 96,
      "leftPx": 40,
      "widthPx": 310,
      "heightPx": 96,
      "text": "Balance: $2,340.18\nStatus: Active",
      "style": { "textColor": "#111111" },
      "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 }
    }
  ],
  "components": [
    {
      "id": "cmp_card_1",
      "name": "Card",
      "bbox": { "topPx": 48, "leftPx": 24, "widthPx": 342, "heightPx": 160 },
      "zIndex": 1
    }
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
cardBg=I(screen,{type:"rect",name:"Card/Background"})
U(cardBg,{x:24,y:48,width:342,height:160,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
cardTitle=I(screen,{type:"text",name:"Card/Title",content:"Account Overview"})
U(cardTitle,{x:40,y:64,width:310,height:24,textColor:"#111111",fontFamily:"Inter",fontSize:16,fontWeight:600})
cardBody=I(screen,{type:"text",name:"Card/Body",content:"Balance: $2,340.18\\nStatus: Active"})
U(cardBody,{x:40,y:96,width:310,height:96,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

## Example 2 — Input field with validation error

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Input]                                                     │
├──────────────────────────────────────────────────────────────┤
│ Email                                                      ! │
│ [ user@example.com______________________________ ]           │
│ Error: Please enter a valid email                            │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "cmp_input_email",
  "name": "Input",
  "type": "tui-input",
  "bbox": { "topPx": 240, "leftPx": 24, "widthPx": 342, "heightPx": 132 },
  "zIndex": 2,
  "layout": { "paddingPx": 16, "gapPx": 8, "align": "left", "valign": "top" },
  "style": {
    "fillColor": "#ffffff",
    "textColor": "#111111",
    "strokeColor": "#ef4444",
    "strokeThickness": 1,
    "cornerRadius": 12,
    "opacity": 1
  },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "truncate", "ellipsis": "…", "maxLines": 1 },
  "state": { "focused": true, "disabled": false, "loading": false, "error": "Please enter a valid email" },
  "hotkeys": ["<tab>", "<enter>", "<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    {
      "id": "cmp_input_email",
      "name": "Input",
      "bbox": { "topPx": 240, "leftPx": 24, "widthPx": 342, "heightPx": 132 },
      "zIndex": 2
    }
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
field=I(screen,{type:"rect",name:"Input/Field"})
U(field,{x:24,y:240,width:342,height:132,fillColor:"#ffffff",strokeColor:"#ef4444",strokeThickness:1,cornerRadius:12})
label=I(screen,{type:"text",name:"Input/Label",content:"Email"})
U(label,{x:40,y:256,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
value=I(screen,{type:"text",name:"Input/Value",content:"user@example.com"})
U(value,{x:40,y:284,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
err=I(screen,{type:"text",name:"Input/Error",content:"Error: Please enter a valid email"})
U(err,{x:40,y:312,width:310,height:20,textColor:"#ef4444",fontFamily:"Inter",fontSize:12,fontWeight:400})
```

## Example 3 — Multi-component page and required summary

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Profile]                                                   │
├──────────────────────────────────────────────────────────────┤
│ Name: Ada Lovelace                                          │
│ Role: Engineer                                              │
├──────────────────────────────────────────────────────────────┤
│ [Rate]  * * * * .  (4/5)                                    │
├──────────────────────────────────────────────────────────────┤
│ Keys: <tab> next  <enter> edit  <esc> back                   │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: COMPONENT_SPEC

```json
{
  "id": "cmp_page_profile",
  "name": "Page",
  "type": "tui-page",
  "bbox": { "topPx": 0, "leftPx": 0, "widthPx": 390, "heightPx": 844 },
  "zIndex": 0,
  "layout": { "paddingPx": 24, "gapPx": 16, "align": "left", "valign": "top" },
  "style": { "fillColor": "#ffffff", "textColor": "#111111", "strokeColor": "#e5e7eb", "strokeThickness": 0, "cornerRadius": 0, "opacity": 1 },
  "typography": { "fontFamily": "Inter", "fontSize": 14, "fontWeight": 400, "lineHeight": 20 },
  "overflow": { "mode": "wrap", "ellipsis": "…", "maxLines": 0 },
  "state": { "focused": false, "disabled": false, "loading": false, "error": null },
  "hotkeys": ["<tab>", "<enter>", "<esc>"]
}
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "cmp_profile_header", "name": "Header", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 88 }, "zIndex": 1 },
    { "id": "cmp_rate_1", "name": "Rate", "bbox": { "topPx": 128, "leftPx": 24, "widthPx": 342, "heightPx": 64 }, "zIndex": 2 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Profile"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
headerBg=I(screen,{type:"rect",name:"Header/Background"})
U(headerBg,{x:24,y:24,width:342,height:88,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
name=I(screen,{type:"text",name:"Header/Name",content:"Name: Ada Lovelace"})
U(name,{x:40,y:40,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
role=I(screen,{type:"text",name:"Header/Role",content:"Role: Engineer"})
U(role,{x:40,y:64,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
rateBg=I(screen,{type:"rect",name:"Rate/Background"})
U(rateBg,{x:24,y:128,width:342,height:64,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
rateText=I(screen,{type:"text",name:"Rate/Text",content:"* * * * .  (4/5)"})
U(rateText,{x:40,y:152,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
```

