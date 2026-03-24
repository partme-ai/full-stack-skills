# Bootstrap (Vue 3) → Pencil .pen Style Mapping

When **pencil-design-from-stitch-html** target framework is **Bootstrap / BootstrapVue Next** (stitch-vue-bootstrap-components, pencil-ui-design-system-bootstrap), use this doc to map Stitch HTML / Tailwind to Pencil .pen node properties. Bootstrap uses 0.375rem (6px) radius, 16px base font.

Generic mapping: [tailwind-to-pencil-styles.md](tailwind-to-pencil-styles.md). Component semantics: sections 0 and 14 in this doc.

---

## 0. Component → Pencil mapping

Each row gives **official doc link**, **key API (size/layout)**, and **Pencil .pen properties**. Bootstrap 5 docs: <https://getbootstrap.com/docs/5.3/>; Vue 3 wrappers: BootstrapVue Next.

| Component | Official doc | Key API (size/layout) | Pencil node type | Pencil mapping (width, height, fill, padding, cornerRadius, stroke, text) |
|-----------|--------------|------------------------|------------------|----------------------------------------------------------------------------|
| **Button** | [Bootstrap Buttons](https://getbootstrap.com/docs/5.3/components/buttons/) | Height from padding-y + font-size, ~2.375rem (38px); radius 0.375rem (6px) | frame or ref | height **38**, padding `[6,12]` (0.375rem 1rem), cornerRadius **6**; primary fill `#0d6efd`; text 16px (1rem) `#ffffff`. |
| **Form control** | [Bootstrap Forms](https://getbootstrap.com/docs/5.3/components/forms/) | Same height as button 38px; padding 0.375rem 0.75rem; border 1px solid #dee2e6 | frame or ref | height **38**, padding `[6,12]`, fill `#ffffff`, stroke 1px `#dee2e6`, cornerRadius **6**; text 16px `#212529`, placeholder `#6c757d`. |
| **Card** | [Bootstrap Card](https://getbootstrap.com/docs/5.3/components/card/) | Padding 1rem (16px); radius 0.375rem; border or shadow | frame or ref | width fill_container, padding **24** (1.5rem), cornerRadius **6**, fill `#ffffff`; stroke 1px `#dee2e6` or light shadow. |
| **Alert** | [Bootstrap Alerts](https://getbootstrap.com/docs/5.3/components/alerts/) | padding 1rem 1.5rem; radius 0.375rem; type sets bg | frame or ref | padding **12**–16, cornerRadius **6**; info fill `#cff4fc`, text `#055160`. |
| **Input group** | [Bootstrap Input group](https://getbootstrap.com/docs/5.3/components/input-group/) | Same height as form control 38; addon same height | frame horizontal; input and button height **38**, stroke 1px `#dee2e6`. | Same. |
| **Nav** | [Bootstrap Nav](https://getbootstrap.com/docs/5.3/components/nav/) | Tabs as flex; item padding | frame horizontal gap 0; item padding `[8,16]`; active border-bottom or fill. | Same. |

**Note:** Bootstrap uses 1rem=16px, 0.375rem=6px; control height 2.375rem ≈ 38px. Use table for height, padding, cornerRadius, stroke.

---

## 1. Scale convention

- **Bootstrap:** 1rem = 16px; control height ~38px (2.375rem); radius 0.375rem = 6px.
- **Pencil:** Use **px** for all dimensions.

---

## 2. Background (fill)

| Semantic / scenario | .pen property | Value |
|---------------------|---------------|--------|
| Page background | `fill` | `"#ffffff"` or `"#f8f9fa"` |
| Card (b-card) | `fill` | `"#ffffff"` |
| Primary button (btn-primary) | `fill` | `"#0d6efd"` |
| Input | `fill` | `"#ffffff"` |
| Alert info | `fill` | `"#cff4fc"` |
| Divider | `fill` | `"#dee2e6"` |

---

## 3. Color (text and borders)

| Usage | .pen value |
|-------|------------|
| Primary text | `"#212529"` |
| Body | `"#212529"`, `"#6c757d"` |
| Placeholder / hint | `"#6c757d"` |
| Primary / link | `"#0d6efd"` |
| Button text (on primary) | `"#ffffff"` |
| Border | `"#dee2e6"` |
| Alert text | `"#055160"` (info) |

---

## 4. Size (width, height)

| Semantic | .pen property | Value (px) |
|----------|---------------|------------|
| Full width | `width` | `"fill_container"` |
| Input / button | `height` | 38 |
| Icon | width/height | 16, 20, 24 |

---

## 5. Margin / spacing

- Use parent **gap**; Bootstrap typical 8, 12, 16, 24 (0.5rem–1.5rem).
| Scenario | .pen approach |
|----------|----------------|
| Form items / inside card | Parent frame `gap: 16`, `gap: 24` |

---

## 6. Padding

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Card (b-card) | `padding` | 24 |
| Input | `padding` | `[8, 12]` |
| Button | `padding` | `[0, 12]` |
| Alert | `padding` | `[12, 16]` |

---

## 7. Gap (flex)

| Scenario | Value (px) |
|----------|------------|
| Form items / blocks | 12, 16, 24 |

---

## 8. Shadow

| Scenario | .pen approach |
|----------|----------------|
| Card | Bootstrap light shadow; blur 6–8, offset y 2, rgba(0,0,0,0.075) or omit |

---

## 9. Border radius (cornerRadius)

| Scenario | .pen property | Value (px) |
|----------|---------------|------------|
| Input / button / card / Alert | `cornerRadius` | 6 |
| Large radius | `cornerRadius` | 8, 12 |

---

## 10. Border (stroke)

| Scenario | .pen property | Value |
|----------|----------------|------|
| Input / card | `stroke` | `{ align: "inside", fill: "#dee2e6", thickness: 1 }` |
| Divider | frame height 1 | fill `"#dee2e6"` |
| Alert | `stroke.fill` | `"#0dcaf0"` light |

---

## 11. Typography

| Usage | fontSize (px) | fontWeight | fill |
|-------|---------------|------------|------|
| Heading | 16, 18, 20 | "600" | "#212529" |
| Body / input | 16 | "400" | "#212529" |
| Hint / placeholder | 14, 16 | "400" | "#6c757d" |
| Primary button | 16 | "500" | "#ffffff" |
| Link | 16 | "400" | "#0d6efd" |

---

## 12. Bootstrap design tokens

| Token | Pencil value |
|-------|--------------|
| Primary | `#0d6efd` |
| Background | `#ffffff`, `#f8f9fa` |
| Border | `#dee2e6` |
| Text | `#212529` |
| Text muted | `#6c757d` |
| Radius | 6 (0.375rem) |
| Input/button height | 38 |

---

## 13. Quick lookup (Bootstrap)

| Style aspect | .pen property | Bootstrap common values |
|--------------|---------------|--------------------------|
| Background | `fill` | `#ffffff` / `#0d6efd` |
| Text | `fill` (text) | `#212529` / `#6c757d` / `#0d6efd` |
| Input | fill, padding, stroke, height, cornerRadius | #fff, [8,12], #dee2e6 1px, 38, 6 |
| Primary button | fill, height, cornerRadius, text | #0d6efd, 38, 6, 16px #fff |
| Card | fill, padding, cornerRadius | #fff, 24, 6 |
| Divider | fill | #dee2e6, height 1 |

---

## 14. Component semantics table

| Component semantic | fill | padding | cornerRadius | stroke | height/width | Text fontSize / fill | Notes |
|--------------------|------|---------|--------------|--------|--------------|----------------------|-------|
| **Input (b-form-input)** | `#ffffff` | 8 12 | 6 | 1px `#dee2e6` | 38 | 16px `#212529`; placeholder `#6c757d` | 0.375rem radius |
| **Primary button (b-button)** | `#0d6efd` | 0 12 | 6 | — | 38 | 16px `#ffffff` | btn-primary |
| **Card (b-card)** | `#ffffff` | 24 | 6 | 1px `#dee2e6` | fit_content | Title 16px `#212529` | 0.375rem |
| **Alert (b-alert)** | `#cff4fc` (info) | 12 16 | 6 | 1 `#0dcaf0` light | fit_content | 14px `#055160` | variant=info |
| **Divider** | — | — | — | — | 1 | — | fill `#dee2e6` |

---

## 15. Pencil design system and constraints

**Mapping:** stitch-vue-bootstrap-components → **pencil-ui-design-system-bootstrap** (.pen refs: b-*). Ensure the .pen has this design system initialized; use **refs** for card, alert, button, form, table.

**Tokens:** See section 12.

**Constraints (align with stitch-vue-bootstrap-components):**
- **Card / section:** Use **b-card** ref (title or #header slot). Do not use raw frame with custom header.
- **Tips / notice:** Use **b-alert** ref (variant=info or warning). Do not use raw div + .tips-text.
- **Form hints:** Use **b-form-group** description or label slot when ref exists.
- **Button / Table / Form:** Use **b-button**, **b-table**, **b-form-*** refs.

**batch_design conventions:** Section: `I(main, { type: "ref", ref: "b-card-id", descendants: { "titleSlot": { content: "Basic Info" } } })`. Alert below upload: insert **b-alert** ref with variant info or warning.

Use with [html-to-pencil-mapping.md](html-to-pencil-mapping.md).
