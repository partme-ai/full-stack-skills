# Stitch HTML → uView Pro Mapping

Stitch exports **Tailwind-based HTML**. When converting, map the following patterns to uView Pro components. Use this reference when parsing Stitch's `htmlCode` (e.g. from `get_screen`).

- **Utility-level (Tailwind class → rpx/theme)**: spacing, typography, colors, borders, shadows → see [tailwind-to-uviewpro.md](tailwind-to-uviewpro.md). Do not copy Tailwind class names into the Vue template.

**Rule: Use framework components when available; do not replace them with generic `<view>`/`<text>` + custom class.** Use **u-card** for cards, **u-section** for section headers (including right-side content), **u-text** for label hints and tip text, **u-line** / **u-divider** for dividers.

## 1. Page structure

| Stitch HTML pattern | uView Pro |
|---------------------|-----------|
| `<header class="sticky top-0 ...">` with back icon + `<h1>` title | `<u-navbar title="Page Title" :autoBack="true" placeholder border></u-navbar>` |
| `<div class="sticky ... grid grid-cols-3 text-center">` with multiple `<button>` (one active, underline) | **`<u-tabs :list="list" :current="current" @change="...">`** — do **not** keep as raw buttons/divs. Extract tab labels into `list = [{ name: 'Tab 1' }, ...]`. |
| `<main class="px-4 py-4 space-y-4">` | `<view class="content">` with padding (e.g. 32rpx). |
| `<section class="bg-card-light ... rounded-xl p-4 shadow-soft">` with only a title | **`<u-card title="Basic Info" :padding="32">...</u-card>`** — do **not** use `<view class="card">` + custom header/title. |
| `<section>` with `<h2>` + right-side content (e.g. switch, link) | **`<u-card :padding="32">`** + **`<u-section title="Section Title">`** with **`<template #right>`** for the right content (e.g. `<u-text>` + `<u-switch>`). Do not use custom card-header-row. |
| Divider line between content blocks | **`<u-line color="#e5e7eb" margin="0">`** or **`<u-divider>`** — do not use only `<view class="divider">` with border style. |

## 2. Form fields

| Stitch HTML pattern | uView Pro |
|---------------------|-----------|
| `<label class="block ...">` with `<span class="text-red-500">*</span>` + `<input>` or `<select>` | `<u-form-item label="..." prop="..." required borderBottom>` + u-input or u-picker. |
| `<label>... <span class="text-xs ...">(optional)</span></label>` | `<u-form-item>` with **`<template #label>`**: main `<text>` + **`<u-text text=" (optional)" type="info" size="24" />`** — do **not** use `<text class="label-optional">`. Same for other hints (e.g. display-only, no limit). |
| `<input type="text" placeholder="...">` | `<u-input v-model="form.xxx" placeholder="..." border="none">` |
| `<select><option>Select category</option><option>Option A</option>...</select>` | **u-input** `type="select"` + **:select-open** + **u-picker** with **v-model**, **mode="selector"**, **:range** = 1D array of option texts, e.g. `['Option A','Option B','Option C']`. Do not use `:columns` or 2D array. |
| `<input type="number" placeholder="0.00">` with minus/plus buttons | `<u-number-box v-model="form.xxx" :min="0" :step="0.01">` (or :step="1" for integer). |
| `<input type="checkbox" class="sr-only peer">` + custom toggle div | `<u-switch v-model="form.xxx" activeColor="#1677FF">` |
| Row of `<input type="radio" name="sales_method">` with labels | `<u-radio-group v-model="form.salesMethod">` + `<u-radio label="Option A" value="mall">` … Use **value** (e.g. mall, points, both), not **name**. |

## 3. Upload and accordion

| Stitch HTML pattern | uView Pro |
|---------------------|-----------|
| `<div class="w-24 h-24 border-2 border-dashed ...">` with add icon + upload label | `<u-upload :fileList="fileList" @afterRead="afterRead" @delete="deletePic" :maxCount="5">` + below it use **`<u-text text="Suggested size..." type="info" size="24" />`** and **`<u-text type="warning" size="24" />`** for tips — do **not** use custom `.tips-text` / `.tips-warn`. |
| `<details><summary>More info</summary><div>...</div></details>` | `<u-collapse><u-collapse-item title="More info">...</u-collapse-item></u-collapse>` |

## 4. Layout

| Stitch HTML pattern | uView Pro |
|---------------------|-----------|
| `class="grid grid-cols-2 gap-4"` with two inputs | `<u-row gutter="20"><u-col span="6">...</u-col><u-col span="6">...</u-col></u-row>` |
| Divider line | **`<u-line color="#e5e7eb" margin="...">`** or **`<u-divider>`** — do not use only custom view + border. |

## 5. Buttons and rich area

| Stitch HTML pattern | uView Pro |
|---------------------|-----------|
| `<button class="... bg-primary text-white ...">` with icon + text | `<u-button type="primary" icon="photo" text="Insert image">` |
| `contenteditable="true"` block + toolbar | Use **u-textarea** for simple rich text, or a `<view>` with static content + **u-button** for "Insert image"; avoid raw contenteditable in uni-app. |

## 6. Stitch design tokens (Tailwind) → rpx / theme

Stitch HTML often uses:

- **Primary**: `#1677FF` — use as `activeColor` (e.g. u-switch, u-radio, u-tabs) or keep; uView default primary is `#3c9cff`, both are valid.
- **Background**: `#F5F6FA` (background-light) → page background.
- **Card**: `#FFFFFF`, `rounded-xl` (0.75rem) → card border-radius 20rpx.
- **Shadow**: `shadow-soft` → box-shadow 0 2rpx 8rpx rgba(0,0,0,0.04).
- **Icons**: Stitch uses Material Symbols (e.g. `chevron_left`, `expand_more`, `add`). Map to uView Pro icon **name** where possible: e.g. `expand_more` → `arrow-down`, `add` → `plus`, `chevron_left` → back (navbar :autoBack handles it).

## 7. Do not copy literally (use framework components)

- **Card / section**: Do **not** use `<view class="card">` + `<view class="card-header">` + `<text class="card-title">` — use **u-card** with `title` prop, or **u-card** + **u-section** when the block has title + right content.
- **Label hints / tip text**: Do **not** use `<text class="label-optional">` / `.tips-text` / `.tips-warn` / `.unit` — use **u-text** with `type="info"` or `type="warning"`, `size="24"` or `28`, and optional `block`.
- **Divider**: Do **not** use only custom `<view>` with border — use **u-line** or **u-divider**.
- **Tab bar**: Do **not** keep Stitch's `<button>` tab bar — always convert to **u-tabs**.
- **Select dropdown**: Do **not** keep native `<select>` — use **u-input type="select"** + **u-picker** with **v-model** and **:range** (1D).
- **Slots**: Do **not** use `slot="label"` or `slot="suffix"` — use **#label**, **#suffix** (Vue 3).
- **Radio**: Do **not** use raw `<input type="radio">` — use **u-radio-group** + **u-radio** with **value** and **label**.
- **Styling**: Do **not** use Tailwind classes in the Vue template — convert to rpx, uView props, and scoped style.

Consult [tailwind-to-uviewpro.md](tailwind-to-uviewpro.md) for Tailwind utility → rpx/theme, [contract.md](contract.md) for API details and anti-patterns, and [component-index.md](component-index.md) for component list.
