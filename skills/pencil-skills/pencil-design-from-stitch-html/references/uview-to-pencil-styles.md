# uView 2 → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **uView 2** (stitch-uview-components, pencil-ui-design-system-uview), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties so the design matches uView 2 specs.

Generic Tailwind mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. Prefer this table by component, then combine with tokens below.

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [uView 2.0 Button](https://www.uviewui.com/components/button.html) | size large/normal/mini; shape square/circle; default height ~34px, large taller | frame or ref u-button | Primary: width fill_container or fixed, height **44**, fill `#3c9cff`, padding `[0,16]`, cornerRadius **22** (shape=circle); text 16px `#ffffff`. Mini: height ~28. |
| **Input** | [uView 2.0 Input](https://www.uviewui.com/components/input.html) | border surround/bottom/none; shape square/circle; fontSize 15px; color #303133; placeholderStyle #c0c4cc | frame or ref u-input | width fill_container, height **44**, fill `#ffffff`, padding **12**, cornerRadius **4**, stroke 1px `#dadbde`; text fontSize **14**, fill `#303133`; placeholder fill `#c0c4cc`. Prefix/suffix icon 20×20, fill `#909399`. |
| **Cell** | [uView 2.0 Cell](https://www.uviewui.com/components/cell.html) | row height by content + padding; list row, bottom divider | frame or ref u-cell | width fill_container, height **44**–52, padding `[12,16]`, stroke `{ bottom: 1 }` fill `#e5e7eb`; title 14px `#303133`, value 14px `#606266`. |
| **Line** | [uView 2.0 Line](https://www.uviewui.com/components/line.html) | divider; length, color | frame or rectangle | height **1**, width fill_container, fill `#dadbde` or `#e5e7eb`. |
| **Divider** | [uView 2.0 Divider](https://www.uviewui.com/components/divider.html) | optional text (e.g. "or"); line+text+line | parent frame horizontal layout; two frames height 1 fill `#dadbde`; center text 12px `#909399`. | Same. |
| **Navbar** | [uView 2.0 Navbar](https://www.uviewui.com/components/navbar.html) | height ~44px; left slot, title center, right slot | frame | height **44**, padding `[0,16]`, fill `#ffffff`, stroke bottom 1px `#e5e7eb`; title 16px `#303133`; icon 24×24. |
| **Tabs** | [uView 2.0 Tabs](https://www.uviewui.com/components/tabs.html) | bar height ~44; active underline, primary color | frame horizontal; each item frame + text; active text fill `#3c9cff`, stroke bottom 2px. | Same. |
| **Text** | [uView 2.0 Text](https://www.uviewui.com/components/text.html) | type, size control style | text | Primary 14px `#303133`; tips 12px `#909399`; see Typography below. |

**Note:** Official `size` (e.g. Button large/mini), `border` (Input surround/bottom) affect height and border; use table for height, stroke, cornerRadius. If .pen uses pencil-ui-design-system-uview, prefer **ref** then override descendants per table.

---

## 1. Scale convention

- **uView 2:** Design in px; for rpx alignment, 750 design width → 1px ≈ 2rpx (e.g. 16px → 32rpx).
- **Pencil:** Use **px** for width, height, padding, gap, fontSize, cornerRadius; design variables e.g. `$--primary` when available.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#f3f4f6"` |
| Card / white block | `fill` | `"#ffffff"` |
| Primary block / button | `fill` | `"#3c9cff"` |
| Input background | `fill` | `"#ffffff"` |
| Divider | `fill` | `"#dadbde"` or `"#e5e7eb"` |
| Transparent | `fill` | omit or transparent |

---

## 3. Color (text and borders)

| Usage | .pen value (text fill or stroke.fill) |
|-------|----------------------------------------|
| Primary text | `"#303133"` |
| Secondary / description | `"#606266"` |
| Hint / placeholder | `"#909399"`, placeholder `"#c0c4cc"` |
| Link / primary | `"#3c9cff"` |
| Error | `"#ee0a24"` or `"#ef4444"` |
| Success | `"#07c160"` |
| Button text (on primary) | `"#ffffff"` |
| Border default | `"#dadbde"` |
| Border divider | `"#e5e7eb"` |
| Icon secondary | `"#909399"` |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input height | `height` | 44 |
| Primary button height | `height` | 44 |
| Icon header/tab | width/height | 24 |
| Icon inside input | width/height | 20 |
| Round icon button | width/height | 40 |
| Screen root | height | 844 or get_screen value |

---

## 5. Margin / spacing

- Use parent **gap** for spacing; uView typical 8, 12, 16, 24.
| Scenario | .pen approach |
|----------|----------------|
| Between blocks | Parent frame `gap: 16` or `gap: 24` |
| Between form items | Parent frame `gap: 8` or `gap: 12` |
| Inline spacing | Parent frame `gap: 12` |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Page left/right | `padding` | `[0, 16]` or 16 |
| Card inner | `padding` | 16 |
| Input inner | `padding` | 12 |
| Button left/right | `padding` | `[0, 16]` |
| Cell row | `padding` | `[12, 16]` |

---

## 7. Gap (flex)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Between form items | `gap` | 8, 12 |
| Between blocks | `gap` | 16, 24 |
| Title to content | `gap` | 12, 16 |

---

## 8. Shadow

- uView 2 cards often use light shadow; if effect not supported, use stroke to separate.
| Scenario | .pen approach |
|----------|----------------|
| Card | `effect: { type: "shadow", blur: 8, offset: { x: 0, y: 2 }, color: "rgba(0,0,0,0.04)" }` or omit |

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Default / input | `cornerRadius` | 4 |
| Card / block | `cornerRadius` | 8 |
| Primary button pill | `cornerRadius` | 22 |
| Round icon button | `cornerRadius` | 20 |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Input / secondary button | `stroke` | `{ align: "inside", fill: "#dadbde", thickness: 1 }` |
| Cell bottom divider | `stroke.thickness` | `{ bottom: 1 }`, `stroke.fill` `"#e5e7eb"` |
| Divider | frame height 1, fill `"#dadbde"` | — |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| Page title | 18, 20 | "600" | "#303133" |
| Block title | 16 | "600" | "#303133" |
| Body / input | 14 | "400" | "#303133" |
| Hint / secondary | 12 | "400" | "#909399" |
| Primary button | 16 | "500" | "#ffffff" |
| Link | 12, 14 | "400" | "#3c9cff" |

---

## 12. uView 2 design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#3c9cff` |
| Page background | `#f3f4f6` |
| Card background | `#ffffff` |
| Border | `#dadbde` |
| Border light | `#e5e7eb` |
| Text primary | `#303133` |
| Text secondary | `#606266` |
| Text hint | `#909399` |
| Placeholder | `#c0c4cc` |
| Radius default | 4 |
| Radius card | 8 |
| Input/button height | 44 |

---

## 13. Quick lookup (uView 2)

| Style aspect | .pen property | uView 2 common values |
|--------------|---------------|------------------------|
| Background | `fill` | `#f3f4f6` / `#ffffff` / `#3c9cff` |
| Text color | `fill` (text) | `#303133` / `#606266` / `#909399` / `#3c9cff` |
| Input | fill, padding, stroke, height, fontSize | #fff, 12, #dadbde 1px, 44, 14 |
| Primary button | fill, height, cornerRadius, text | #3c9cff, 44, 22, 16px #fff |
| Card | fill, padding, cornerRadius | #fff, 16, 8 |
| Divider | fill or stroke | #dadbde, height 1 |

---

## 14. Component semantics table

Use this table for batch_design: pick component semantic (input, primary button, card, cell, divider, hint), then apply the .pen properties below.

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input (u-input)** | `#ffffff` | 12 | 4 | 1px `#dadbde` | 44 | 14px `#303133`; placeholder `#c0c4cc` | Left icon 20×20, fill `#909399` |
| **Primary button (u-button)** | `#3c9cff` | 0 16 | 22 (pill) | — | 44 | 16px `#ffffff` | type=primary |
| **Secondary button** | transparent | 0 16 | 22 | 1px `#dadbde` | 44 | 14px `#303133` | |
| **Card / block** | `#ffffff` | 16 | 8 | — or 1 `#e5e7eb` | fit_content | Title 16px `#303133` | Use frame when no Card ref |
| **Cell row** | `#ffffff` | 12 16 | 0 | 1 bottom `#e5e7eb` | 44–52 | Title 14px `#303133`, value 14px `#606266` | |
| **Divider** | — | — | — | — | 1 | — | frame height 1, fill `#dadbde` or u-line ref |
| **Hint / secondary text** | — | — | — | — | — | 12px `#909399` | u-text or text node |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-uview-components → **pencil-ui-design-system-uview** (.pen refs: u-*). Ensure the .pen has this design system initialized before generating batch_design; use **refs** instead of raw frame/text where the framework provides a component.

**Tokens:** See section 12.

**Constraints (align with stitch-uview-components):**
- **Card-like section:** No Card in uView 2 → use **u-cell-group** pattern: frame (vertical) + **u-cell** refs for rows, or wrapper frame + **u-text** for section title. Do not draw a generic “card” frame if the design system exposes cell-group.
- **Label hints / tips:** Use **u-text** ref or text node (fontSize 12px for hints).
- **Divider:** Use **u-line** or **u-divider** ref if available; else frame height 1, fill #dadbde.
- **Button / Input / Tabs:** Use **u-button**, **u--input** (or u-input), **u-tabs** when present.

**batch_design conventions:** Prefer `I(parent, { type: "ref", ref: "<componentId>" })` for buttons, inputs, cells, tabs; use `descendants` to override label/content. Section block: insert frame (vertical) then **u-cell** refs as rows, or **u-cell-group** ref if provided.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md) when target is uView 2 for batch_design.
