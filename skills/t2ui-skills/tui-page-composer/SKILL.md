---
name: tui-page-composer
description: "Generate and render a pixel-precise ASCII TUI Page Composer component with complete output blocks (TUI_RENDER, COMPONENT_SPEC, PENCIL_SPEC, PENCIL_BATCH_DESIGN) for Pencil MCP drawing workflows. Use when the user asks to create a page composer in a terminal UI, text-based interface, or Pencil MCP project."
---


## Purpose

Turn product design descriptions into a full-page text UI (TUI) that is also machine-readable and drawable:
- Output a combined `TUI_RENDER` for the entire page.
- Output a per-component summary table.
- Output a consolidated `PENCIL_SPEC` and `PENCIL_BATCH_DESIGN` plan (≤25 ops per call).

This skill assumes you follow the shared contract and grid→pixel mapping from `tui-front-ui`.

## Workflow

1. **Parse input** — Read the input model JSON (widthCols, grid, props, state, style, typography, layout, hotkeys).
2. **Calculate layout** — Convert column/row positions to pixel coordinates using the grid (cellWidthPx=8, cellHeightPx=16).
3. **Render TUI_RENDER** — Build the monospace ASCII art with box-drawing characters, respecting widthCols.
4. **Build COMPONENT_SPEC** — Emit the JSON spec with bbox, style, typography, state, and hotkeys.
5. **Build PENCIL_SPEC** — Emit the canvas and component list for Pencil MCP.
6. **Plan PENCIL_BATCH_DESIGN** — Emit batch_design calls (max 25 ops per call) to create the design in Pencil.
7. **Validate** — Verify bbox dimensions in COMPONENT_SPEC match the TUI_RENDER grid; confirm batch ops stay within the 25-op limit.

## Inputs (Recommended)

Provide a page request and a component list:

```json
{
  "page": {
    "name": "Settings",
    "widthCols": 70,
    "canvas": { "widthPx": 390, "heightPx": 844 },
    "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
    "paddingPx": 24,
    "gapPx": 16,
    "backgroundColor": "#ffffff"
  },
  "components": [
    {
      "id": "cmp_nav",
      "type": "tui-navbar",
      "preferredSizePx": { "widthPx": 342, "heightPx": 56 },
      "zIndex": 10
    }
  ]
}
```

## Output Contract (Mandatory)

### OUTPUT: TUI_RENDER

```text
...monospace-only text...
```

### OUTPUT: PAGE_SUMMARY

```text
| id         | type        | top | left | width | height | z | keyProps | state | hotkeys |
|------------|-------------|-----|------|-------|--------|---|----------|-------|---------|
| cmp_nav    | tui-navbar  |  24 |   24 |   342 |     56 |10 | ...      | ...   | ...     |
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
screen=I(root,{type:"frame",name:"Settings"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
...up to 25 ops...
```

## Composition Rules (Strict)

### 1) Layout model

- Use a single page frame as root.
- Default layout: vertical stacking within page padding.
- Place components by ascending `topPx`; break ties using `zIndex`.
- Preserve requested `zIndex` in both `COMPONENT_SPEC` and drawing order:
  - Background blocks first
  - Content blocks next
  - Overlays (modal/toast) last

### 2) Geometry calculation

Given:
- `paddingPx`
- `gapPx`
- each component `preferredSizePx` or computed size from its `TUI_RENDER` grid bbox

Compute:
- `leftPx = paddingPx`
- `topPx = paddingPx + sum(prev.heightPx + gapPx)`
- `widthPx = canvas.widthPx - paddingPx * 2` unless a component requests a smaller width

### 3) ASCII rendering layout

- Use one outer page frame.
- Render each component as a framed block and separate blocks with a single blank line.
- Ensure the entire page does not exceed `page.widthCols`.

### 4) Interactions

- Combine hotkeys and de-duplicate:
  - Page-level default: `<tab> next`, `<esc> back`
  - Component-level only if meaningful
- Do not show hotkeys for disabled components.

## Pencil MCP Execution Playbook

1. `get_editor_state(include_schema=false)`
2. `open_document("new")` (or an existing `.pen` file path)
3. Apply `PENCIL_BATCH_DESIGN` in multiple calls (≤25 ops/call).
4. `snapshot_layout(filePath, maxDepth=2, problemsOnly=true)`
5. `get_screenshot(filePath, nodeId)` for the page frame node

If any layout problems are returned, create a follow-up `batch_design` patch block.

## Example — Settings page with 4 components

### OUTPUT: TUI_RENDER

