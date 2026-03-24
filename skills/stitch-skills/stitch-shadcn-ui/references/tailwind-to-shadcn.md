# Tailwind → shadcn/ui (React + Tailwind) Mapping

When converting **Stitch HTML** (Tailwind-based) to React + **shadcn/ui**, **keep Tailwind utility classes** and map Stitch design tokens to **shadcn theme** (CSS variables in `globals.css`: `:root` and `.dark`). Use **shadcn components** (Button, Card, Input, etc.) instead of raw HTML; pass Tailwind classes via `className` or `cn()`. Do not use raw hex when a theme variable exists.

Reference: [Tailwind CSS v4 Docs](https://tailwindcss.com/docs). [shadcn/ui](https://ui.shadcn.com) uses Tailwind + Radix/Base UI; theme is CSS variables (--background, --foreground, --primary, --muted, etc.).

## Scale convention

- **Tailwind**: Default scale (p-4, text-sm, etc.) — keep in output.
- **shadcn**: Theme is driven by CSS variables in `globals.css` (e.g. `--background`, `--foreground`, `--primary`, `--primary-foreground`, `--muted`, `--muted-foreground`, `--border`, `--radius`). Use **semantic class names** where shadcn provides them: `bg-background`, `text-foreground`, `bg-muted`, `text-muted-foreground`, `border`, `rounded-lg` (from --radius).

---

## 1. Layout

| Tailwind pattern | shadcn/ui |
|------------------|-----------|
| `flex` | `className="flex"` (keep) |
| `flex flex-col` | `className="flex flex-col"` |
| `flex items-center` | `className="flex items-center"` |
| `flex justify-between` | `className="flex justify-between"` |
| `grid` | `className="grid grid-cols-2"` etc. (keep) |
| `sticky top-0` | `className="sticky top-0"`; consider **Header** or layout block if project uses shadcn blocks |
| `sticky top-14` | `className="sticky top-14"` or theme spacing |

Keep Tailwind layout; use **shadcn blocks** (e.g. sidebar, dashboard) if the project has them.

---

## 2. Spacing

| Tailwind | shadcn/ui |
|----------|-----------|
| `p-*`, `px-*`, `py-*`, `mb-*`, `gap-*`, `space-y-*` | Keep (Tailwind spacing) |

No conversion; Tailwind spacing is the standard.

---

## 3. Sizing

| Tailwind | shadcn/ui |
|----------|-----------|
| `w-full`, `w-*`, `h-*`, `min-h-*` | Keep |

---

## 4. Typography

| Tailwind | shadcn/ui |
|----------|-----------|
| `text-xs` ~ `text-2xl` | Keep |
| `font-normal`, `font-medium`, `font-bold` | Keep |
| `text-gray-500`, `text-gray-400` | Prefer **text-muted-foreground** (theme) |
| `text-gray-900` | Prefer **text-foreground** |
| `text-primary` | Keep; ensure --primary is set in globals.css |
| `placeholder-gray-300` | Prefer **placeholder:text-muted-foreground** |

Use **semantic tokens** where shadcn defines them: `text-foreground`, `text-muted-foreground`, `text-primary`.

---

## 5. Colors (Stitch theme → shadcn theme)

| Stitch / Tailwind | shadcn/ui |
|-------------------|-----------|
| `primary`, `bg-primary`, `text-primary` | Map to **--primary**, **--primary-foreground** in globals.css; use `bg-primary`, `text-primary`, `text-primary-foreground` in classNames |
| `background-light` | Map to **--background** (light); use `bg-background` |
| `background-dark` | Map to **--background** in `.dark` |
| `card-light`, `card-dark` | Map to **--card**, **--card-foreground**; use **<Card>** and `bg-card`, `text-card-foreground` |
| `border-light`, `border-dark` | Map to **--border**; use `border` or `border-border` |
| `text-red-500` (required/error) | Use **text-destructive** (--destructive) or form error state |
| `bg-gray-50`, `dark:bg-gray-800` | Use **bg-muted** (--muted) and **dark:bg-muted** |

**Rule**: Define Stitch tokens (e.g. #1677FF for primary) in `globals.css` under `:root` and `.dark`; then use shadcn semantic classes in JSX.

---

## 6. Borders

| Tailwind | shadcn/ui |
|----------|-----------|
| `border`, `border-b`, `border-0` | Keep; or use `border-border` (theme) |
| `border-2 border-dashed` | Keep |
| `rounded`, `rounded-lg`, `rounded-xl`, `rounded-full` | Keep; shadcn uses **--radius** (often 0.5rem); use `rounded-lg` for cards/inputs to match theme |
| `border-gray-200`, `dark:border-gray-700` | Prefer **border** (uses --border) |

---

## 7. Effects

| Tailwind | shadcn/ui |
|----------|-----------|
| `shadow-sm`, `shadow-md`, `shadow-inner` | Keep |
| `shadow-soft`, `shadow-floating` (Stitch) | Add to tailwind.config theme.boxShadow or use existing shadow utilities; Card uses `shadow-sm` by default |

---

## 8. Interactivity and states

| Tailwind | shadcn/ui |
|----------|-----------|
| `hover:bg-gray-100` | Keep or use **hover:bg-accent** (--accent) |
| `focus:ring-1 focus:ring-primary` | Keep; shadcn Input/Button have focus styles; use **focus-visible:ring-2** etc. if needed |
| `dark:` variants | Keep; ensure `.dark` is applied (e.g. on html) and variables set in `.dark` |
| `peer`, `peer-checked:` | Keep for custom components; or use **RadioGroup**, **Switch** from shadcn |

---

## 9. Icons (Stitch Material → shadcn)

| Stitch / Material | shadcn/ui |
|-------------------|-----------|
| `chevron_left`, `expand_more`, `add`, `remove` | Use **Lucide React** (shadcn default): `<ChevronLeft />`, `<ChevronDown />`, `<Plus />`, `<Minus />` |
| `add_photo_alternate` | `<ImagePlus />` |

Import from `lucide-react`; pass `className` for size/color (e.g. `className="h-4 w-4 text-muted-foreground"`).

---

## 10. Components: replace HTML with shadcn

| Stitch HTML | shadcn/ui |
|-------------|-----------|
| `<button class="... bg-primary">` | **<Button>** with `variant="default"` or `variant="primary"`; add Tailwind via `className` |
| `<input type="text">` | **<Input>** with `className` for layout |
| `<select>` | **<Select>** + **SelectTrigger**, **SelectContent**, **SelectItem** |
| Card/section container | **<Card>**, **<CardHeader>**, **<CardContent>**, **<CardFooter>** |
| Tabs (button row) | **<Tabs>** + **TabsList**, **TabsTrigger**, **TabsContent** |
| Modal/dialog | **<Dialog>** + **DialogTrigger**, **DialogContent**, **DialogHeader**, **DialogFooter** |
| Checkbox / switch | **<Checkbox>**, **<Switch>** |
| Form layout | **<Form>** (react-hook-form + zod) + **FormField**, **FormItem**, **FormLabel**, **FormControl** if project uses them |

Use **cn()** (clsx + tailwind-merge) to merge component default classes with Tailwind: `className={cn("flex gap-4", className)}`.

---

## 11. Do not copy literally

- Do **not** use raw hex in className when a theme variable exists (use `bg-primary`, `text-muted-foreground`, not `bg-[#1677FF]`).
- Do **not** use raw `<button>`, `<input>`, `<select>` for UI — use **Button**, **Input**, **Select** from `components/ui/`.
- Do **not** leave Stitch-only token names (e.g. `background-light`) unless mapped in globals.css; use **--background**, **--card**, **--primary** etc.
- Do **sync** Stitch colors/radius/shadow with **globals.css** and **tailwind.config** so semantic classes work.

For installation and customization, see the skill [SKILL.md](../SKILL.md) and [ui.shadcn.com](https://ui.shadcn.com).
