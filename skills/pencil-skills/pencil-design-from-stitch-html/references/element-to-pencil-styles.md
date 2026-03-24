# Element Plus → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **Element Plus** (stitch-vue-element-components, pencil-ui-design-system-element), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties. Element default sizes are compact (e.g. input 32px height), suited for admin/desktop.

Generic mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. Element Plus docs: <https://element-plus.org/zh-CN/>; component list in left nav.

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [Element Plus Button](https://element-plus.org/zh-CN/component/button.html) | size large/default/small; type; round, circle | frame or ref | default: height **32**, fill `#409EFF`, padding `[0,16]`, cornerRadius **4**; large height **40**; small height **24**; text 14px `#ffffff`. |
| **Input** | [Element Plus Input](https://element-plus.org/zh-CN/component/input.html) | size large/default/small; prefix/suffix slots; height bound to size | frame or ref | default: height **32**, fill `#ffffff`, padding `[8,12]`, stroke 1px `#dcdfe6`, cornerRadius **4**; large 40; small 24; text 14px `#303133`, placeholder `#c0c4cc`. |
| **Card** | [Element Plus Card](https://element-plus.org/zh-CN/component/card.html) | header/body slots; padding | frame or ref | width fill_container, padding **20**, cornerRadius **4**, fill `#ffffff`; header padding 18–20. |
| **Form** | [Element Plus Form](https://element-plus.org/zh-CN/component/form.html) | label width, label-position, spacing | parent frame vertical gap 12–16; label 14px `#606266`; controls per Input/Select mapping. | Same. |
| **Alert** | [Element Plus Alert](https://element-plus.org/zh-CN/component/alert.html) | type success/warning/info/error; padding | frame or ref | padding **12**, cornerRadius **4**; info fill `#ecf5ff`, text `#409EFF`; success fill `#f0f9eb`; error fill `#fef0f0`. |
| **Divider** | [Element Plus Divider](https://element-plus.org/zh-CN/component/divider.html) | horizontal/vertical; optional text | line: height 1, fill `#e4e7ed`; with text: center text 14px `#909399`. | Same. |
| **Table** | [Element Plus Table](https://element-plus.org/zh-CN/component/table.html) | row height, border, header bg | frame table layout; header height ~48, fill `#fafafa`, stroke 1px `#e4e7ed`; row height ~48, text 14px. | Same. |

**Note:** Official `size` maps directly to control height (large 40, default 32, small 24). Use table for height, padding, cornerRadius.

---

## 1. Scale convention

- **Element Plus:** Default 14px font, 32px control height; spacing typical 8, 12, 16, 20.
- **Pencil:** Use **px** for all dimensions.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#f5f7fa"` or `"#ffffff"` |
| Card (el-card) | `fill` | `"#ffffff"` |
| Primary button | `fill` | `"#409EFF"` |
| Input | `fill` | `"#ffffff"` |
| Alert info | `fill` | `"#ecf5ff"` |
| Divider | `fill` | `"#e4e7ed"` |

---

## 3. Color (text and borders)

| Usage | .pen value |
|-------|------------|
| Primary text | `"#303133"` |
| Regular | `"#606266"` |
| Secondary / placeholder | `"#909399"`, placeholder `"#c0c4cc"` |
| Primary / link | `"#409EFF"` |
| Error | `"#f56c6c"` |
| Button text (on primary) | `"#ffffff"` |
| Border | `"#dcdfe6"` / `"#e4e7ed"` |
| Icon | `"#909399"` |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input (default) | `height` | 32 |
| Primary button | `height` | 32 |
| Large control | `height` | 40 |
| Icon | width/height | 16, 18, 20 |

---

## 5. Margin / spacing

- Use parent **gap**; Element typical 8, 12, 16, 20.
| Scenario | .pen approach |
|----------|----------------|
| Between form items | Parent frame `gap: 12` or `gap: 16` |
| Inside card | Parent frame `gap: 16`, `gap: 20` |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Card (el-card) | `padding` | 20 |
| Input inner | `padding` | `[8, 12]` |
| Button | `padding` | `[0, 16]` |
| Alert | `padding` | 12 |

---

## 7. Gap (flex)

| Scenario | Value (px) |
|----------|------------|
| Form items | 12, 16, 20 |
| Blocks | 16, 20, 24 |

---

## 8. Shadow

| Scenario | .pen approach |
|----------|----------------|
| Card | Element default light shadow; blur 4–8, offset y 1–2, rgba(0,0,0,0.08) or omit |

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Input / button / card | `cornerRadius` | 4 |
| Large radius | `cornerRadius` | 8 |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Input | `stroke` | `{ align: "inside", fill: "#dcdfe6", thickness: 1 }` |
| Divider | frame height 1 | fill `"#e4e7ed"` |
| Alert border | `stroke.fill` | `"#409EFF"` light |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| Heading | 16, 18 | "600" | "#303133" |
| Body / input | 14 | "400" | "#303133" |
| Hint / description | 12, 14 | "400" | "#909399" |
| Primary button | 14 | "500" | "#ffffff" |
| Link | 14 | "400" | "#409EFF" |

---

## 12. Element Plus design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#409EFF` |
| Page/card background | `#ffffff`, `#f5f7fa` |
| Border | `#dcdfe6` / `#e4e7ed` |
| Text primary | `#303133` |
| Text regular | `#606266` |
| Text secondary | `#909399` |
| Placeholder | `#c0c4cc` |
| Radius | 4 |
| Input/button height (default) | 32 |

---

## 13. Quick lookup (Element Plus)

| Style aspect | .pen property | Element common values |
|--------------|---------------|------------------------|
| Background | `fill` | `#ffffff` / `#409EFF` |
| Text | `fill` (text) | `#303133` / `#606266` / `#409EFF` |
| Input | fill, padding, stroke, height, cornerRadius | #fff, [8,12], #dcdfe6 1px, 32, 4 |
| Primary button | fill, height, cornerRadius, text | #409EFF, 32, 4, 14px #fff |
| Card | fill, padding, cornerRadius | #fff, 20, 4 |
| Divider | fill | #e4e7ed, height 1 |

---

## 14. Component semantics table

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input (el-input)** | `#ffffff` | 8 12 | 4 | 1px `#dcdfe6` | 32 | 14px `#303133`; placeholder `#c0c4cc` | size default |
| **Primary button (el-button)** | `#409EFF` | 0 16 | 4 | — | 32 | 14px `#ffffff` | type=primary |
| **Card (el-card)** | `#ffffff` | 20 | 4 | — | fit_content | Title 16px `#303133` | shadow optional |
| **Form item** | — | 0 0 12 0 | 0 | — | — | label 14px `#303133`; error 12px `#f56c6c` | el-form-item |
| **Divider (el-divider)** | — | — | — | — | 1 | — | fill `#e4e7ed` |
| **Alert (el-alert)** | `#ecf5ff` (info) | 12 | 4 | 1 `#409EFF` light | fit_content | 14px `#409EFF` | type=info |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-vue-element-components → **pencil-ui-design-system-element** (.pen refs: el-*). Ensure the .pen has this design system initialized; use **refs** for card, alerts, button, form, input, table.

**Tokens:** See section 12.

**Constraints (align with stitch-vue-element-components):**
- **Card / section:** Use **el-card** ref (shadow=hover, #header slot if needed). Do not use raw frame for card.
- **Tips / notice:** Use **el-alert** ref (type=info | warning | success). Do not use raw div + .tips-text.
- **Button / Form / Table:** Use **el-button**, **el-form**, **el-input**, **el-table** refs.

**batch_design conventions:** Section: `I(main, { type: "ref", ref: "el-card-id", descendants: { "headerSlot": { content: "Basic Info" } } })`. Alert: insert **el-alert** ref with type and title/content.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md).
