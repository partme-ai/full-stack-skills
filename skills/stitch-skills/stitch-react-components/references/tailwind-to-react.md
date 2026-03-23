# Tailwind → React (Vite/React + Tailwind) Mapping

When converting **Stitch HTML** (Tailwind-based) to React (Vite + TypeScript + Tailwind), **keep Tailwind utility classes** in the output but **map Stitch design tokens to the project theme** (tailwind.config, CSS variables). Do not copy raw hex or arbitrary values when a theme key exists. Replace semantic HTML (header, form, tabs) with React components where the project defines them.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). Align with project `resources/style-guide.json` or `tailwind.config.*` if present.

## Scale convention

- **Tailwind default**: `1` = 0.25rem = 4px; spacing/typography use Tailwind scale (p-4, text-sm, etc.).
- **React output**: Prefer **theme-mapped** class names: e.g. `bg-primary`, `text-primary`, `rounded-xl` from Stitch config → ensure these exist in project `tailwind.config` theme.extend (colors, borderRadius, boxShadow). If the project has no Tailwind theme, add Stitch tokens to config or use Tailwind defaults.

---

## 1. Layout

| Tailwind pattern | React (keep or map) |
|------------------|----------------------|
| `flex` | `className="flex"` (keep) |
| `flex flex-col` | `className="flex flex-col"` |
| `flex items-center` | `className="flex items-center"` |
| `flex justify-between` | `className="flex justify-between"` |
| `grid` | `className="grid grid-cols-2"` etc. (keep) |
| `grid grid-cols-2`, `grid-cols-3` | Keep; or use project grid component if any |
| `sticky top-0` | `className="sticky top-0"` |
| `sticky top-14` | `className="sticky top-14"` or theme spacing token |

Use **Tailwind layout classes** as-is; ensure Tailwind is configured and content paths include the component files.

---

## 2. Spacing

| Tailwind | React |
|----------|--------|
| `p-2` ~ `p-5` | Keep `p-2`, `p-3`, `p-4`, `p-5` |
| `px-4`, `py-2` | Keep |
| `mb-*`, `gap-*`, `space-y-*` | Keep (`mb-4`, `gap-4`, `space-y-4`) |

No conversion needed; Tailwind classes are the output. If project uses custom spacing scale, align theme in tailwind.config.

---

## 3. Sizing

| Tailwind | React |
|----------|--------|
| `w-full`, `w-10`, `w-24` | Keep |
| `h-*`, `min-h-*` | Keep (e.g. `h-24`, `min-h-screen`) |

Keep Tailwind sizing; use theme width/height in config if project defines them.

---

## 4. Typography

| Tailwind | React |
|----------|--------|
| `text-xs` ~ `text-2xl` | Keep (`text-sm`, `text-lg`, etc.) |
| `font-normal`, `font-medium`, `font-bold` | Keep |
| `text-gray-500`, `text-gray-400` | Keep or map to theme: e.g. `text-muted-foreground` if project uses shadcn-style tokens |
| `text-primary` | Prefer **theme** key: ensure `primary` is in theme.colors so `text-primary` works |
| `placeholder-gray-300` | Keep or `placeholder:text-muted-foreground` if theme exists |

Prefer **theme color names** over raw gray-* when the project has semantic tokens (e.g. `text-foreground`, `text-muted-foreground`).

---

## 5. Colors (Stitch theme → project theme)

| Stitch / Tailwind | React |
|-------------------|--------|
| `primary`, `bg-primary`, `text-primary` | Map to **tailwind.config** theme.extend.colors.primary (#1677FF or project choice); then use `bg-primary`, `text-primary` in JSX |
| `background-light` | Map to theme color (e.g. background) or keep as custom: `bg-[#F5F6FA]` only if no theme |
| `card-light`, `card-dark` | Map to theme (e.g. card, card-foreground) or define in config |
| `border-light`, `border-dark` | Map to theme border color |
| `shadow-soft`, `shadow-floating` | Map to theme.boxShadow in tailwind.config so `shadow-soft` works |

**Rule**: Extract Stitch `tailwind.config` (from HTML `<script>` or DESIGN.md); sync with project `tailwind.config.*` and `resources/style-guide.json` if present. Use **theme keys** in className, not raw hex.

---

## 6. Borders

| Tailwind | React |
|----------|--------|
| `border`, `border-b`, `border-0` | Keep |
| `border-2 border-dashed` | Keep |
| `rounded`, `rounded-lg`, `rounded-xl`, `rounded-full` | Keep; ensure theme has borderRadius if Stitch overrides (e.g. rounded-xl = 0.75rem) |
| `border-gray-200`, `dark:border-gray-700` | Keep or map to theme `border`, `border-muted` |

Keep Tailwind border classes; add Stitch radius/shadow to theme if they use custom values.

---

## 7. Effects

| Tailwind | React |
|----------|--------|
| `shadow-sm`, `shadow-md`, `shadow-inner` | Keep |
| `shadow-soft`, `shadow-floating` (Stitch) | Define in theme.boxShadow in config; then use `shadow-soft` in JSX |

---

## 8. Interactivity and states

| Tailwind | React |
|----------|--------|
| `hover:bg-gray-100` | Keep `hover:bg-gray-100` or theme `hover:bg-accent` |
| `focus:ring-1 focus:ring-primary` | Keep; ensure `primary` in theme |
| `dark:` variants | Keep (`dark:bg-gray-800`, `dark:text-white`); ensure dark mode is configured (class or media) |
| `peer`, `peer-checked:` | Keep if using Tailwind; or replace with React state + conditional class |

---

## 9. Icons (Stitch Material Symbols → React)

| Stitch / Material | React |
|-------------------|--------|
| `chevron_left`, `expand_more`, `add`, `remove` | Use project icon set (e.g. Lucide, Heroicons, or Material Symbols); e.g. `<ChevronLeft />`, `<Plus />` |
| `add_photo_alternate` | `<ImagePlus />` or equivalent from icon library |

Do not output Material Symbols font in React unless the project uses it; use the project’s chosen icon component.

---

## 10. Do not copy literally

- Do **not** use raw hex in className when a theme key exists (e.g. use `bg-primary` not `bg-[#1677FF]` if primary is in theme).
- Do **not** leave Stitch-only token names (e.g. `background-light`) in JSX unless they are defined in project tailwind.config; map them to theme.extend.
- Do **not** use raw `<button>`, `<input>` for UI when the project has shared components (e.g. Button, Input); use those components with Tailwind classes passed via className.
- Do **extract** Stitch tailwind.config (colors, borderRadius, boxShadow) and **sync** with project config so generated class names are valid and consistent.

For project structure and validation, use [resources/architecture-checklist.md](../resources/architecture-checklist.md).
