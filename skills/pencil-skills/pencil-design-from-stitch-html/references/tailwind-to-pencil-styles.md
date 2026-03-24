# Tailwind → Pencil .pen Style Mapping

This document defines the **exact mapping** from Stitch HTML Tailwind classes to Pencil .pen node properties. Use it to achieve 100% precise correspondence for **background, color, size, margin, padding, shadow, border-radius**, and typography.

**Target framework:** When a target framework is set (uView 2, uView Pro, Bootstrap, Element Plus, Layui, Vant), prefer that framework’s **tokens** and **refs** from its **\*-to-pencil-styles.md** ([uview](uview-to-pencil-styles.md), [uviewpro](uviewpro-to-pencil-styles.md), [element](element-to-pencil-styles.md), [bootstrap](bootstrap-to-pencil-styles.md), [layui](layui-to-pencil-styles.md), [vant](vant-to-pencil-styles.md)) sections 12 (tokens) and 15 (design system and constraints), and sections 0 and 14 for component-level styles. See also section 15–16 below. When no target is set, use only the generic tables below.

---

## 1. Scale convention

- **Tailwind default:** `1` = 0.25rem = 4px.
- **Pencil:** Use numeric **px** for layout (padding, gap, width, height, fontSize). Design tokens (e.g. `$--background`) can be used when the .pen has variables; otherwise use hex or named colors below.

---

## 2. Background (fill)

| Tailwind class | .pen property | Value |
|----------------|---------------|--------|
| `bg-white` | `fill` | `"#ffffff"` |
| `bg-gray-50` | `fill` | `"#f9fafb"` |
| `bg-gray-100` | `fill` | `"#f3f4f6"` |
| `bg-page`, `bg-background-light` (Stitch token) | `fill` | `"#f5f6fa"` (page bg) |
| `bg-card-light` (Stitch token) | `fill` | `"#ffffff"` (card bg) |
| `bg-primary` | `fill` | `"#1677ff"` or `"#3c9cff"` |
| `bg-red-500` | `fill` | `"#ef4444"` |
| `bg-transparent` | `fill` | omit or transparent |
| Design variable (if .pen has tokens) | `fill` | `"$--background"`, `"$--card"`, `"$--primary"` |

Apply to **frame** nodes (containers). For **text** nodes, use `fill` for text color (see Typography).

---

## 3. Color (text and borders)

| Tailwind class | Usage | .pen value |
|----------------|--------|------------|
| `text-gray-900`, `text-black` | Primary text | `fill: "#303133"` (text node) |
| `text-gray-700`, `text-gray-800` | Secondary heading | `fill: "#374151"` or `"#303133"` |
| `text-gray-600` | Body text | `fill: "#606266"` |
| `text-gray-500`, `text-gray-400` | Hint / optional | `fill: "#909399"` |
| `text-primary` | Links, active tab | `fill: "#1677ff"` |
| `text-red-500` | Error, required asterisk | `fill: "#ef4444"` |
| `text-white` | On primary button | `fill: "#ffffff"` |
| Border color `border-gray-200` | Stroke on frame | `stroke.fill: "#e5e7eb"` |
| `border-gray-300` | Stronger border | `"#d1d5db"` |

---

## 4. Size (width, height)

| Tailwind class | .pen property | Value (px) |
|----------------|---------------|------------|
| `w-full` | `width` | `"fill_container"` |
| `w-10` | `width` | 40 |
| `w-24` | `width` | 96 |
| `w-48` | `width` | 192 |
| `h-6` | `height` | 24 |
| `h-10` | `height` | 40 |
| `h-12` | `height` | 48 |
| `h-24` | `height` | 96 |
| `min-h-screen` | `height` | `"fit_content(844)"` or screen height from get_screen |
| `min-w-*` | `width` | Convert (e.g. min-w-32 → 128) or use fill_container |

Icon size: typically 24×24 for header/tabs; 20 for small buttons.

---

## 5. Margin

Pencil frames use **layout** (vertical/horizontal) and **gap** for spacing between siblings. For “margin” effect:

- **Margin between sections:** Use **gap** on the parent frame (e.g. main has gap 16 → 16px between card1 and card2).
- **Margin on a single node:** If .pen schema supports `margin` on node, map as below; otherwise simulate with padding on parent or extra gap.

| Tailwind class | Effect | .pen approach |
|----------------|--------|----------------|
| `m-2` ~ `m-5` | margin 8–20px | Parent gap or node `margin` if supported (e.g. margin: 8). |
| `mt-2`, `mb-4` | margin-top 8, margin-bottom 16 | `margin: { top: 8 }` or `{ bottom: 16 }` (if schema has margin). |
| `mx-4` | margin left/right 16 | `margin: { left: 16, right: 16 }`. |
| `space-y-4` | 16px between children | Parent frame `gap: 16`. |
| `space-y-6` | 24px between children | Parent frame `gap: 24`. |

When in doubt, use **parent padding + gap** to approximate margin (e.g. main padding 16, gap 16 → first child has “margin” 16 from edges and 16 between siblings).

---

## 6. Padding

