# HTML Element → Pencil Node Mapping (100% Correspondence)

This document defines the **exact mapping** from Stitch HTML elements (and common Tailwind patterns) to Pencil .pen node types and `batch_design` operations. Use it to decompose Stitch HTML into drawing actions that produce a 1:1 layout and style match.

---

## Role and relationship to other docs

| Doc | Responsibility | This doc |
|-----|----------------|----------|
| **html-to-pencil-mapping.md** | **HTML structure → Pencil node type and hierarchy**: which tag/block becomes which node (frame / text / icon_font / ref), parent-child, and layout (vertical/horizontal). Does **not** define numeric style values. | ✓ You are here. |
| **tailwind-to-pencil-styles.md** | **Tailwind class → .pen property values**: fill, padding, gap, cornerRadius, stroke, fontSize, etc. Applied to the nodes chosen by this mapping. | — |
| **\*-to-pencil-styles.md** (per framework) | **Component semantics → ref or primitive + tokens**: when the target is uView/Element/Vant etc., “this is an Input/Button/Card” → use which ref and which fill/height/padding (sections 0, 12, 14, 15). | — |

**Pipeline:** (1) Use **this doc** to decide “this `<section>` → one frame as card, children = header frame + body frame”; “this `<input>` → frame or ref”. (2) Use **Tailwind** (and, if target set, **framework** doc) to fill in exact fill, padding, height, fontSize for those nodes. (3) Use SKILL **Execution order and batch split** to assign operations to batches (≤25 ops per batch). So this doc remains necessary: it answers “what node type and parent?”; Tailwind and framework docs answer “what property values?”.

---

## 1. Mapping Principles

- **One logical block → one or more Pencil nodes.** A `<section>` with title + content becomes one `frame` (container) plus child nodes (title `text`, content `frame`).
- **Parent before children.** Operations must create parent nodes before inserting children; execution order is defined in the pencil-design-from-stitch-html [SKILL.md](../SKILL.md) section **Execution order and batch split**.
- **Styles come from Tailwind.** Each node gets properties (fill, padding, gap, stroke, cornerRadius, fontSize, etc.) from the element’s class list; see [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md).
- **Binding names are unique per batch.** Use names like `root`, `header`, `main`, `card1`, `section1Title`, `inputRow1` so later batches can reference parents (e.g. `I(main, ...)`).
- **Target framework.** When a **target framework** is set (uView 2, uView Pro, Bootstrap, Element Plus, Layui, Vant), prefer **design-system refs** instead of raw frame/text for card, section, hints, divider, button, input, tabs; see that framework’s *-to-pencil-styles.md section 15 and [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md) section 16.

---

## 2. Document and Root

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<body>` or page root | Single root `frame` under `document` | layout: `"vertical"`, width from get_screen (e.g. 390). **Height:** use a **fixed** value (e.g. 844 or 884) so the root has a defined size; `fit_content` on the root can cause a blank canvas in Pencil when children use `fill_container`. |
| Optional wrapper `<div class="min-h-screen ...">` | Merged into root frame | Same fill (background). Prefer root height **844** or **884** (or screen height from Stitch). |

**Root frame convention (avoids blank canvas):** Set `height: 844` (or 884 / Stitch screen height). Use `layout: "vertical"` so children with `fill_container` width lay out correctly.

**Operation example (Batch 1):**
```javascript
root=I(document, {type: "frame", name: "Screen", layout: "vertical", width: 390, height: 844, fill: "#f5f6fa", placeholder: true})
```

---

## 3. Header (Top Bar)

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<header class="sticky top-0 ...">` | One `frame` | layout: `"horizontal"`, height: 56 or 64, padding from class (e.g. px-4 → padding [0,16]), fill: #fff or from class, stroke bottom 1px if border. |
| Back / left icon | `icon_font` node | iconFontFamily: `"Material Symbols Rounded"`, iconFontName: `"arrow_back"`, width/height: 24, fill from --foreground. |
| `<h1>` or title text | `text` node | content from innerText, fontSize/fontWeight/fill from Tailwind (text-lg, font-bold, text-gray-900). |
| Right-side actions (optional) | `frame` (horizontal) + icon or `text` | Same row, justifyContent: `"end"`. |

