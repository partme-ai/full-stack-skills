# Layui-Vue → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **Layui-Vue** (stitch-vue-layui-components, pencil-ui-design-system-layui), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties. Layui uses minimal styling: radius 2px or 4px only, primary #16baaa.

Generic mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. Layui-Vue docs: <https://layui-vue.gitee.io/> or <https://layui.dev/>.

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [Layui-Vue Button](https://layui-vue.gitee.io/zh/component/button.html) | size default/lg/sm; type primary/default; radius 2px or 4px | frame or ref | height **38**, padding `[0,16]`, cornerRadius **2** or **4**; primary fill `#16baaa`; text 14px `#ffffff`. |
| **Input** | [Layui-Vue Input](https://layui-vue.gitee.io/zh/component/input.html) | height ~38 (same as button); border, radius 2/4px | frame or ref | height **38**, padding `[8,12]`, fill `#ffffff`, stroke 1px `#e2e2e2`, cornerRadius **2** or **4**; text 14px `#303133`, placeholder `#909399`. |
| **Card** | [Layui-Vue Card](https://layui-vue.gitee.io/zh/component/card.html) | padding, radius, minimal shadow | frame or ref | width fill_container, padding **16**, cornerRadius **2** or **4**, fill `#ffffff`; optional 1px stroke `#e2e2e2`. |
| **Form** | [Layui-Vue Form](https://layui-vue.gitee.io/zh/component/form.html) | label position, spacing | parent frame vertical gap 12–16; label 14px `#303133`; controls per Input mapping. | Same. |
| **Divider** | [Layui-Vue Divider](https://layui-vue.gitee.io/zh/component/divider.html) | horizontal/vertical; optional text | line: height 1, fill `#e2e2e2`; text 12px `#909399`. | Same. |
| **Table** | [Layui-Vue Table](https://layui-vue.gitee.io/zh/component/table.html) | row height, border, header bg | frame table layout; header fill `#fafafa`, stroke 1px `#e2e2e2`; row height ~40, text 14px. | Same. |

**Note:** Layui-Vue uses radius **2 or 4 only**, control height ~38px, primary #16baaa. Use table above for height, cornerRadius, stroke; refer to official API for details.

---

## 1. Scale convention

- **Layui-Vue:** 14px font, 38px control height; radius strictly 2px or 4px.
- **Pencil:** Use **px** for all dimensions.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#ffffff"` or `"#f6f6f6"` |
| Card (lay-card) | `fill` | `"#ffffff"` |
| Primary button | `fill` | `"#16baaa"` |
| Input | `fill` | `"#ffffff"` |
| Divider | `fill` | `"#e2e2e2"` |

---

## 3. Color (text and borders)

| Usage | .pen value |
|-------|------------|
| Primary text | `"#303133"` |
| Secondary / placeholder | `"#909399"` |
| Primary / link | `"#16baaa"` |
| Button text (on primary) | `"#ffffff"` |
| Border | `"#e2e2e2"` |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input / button | `height` | 38 |
| Icon | width/height | 16, 20 |

---

## 5. Margin / spacing

- Use parent **gap**; Layui typical 12, 16.
| Scenario | .pen approach |
|----------|----------------|
| Form items / blocks | Parent frame `gap: 12`, `gap: 16` |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Card | `padding` | 16 |
| Input | `padding` | `[8, 12]` |
| Button | `padding` | `[0, 16]` |

---

## 7. Gap (flex)

| Scenario | Value (px) |
|----------|------------|
| Form items / blocks | 12, 16 |

---

## 8. Shadow

- Layui uses little shadow; cards often use border only. Omit or very light shadow.

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Input / button / card | `cornerRadius` | 2 or 4 (**only these two**) |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Input / card | `stroke` | `{ align: "inside", fill: "#e2e2e2", thickness: 1 }` |
| Divider (lay-divider) | frame height 1 | fill `"#e2e2e2"` |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| Heading | 14, 16 | "600" | "#303133" |
| Body / input | 14 | "400" | "#303133" |
| Hint | 12, 14 | "400" | "#909399" |
| Primary button | 14 | "500" | "#ffffff" |
| Link | 14 | "400" | "#16baaa" |

---

## 12. Layui-Vue design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#16baaa` |
| Background | `#ffffff`, `#f6f6f6` |
| Border | `#e2e2e2` |
| Text | `#303133` |
| Text secondary | `#909399` |
| Radius | **2 or 4 only** |
| Input/button height | 38 |

---

## 13. Quick lookup (Layui-Vue)

| Style aspect | .pen property | Layui common values |
|--------------|---------------|---------------------|
| Background | `fill` | `#ffffff` / `#16baaa` |
| Text | `fill` (text) | `#303133` / `#909399` / `#16baaa` |
| Input | fill, padding, stroke, height, cornerRadius | #fff, [8,12], #e2e2e2 1px, 38, 4 |
| Primary button | fill, height, cornerRadius, text | #16baaa, 38, 4, 14px #fff |
| Card | fill, padding, cornerRadius | #fff, 16, 4 |
| Divider | fill | #e2e2e2, height 1 |

---

## 14. Component semantics table

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input (lay-input)** | `#ffffff` | 8 12 | 4 | 1px `#e2e2e2` | 38 | 14px `#303133`; placeholder `#909399` | radius 2px/4px only |
| **Primary button (lay-button)** | `#16baaa` | 0 16 | 4 | — | 38 | 14px `#ffffff` | flat |
| **Card (lay-card)** | `#ffffff` | 16 | 4 | 1px `#e2e2e2` | fit_content | 14px `#303133` | minimal |
| **Divider (lay-divider)** | — | — | — | — | 1 | — | fill `#e2e2e2` |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-vue-layui-components → **pencil-ui-design-system-layui** (.pen refs: lay-*). Ensure the .pen has this design system initialized; use **refs** for card, divider, button, input.

**Tokens:** See section 12.

**Constraints (align with stitch-vue-layui-components):**
- **Card / section:** Use **lay-card** ref. Do not use raw div.card.
- **Divider:** Use **lay-divider** ref. Do not use only view + border.
- **Button / Input:** Use **lay-button**, **lay-input** refs. Flat, minimalist; radius 2px/4px only.

**batch_design conventions:** Section: `I(main, { type: "ref", ref: "lay-card-id", descendants: { "headerId": { content: "Basic Info" } } })`. Divider between blocks: insert **lay-divider** ref.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md).
