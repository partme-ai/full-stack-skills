# Vant 4 → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **Vant 4** (stitch-vue-vant-components, pencil-ui-design-system-vant), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties. Vant is mobile-first: 375 design width, 44px control height, primary #1989fa.

Generic mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. Vant 4 docs: <https://vant-ui.github.io/vant/#/zh-CN> (or vant-contrib.github.io/vant).

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [Vant 4 Button](https://vant-ui.github.io/vant/#/zh-CN/button) | size large/normal/small; type; block, round, square | frame or ref | Primary: height **44**, fill `#1989fa`, padding `[0,16]`, cornerRadius **8** (round → 22); text 16px `#ffffff`. Large taller. |
| **Field** | [Vant 4 Field](https://vant-ui.github.io/vant/#/zh-CN/field) | label+input row; left label, right control; height ~44 | frame or ref | width fill_container, height **44**, padding `[12,16]`, fill `#ffffff`, stroke bottom 1px `#ebedf0`; label 14px `#323233`, input 14px; placeholder `#c8c9cc`. |
| **Cell** | [Vant 4 Cell](https://vant-ui.github.io/vant/#/zh-CN/cell) | row height 44; left title, right value/icon; bottom divider | frame or ref | width fill_container, height **44**, padding `[12,16]`, stroke bottom 1px `#ebedf0`; title 14px `#323233`, value 14px `#969799`. |
| **NavBar** | [Vant 4 NavBar](https://vant-ui.github.io/vant/#/zh-CN/nav-bar) | height ~46; left arrow, title, right slot | frame or ref | height **46**, padding `[0,16]`, fill `#ffffff`; title 16px `#323233`; icon ~22×22. |
| **CellGroup** | [Vant 4 CellGroup](https://vant-ui.github.io/vant/#/zh-CN/cell-group) | inset (card style): radius, margin | parent frame; inset: container padding 12–16, cornerRadius 8, fill `#ffffff`. | Same. |
| **Divider** | [Vant 4 Divider](https://vant-ui.github.io/vant/#/zh-CN/divider) | optional text (e.g. "or") | line: height 1, fill `#ebedf0`; text 12px `#969799`. | Same. |
| **Tab** | [Vant 4 Tab](https://vant-ui.github.io/vant/#/zh-CN/tab) | tab bar height; active primary, underline | frame horizontal; item height ~44; active text fill `#1989fa`, stroke bottom 2px. | Same. |

**Note:** Official `size`, `round`, `block` affect button height and radius; Field/Cell row height baseline 44px. Use table for height, padding, cornerRadius, stroke.

---

## 1. Scale convention

- **Vant 4:** 375 design width; 44px control height; radius 2/4/8px.
- **Pencil:** Use **px** for layout; if canvas 390 wide, close to 375, use as-is.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#f7f8fa"` |
| Card / Cell group | `fill` | `"#ffffff"` |
| Primary button (van-button) | `fill` | `"#1989fa"` |
| Input area (van-field) | `fill` | `"#ffffff"` |
| Divider | `fill` | `"#ebedf0"` |
| NavBar | `fill` | `"#ffffff"` |

---

## 3. Color (text and borders)

| Usage | .pen value |
|-------|------------|
| Primary text / title | `"#323233"` |
| Secondary / value | `"#969799"` |
| Placeholder / description | `"#c8c9cc"` |
| Primary / link | `"#1989fa"` |
| Button text (on primary) | `"#ffffff"` |
| Border / divider | `"#ebedf0"` |
| Icon | `"#969799"` |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input / Field / Cell | `height` | 44 |
| Primary button | `height` | 44 |
| NavBar | `height` | 46 |
| Icon NavBar | width/height | 22 |
| Round icon button | width/height | 40 |

---

## 5. Margin / spacing

- Use parent **gap**; Vant typical 12, 16, 24.
| Scenario | .pen approach |
|----------|----------------|
| Cell group / blocks | Parent frame `gap: 0` (Cell uses border-b); between blocks gap 16, 24 |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Page left/right | `padding` | 16 |
| Cell / Field | `padding` | `[12, 16]` |
| Primary button | `padding` | `[0, 16]` |
| NavBar | `padding` | `[0, 16]` |
| CellGroup inset | container padding | 12, 16 |

---

## 7. Gap (flex)

| Scenario | Value (px) |
|----------|------------|
| Icon button group | 24 |
| Between blocks | 16, 24 |

---

## 8. Shadow

| Scenario | .pen approach |
|----------|----------------|
| CellGroup card style | Light shadow or cornerRadius 8; omit if no effect |

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Primary button | `cornerRadius` | 8 |
| Card-style CellGroup | `cornerRadius` | 8 |
| Round icon button | `cornerRadius` | 20 |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Cell / Field bottom | `stroke.thickness` | `{ bottom: 1 }`, fill `"#ebedf0"` |
| NavBar bottom | same | `"#ebedf0"` |
| Divider | frame height 1 | fill `"#ebedf0"` |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| NavBar title | 16 | "500" | "#323233" |
| Cell title / input | 14 | "400" | "#323233" |
| Cell value / secondary | 14 | "400" | "#969799" |
| Placeholder | 14 | "400" | "#c8c9cc" |
| Primary button | 16 | "500" | "#ffffff" |
| Link | 14 | "400" | "#1989fa" |

---

## 12. Vant 4 design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#1989fa` |
| Page background | `#f7f8fa` |
| Card/Cell background | `#ffffff` |
| Border | `#ebedf0` |
| Text primary | `#323233` |
| Text secondary | `#969799` |
| Placeholder | `#c8c9cc` |
| Radius button/card | 8 |
| Input/button/cell height | 44 |
| NavBar height | 46 |

---

## 13. Quick lookup (Vant 4)

| Style aspect | .pen property | Vant common values |
|--------------|---------------|---------------------|
| Background | `fill` | `#f7f8fa` / `#ffffff` / `#1989fa` |
| Text | `fill` (text) | `#323233` / `#969799` / `#1989fa` |
| Field/Cell | fill, padding, stroke bottom, height | #fff, [12,16], #ebedf0 1px, 44 |
| Primary button | fill, height, cornerRadius, text | #1989fa, 44, 8, 16px #fff |
| CellGroup card | fill, cornerRadius, padding | #fff, 8, 12–16 |
| NavBar | fill, height, stroke bottom, title 16px | #fff, 46, #ebedf0 1px |
| Divider | fill | #ebedf0, height 1 |

---

## 14. Component semantics table

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input / field (van-field)** | `#ffffff` | 12 16 | 0 | 1 bottom `#ebedf0` | 44 | 14px `#323233`; placeholder `#c8c9cc` | 375 mobile base |
| **Primary button (van-button)** | `#1989fa` | 0 16 | 8 | — | 44 | 16px `#ffffff` | block = full width |
| **Cell (van-cell)** | `#ffffff` | 12 16 | 0 | 1 bottom `#ebedf0` | 44 | Title 14px `#323233`; value 14px `#969799` | |
| **Cell Group card style** | `#ffffff` | 0 | 8 | — | fit_content | — | inset style |
| **Divider** | — | — | — | — | 1 | — | fill `#ebedf0` |
| **NavBar** | `#ffffff` | 0 16 | 0 | 1 bottom `#ebedf0` | 46 | 16px `#323233`; icon 22×22 | height 46px |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-vue-vant-components → **pencil-ui-design-system-vant** (.pen refs: van-*). Ensure the .pen has this design system initialized; use **refs** for cell-group, field, card, nav-bar, tabs, button.

**Tokens:** See section 12.

**Constraints (align with stitch-vue-vant-components):**
- **Card-like section:** Use **van-cell-group** ref with inset for card style; rows as **van-cell** refs. Do not use raw div.card.
- **Form row / hint:** Use **van-field** ref (label, placeholder, rules). Do not use raw label + input.
- **Product card:** Use **van-card** ref (thumb, title, price, desc).
- **NavBar / Tabs / Button:** Use **van-nav-bar**, **van-tabs**, **van-button** refs.

**batch_design conventions:** Section: `I(main, { type: "ref", ref: "van-cell-group-inset-id" })` then `I(cellGroup, { type: "ref", ref: "van-cell-id", descendants: { "titleId": { content: "Label" }, "valueId": { content: "Value" } } })`. Form: insert **van-field** refs with label and placeholder.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md).