**Operation example:**
```javascript
header=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 56, padding: [0, 16], alignItems: "center", gap: 12, fill: "#ffffff", stroke: {align: "inside", fill: "#e5e7eb", thickness: {bottom: 1}}})
backIcon=I(header, {type: "icon_font", iconFontFamily: "Material Symbols Rounded", iconFontName: "arrow_back", width: 24, height: 24, fill: "#303133"})
titleText=I(header, {type: "text", content: "Create Product", fontSize: 18, fontWeight: "600", fill: "#303133"})
```

---

## 4. Tabs (Tab Bar)

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<div class="grid grid-cols-3 ...">` with 3 tab buttons | One `frame` (horizontal) | layout: `"horizontal"`, width: fill_container, height: 44–48, gap: 0; each child equal width (fill_container). |
| Each tab (inactive) | `frame` + `text` | Vertical center; text from button/label; fontSize 14, fill: #606266. |
| Active tab | Same + underline | Add stroke bottom 2px, fill: primary (#1677ff); text fill: primary. |

**Operation example:**
```javascript
tabsWrap=I(root, {type: "frame", layout: "horizontal", width: "fill_container", height: 48, fill: "#ffffff", stroke: {align: "inside", fill: "#e5e7eb", thickness: {bottom: 1}}})
tab1=I(tabsWrap, {type: "frame", layout: "vertical", width: "fill_container", height: "fill_container", justifyContent: "center", alignItems: "center"})
tab1Text=I(tab1, {type: "text", content: "Service", fontSize: 14, fill: "#1677ff", fontWeight: "600"})
// tab2, tab3 similar; active tab has stroke bottom
```

---

## 5. Main Content Area

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<main class="px-4 py-4 space-y-4">` | One `frame` | layout: `"vertical"`, width: fill_container, padding from Tailwind (p-4 → 16, or px-4 py-4 → [16,16]), gap from space-y-4 → 16. Fill transparent or page bg. |
| `space-y-4` / `space-y-6` | gap on same frame | gap: 16 (space-y-4) or 24 (space-y-6). |

**Operation example:**
```javascript
main=I(root, {type: "frame", layout: "vertical", width: "fill_container", height: "fit_content(800)", padding: 16, gap: 16, placeholder: true})
```

---