| Tailwind class | .pen property | Value (px) |
|----------------|---------------|------------|
| `p-2` | `padding` | 8 |
| `p-3` | `padding` | 12 |
| `p-4` | `padding` | 16 |
| `p-5` | `padding` | 20 |
| `p-6` | `padding` | 24 |
| `p-8` | `padding` | 32 |
| `px-4` | `padding` | `[0, 16]` (top/bottom 0, left/right 16) |
| `py-2` | `padding` | `[8, 0]` |
| `py-4` | `padding` | `[16, 0]` |
| `px-4 py-3` | `padding` | `[12, 16]` (vertical, horizontal) |

Use array form when directions differ: `[top, right, bottom, left]` or `[vertical, horizontal]` per .pen schema.

---

## 7. Gap (flex/grid)

| Tailwind class | .pen property | Value (px) |
|----------------|---------------|------------|
| `gap-1` | `gap` | 4 |
| `gap-2` | `gap` | 8 |
| `gap-3` | `gap` | 12 |
| `gap-4` | `gap` | 16 |
| `gap-5` | `gap` | 20 |
| `gap-6` | `gap` | 24 |
| `gap-8` | `gap` | 32 |
| `space-y-4` | `gap` (on vertical frame) | 16 |
| `space-y-6` | `gap` | 24 |

Apply to **frame** with `layout: "vertical"` or `"horizontal"`.

---

## 8. Shadow

| Tailwind class | .pen approach | Value |
|----------------|---------------|--------|
| `shadow-sm` | `effect` or `shadow` (if schema supports) | Light blur, small offset (e.g. 0 1px 2px rgba(0,0,0,0.05)) |
| `shadow` | Same | 0 1px 3px rgba(0,0,0,0.1) |
| `shadow-md` | Same | 0 4px 6px rgba(0,0,0,0.1) |
| `shadow-soft` (Stitch token) | Same | 0 2px 8px rgba(0,0,0,0.04) |
| `shadow-lg` | Same | 0 10px 15px rgba(0,0,0,0.1) |

If .pen schema uses a single **shadow** or **effect** property, map the Tailwind shadow to that structure (e.g. `{ blur: 8, offset: { x: 0, y: 2 }, color: "rgba(0,0,0,0.04)" }`). If not supported, omit and rely on stroke/border for card separation.

---

## 9. Border radius (cornerRadius)

| Tailwind class | .pen property | Value (px) |
|----------------|---------------|------------|
| `rounded` | `cornerRadius` | 4 |
| `rounded-md` | `cornerRadius` | 6 |
| `rounded-lg` | `cornerRadius` | 8 |
| `rounded-xl` | `cornerRadius` | 12 |
| `rounded-2xl` | `cornerRadius` | 16 |
| `rounded-full` | `cornerRadius` | 9999 (pill/circle) |

Apply to **frame** (cards, buttons, inputs).

---

## 10. Border (stroke)

| Tailwind class | .pen property | Value |
|----------------|---------------|--------|
| `border` | `stroke` | `{ align: "inside", fill: "#e5e7eb", thickness: 1 }` |
| `border-2` | `stroke.thickness` | 2 |
| `border-t` | `stroke.thickness` | `{ top: 1 }` (only top) |
| `border-b` | `stroke.thickness` | `{ bottom: 1 }` |
| `border-dashed` | Stroke style | If schema supports dashed, set; else use solid. |
| `border-gray-200` | `stroke.fill` | `"#e5e7eb"` |
| `border-gray-300` | `stroke.fill` | `"#d1d5db"` |

Use **stroke** on **frame** nodes for input boxes, cards, dividers (height 1 frame with fill or stroke).

---

## 11. Typography

| Tailwind class | .pen property (text node) | Value |
|----------------|----------------------------|--------|
| `text-xs` | `fontSize` | 12 |
| `text-sm` | `fontSize` | 14 |
| `text-base` | `fontSize` | 16 |
| `text-lg` | `fontSize` | 18 |
| `text-xl` | `fontSize` | 20 |
| `text-2xl` | `fontSize` | 24 |
| `font-normal` | `fontWeight` | `"400"` |
| `font-medium` | `fontWeight` | `"500"` |
| `font-semibold` | `fontWeight` | `"600"` |
| `font-bold` | `fontWeight` | `"700"` |
| `text-gray-900` | `fill` | `"#303133"` |
| `text-gray-600` | `fill` | `"#606266"` |
| `text-gray-500` | `fill` | `"#909399"` |
| `font-sans` | `fontFamily` | `"$--font-primary"` or system UI stack |

Apply to **text** nodes. Combine with **content** (innerText from HTML).

---

## 12. Stitch Design Tokens (Common)

| Stitch / Tailwind token | Pencil value |
|--------------------------|--------------|
| Primary | `#1677ff` (fill, text, stroke) |
| Page background | `#f5f6fa` |
| Card background | `#ffffff` |
| Card border | `#e5e7eb`, 1px |
| Text primary | `#303133` |
| Text secondary | `#606266` |
| Text hint | `#909399` |
| Warning / orange | `#f9ae3d` or `#ff976a` |
| Error / red | `#ef4444` or `#ee0a24` |
| Success / green | `#07c160` or `#67c23a` |
| Shadow soft | 0 2px 8px rgba(0,0,0,0.04) |
| Rounded card | cornerRadius 12 (rounded-xl) |

