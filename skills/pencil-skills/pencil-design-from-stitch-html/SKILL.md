---
name: pencil-design-from-stitch-html
description: "When you need to turn Stitch page HTML (or a Stitch URL) into a Pencil .pen design. Parses DOM and Tailwind, applies HTML→Pencil mapping and execution order, outputs sequential batch_design for layout and style fidelity (background, color, size, margin, padding, shadow). Supports multi-framework tokens."
allowed-tools: "stitch*:*, mcp_pencil*, Bash, Read, Write, web_fetch"
---


# Stitch HTML / URL to Pencil design (pencil-design-from-stitch-html)

**Constraint**: Use this skill when the user wants to turn a **Stitch screen** (HTML or Stitch URL/IDs) into a **Pencil .pen design** that matches the page layout and style (100% precise correspondence). Combines Stitch MCP (get_screen, htmlCode) when input is URL with Pencil MCP (open_document, batch_design, find_empty_space_on_canvas, get_screenshot).

This skill belongs to **pencil-skills**. When input is a Stitch URL or projectId/screenId, Stitch MCP (get_screen) is used to obtain HTML; Stitch skills are responsible for PRD→prototype only, and this skill is responsible for **prototype→.pen design**.

You are a **design conversion specialist**: Stitch exports Tailwind-based HTML; Pencil uses a node tree and `batch_design` (I/U/R/M/D/C/G). This skill defines **HTML element → Pencil node** mapping rules, **strict execution order**, and **Tailwind → .pen style** mapping (background, color, size, margin, padding, shadow, border-radius) so the drawn artboard is a precise visual match.

## Prerequisites