```text
┌──────────────────────────────────────────────────────────────┐
│ [Settings]                                                   │
├──────────────────────────────────────────────────────────────┤
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ [Navbar]  Settings                               [Back]  │ │
│ └──────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ [Form]                                                    │ │
│ │ Username: [ ada_lovelace________________________ ]        │ │
│ │ Email:    [ ada@example.com______________________ ]       │ │
│ └──────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ [Rate]  * * * * .  (4/5)                                  │ │
│ └──────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ [Button]  Save changes                                    │ │
│ └──────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────┤
│ Keys: <tab> next  <enter> action  <esc> back                 │
└──────────────────────────────────────────────────────────────┘
```

### OUTPUT: PAGE_SUMMARY

```text
| id            | type        | top | left | width | height | z  | keyProps               | state              | hotkeys                 |
|---------------|-------------|-----|------|-------|--------|----|------------------------|--------------------|-------------------------|
| cmp_nav       | tui-navbar  |  24 |   24 |   342 |     56 | 10 | title=Settings         | focused=false      | <esc>                   |
| cmp_form      | tui-form    |  96 |   24 |   342 |    128 |  1 | fields=2               | focused=true       | <tab>                   |
| cmp_rate      | tui-rate    | 240 |   24 |   342 |     64 |  1 | value=4,count=5        | disabled=false     | <left>/<right>,<enter>  |
| cmp_save      | tui-button  | 320 |   24 |   342 |     56 |  2 | variant=primary        | disabled=false     | <enter>                 |
```

### OUTPUT: PENCIL_SPEC

```json
{
  "canvas": { "widthPx": 390, "heightPx": 844, "backgroundColor": "#ffffff" },
  "grid": { "cellWidthPx": 8, "cellHeightPx": 16 },
  "nodes": [],
  "components": [
    { "id": "cmp_nav", "name": "Navbar", "bbox": { "topPx": 24, "leftPx": 24, "widthPx": 342, "heightPx": 56 }, "zIndex": 10 },
    { "id": "cmp_form", "name": "Form", "bbox": { "topPx": 96, "leftPx": 24, "widthPx": 342, "heightPx": 128 }, "zIndex": 1 },
    { "id": "cmp_rate", "name": "Rate", "bbox": { "topPx": 240, "leftPx": 24, "widthPx": 342, "heightPx": 64 }, "zIndex": 1 },
    { "id": "cmp_save", "name": "Button", "bbox": { "topPx": 320, "leftPx": 24, "widthPx": 342, "heightPx": 56 }, "zIndex": 2 }
  ]
}
```

### OUTPUT: PENCIL_BATCH_DESIGN

```text
CALL 1:
root=G()
screen=I(root,{type:"frame",name:"Settings"})
U(screen,{width:390,height:844,x:0,y:0})

CALL 2:
navBg=I(screen,{type:"rect",name:"Navbar/Background"})
U(navBg,{x:24,y:24,width:342,height:56,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
navTitle=I(screen,{type:"text",name:"Navbar/Title",content:"Settings"})
U(navTitle,{x:40,y:40,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:16,fontWeight:600})

formBg=I(screen,{type:"rect",name:"Form/Background"})
U(formBg,{x:24,y:96,width:342,height:128,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
uLabel=I(screen,{type:"text",name:"Form/UsernameLabel",content:"Username"})
U(uLabel,{x:40,y:112,width:90,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
uValue=I(screen,{type:"text",name:"Form/UsernameValue",content:"ada_lovelace"})
U(uValue,{x:140,y:112,width:210,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})
eLabel=I(screen,{type:"text",name:"Form/EmailLabel",content:"Email"})
U(eLabel,{x:40,y:140,width:90,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:600})
eValue=I(screen,{type:"text",name:"Form/EmailValue",content:"ada@example.com"})
U(eValue,{x:140,y:140,width:210,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})

CALL 3:
rateBg=I(screen,{type:"rect",name:"Rate/Background"})
U(rateBg,{x:24,y:240,width:342,height:64,fillColor:"#ffffff",strokeColor:"#e5e7eb",strokeThickness:1,cornerRadius:12})
rateText=I(screen,{type:"text",name:"Rate/Text",content:"* * * * .  (4/5)"})
U(rateText,{x:40,y:264,width:310,height:20,textColor:"#111111",fontFamily:"Inter",fontSize:14,fontWeight:400})

saveBg=I(screen,{type:"rect",name:"Button/Background"})
U(saveBg,{x:24,y:320,width:342,height:56,fillColor:"#111111",strokeColor:"#111111",strokeThickness:1,cornerRadius:12})
saveText=I(screen,{type:"text",name:"Button/Text",content:"Save changes"})
U(saveText,{x:40,y:338,width:310,height:20,textColor:"#ffffff",fontFamily:"Inter",fontSize:14,fontWeight:600})
```