---

## 13. Quick lookup (Tailwind)

| Style aspect | Tailwind example | .pen property | Example value |
|--------------|------------------|---------------|---------------|
| Background | `bg-white`, `bg-card-light` | `fill` | `"#ffffff"` |
| Text color | `text-gray-900`, `text-primary` | `fill` (on text) | `"#303133"`, `"#1677ff"` |
| Width | `w-full`, `w-24` | `width` | `"fill_container"`, 96 |
| Height | `h-12`, `min-h-screen` | `height` | 48, `"fit_content(844)"` |
| Margin | `space-y-4`, `mb-4` | `gap` (parent) or `margin` | 16, `{ bottom: 16 }` |
| Padding | `p-4`, `px-4 py-3` | `padding` | 16, `[12, 16]` |
| Gap | `gap-4`, `space-y-6` | `gap` | 16, 24 |
| Shadow | `shadow-soft`, `shadow-md` | `effect` / `shadow` | 0 2px 8px rgba(0,0,0,0.04) |
| Border radius | `rounded-xl`, `rounded-lg` | `cornerRadius` | 12, 8 |
| Border | `border`, `border-t` | `stroke` | thickness 1, fill #e5e7eb |
| Font size | `text-sm`, `text-lg` | `fontSize` | 14, 18 |
| Font weight | `font-bold`, `font-medium` | `fontWeight` | `"700"`, `"500"` |

---

## 14. Tailwind / HTML → component semantics

When parsing HTML, infer component semantic from classes and tags, then look up the target framework’s **\*-to-pencil-styles.md** (section 14) for exact fill, padding, cornerRadius, stroke, height, fontSize.

| Common Tailwind / HTML pattern | Suggested component semantic | Typical framework |
|--------------------------------|-----------------------------|-------------------|
| `input`, `border rounded-md h-11 px-3` | Input | All |
| Primary `button`, `rounded-full`, full width | Primary button | uView / uView Pro / Vant |
| Primary `button`, small `rounded` | Primary button | Element / Bootstrap / Layui |
| `bg-white rounded-lg p-4 shadow-sm` | Card | All |
| `flex items-center border-b` row | Cell / Section row | uView / uView Pro / Vant |
| `h-[1px] bg-gray-100`, centered “or” text | Divider | All |
| `text-primary text-sm`, “Forgot password” | Link / hint | All |
| `flex gap-6 justify-center` round icon buttons | Third-party login icon buttons | All (size per framework: e.g. uView 40×40 round) |

**Usage:** With a target framework set, (1) resolve component semantic from the table above; (2) open that framework’s *-to-pencil-styles.md and use section 0 (official links) and section 14 (component semantics table) for exact .pen properties; (3) prefer refs when .pen has the design system (section 15), then override descendants per section 14.

---

## 15. Framework ↔ Pencil design system

| Stitch conversion skill | Pencil design system | .pen refs |
|-------------------------|----------------------|-----------|
| stitch-uview-components | pencil-ui-design-system-uview | u-* |
| stitch-uviewpro-components | pencil-ui-design-system-uviewpro | u-* |
| stitch-vue-bootstrap-components | pencil-ui-design-system-bootstrap | b-* |
| stitch-vue-element-components | pencil-ui-design-system-element | el-* |
| stitch-vue-layui-components | pencil-ui-design-system-layui | lay-* |
| stitch-vue-vant-components | pencil-ui-design-system-vant | van-* |

**Rule:** Before generating batch_design, if a target framework is set, ensure the .pen has the corresponding **pencil-ui-design-system-*** initialized (variables + component refs). Use **refs** from that design system instead of raw frame/text where the framework provides a component. Per-framework constraints and batch_design conventions: see that framework’s *-to-pencil-styles.md section 15.

---

## 16. Refs vs primitives by framework

| Target framework | Card/Section | Hints/Tips | Divider | Button | Input/Form |
|------------------|--------------|------------|---------|--------|------------|
| uView 2 | u-cell-group + u-cell or frame+u-text | u-text | u-line / u-divider | u-button | u-input, u-cell |
| uView Pro | u-card, u-section | u-text (type=info/warning) | u-line, u-divider | u-button | u-input, u-form-item |
| Bootstrap | b-card | b-alert | — | b-button | b-form-group, b-form-input |
| Element Plus | el-card | el-alert | — | el-button | el-input, el-form |
| Layui | lay-card | — | lay-divider | lay-button | lay-input |
| Vant | van-cell-group + van-cell | van-field label | — | van-button | van-field |

When **no target framework** is set, use **primitives** (frame, text, icon_font) and this document’s generic tables for layout/style without design-system dependency.

Use this table together with [html-to-pencil-mapping.md](html-to-pencil-mapping.md) and the pencil-design-from-stitch-html [SKILL.md](../SKILL.md) (Execution order and batch split) to produce batch_design operations that match Stitch HTML layout and style with 100% precision.
