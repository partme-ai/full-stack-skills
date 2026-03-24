# Tailwind → uView 2 (uni-app) Mapping

When converting **Stitch HTML** (Tailwind-based) to uni-app + Vue 2 + uView 2, map utility classes to **rpx**, **uView theme**, or **component props**. Do not output Tailwind class names in the Vue template.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with [contract.md](contract.md).

## Scale convention

- Tailwind default: `1` = 0.25rem = 4px.
- **rpx**: 750 design width → `1px ≈ 2rpx`; use integer rpx (e.g. 16rpx, 32rpx).
- uView 2 spacing (px): 4, 8, 12, 16, 20, 24, 32, 40 → map to same in rpx (8, 16, 24, 32, 40, 48, 64, 80).

---

## 1. Layout

| Tailwind pattern | uView 2 / uni-app |
|------------------|-------------------|
| `flex` | `<view>` with `display: flex` in style, or `<u-row>` |
| `flex flex-col` | `<view style="display:flex; flex-direction: column;">` or vertical `<u-row>` |
| `flex items-center` | `align-items: center` in style |
| `flex justify-between` | `justify-content: space-between` in style; or `<u-row justify="space-between">` |
| `grid` | `<u-row>` + `<u-col span="...">` (uView gutter e.g. `gutter="10"`) |
| `grid grid-cols-2` | `<u-row gutter="10"><u-col span="6">...</u-col><u-col span="6">...</u-col></u-row>` |
| `grid grid-cols-3` | `<u-col span="4">` × 3 |
| `sticky top-0` | `position: sticky; top: 0` in style; or `<u-navbar>` for header |
| `sticky top-14` | Second sticky block; `top` in rpx (e.g. 88rpx) |

---

## 2. Spacing

| Tailwind | px (approx) | rpx (use this) |
|----------|-------------|----------------|
| `p-2` | 8 | 16rpx |
| `p-3` | 12 | 24rpx |
| `p-4` | 16 | 32rpx |
| `p-5` | 20 | 40rpx |
| `px-4`, `py-2` etc. | — | 32rpx horizontal; 16rpx vertical (scale 1:2) |
| `mb-1` ~ `mb-5` | 4 ~ 20 | 8rpx ~ 40rpx |
| `gap-2`, `gap-4` | 8, 16 | 16rpx, 32rpx; or `<u-row gutter="20">` |
| `space-y-4` | 16 | margin-bottom 32rpx on children or flex gap |

---

## 3. Sizing

| Tailwind | rpx |
|----------|-----|
| `w-full` | width: 100% or 750rpx |
| `w-10`, `w-24` | 80rpx, 192rpx |
| `h-6`, `h-10`, `h-24` | 48rpx, 80rpx, 192rpx |
| `min-h-*` | min-height in rpx (px × 2) |

---

## 4. Typography

| Tailwind | uView 2 |
|----------|---------|
| `text-xs` | 24rpx (small); uView font 12px → 24rpx |
| `text-sm` | 28rpx (content); 14px → 28rpx |
| `text-base` | 30rpx; 16px → 30rpx |
| `text-lg` | 36rpx (title); 18px → 36rpx |
| `font-normal` / `font-medium` / `font-bold` | font-weight: 400 / 500 / 700 |
| `text-gray-500`, `text-gray-400` | u-tips-color #909193, u-content-color #606266 |
| `text-gray-900` | u-main-color #303133 |
| `text-primary` | u-primary #3c9cff |
| `placeholder-gray-300` | placeholder style color |

---

## 5. Colors (Stitch theme → uView 2)

| Stitch / Tailwind | uView 2 |
|-------------------|---------|
| `primary`, `bg-primary`, `text-primary` | u-primary #3c9cff; use for buttons, tabs activeColor |
| `background-light` | u-bg-color #f3f4f6 (page background) |
| `card-light` | #ffffff (card) |
| `border-light` | u-border-color #dadbde |
| `text-red-500` (required) | Use u-form required or #f56c6c |
| `bg-gray-50`, `dark:bg-gray-800` | #f3f4f6; dark #1E1E1E if supporting dark |

---

## 6. Borders

| Tailwind | uView 2 |
|----------|---------|
| `border` | border: 1px solid #dadbde |
| `border-b` | border-bottom only |
| `border-0` | border: none |
| `border-2 border-dashed` | 2rpx dashed (upload area) |
| `rounded` | border-radius: 8rpx (uView radius 8) |
| `rounded-lg` | 16rpx |
| `rounded-xl` | 20rpx |
| `rounded-full` | 9999px (pill/circle) |
| `border-gray-200` | #dadbde |

---

## 7. Effects

| Tailwind | uView 2 |
|----------|---------|
| `shadow-sm`, `shadow-soft` (Stitch) | box-shadow: 0 2rpx 8rpx rgba(0,0,0,0.04) |
| `shadow-inner` | inset shadow in rpx |
| `shadow-md` | Slightly stronger in rpx |

---

## 8. Interactivity

| Tailwind | uView 2 |
|----------|---------|
| `hover:bg-gray-100` | Use uView component hover or @click + class |
| `focus:ring-1 focus:ring-primary` | u-input built-in focus; no Tailwind in template |
| `peer` / `peer-checked:` | Use `<u-switch>`, `<u-radio-group>`; do not replicate with peer |

---

## 9. Icons (Stitch Material Symbols → uView 2)

| Stitch / Material | uView 2 |
|-------------------|---------|
| `chevron_left` | `<u-navbar :autoBack="true">` (no icon) |
| `expand_more` | `<u-icon name="arrow-down">` |
| `add` | `<u-icon name="plus">` |
| `remove` | minus or “-” in number-box |
| `add_photo_alternate` | `photo` or similar |

Use **u-icon** with uView 2 icon **name**; see [component-index.md](component-index.md).

---

## 10. Do not copy literally

- Do **not** put Tailwind class names in the Vue template unless the project uses Tailwind.
- Do **not** use raw `<button>`, `<input>`, `<select>` for UI — use **u-button**, **u--input** / **u-input**, **u-form** per [contract.md](contract.md).
- Do convert all spacing and typography to **rpx** or component props.

For component API and invariants, use [contract.md](contract.md) and [component-index.md](component-index.md).
