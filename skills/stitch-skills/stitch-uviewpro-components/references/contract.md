# uView Pro Design Contract (Stitch HTML → uni-app Page Mapping)

When converting Stitch-generated HTML to uni-app + Vue 3 + uView Pro, map structure and styles to the following. Align with stitch-ui-design-spec-uviewpro (same repo) for generation-time constraints. **Use rpx** for typography and spacing. Components use the **u-** prefix (same as uView 2; uView Pro is the Vue 3 package `uview-pro`, easycom: `^u-(.*)` → `uview-pro/components/u-$1`).

## 1. Design Tokens

### Stitch HTML tokens (when converting from Stitch export)
Stitch-generated HTML often uses Tailwind tokens such as **primary `#1677FF`**, `background-light`/`card-light`, `rounded-xl`, `shadow-soft`. Map these to uView theme or rpx as needed; primary `#1677FF` is valid for `activeColor` (u-tabs, u-switch, u-radio). For full Stitch HTML → structure/forms/tokens mapping, see [stitch-html-patterns.md](stitch-html-patterns.md).

### Colors (Standard Theme)
- **Primary**: `#3c9cff` (Blue)
- **Success**: `#5ac725`, **Warning**: `#f9ae3d`, **Danger**: `#f56c6c`, **Info**: `#909399`
- **Main Text**: `#303133`, **Content**: `#606266`, **Tips**: `#909399`, **Light**: `#c0c4cc`
- **Border**: `#dadbde`, **Background**: `#f3f4f6`

### Typography (rpx)
- Main Title: 32rpx or 36rpx (Bold)
- Content: 28rpx (Base)
- Tips/Secondary: 24rpx
- Small: 20rpx

### Radius & Spacing
- Radius: 8rpx (Small), 16rpx (Card), 9999px (Circle/Pill).
- Spacing: Use gap in flex or utility classes; rpx where appropriate.

## 2. Component Mapping (Stitch HTML → uView Pro)

**Rule: Use framework components when available; do not replace with generic view/text + custom class.** See [component-index.md](component-index.md) “Design element → Component mapping”.

### Layout
- **Card**: **`<u-card title="Title" :padding="32">Content</u-card>`**. When the block has title + right content (e.g. switch, link), use **`<u-card :padding="32">`** + **`<u-section title="Title">`** + **`<template #right>...</template>`**. Do not use `<view class="card">` + `<view class="card-header">` + `<text class="card-title">`.
- **Section header (with right)**: **`<u-section title="Section Title">`** + **#right** slot. Do not use custom card-header-row.
- **Flex Grid**: `<u-row>`, `<u-col span="6">`.
- **Gap**: `<u-gap height="20" bgColor="#f3f4f6"></u-gap>`.
- **Divider**: **`<u-line color="#e5e7eb" margin="...">`** or **`<u-divider text="End">`**. Do not use only view + border style.
- **Label hints / tip text**: **`<u-text text=" (optional)" type="info" size="24" />`**, **`<u-text type="warning" size="24" />`**, etc. Do not use `<text class="label-optional">`, `.tips-text`, `.tips-warn`, `.unit`.

### Buttons
- **Tag**: `<u-button>` — type: primary, success, info, warning, error; size: large, normal, small, mini; shape: circle, round; props: plain, disabled, loading, icon; event: @click.

### Forms
- **Wrapper**: `<u-form :model="form" ref="uForm">`; methods: validate(), validateField(), resetFields(), clearValidate().
- **Item**: `<u-form-item label="Name" prop="name" borderBottom>` — custom label: use **#label** or **v-slot:label** (Vue 3). **All slots in Vue 3 must use `#slotname` or `v-slot:slotname`**; never use `slot="label"` or `slot="suffix"`. Example: `<template #label><text>Label</text><u-text text=" (optional)" type="info" size="24" /></template>`. Do not use `<text class="sub">` for hints. For u-input suffix icon, use `<template #suffix>...</template>`.
- **Input**: `<u-input v-model="form.name" border="none" placeholder="Please input">` — props: type (text | number | password | textarea | **select**), size, disabled, readonly, clearable; for **type="select"** use **:select-open="show"** (bound to picker visibility) and **@click** to set show=true; pair with **u-picker** or **u-action-sheet** for options.
- **Picker (single column)**: `<u-picker v-model="show" mode="selector" :range="options" @confirm="onConfirm">` — use **v-model** for show/hide (not **:show**). **:range** must be a **1D array** (e.g. `['A','B','C']`), not 2D like `[['A','B','C']]`. Do **not** use **:columns**. **@confirm** receives selection (array of indices per official doc); set value with `options[e[0]]` or `options[e.value?.[0]]`. Close picker in handler: `show = false`.
- **Radio**: `<u-radio-group v-model="form.value">` + `<u-radio label="Display text" value="opt1">` — use **value** (not name) for the option value; **label** for display. **active-color** on group or radio. Horizontal row: **wrap="false"** (default). Do not use customStyle or placement (not in API).
- **Upload**: `<u-upload :fileList="fileList1" @afterRead="afterRead" ...></u-upload>`

