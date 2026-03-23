# Tailwind → uView Pro (uni-app) Mapping

When converting **Stitch HTML** (Tailwind-based) to uni-app + Vue 3 + uView Pro, map utility classes to **rpx**, **uView theme**, or **component props**. Do not output Tailwind class names in the Vue template.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Stitch often uses Tailwind or Tailwind-like utilities (e.g. `primary` from theme config).

## Scale convention

- Tailwind default: `1` = 0.25rem = 4px.
- **rpx**: 750 design width → `1px ≈ 2rpx` for spacing/typography; use integer rpx (e.g. 16rpx, 32rpx).

---

## 1. Layout

| Tailwind pattern | uView Pro / uni-app |
|------------------|---------------------|
| `flex` | `<view class="...">` with `display: flex` in style, or `<u-row>` |
| `flex flex-col` | `<view style="display:flex; flex-direction: column;">` or vertical `<u-row>` |
| `flex items-center` | `align-items: center` in style |
| `flex justify-between` | `justify-content: space-between` in style |
| `grid` | `<u-row>` + `<u-col>` with span, or flex wrap |
| `grid grid-cols-2` | `<u-row><u-col span="6">...</u-col><u-col span="6">...</u-col></u-row>` (2 cols) |
| `grid grid-cols-3` | `<u-row><u-col span="4">` × 3 |
| `sticky top-0` | `position: sticky; top: 0` in style (navbar/header) — or use `<u-navbar>` which handles placeholder |
| `sticky top-14` | Second sticky block (e.g. tabs below navbar); style `top` in rpx if needed (e.g. 88rpx) |

---

## 2. Spacing

| Tailwind | px (approx) | rpx (use this) |
|----------|-------------|-----------------|
| `p-2` | 8 | 16rpx |
| `p-3` | 12 | 24rpx |
| `p-4` | 16 | 32rpx |
| `p-5` | 20 | 40rpx |
| `px-4` | 16 horizontal | padding-left/right: 32rpx |
| `py-2` | 8 vertical | padding-top/bottom: 16rpx |
| `py-3` | 12 | 24rpx |
| `py-4` | 16 | 32rpx |
| `mb-1` ~ `mb-5` | 4 ~ 20 | 8rpx ~ 40rpx (mb-2→16rpx, mb-4→32rpx) |
| `gap-2` | 8 | 16rpx (flex gap or u-row gutter) |
| `gap-4` | 16 | 32rpx or `<u-gap height="32" />` |
| `space-y-4` | 16 between children | margin-bottom on children or gap in flex column: 32rpx |
| `gap-3` | 12 | 24rpx |

Use **u-row** `gutter` in rpx (e.g. `gutter="20"`) for column gap when using u-col.

---

## 3. Sizing

| Tailwind | px (approx) | rpx |
|----------|-------------|-----|
| `w-full` | 100% | width: 100% or 750rpx |
| `w-10` | 40 | 80rpx |
| `w-24` | 96 | 192rpx |
| `h-6` | 24 | 48rpx (e.g. switch) |
| `h-10` | 40 | 80rpx |
| `h-24` | 96 | 192rpx |
| `min-h-*` | — | min-height in rpx (e.g. min-height: 420px → 840rpx for fixed-height editor) |

---

## 4. Typography

| Tailwind | Typical px | uView Pro |
|----------|------------|-----------|
| `text-xs` | 12 | 24rpx (small) |
| `text-sm` | 14 | 28rpx (content) |
| `text-base` | 16 | 30rpx |
| `text-lg` | 18 | 36rpx (title) |
| `text-2xl` | 24 | 48rpx (icon size) |
| `font-normal` | 400 | font-weight: 400 |
| `font-medium` | 500 | font-weight: 500 |
| `font-bold` | 700 | font-weight: 700 |
| `text-gray-500`, `text-gray-400` | — | color: #909399 (Tips) or #606266 (Content) per [contract](contract.md) |
| `text-gray-900` dark:`text-white` | — | Main text: #303133; dark use theme or #fff |
| `text-primary` | theme | color: #1677FF or uView primary #3c9cff |
| `placeholder-gray-300` | — | placeholder class or style color |

