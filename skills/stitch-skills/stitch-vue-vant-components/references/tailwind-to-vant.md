# Tailwind → Vant 4 (Vue 3) Mapping

When converting **Stitch HTML** (Tailwind-based) to Vue 3 + Vant 4, map utility classes to **rem/px**, **Vant CSS variables / theme**, or **component props**. Mobile-first (375px base); do not output Tailwind class names unless the project uses Tailwind.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with [contract.md](contract.md).

## Scale convention

- Tailwind default: `1` = 0.25rem = 4px.
- **Vant**: Base 14px; padding 4/8/12/16px (van-padding-*); radius 2/4/8/999px (van-radius-*). Use **rem** or **px** in style; Vant uses CSS vars (e.g. `--van-button-primary-background`).
- 375px design: `1px` ≈ 1px; for rem, base 14px → 0.25rem ≈ 3.5px, 1rem = 14px if root 14px.

---

## 1. Layout

| Tailwind pattern | Vant 4 |
|------------------|--------|
| `flex` | `<div class="van-flex">` or style `display: flex` (Vant has flex utilities in some components) |
| `flex flex-col` | `flex-direction: column` in style |
| `flex items-center` | `align-items: center` |
| `flex justify-between` | `justify-content: space-between` |
| `grid` | `<van-row>`, `<van-col span="12">` |
| `grid grid-cols-2` | `<van-row><van-col span="12">` × 2 |
| `grid grid-cols-3` | `<van-col span="8">` × 3 |
| `sticky top-0` | `position: sticky; top: 0`; or `<van-nav-bar>` (fixed by default) |
| `sticky top-14` | Second sticky; `top: 56px` or 3.5rem |

---

## 2. Spacing

| Tailwind | px | Vant 4 |
|----------|-----|--------|
| `p-2` | 8 | 8px or var(--van-padding-md) if defined |
| `p-3` | 12 | 12px |
| `p-4` | 16 | 16px (van-padding-base) |
| `p-5` | 20 | 20px |
| `px-4`, `py-2` | 16, 8 | padding-left/right 16px; top/bottom 8px |
| `mb-*`, `gap-*` | — | margin-bottom / gap in px (4, 8, 12, 16) |
| `space-y-4` | 16 | margin-bottom 16px on children |

Prefer **px** for mobile (14px, 16px) or Vant padding/ margin vars.

---

## 3. Sizing

| Tailwind | Vant 4 |
|----------|--------|
| `w-full` | width: 100% |
| `w-10`, `w-24` | 40px, 96px |
| `h-6`, `h-10`, `h-24` | 24px, 40px, 96px |
| `min-h-*` | min-height in px |

---

## 4. Typography

| Tailwind | Vant 4 |
|----------|--------|
| `text-xs` | 12px (small) |
| `text-sm` | 14px (base) |
| `text-base` | 16px |
| `text-lg` | 18px (large) |
| `font-normal` / `font-medium` / `font-bold` | font-weight: 400 / 500 / 700 |
| `text-gray-500`, `text-gray-400` | #969799 (Text Regular) |
| `text-gray-900` | #323233 (Text Main) |
| `text-primary` | #1989fa (Vant primary) |
| `placeholder-gray-300` | placeholder color; van-field has built-in |

---

## 5. Colors (Stitch theme → Vant 4)

| Stitch / Tailwind | Vant 4 |
|-------------------|--------|
| `primary`, `bg-primary`, `text-primary` | #1989fa; use for type="primary", or --van-primary-color |
| `background-light` | #f7f8fa (page background) |
| `card-light` | #ffffff |
| `border-light` | #ebedf0 |
| `text-red-500` (required) | Use van-field :rules required or #ee0a24 |
| `bg-gray-50` | #f7f8fa |

---

## 6. Borders

| Tailwind | Vant 4 |
|----------|--------|
| `border` | border: 1px solid #ebedf0 |
| `border-b` | border-bottom only |
| `border-0` | border: none |
| `border-2 border-dashed` | 2px dashed (upload) |
| `rounded` | border-radius: 4px (van-radius-md) |
| `rounded-lg` | 8px |
| `rounded-xl` | 12px (or 8px to match van-radius-lg) |
| `rounded-full` | 999px (pill) |
| `border-gray-200` | #ebedf0 |

---

## 7. Effects

| Tailwind | Vant 4 |
|----------|--------|
| `shadow-sm`, `shadow-soft` | box-shadow: 0 2px 8px rgba(0,0,0,0.04) |
| `shadow-inner` | inset shadow |
| `shadow-md` | Slightly stronger shadow |

---

## 8. Interactivity

| Tailwind | Vant 4 |
|----------|--------|
| `hover:bg-gray-100` | Use van-button/van-cell active styles or class binding |
| `focus:ring-1 focus:ring-primary` | van-field has focus style; no Tailwind in template |
| `peer` / `peer-checked:` | Use `<van-checkbox>`, `<van-radio-group>`; do not use peer |

---

## 9. Icons (Stitch Material → Vant)

| Stitch / Material | Vant 4 |
|-------------------|--------|
| `chevron_left` | `<van-nav-bar left-arrow />` |
| `expand_more` | `<van-icon name="arrow-down" />` |
| `add` | `<van-icon name="plus" />` |
| `remove` | `<van-icon name="minus" />` |
| `add_photo_alternate` | `<van-icon name="photo-o" />` or similar |

Use **van-icon** with Vant icon **name**; see [component-index.md](component-index.md).

---

## 10. Do not copy literally

- Do **not** put Tailwind class names in the template unless the project uses Tailwind.
- Do **not** use raw `<button>`, `<input>`, `<select>` — use **van-button**, **van-field**, **van-picker** per [contract.md](contract.md).
- Do convert spacing/typography to **px** or Vant theme vars so output is framework-native.

For component API and invariants, use [contract.md](contract.md) and [component-index.md](component-index.md).