### Navigation
- **Navbar**: `<u-navbar title="Home" @leftClick="leftClick" :autoBack="true">`
- **Tabs**: **Always use `<u-tabs>` for tab switchers**; do **not** replace with custom `<view class="tab-header">` or raw divs. Use `<u-tabs :list="list1" :current="current" @change="onChange">` — list items `[{ name: 'Tab1' }, ...]`; bind **:current** (0-based index); **@change(index)** receives number, set `current = index`. Use **active-color** / **inactive-color** (e.g. `#2979ff`). Do not use lineColor, activeStyle, inactiveStyle, itemStyle, or custom HTML tabs.
- **IndexList**: `<u-index-list :indexList="indexList">...</u-index-list>`

### List & Data
- **SwipeAction**: `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>`
- **List**: `<u-list @scrolltolower="scrolltolower">...</u-list>` (Load more)
- **Grid**: `<u-grid :col="3">...</u-grid>`
- **Waterfall**: `<u-waterfall v-model="flowList">...</u-waterfall>`

### Feedback
- **Toast**: In template `<u-toast ref="uToast"></u-toast>`; JS: `uni.$u.toast('Hello')`.
- **Code**: `<u-code :seconds="60" @end="end"></u-code>` (SMS countdown)

### Icons
- **Tag**: `<u-icon name="photo" color="#2979ff" size="28"></u-icon>`

## 3. Component API and full index
- **Full component list**: See [references/component-index.md](component-index.md) for all uView Pro components (80+) with minimal usage; **consult it when generating pages** so you use u-modal, u-popup, u-action-sheet, u-empty, u-avatar, u-badge, u-picker, u-calendar, etc., instead of raw HTML.
- **API details**: See [api/component-api.md](../api/component-api.md) for Button / Input / Form / Toast / Navbar / Tabs / List / SwipeAction / Upload props and events.

## 4. Script Setup (Vue 3)
- Use `<script setup lang="ts">`.
- Import hooks/utils from uview-pro if needed; rely on global `uni.$u` for trim, test, route, http.

## 5. Invariants and anti-patterns

- **Use framework components when available**: Do not use generic `<view>` / `<text>` + custom class when a u-* component exists. **Card** → **u-card** (with `title` or + **u-section** for title+right). **Secondary label / hint** → **u-text** (type="info"/"warning", size="24"). **Divider** → **u-line** / **u-divider**. No `.card`, `.card-header`, `.card-title`, `.label-optional`, `.tips-text`, `.tips-warn`, `.unit` in templates.
- **Use u-* only**: Do not use raw `<button>`, `<input>`, `<select>`, `<a>` for interactive UI when a u-* component exists. Prefer `<u-button>`, `<u-input>`, `<u-select>`, `<u-link>`.
- **Tabs**: Use **:current** and **@change(index)**; props **active-color**, **inactive-color**. Do not use lineColor, activeStyle, inactiveStyle, itemStyle.
- **Picker**: Use **v-model** for visibility; **mode="selector"** and **:range** (1D array) for single-column; **@confirm** returns selection (see official Picker doc). Do not use :show or :columns.
- **Radio**: Use **value** and **label** on u-radio; v-model on u-radio-group binds the selected **value**. Do not use name (deprecated) or customStyle.
- **Slots (Vue 3)**: Always **#slotname** or **v-slot:slotname** (e.g. **#label**, **#suffix**, **#right**). Never **slot="label"** or **slot="suffix"** — these are invalid in Vue 3 and will not work.
- **Tab switcher**: Always use **u-tabs**; never implement tabs with custom `<view class="tab-item">` / divs.
- **Modals/dialogs**: Use `<u-modal>` or `<u-popup>`, not custom div + fixed.
- **Bottom sheet / action menu**: Use `<u-action-sheet>` or `<u-popup mode="bottom">`, not custom overlay.
- **Empty state**: Use `<u-empty>`, not plain text "No data".
- **Loading**: Use `<u-loading>` or `<u-loading-popup>`, not raw div.
- **Discover components**: Before drafting a page, consult [references/component-index.md](component-index.md) for the full uView Pro component list and minimal usage; choose the right u-* for each design element.
- Register pages in `pages.json`; use rpx for responsive layout.
- Keep section spacing consistent within a screen.
