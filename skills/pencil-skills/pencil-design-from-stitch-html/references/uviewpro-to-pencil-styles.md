# uView Pro → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **uView Pro** (stitch-uviewpro-components, pencil-ui-design-system-uviewpro), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties. uView Pro uses rpx (750 design width); write px in Pencil, 1px ≈ 2rpx for reference.

Generic mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. uView Pro docs: <https://uviewpro.cn/zh/guide/intro.html>; components: <https://uviewpro.cn/zh/components/intro.html>.

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [uView Pro Button](https://uviewpro.cn/zh/components/button.html) | size large/default/small; shape square/circle; type primary/default | frame or ref | Primary: height **48**, fill `#3c9cff`, padding `[0,16]`, cornerRadius **24** (circle); text 16px `#ffffff`. |
| **Input** | [uView Pro Input](https://uviewpro.cn/zh/components/input.html) | border style, radius, placeholder color; height by padding + font | frame or ref | width fill_container, height **44**, fill `#ffffff`, padding **12**, cornerRadius **4**, stroke 1px `#e5e7eb`; text 14px `#303133`, placeholder `#c0c4cc`. |
| **Cell** | [uView Pro Cell](https://uviewpro.cn/zh/components/cell.html) | left title, right value/arrow; bottom divider | frame or ref | width fill_container, height **44**–52, padding `[12,16]`, stroke bottom 1px `#e5e7eb`; title 14px `#303133`, value 14px `#606266`. |
| **Card** | [uView Pro Card](https://uviewpro.cn/zh/components/card.html) | padding, radius, shadow | frame or ref | width fill_container, padding **16**, cornerRadius **8**, fill `#ffffff`; optional shadow. |
| **Navbar** | [uView Pro Navbar](https://uviewpro.cn/zh/components/navbar.html) | height ~44–48; left/center/right slots | frame or ref | height **44**–48, padding `[0,16]`, fill `#ffffff`, stroke bottom 1px `#e5e7eb`; title 16px `#303133`; icon 24×24. |
| **Section** | [uView Pro Section](https://uviewpro.cn/zh/components/section.html) | title row height, left/right padding | frame | height **48**, padding **16**; title 16px `#303133`. |
| **Divider** | [uView Pro Divider](https://uviewpro.cn/zh/components/divider.html) | line height, color, optional text | frame or text | Line: height 1, fill `#e5e7eb`; text 12px `#909399`. |
| **Form** | [uView Pro Form](https://uviewpro.cn/zh/components/form.html) | label–input spacing, required asterisk | parent frame vertical gap 12–16; label 14px; input per Input mapping. | Same. |

**Note:** Official `size`, `shape`, `border` affect height and radius; use table for height, cornerRadius, stroke. If .pen uses pencil-ui-design-system-uviewpro, prefer **ref** then override descendants per table.

---

## 1. Scale convention

- **uView Pro:** 750 design width, 1px ≈ 2rpx (e.g. 16px → 32rpx, 14px → 28rpx).
- **Pencil:** Use **px** for layout and font; variables e.g. `$--primary` when .pen has them.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#f5f6fa"` |
| Card / white block | `fill` | `"#ffffff"` |
| Primary / primary button | `fill` | `"#3c9cff"` |
| Input | `fill` | `"#ffffff"` |
| Divider | `fill` | `"#e5e7eb"` |

---

## 3. Color (text and borders)

| Usage | .pen value |
|-------|------------|
| Primary text | `"#303133"` |
| Secondary | `"#606266"` |
| Hint / optional | `"#909399"`; placeholder `"#c0c4cc"` |
| Link / primary | `"#3c9cff"` |
| Button text (on primary) | `"#ffffff"` |
| Border | `"#e5e7eb"` |
| Icon | `"#909399"` |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input height | `height` | 44 |
| Primary button height | `height` | 48 |
| Icon header | width/height | 24 |
| Icon inside input | width/height | 20 |
| Section title row | height | 48 |

---

## 5. Margin / spacing

- Use parent **gap**; uView Pro typical 16, 24, 32 (32rpx, 48rpx, 64rpx).
| Scenario | .pen approach |
|----------|----------------|
| Inside card blocks | Parent frame `gap: 16` |
| Form items | Parent frame `gap: 12` or `gap: 16` |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Page left/right | `padding` | 16 |
| Card (u-card) | `padding` | 16 |
| Input inner | `padding` | 12 |
| Primary button | `padding` | `[0, 16]` |
| Section row | `padding` | 16 |

---

## 7. Gap (flex)

| Scenario | Value (px) |
|----------|------------|
| Form items / between blocks | 12, 16, 24 |

---

## 8. Shadow

| Scenario | .pen approach |
|----------|----------------|
| Card | shadow-sm: blur 8, offset y 2, rgba(0,0,0,0.04); omit if no effect support |

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Input | `cornerRadius` | 8 |
| Card | `cornerRadius` | 12 |
| Primary button pill | `cornerRadius` | 24 |
| Round icon button | `cornerRadius` | 20 |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Input | `stroke` | `{ align: "inside", fill: "#e5e7eb", thickness: 1 }` |
| Section bottom divider | `stroke.thickness` | `{ bottom: 1 }`, fill `"#e5e7eb"` |
| Divider (u-line) | frame height 1 | fill `"#e5e7eb"` |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| Page / card title | 16, 20 | "600" | "#303133" |
| Section title | 15 | "500" | "#303133" |
| Body / input | 14 | "400" | "#303133" |
| Hint / optional | 12 | "400" | "#909399" |
| Primary button | 16 | "500" | "#ffffff" |
| Link | 14 | "400" | "#3c9cff" |

---

## 12. uView Pro design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#3c9cff` |
| Page background | `#f5f6fa` |
| Card background | `#ffffff` |
| Border | `#e5e7eb` |
| Text primary | `#303133` |
| Text secondary | `#606266` |
| Text hint | `#909399` |
| Placeholder | `#c0c4cc` |
| Radius input | 8 |
| Radius card | 12 |
| Input height | 44 |
| Button height | 48 |

---

## 13. Quick lookup (uView Pro)

| Style aspect | .pen property | uView Pro common values |
|--------------|---------------|--------------------------|
| Background | `fill` | `#f5f6fa` / `#ffffff` / `#3c9cff` |
| Text | `fill` (text) | `#303133` / `#606266` / `#909399` / `#3c9cff` |
| Input | fill, padding, stroke, height, cornerRadius | #fff, 12, #e5e7eb 1px, 44, 8 |
| Primary button | fill, height, cornerRadius, text | #3c9cff, 48, 24, 16px #fff |
| Card | fill, padding, cornerRadius | #fff, 16, 12 |
| Divider | fill | #e5e7eb, height 1 |

---

## 14. Component semantics table

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input (u-input)** | `#ffffff` | 12 | 8 | 1px `#e5e7eb` | 44 | 14px `#303133`; placeholder `#c0c4cc` | Icon 20×20 `#909399`; 750 rpx base |
| **Primary button (u-button)** | `#3c9cff` | 0 16 | 24 (pill) | — | 48 | 16px `#ffffff` | round full |
| **Card (u-card)** | `#ffffff` | 16 | 12 | — | fit_content | Title 16px `#303133` | shadow-sm optional |
| **Section title row** | `#ffffff` | 16 | 0 | 1 bottom `#e5e7eb` | 48 | Left 15px `#303133`; right slot | u-section ref |
| **Form item (u-form-item)** | — | 12 0 | 0 | — | 32–44 | label 14px `#303133`; hint 12px `#909399` | |
| **Divider (u-line)** | — | — | — | — | 1 | — | fill `#e5e7eb` or ref |
| **Hint (u-text type=info)** | — | — | — | — | — | 12px `#909399` | Optional, description |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-uviewpro-components → **pencil-ui-design-system-uviewpro** (.pen refs: u-*). Ensure the .pen has this design system initialized; use **refs** for card, section, hints, divider, button, input, tabs.

**Tokens:** See section 12.

**Constraints (align with stitch-uviewpro-components):**
- **Card / section:** Use **u-card** ref with title prop (or slot); for “title + right content” use **u-card** + **u-section** ref with #right slot. Do not use raw frame + text for card header.
- **Label hints / tips:** Use **u-text** ref with type="info" or type="warning", size 24. Do not use raw text for (选填), (前端显示), (0为不限).
- **Divider:** Use **u-line** or **u-divider** ref. Do not use only view + border.
- **Tabs:** Use **u-tabs** ref; do not draw custom tab buttons.
- **Form:** Use **u-form-item** + **u-input** / **u-number-box** / **u-switch** / **u-radio-group** refs where available.

**batch_design conventions:** Card: `I(main, { type: "ref", ref: "u-card-id", descendants: { "titleId": { content: "Basic Info" } } })`. Section with right widget: insert **u-section** ref, set title and #right slot. Hint: **u-text** ref with type="info", size=24.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md).