- Stitch MCP Server (https://stitch.withgoogle.com/docs/mcp/guide/) when user provides Stitch URL or projectId/screenId
- Pencil MCP (batch_design, batch_get, open_document, find_empty_space_on_canvas, get_screenshot)
- Stitch projectId and screenId (from URL or list_projects / list_screens), or user-pasted HTML
- Optional: existing .pen file with design system (pencil-ui-design-system-*); otherwise use primitive nodes (frame, text, icon_font)

## Core References (must follow)

- **[HTML → Pencil mapping](references/html-to-pencil-mapping.md)** — Which HTML element/semantic block maps to which Pencil node type and batch_design operation (frame, text, ref, icon_font).
- **Execution order and batch split** — Defined in the section below: strict phase order, ≤25 ops per batch_design; canvas prep → root → header → main → sections/cards → forms → footer.
- **[Tailwind → Pencil styles](references/tailwind-to-pencil-styles.md)** — Background, color, size, margin, padding, shadow, border-radius, typography: Tailwind class → .pen property value (fill, padding, gap, stroke, cornerRadius, fontSize, fontWeight, textColor).
- **Per-framework style docs** — When a target framework is set, use that framework’s **\*-to-pencil-styles.md** (sections 0, 12, 14, 15) for component styles, tokens, and design-system refs/constraints: [uview](references/uview-to-pencil-styles.md), [uviewpro](references/uviewpro-to-pencil-styles.md), [element](references/element-to-pencil-styles.md), [bootstrap](references/bootstrap-to-pencil-styles.md), [layui](references/layui-to-pencil-styles.md), [vant](references/vant-to-pencil-styles.md). Cross-framework mapping and "refs vs primitives": [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md) sections 15–16.

## Optional Target Framework

- **Agnostic (default):** No target → use primitive nodes (frame, text, icon_font) and [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md) for maximum layout/style fidelity without design-system dependency.
- **Target set:** User or config specifies one of: **uView 2**, **uView Pro**, **Bootstrap**, **Element Plus**, **Layui**, **Vant** → (1) use the corresponding **\*-to-pencil-styles.md** for full style mapping and section 15 for design-system refs and batch_design conventions; (2) ensure .pen has the corresponding **pencil-ui-design-system-*** initialized so the .pen aligns with the stitch-*-components skills.

## Retrieval and HTML

1. **Resolve screen**: From Stitch design URL parse projectId/screenId, or use `list_projects` → `list_screens` → pick screen. If user provides pasted HTML, skip to Parse.
2. **get_screen**: Call Stitch MCP `get_screen` with projectId and screenId; obtain `htmlCode.downloadUrl`, `screenshot.downloadUrl`, width, height, title.
3. **Download HTML**: Fetch HTML from `htmlCode.downloadUrl` (Bash script or web_fetch); save to e.g. `temp/source.html`. If fetch fails, ask user to paste HTML.
4. **Parse**: Extract DOM tree and per-node class list (Tailwind). Preserve element semantics: header, main, section, form, input, button, label, etc.

## Conversion Pipeline

1. **Apply mapping** (see [html-to-pencil-mapping.md](references/html-to-pencil-mapping.md)): For each HTML element, determine Pencil node type (frame / text / ref / icon_font), parent binding, and default layout/size. If **target framework** is set, prefer design-system refs per that framework's *-to-pencil-styles.md section 15 and [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md) section 16.
2. **Apply styles** (see [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md)): For each node, resolve Tailwind classes to .pen properties; when target framework is set, prefer that framework's tokens (section 12 of its *-to-pencil-styles.md) and refs (section 15).
3. **Build execution plan** (see **Execution order and batch split** below): Split operations into ordered batches (Batch 1: document + root + header + main placeholder; Batch 2: header content; Batch 3–N: per section/card; etc.). Each batch ≤25 ops. When target framework is set, use refs for section/card/hint/divider per that framework's *-to-pencil-styles.md section 15.
4. **Run Pencil**: Open document (`open_document('new')` or path); optionally `find_empty_space_on_canvas` for root frame position; then call `batch_design` once per batch in order. After each batch (or at end), call `get_screenshot` on root frame to verify.

## Execution Steps

1. **Stitch** (if URL/IDs): Get projectId/screenId → get_screen → download HTML (and optionally screenshot for reference). Else use user-pasted HTML.
2. **Parse HTML**: Build DOM tree + class list per node; identify semantic regions (header, main, sections, forms).
3. **Plan batches**: From the execution order phases below, produce N batch_design payloads (filePath + operations string). Use unique binding names per batch; parent refs from previous batch (e.g. `main` from Batch 1 used as parent in Batch 3).
4. **Pencil**: open_document → find_empty_space_on_canvas (if needed) → batch_design(Batch 1) → batch_design(Batch 2) → … → get_screenshot(root) for verification.
5. **Verify**: Compare screenshot with Stitch screenshot; note any layout or style gaps for next iteration.

## Execution order and batch split

Strict execution order for converting Stitch HTML into Pencil `batch_design` calls: parents must exist before children; each batch **at most 25 operations** (Pencil recommendation).

### 1. Phase overview

| Phase | Description | Typical batch | Parent ref |
|-------|-------------|---------------|------------|
| 0 | Canvas prep (optional) | — | — |
| 1 | Document + root + header + main placeholder | Batch 1 | document → root, main |
| 2 | Header content (back, title, actions) | Batch 2 | header |
| 3 | Tabs bar (if present) | Batch 3 | root |
| 4 | Section 1 (card + title + body placeholder) | Batch 4 | main |
| 5 | Section 1 body (form rows, inputs, buttons) | Batch 5 | card1Body |
| 6 | Section 2 (card + …) | Batch 6 | main |
| 7 | Section 2 body | Batch 7 | card2Body |
| … | One batch per section body if large | … | … |
| N | Footer or final dividers | Batch N | main |

Parents created in an earlier batch are referenced by **binding name** in later batches (e.g. `I(main, ...)`, `I(card1Body, ...)`). Binding names are **unique per batch**; do not reuse the same name across batches for different nodes.

When a target framework is set, use that framework's refs for section/card, hints, divider, button, input, tabs per that framework's *-to-pencil-styles.md section 15 and [tailwind-to-pencil-styles.md](references/tailwind-to-pencil-styles.md) section 16.

### 2. Phase 0: Canvas prep (optional)

- **When**: Before any `batch_design`, if the artboard must be placed at a specific position on the canvas.
- **Actions**: Call `find_empty_space_on_canvas` with desired width/height (e.g. screen width × height from Stitch get_screen). Use returned position when creating the root frame in Phase 1 (x, y on document). No `batch_design` in this phase.

### 3. Phase 1: Root and main structure (Batch 1)

**Goal**: Create the root frame, header frame, and main content placeholder so all later content has a parent.

**Order of operations (≤25):** (1) Insert **root** frame under `document`: layout vertical, width from screen (e.g. 390), **height a fixed value (844 or 884)** so the canvas is not blank—avoid root `fit_content` when children use fill_container. Fill = page background. (2) Insert **header** frame under `root`: layout horizontal, height 56 or 64, width fill_container, padding, fill #fff, optional stroke bottom. (3) Insert **main** frame under `root`: layout vertical, width fill_container, height fit_content(800), padding 16, gap 16, placeholder true.

**Binding names for later batches:** `root`, `header`, `main`. Style: root fill from `<body>` or wrapper class (bg-*); header/main padding and gap from Tailwind (p-4, space-y-4 → 16).

### 4. Phase 2: Header content (Batch 2)

**Goal**: Fill the header with back icon, title text, and optional right actions. **Parent:** `header`. Insert backIcon (icon_font arrow_back), titleText (content = page title), and optionally headerRight frame with actions. Binding names: `backIcon`, `titleText`, `headerRight`.

### 5. Phase 3: Tabs bar (Batch 3, if present)

**Goal**: Create the tab row. **Parent:** `root`. Insert **tabsWrap** frame under root (horizontal, height 48), then tab1/tab1Text, tab2/tab2Text, tab3/tab3Text under tabsWrap. If more than 3 tabs, split into Batch 3a/3b or keep under 25 ops total.

### 6. Phase 4–5: First section / card (Batch 4 + 5)

**Batch 4** — Parent: `main`. Insert **card1** frame (vertical, fill_container, padding 24, gap 16, fill #fff, cornerRadius 12, stroke 1px); **card1Header** under card1; **card1Title** under card1Header; optional **card1Right**; **card1Body** under card1 (vertical, placeholder true).

**Batch 5** — Parent: `card1Body`. For each form row: insert row frame, label text, input frame (or ref). If more than ~8 rows, split into Batch 5a, 5b. Binding names: `card1`, `card1Header`, `card1Title`, `card1Body`.

### 7. Phase 6–7: Second section (Batch 6 + 7)

Same pattern: **Batch 6** — card2, card2Header, card2Title, card2Body under `main`. **Batch 7** — card2Body children. Repeat for Section 3, 4, … (Batch 8, 9, …). If one section has very many rows, use multiple batches with same parent (e.g. card3Body).

### 8. Phase N: Footer and final elements

Insert any footer frame under `main`, or final divider lines. Keep under 25 ops; if many small elements, group into one batch.

### 9. Batch size and naming rules

- **Max 25 operations per `batch_design` call.** Split large section bodies (e.g. 15 form rows → Batch 5 first 7, Batch 5b next 8).
- **Binding names:** Unique per batch; use descriptive names (card1, card1Body, inputRow1, labelName). In the **next** batch, reference parents by the binding name from the **previous** batch.
- **Placeholder:** Use `placeholder: true` on frames that will receive many children in the next batch (main, card1Body).

### 10. Execution order checklist

Before running Pencil: [ ] Phase 0 optional find_empty_space_on_canvas; [ ] Phase 1 Batch 1 — root, header, main; [ ] Phase 2 Batch 2 — header content; [ ] Phase 3 Batch 3 — tabs if any; [ ] Phase 4–5 Batch 4–5 — card1 + card1Body + body children; [ ] Phase 6–7 Batch 6–7 — card2 + card2Body; [ ] … repeat for remaining sections; [ ] Phase N footer/final; [ ] After all batches: get_screenshot(root) to verify.

### 11. Example: Minimal page (header + 1 card + 2 rows)

| Batch | Ops | Content |
|-------|-----|---------|
| 1 | 3 | root, header, main |
| 2 | 2 | backIcon, titleText under header |
| 3 | 6 | card1, card1Header, card1Title, card1Body |
| 4 | 5 | row1, label1, input1; row2, label2, input2 under card1Body |

Total: 4 batches, 16 operations. Order is fixed: 1 → 2 → 3 → 4.

## Integration

- **Stitch screens**: Same pattern as stitch-remotion / stitch-uviewpro-components: list_projects, list_screens, get_screen, download URLs (when user provides Stitch URL/IDs).
- **Pencil**: Same pattern as pencil-ui-designer / pencil-mcp-batch-design: open_document, batch_design (≤25 ops per call), get_screenshot for visual check.
- **Design system**: If .pen has a design system (e.g. uView Pro), prefer refs for Card, Button, Input, Tabs; otherwise use primitive frame + text + icon_font for 100% control over size/margin/shadow.

## File Structure

```
skills/pencil-design-from-stitch-html/
├── SKILL.md
├── LICENSE.txt
├── references/
│   ├── html-to-pencil-mapping.md   # Element → node + op rule
│   ├── tailwind-to-pencil-styles.md # Generic Tailwind → Pencil; §15–16 framework mapping + refs vs primitives
│   ├── uview-to-pencil-styles.md   # uView 2 → Pencil (full style table + §15 refs/constraints)
│   ├── uviewpro-to-pencil-styles.md
│   ├── element-to-pencil-styles.md
│   ├── bootstrap-to-pencil-styles.md
│   ├── layui-to-pencil-styles.md
│   └── vant-to-pencil-styles.md
└── examples/
    ├── usage.md                    # When to use, steps, MCP flow, example prompts
    ├── sample-batch-ops.md         # Minimal page → one batch_design (≤25 ops)
    ├── sample-multi-batch.md       # Header + card + form rows → four batches
    ├── sample-with-framework-refs.md # Same page with target framework (refs + tokens)
    └── sample-simple-create-product.md # Simplified Create Product (1–2 batches) for quick validation
```

## Keywords

**English:** Stitch, Pencil, batch_design, .pen, HTML to design, Tailwind, layout, fidelity.  
**中文关键词：** Stitch、Pencil、绘图、HTML 转设计稿、批动作。

## References

- [Stitch MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
- [Pencil MCP tools](https://github.com/google-labs-code/pencil-skills) / pencil-skills [stitch-html-to-pencil-batch.md](../../docs/stitch-html-to-pencil-batch.md)
- [HTML → Pencil mapping](references/html-to-pencil-mapping.md)
- [Tailwind → Pencil styles](references/tailwind-to-pencil-styles.md) (includes §15–16 framework mapping and refs vs primitives)
- Per-framework style tables (incl. refs/constraints §15): [uview](references/uview-to-pencil-styles.md), [uviewpro](references/uviewpro-to-pencil-styles.md), [element](references/element-to-pencil-styles.md), [bootstrap](references/bootstrap-to-pencil-styles.md), [layui](references/layui-to-pencil-styles.md), [vant](references/vant-to-pencil-styles.md)
- [Examples](examples/usage.md): [usage](examples/usage.md), [single batch](examples/sample-batch-ops.md), [multi-batch](examples/sample-multi-batch.md), [with framework refs](examples/sample-with-framework-refs.md), [simplified Create Product](examples/sample-simple-create-product.md)