## 6. Section / Card Block

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<section class="... rounded-xl p-4 shadow-soft bg-white">` | One `frame` | layout: `"vertical"`, width: fill_container, padding from p-4 → 16 or 24; fill from bg (e.g. #ffffff); cornerRadius from rounded-xl → 12; shadow from [tailwind-to-pencil-styles](tailwind-to-pencil-styles.md). |
| Section with only title | Same frame + first child `text` | Title = h2 innerText; fontSize/fontWeight from text-sm font-bold → 14, 600. |
| Section with title + right content (e.g. switch) | Frame (horizontal) as first row: left `text`, right `frame` (switch placeholder or icon). | justifyContent: space_between, alignItems: center. |

**Operation example:**
```javascript
card1=I(main, {type: "frame", name: "Basic Info", layout: "vertical", width: "fill_container", padding: 24, gap: 16, fill: "#ffffff", cornerRadius: 12, stroke: {align: "inside", fill: "#e5e7eb", thickness: 1})
card1Header=I(card1, {type: "frame", layout: "horizontal", width: "fill_container", justifyContent: "space_between", alignItems: "center"})
card1Title=I(card1Header, {type: "text", content: "Basic Info", fontSize: 14, fontWeight: "600", fill: "#303133"})
card1Body=I(card1, {type: "frame", layout: "vertical", width: "fill_container", gap: 16, placeholder: true})
```

---

## 7. Form Fields (Label + Input Row)

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<label class="block ...">` + `<input>` | One row: optional label `text` + input area | Row = frame (horizontal) or (vertical). Label: text node, fontSize 14, fill #606266. Input: frame with padding, stroke, cornerRadius (input-like box) or ref to Input component. |
| Label with hint `(optional)` | Label = main text + secondary `text` | Second text: fontSize 12, fill #909399. |
| `<input type="text" placeholder="...">` | Frame (rectangle) or ref | Min height 40; padding 8–12; stroke 1px #e5e7eb; cornerRadius 4–8; placeholder not drawn as node but can add hint text below. |
| `<select>` | Same as input + optional chevron icon | Right side: icon_font expand_more. |
| `<input type="number">` with +/- | Frame + left “−” text/icon + value text + right “+” | Or single frame with placeholder text “0.00”. |
| `<input type="checkbox">` toggle style | Small frame (24×24) + cornerRadius 12, fill when “on” | Or ref to Switch component. |
| Radio group | Horizontal frame + several radio frames (circle stroke + dot when selected) | Each option: circle + text. |

---

## 8. Upload Area

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<div class="border-2 border-dashed ...">` with add icon | One `frame` | width/height from class (e.g. 96×96); stroke dashed 2px #e5e7eb; fill #fafafa; center icon_font “add”. |
| Tip text below | `text` node(s) | fontSize 12, fill #909399 (info) or warning color. |

---

## 9. Buttons

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<button class="... bg-primary text-white rounded-lg px-4 py-2">` | One `frame` + `text` | frame: padding [8,16], cornerRadius 8, fill primary (#1677ff); text: content, fontSize 14, fill #fff. Or ref to Button component. |
| Icon + text button | frame (horizontal) + icon_font + text | gap 8, alignItems center. |

---

## 10. Divider / Line

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<hr>` or `<div class="border-t">` | One `frame` | height: 1, width: fill_container, fill: #e5e7eb (or stroke). |
| Between content blocks | Same | Insert between section frames as sibling. |

---

## 11. Text Only (No Container)

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<p>`, `<span>` with only text | `text` node | content from innerText; fontSize, fontWeight, fill from Tailwind. |
| Small / hint text | fontSize 12, fill #909399. |
| Bold title | fontWeight "600" or "700", fontSize 14–18. |

---

## 12. Images

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<img src="...">` | Use G() to apply image fill to a frame, or placeholder frame | Insert frame with width/height from img or class; then G(frameId, "stock" or "ai", description). |
| Stitch often uses placeholder URLs | Prefer frame with fill #f0f0f0 + optional “Image” text. |

---

## 13. Collapse / Accordion

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `<details><summary>More</summary><div>...</div></details>` | Frame (vertical): summary row + body frame | Summary row: horizontal frame with title text + chevron icon (expand_more / expand_less). Body: vertical frame, padding, gap; content as child nodes. |

---

## 14. Grid Layouts (2-Col, 3-Col)

| HTML | Pencil node / operation | Notes |
|------|-------------------------|--------|
| `grid grid-cols-2 gap-4` | One `frame` (horizontal), gap 16 | Two children: each width `fill_container` (equal). |
| `grid grid-cols-3` | Same, three children. |
| Children (e.g. form items) | Each child = frame (vertical) with label + input as above. |

---

## 15. Summary Table (Quick Lookup)

| HTML element / pattern | Pencil node type | Key .pen properties |
|------------------------|------------------|---------------------|
| body / page root | frame | layout vertical, width/height, fill (background) |
| header (sticky bar) | frame | layout horizontal, height 56–64, padding, fill, stroke bottom |
| main (content) | frame | layout vertical, padding, gap |
| section / card | frame | layout vertical, padding, fill, cornerRadius, stroke, shadow |
| h1, h2, title | text | content, fontSize, fontWeight, fill |
| label, p, span | text | content, fontSize, fill |
| input (text/number) | frame or ref | padding, stroke, cornerRadius, height |
| button | frame + text or ref | padding, fill, cornerRadius, text content |
| tabs row | frame (horizontal) | gap 0, children equal width |
| divider / hr | frame | height 1, fill or stroke |
| icon (back, add, chevron) | icon_font | iconFontFamily, iconFontName, width, height, fill |
| upload dashed box | frame | stroke dashed, fill, icon_font add |

All numeric values (padding, gap, cornerRadius, fontSize) must be resolved from [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md); when a target framework is set, use that framework’s *-to-pencil-styles.md (sections 12 and 14) for tokens and component semantics.
