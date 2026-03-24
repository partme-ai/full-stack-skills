# uView 2.0 Design Contract (Stitch HTML → uni-app Page Mapping)

When converting Stitch-generated HTML to uni-app + Vue 2 + uView 2.0, map structure and styles to the following. Align with stitch-ui-design-spec-uview (same repo) for generation-time constraints.

## 1. Design Tokens

### Colors (uView theme)
- **Primary**: `#3c9cff` (u-primary)
- **Success**: `#5ac725`, **Warning**: `#f9ae3d`, **Error**: `#f56c6c`, **Info**: `#909399`
- **Text**: u-main-color `#303133`, u-content-color `#606266`, u-tips-color `#909193`, u-light-color `#c0c4cc`
- **Surfaces**: u-bg-color `#f3f4f6`, u-border-color `#dadbde`

### Typography
- Font sizes (px): 12, 14, 16, 18, 20, 24. Titles: 600; body: 400; emphasis: 500.

### Spacing & Radius
- Spacing (px): 4, 8, 12, 16, 20, 24, 32, 40.
- Radius: 8, 12, 999. Border: #dadbde.

## 2. Component Mapping (Stitch HTML → uView 2)

**Rule: Use framework components when available; do not replace with generic view/text + custom class.** uView 2 has no Card; use **u-cell-group** + **u-cell** for card-like blocks, **u-text** for titles and label hints, **u-line** / **u-divider** for dividers. No custom `.card`, `.card-header`, `.card-title`, `.label-optional`, `.tips-text`, `.unit`.

### Layout
- **Card-like section**: **u-cell-group** with **u-cell** (title/value/label); or minimal wrapper with **u-text** for section title. Do not use `<view class="card">` + custom header/title.
- **Label hints / tip text**: **u-text** (e.g. type/size per uView Text API) for optional/hint text; do not use `<text class="label-optional">` or `.tips-text` / `.unit`.
- **Divider**: **u-line** or **u-divider**; do not use only view + border.
- **Grid**: `<u-row justify="space-between" gutter="10">`, `<u-col span="6">`.
- **Cell**: `<u-cell-group>`, `<u-cell title="Title" value="Content" />`.

### Forms
- **Form**: `<u--form :model="form" :rules="rules" ref="uForm">` or `<u-form>`; validate with `this.$refs.uForm.validate()`.
- **Input**: `<u--input v-model="form.name" />` or `<u-input border="surround">`; props: clearable, error, error-message, prefix-icon, suffix-icon.
- **Button**: `<u-button type="primary" text="Submit" @click="onSubmit">` — type: primary, success, error, warning, info; size: default, medium, mini; props: disabled, :loading, icon.

### Navigation
- **Navbar**: `<u-navbar title="Title" @leftClick="leftClick" :autoBack="true">`.
- **Tabs**: `<u-tabs :list="list1"></u-tabs>` (list = { name, ... }[]).
- **Steps**: `<u-steps :current="1">...</u-steps>`.

### List & Data
- **SwipeAction**: `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>`.
- **IndexList**: `<u-index-list :indexList="indexList">...</u-index-list>`.
- **Waterfall**: `<u-waterfall v-model="flowList">...</u-waterfall>`.

### Feedback
- **Toast**: In template `<u-toast ref="uToast" />`; call `this.$refs.uToast.show({ type: 'success', message: '...' })`.
- **Modal**: `<u-modal v-model="show" title="..." content="..." show-cancel-button @confirm @cancel>`.
- **Code**: `<u-code :seconds="60" ref="uCode" @change="codeChange"></u-code>` (SMS countdown).

## 3. Component API quick reference
- See [api/component-api.md](../api/component-api.md) for Button / Input / Form / Modal / Toast / Navbar / Tabs / SwipeAction props and events.

## 4. Invariants

- **Use framework components when available**: Do not use generic `<view>` / `<text>` + custom class when a u-* component exists. Card-like blocks → **u-cell-group** + **u-cell** or wrapper + **u-text**. Hints/tips → **u-text**. Divider → **u-line** / **u-divider**. No `.card`, `.card-header`, `.card-title`, `.label-optional`, `.tips-text`, `.unit` in templates.
- Use uView 2 component names (u-*); do not use raw HTML for buttons, forms, layout when a uView component exists.
- Register pages in `pages.json`; use rpx for responsive layout where appropriate.
- Keep section spacing consistent (e.g. 24 or 32) within a screen.
- Form: use `u--form` or `u-form` with `:model` and `:rules`; call `validate()` on submit.
