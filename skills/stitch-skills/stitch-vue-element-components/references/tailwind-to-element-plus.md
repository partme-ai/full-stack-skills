# Tailwind → Element Plus (Vue 3) Mapping

When converting **Stitch HTML** (Tailwind-based) to Vue 3 + Element Plus, map utility classes to **rem/px**, **Element Plus theme / CSS variables**, or **component props**. Do not output Tailwind class names in the template unless the project uses Tailwind.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with [contract.md](contract.md).

## Scale convention

- Tailwind default: `1` = 0.25rem = 4px.
- **Element Plus**: Base font 14px; sizes Extra Small 12px, Small 13px, Base 14px, Medium 16px, Large 18px, Extra Large 20px. Radius: 2px (small), 4px (base), 20px/9999px (round). Use **px** or **rem** in style; Element uses CSS vars (--el-color-primary, --el-border-radius-base, etc.).

---

## 1. Layout

| Tailwind pattern | Element Plus |
|------------------|--------------|
| `flex` | `<div style="display: flex">` or el-row with flex (el-row can be flex) |
| `flex flex-col` | `flex-direction: column` in style |
| `flex items-center` | `align-items: center` |
| `flex justify-between` | `justify-content: space-between` |
| `grid` | **el-row** + **el-col** (24-column); use `:gutter="20"` |
| `grid grid-cols-2` | `<el-row :gutter="20"><el-col :span="12">` × 2 |
| `grid grid-cols-3` | `<el-col :span="8">` × 3 |
| `sticky top-0` | `position: sticky; top: 0`; or use el-header in el-container |
| `sticky top-14` | Second sticky; `top: 56px` or 3.5rem |

---

## 2. Spacing

| Tailwind | px | Element Plus |
|----------|-----|--------------|
| `p-2` | 8 | 8px |
| `p-3` | 12 | 12px |
| `p-4` | 16 | 16px |
| `p-5` | 20 | 20px |
| `px-4`, `py-2` | 16, 8 | padding in px |
| `mb-*`, `gap-*` | — | margin-bottom / gap in px (8, 12, 16, 20) |
| `space-y-4` | 16 | margin-bottom 16px on children or gap |

Use **px** or **rem**; Element form/item spacing often 16px–20px.

---

## 3. Sizing

| Tailwind | Element Plus |
|----------|--------------|
| `w-full` | width: 100% |
| `w-10`, `w-24` | 40px, 96px (or el-input width prop where applicable) |
| `h-6`, `h-10`, `h-24` | 24px, 40px, 96px |
| `min-h-*` | min-height in px |

---

## 4. Typography

| Tailwind | Element Plus |
|----------|--------------|
| `text-xs` | 12px (Extra Small) |
| `text-sm` | 13px (Small) or 14px (Base) |
| `text-base` | 14px (default) |
| `text-lg` | 18px (Large) |
| `font-normal` / `font-medium` / `font-bold` | font-weight: 400 / 500 / 700 |
| `text-gray-500`, `text-gray-400` | --el-text-color-secondary #909399, --el-text-color-regular #606266 |
| `text-gray-900` | --el-text-color-primary #303133 |
| `text-primary` | --el-color-primary #409EFF |
| `placeholder-gray-300` | el-input placeholder uses theme |

Use **Element typography**: default body 14px; headings via style or class.

---

## 5. Colors (Stitch theme → Element Plus)

| Stitch / Tailwind | Element Plus |
|-------------------|--------------|
| `primary`, `bg-primary`, `text-primary` | --el-color-primary #409EFF; use type="primary", color="primary" |
| `background-light` | --el-fill-color-blank or #f5f7fa |
| `card-light` | #ffffff; el-card default |
| `border-light` | --el-border-color #DCDFE6 / #E4E7ED |
| `text-red-500` (required) | Use el-form-item required or --el-color-danger #F56C6C |
| `bg-gray-50` | --el-fill-color-light |

---

## 6. Borders

| Tailwind | Element Plus |
|----------|--------------|
| `border` | border: 1px solid var(--el-border-color) |
| `border-b` | border-bottom only |
| `border-0` | border: none |
| `border-2 border-dashed` | 2px dashed (upload area) |
| `rounded` | border-radius: 4px (--el-border-radius-base) |
| `rounded-lg` | 8px or 4px (Element base) |
| `rounded-xl` | 8px–12px |
| `rounded-full` | border-radius: 20px or 9999px (round button) |
| `border-gray-200` | var(--el-border-color-lighter) |

---

## 7. Effects

| Tailwind | Element Plus |
|----------|--------------|
| `shadow-sm` | box-shadow: var(--el-box-shadow-light) or subtle shadow |
| `shadow-soft` (Stitch) | Same; Element card has shadow="hover" / "always" |
| `shadow-inner` | inset shadow |
| `shadow-md` | var(--el-box-shadow) |

Use **el-card** `shadow="hover"` or `shadow="always"` where appropriate.

---

## 8. Interactivity

| Tailwind | Element Plus |
|----------|--------------|
| `hover:bg-gray-100` | el-button, el-table row have hover; or class binding |
| `focus:ring-1 focus:ring-primary` | el-input, el-select have built-in focus (primary border) |
| `peer` / `peer-checked:` | Use **el-switch**, **el-checkbox-group**, **el-radio-group**; do not use peer |

---

## 9. Icons (Stitch Material → Element Plus)

| Stitch / Material | Element Plus |
|-------------------|--------------|
| `chevron_left` | `<el-icon><ArrowLeft /></el-icon>` (@element-plus/icons-vue) |
| `expand_more` | `<el-icon><ArrowDown /></el-icon>` |
| `add` | `<el-icon><Plus /></el-icon>` |
| `remove` | `<el-icon><Minus /></el-icon>` |
| `add_photo_alternate` | `<el-icon><Picture /></el-icon>` or similar |

Use **@element-plus/icons-vue**; wrap in **<el-icon :size="20" color="...">** per [contract.md](contract.md).

---

## 10. Do not copy literally

- Do **not** put Tailwind class names in the template unless the project uses Tailwind.
- Do **not** use raw `<button>`, `<input>`, `<select>` — use **el-button**, **el-input**, **el-select** per [contract.md](contract.md).
- Do **not** build tables with raw thead/tbody — use **el-table :data** + **el-table-column**.
- Do convert spacing/typography to **px/rem** or Element theme vars.

For component API and invariants, use [contract.md](contract.md) and [component-index.md](component-index.md).
