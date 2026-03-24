# Tailwind → Layui-Vue (Vue 3) Mapping

When converting **Stitch HTML** (Tailwind-based) to Vue 3 + Layui-Vue, map utility classes to **px**, **Layui-Vue theme**, or **component props**. Layui-Vue uses a **minimalist, flat** style: radius **2px or 4px only**; no large rounded corners (8px+). Do not output Tailwind class names in the template unless the project uses Tailwind.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with [contract.md](contract.md).

## Scale convention

- Tailwind default: `1` = 0.25rem = 4px.
- **Layui-Vue**: Spacing 5, 10, 15, 20, 30px (10/15 grid). Font sizes 12, 14, 16, 18, 20, 24, 30px. **Radius: 2px (small), 4px (medium) only.** Border #e2e2e2; focus #16baaa. Buttons: height 38px (normal), 30px (small), 44px (large).

---

## 1. Layout

| Tailwind pattern | Layui-Vue |
|------------------|-----------|
| `flex` | `<div style="display: flex">` or **lay-space** where applicable |
| `flex flex-col` | `flex-direction: column`; or `<lay-space direction="vertical" size="md">` |
| `flex items-center` | `align-items: center` |
| `flex justify-between` | `justify-content: space-between` |
| `grid` | Flex wrap or custom grid; Layui-Vue has no el-row equivalent; use div + flex/grid style |
| `grid grid-cols-2` | Two columns with 50% or flex; gap 10–20px |
| `grid grid-cols-3` | Three columns; gap 10–20px |
| `sticky top-0` | `position: sticky; top: 0`; or **lay-page-header** for page header |
| `sticky top-14` | Second sticky; `top: 56px` |

---

## 2. Spacing

| Tailwind | px | Layui-Vue |
|----------|-----|-----------|
| `p-2` | 8 | 10px (nearest: 10 grid) |
| `p-3` | 12 | 10px or 15px |
| `p-4` | 16 | 15px or 20px |
| `p-5` | 20 | 20px |
| `px-4`, `py-2` | 16, 8 | 20px horizontal; 10px vertical (align to 5/10/15/20) |
| `mb-*`, `gap-*` | — | 10, 15, 20, 30px |
| `space-y-4` | 16 | margin-bottom 15px or 20px; or **lay-space direction="vertical" size="md"** |

Use **10/15/20/30** spacing for consistency.

---

## 3. Sizing

| Tailwind | Layui-Vue |
|----------|-----------|
| `w-full` | width: 100% |
| `w-10`, `w-24` | 40px, 96px |
| `h-6`, `h-10`, `h-24` | 24px, 40px, 96px; buttons: 38px (normal), 30px (sm), 44px (lg) |
| `min-h-*` | min-height in px |

Input height: **38px** per contract.

---

## 4. Typography

| Tailwind | Layui-Vue |
|----------|-----------|
| `text-xs` | 12px |
| `text-sm` | 14px |
| `text-base` | 16px |
| `text-lg` | 18px |
| `font-normal` / `font-medium` / `font-bold` | font-weight: 400 / 500 / 700 (titles 500, body 400) |
| `text-gray-500`, `text-gray-400` | #999, #666 (Layui neutrals) |
| `text-gray-900` | #333 (text) |
| `text-primary` | #16baaa (primary) |
| `placeholder-gray-300` | lay-input placeholder |

---

## 5. Colors (Stitch theme → Layui-Vue)

| Stitch / Tailwind | Layui-Vue |
|-------------------|-----------|
| `primary`, `bg-primary` | #16baaa (primary); use **lay-button type="primary"** |
| `background-light` | #f2f2f2 (bg) |
| `card-light` | #ffffff; card header bg, border-bottom #f6f6f6 |
| `border-light` | #e2e2e2 / #eeeeee |
| `text-red-500` (required) | #FF5722 (danger) or form required |
| `bg-gray-50` | #f2f2f2 |

---

## 6. Borders

| Tailwind | Layui-Vue |
|----------|-----------|
| `border` | border: 1px solid #e2e2e2 |
| `border-b` | border-bottom only |
| `border-0` | border: none |
| `border-2 border-dashed` | 2px dashed (upload) |
| `rounded` | **border-radius: 2px** (Layui small) — do not use 8px |
| `rounded-lg` | **border-radius: 4px** (Layui medium) — do not use 16px |
| `rounded-xl` | **4px max** (Layui does not use large radius) |
| `rounded-full` | 2px or 4px (Layui avoids pill/circle unless requested) |
| `border-gray-200` | #e2e2e2 |

**Invariant**: Radius **2px or 4px only**. No 8px+ rounded corners.

---

## 7. Effects

| Tailwind | Layui-Vue |
|----------|-----------|
| `shadow-sm`, `shadow-soft` | Very subtle or **none** (flat design) |
| `shadow-inner` | Avoid or minimal |
| `shadow-md` | Prefer flat; minimal shadow if needed |

Layui-Vue style: **minimalist, flat, clean**. Avoid heavy shadows.

---

## 8. Interactivity

| Tailwind | Layui-Vue |
|----------|-----------|
| `hover:bg-gray-100` | Table row hover #f8f8f8 per contract; or component hover |
| `focus:ring-1 focus:ring-primary` | lay-input focus border #16baaa; no Tailwind in template |
| `peer` / `peer-checked:` | Use **lay-checkbox**, **lay-radio**; do not use peer |

---

## 9. Icons (Stitch Material → Layui-Vue)

| Stitch / Material | Layui-Vue |
|-------------------|-----------|
| `chevron_left` | lay-page-header @back or icon component |
| `expand_more` | Arrow down icon (Layui icon set) |
| `add` | Plus icon |
| `remove` | Minus icon |
| `add_photo_alternate` | Image/photo icon |

Use Layui-Vue icon props (e.g. **lay-button** `icon`) or project icon set; see [component-index.md](component-index.md).

---

## 10. Do not copy literally

- Do **not** put Tailwind class names in the template unless the project uses Tailwind.
- Do **not** use raw `<button>`, `<input>` — use **lay-button**, **lay-input** per [contract.md](contract.md).
- Do **not** use **rounded-lg / rounded-xl** as 8px+ — use **2px or 4px** only.
- Do convert spacing to **5/10/15/20/30px** and typography to **12/14/16/18/20/24/30px**.

For component API and invariants, use [contract.md](contract.md) and [component-index.md](component-index.md).