Prefer **rpx** for font-size (e.g. 28rpx, 32rpx) and uView text color tokens where applicable.

---

## 5. Colors (Stitch theme → uView)

| Stitch / Tailwind | Value / note | uView Pro |
|-------------------|--------------|-----------|
| `primary`, `bg-primary`, `text-primary` | #1677FF (Stitch) | Use as `activeColor` on u-tabs, u-switch, u-radio; or keep #1677FF in style |
| `background-light` | #F5F6FA | Page background |
| `background-dark` | #121212 | Dark page background (if supporting dark) |
| `card-light` | #FFFFFF | Card background |
| `card-dark` | #1E1E1E | Dark card |
| `border-light` | #E5E7EB | Border color |
| `border-dark` | #333333 | Dark border |
| `text-red-500` (required asterisk) | — | Use `<u-form-item required>` or keep red #f56c6c for asterisk |
| `bg-gray-50` dark:`bg-gray-800` | Input/select bg | Use uView input background or #f3f4f6 / #1E1E1E |

---

## 6. Borders

| Tailwind | uView Pro |
|----------|-----------|
| `border` | border: 1px solid #dadbde (or theme border) |
| `border-b` | border-bottom only |
| `border-0` | border: none (e.g. u-input underline style) |
| `border-2 border-dashed` | 2rpx dashed (e.g. upload area) |
| `rounded` | border-radius: 8rpx |
| `rounded-lg` | border-radius: 16rpx |
| `rounded-xl` | border-radius: 20rpx (card) |
| `rounded-full` | border-radius: 9999px (pill/circle) |
| `border-gray-200` dark:`border-gray-700` | Use theme border or #dadbde / #333 |

---

## 7. Effects

| Tailwind | uView Pro |
|----------|-----------|
| `shadow-sm` | box-shadow: 0 2rpx 8rpx rgba(0,0,0,0.04) |
| `shadow-soft` (Stitch) | Same as above or 0 2px 8px rgba(0,0,0,0.04) → rpx |
| `shadow-inner` | box-shadow: inset … for toolbar |
| `shadow-md` | Slightly stronger shadow in rpx |

---

## 8. Interactivity (hover / focus)

| Tailwind | uView Pro |
|----------|-----------|
| `hover:bg-gray-100` | Use uView button/row hover styles if available; or optional `@click` + class binding |
| `focus:ring-1 focus:ring-primary` | u-input has built-in focus; avoid raw Tailwind in template |
| `peer` / `peer-checked:` | Use `<u-switch v-model>` or `<u-radio-group>`; do not replicate with Tailwind peer |

---

## 9. Icons (Stitch Material Symbols → uView)

| Stitch / Material | uView Pro |
|-------------------|-----------|
| `chevron_left` | Navbar back: use `<u-navbar :autoBack="true">` (no icon needed) |
| `expand_more` | `<u-icon name="arrow-down">` |
| `add` | `<u-icon name="plus">` |
| `remove` | `minus` if available, or text “-” in number-box |
| `format_bold`, `format_size` | Use uView icon name or custom icon |
| `add_photo_alternate` | `photo` or similar for “insert image” |

Prefer **u-icon** with uView icon **name**; fallback to text or image if no match.

---

## 10. Do not copy literally

- Do **not** put Tailwind class names in the Vue template (e.g. no `class="p-4 text-sm"`) unless the project explicitly uses Tailwind.
- Do **not** use raw `<button>`, `<input>`, `<select>` for form UI — use **u-button**, **u-input**, **u-picker** per [contract](contract.md) and [stitch-html-patterns](stitch-html-patterns.md).
- Do convert all spacing and typography to **rpx** or component props so output is framework-native.

For **semantic** patterns (header → navbar, tab bar → u-tabs, form → u-form-item), use [stitch-html-patterns.md](stitch-html-patterns.md). For **component API** and anti-patterns, use [contract.md](contract.md).
