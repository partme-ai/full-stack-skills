# Tailwind → Bootstrap Vue (Vue 3 + Bootstrap 5) Mapping

When converting **Stitch HTML** (Tailwind-based) to Vue 3 + BootstrapVueNext (Bootstrap 5), map Tailwind utilities to **Bootstrap utility classes** or **component props**. Bootstrap uses a 0–5 spacing scale (0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem) and rem-based typography.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with [contract.md](contract.md).

## Scale convention

- **Tailwind**: `1` = 0.25rem = 4px → `p-4` = 16px = 1rem.
- **Bootstrap 5**: spacing `0`–`5` → 0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem. So Tailwind `p-4` → Bootstrap `p-4` (1rem); Tailwind `m-2` → Bootstrap `m-2` (0.5rem); Tailwind `gap-4` → Bootstrap `gap-4` (1rem).
- Many **Tailwind and Bootstrap class names overlap** (e.g. `p-3`, `mb-2`); when both use same scale, you can keep or map 1:1. Prefer **Bootstrap** utility names if the project does not use Tailwind: e.g. `mb-3`, `py-4`, `d-flex`, `justify-content-between`.

---

## 1. Layout

| Tailwind pattern | Bootstrap Vue |
|------------------|----------------|
| `flex` | `d-flex` (Bootstrap) |
| `flex flex-col` | `d-flex flex-column` |
| `flex items-center` | `d-flex align-items-center` |
| `flex justify-between` | `d-flex justify-content-between` |
| `grid` | Use **b-row** + **b-col**; do not use raw CSS grid |
| `grid grid-cols-2` | `<b-row><b-col cols="12" md="6">` × 2 |
| `grid grid-cols-3` | `<b-col cols="12" md="4">` × 3 |
| `sticky top-0` | `sticky-top` (Bootstrap) or `position-sticky top-0`; or use layout component |
| `sticky top-14` | `sticky-top` with offset or custom style |

---

## 2. Spacing

| Tailwind | Bootstrap equivalent |
|----------|------------------------|
| `p-2` | `p-2` (0.5rem) |
| `p-3` | `p-3` (1rem) — Tailwind p-3=12px, Bootstrap p-3=1rem; prefer Bootstrap scale |
| `p-4` | `p-4` (1.5rem) — Tailwind p-4=16px, Bootstrap p-4=1.5rem; or `p-3` for 1rem |
| `p-5` | `p-5` (3rem) |
| `px-4` | `px-3` or `px-4` |
| `py-2`, `py-4` | `py-2`, `py-4` |
| `mb-1` ~ `mb-5` | `mb-1` ~ `mb-5` (same names, check scale: Bootstrap mb-3=1rem) |
| `gap-2`, `gap-4` | `gap-2`, `gap-3`, `gap-4` (Bootstrap 5 has gap utilities) |
| `space-y-4` | `gap-4` on parent (flex/grid) or `mb-4` on children |

Use **Bootstrap spacing scale** (0–5) for consistency.

---

## 3. Sizing

| Tailwind | Bootstrap Vue |
|----------|----------------|
| `w-full` | `w-100` |
| `w-10`, `w-24` | style `width: 2.5rem`, `width: 6rem` or utility `w-25`, `w-50` if applicable |
| `h-*` | `h-100`, `h-auto`, or style height |
| `min-h-*` | style min-height |

---

## 4. Typography

| Tailwind | Bootstrap Vue |
|----------|----------------|
| `text-xs` | `small` or `fs-6` (Bootstrap font-size utilities) |
| `text-sm` | `fs-6` (smaller) |
| `text-base` | default body |
| `text-lg` | `fs-4` or `h5` / `h6` |
| `font-normal` / `font-bold` | `fw-normal`, `fw-bold` |
| `text-gray-500` | `text-muted` |
| `text-gray-900` | default text or `text-dark` |
| `text-primary` | `text-primary` (Bootstrap primary #0d6efd) |
| `text-center` | `text-center` (same) |

Use **Bootstrap typography**: `h1`–`h6`, `.lead`, `text-muted`, `fw-*`, `fs-*`.

---

## 5. Colors (Stitch theme → Bootstrap 5)

| Stitch / Tailwind | Bootstrap Vue |
|-------------------|----------------|
| `primary`, `bg-primary` | `bg-primary`, `text-primary`, `btn-primary` (#0d6efd) |
| `background-light` | `bg-light` (#f8f9fa) |
| `card-light` | `bg-white` or `card` default |
| `border-light` | `border` or `border-secondary` |
| `text-red-500` (required) | `text-danger` or form validation state |
| `bg-gray-50` | `bg-light` |

---

## 6. Borders

| Tailwind | Bootstrap Vue |
|----------|----------------|
| `border` | `border` |
| `border-b` | `border-bottom` |
| `border-0` | `border-0` |
| `border-2 border-dashed` | `border border-2 border-secondary` (dashed via class or style) |
| `rounded` | `rounded` |
| `rounded-lg` | `rounded` or `rounded-3` |
| `rounded-xl` | `rounded-3` |
| `rounded-full` | `rounded-pill` (pill) or `rounded-circle` (circle) |
| `border-gray-200` | `border` (Bootstrap border color) or `border-secondary` |

---

## 7. Effects

| Tailwind | Bootstrap Vue |
|----------|----------------|
| `shadow-sm` | `shadow-sm` (same) |
| `shadow-soft` (Stitch) | `shadow-sm` or `shadow` |
| `shadow-inner` | custom or `shadow-none` + border |
| `shadow-md` | `shadow` |

---

## 8. Interactivity

| Tailwind | Bootstrap Vue |
|----------|----------------|
| `hover:bg-gray-100` | Bootstrap buttons/cards have hover; or `hover` class on table |
| `focus:ring-1 focus:ring-primary` | Use **b-form-input** / **b-form-select**; Bootstrap form controls have focus styles |
| `peer` / `peer-checked:` | Use **b-form-checkbox**, **b-form-radio**; do not use peer |

---

## 9. Icons (Stitch Material → Bootstrap)

| Stitch / Material | Bootstrap Vue |
|-------------------|----------------|
| `chevron_left` | Bootstrap Icons `bi-chevron-left` or icon component |
| `expand_more` | `bi-chevron-down` |
| `add` | `bi-plus` |
| `remove` | `bi-dash` |
| `add_photo_alternate` | `bi-image-plus` or similar |

Use project icon set (Bootstrap Icons, custom); wrap in `<b-icon>` or equivalent if using BootstrapVueNext icon component.

---

## 10. Do not copy literally

- Do **not** output Tailwind-only class names; use **Bootstrap utility classes** (d-flex, p-3, mb-2, text-primary, rounded, shadow-sm) or component props.
- Do **not** use raw `<button class="btn btn-primary">` — use **<b-button variant="primary">** per [contract.md](contract.md).
- Do **not** use raw `<table>` for data — use **<b-table :items :fields>**.
- Do use **b-row** / **b-col** for grid; **b-form-group** + **b-form-input** / **b-form-select** for forms; **b-card** for cards.

For component API and invariants, use [contract.md](contract.md) and [component-index.md](component-index.md).
