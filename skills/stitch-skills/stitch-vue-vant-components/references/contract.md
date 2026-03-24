# Vant 4 Design Contract (Stitch HTML → Vue SFC Mapping)

When converting Stitch-generated HTML to Vue 3 + Vant 4, map structure and styles to the following. Align with stitch-ui-design-spec-vant (same repo) for generation-time constraints. **Mobile-first** (375px base); respect safe areas.

## 1. Design Tokens

### Colors (Vant 4 Defaults)
- **Primary**: `#1989fa` (Blue)
- **Success**: `#07c160` (Green)
- **Warning**: `#ff976a` (Orange)
- **Danger**: `#ee0a24` (Red)
- **Text Main**: `#323233`, **Text Regular**: `#969799`
- **Border**: `#ebedf0`
- **Background**: `#f7f8fa` (Page) / `#ffffff` (Card)

### Typography
- Font: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Segoe UI, Arial, Roboto, 'PingFang SC', 'miui', 'Hiragino Sans GB', 'Microsoft Yahei', sans-serif.
- Base: 14px; large buttons/titles: 16px.

### Spacing & Radius
- Padding: 4px / 8px / 12px / 16px (van-padding-*).
- Radius: 2px / 4px / 8px / 999px (van-radius-*).

## 2. Component Mapping (Stitch HTML → Vant 4)

**Rule: Use framework components when available; do not replace with generic div/span + custom class.** Use **van-cell-group** (inset for card style) for section blocks, **van-cell** for rows with title/value/label, **van-field** label for form hints. No custom `.card`, `.card-header`, `.card-title`, `.tips-text` when van-* equivalents exist.

### Layout
- **Container**: `<van-config-provider>` or `<div class="container">`.
- **Grid**: `<van-row>`, `<van-col span="12">`.
- **Card-like section**: **van-cell-group** with `inset` for card style; **van-cell** for rows. Do not use `<div class="card">` + custom header/title.
- **Cell Group**: `<van-cell-group inset>` (card style) or `<van-cell-group>` (full width).

### Basic
- **Button**: `<van-button type="primary" size="large" round>` — types: primary, success, warning, danger, default; sizes: large, normal, small, mini; props: plain, hairline, disabled, loading, round, block.
- **Cell**: `<van-cell title="Title" value="Content" label="Description" is-link />`
- **Icon**: `<van-icon name="chat-o" />`
- **Image**: `<van-image width="100" height="100" src="..." radius="4" />`

### Forms
- **Form**: `<van-form @submit="onSubmit">`
- **Field**: `<van-field v-model="value" label="Label" placeholder="Placeholder" :rules="[{ required: true }]" />`
- **Search**: `<van-search v-model="value" placeholder="Search..." />`
- **Checkbox/Radio**: `<van-checkbox v-model="checked">Label</van-checkbox>`
- **Picker**: `<van-picker :columns="columns" />` (or inside `<van-popup position="bottom">`)

### Business (E-commerce)
- **Product Card**: `<van-card num="2" price="2.00" desc="Desc" title="Title" thumb="..." />`
- **Submit Bar**: `<van-submit-bar :price="3050" button-text="Submit" @submit="onSubmit" />`
- **Address**: `<van-address-list>`, `<van-address-edit>`
- **Coupon**: `<van-coupon-list>`
- **Swipe Cell**: `<van-swipe-cell>` for delete actions on list items.

### Feedback & Navigation
- **NavBar**: `<van-nav-bar title="Title" left-text="Back" left-arrow />`
- **Tabbar**: `<van-tabbar v-model="active"><van-tabbar-item icon="home-o">Home</van-tabbar-item></van-tabbar>`
- **Sidebar**: `<van-sidebar>`, `<van-sidebar-item>` (category pages)
- **Tabs**: `<van-tabs v-model="active"><van-tab title="Tab 1">...</van-tab></van-tabs>`
- **ActionSheet**: `<van-action-sheet v-model:show="show" :actions="actions" />`
- **Empty**: `<van-empty description="No Data" />`

## 3. Component API quick reference
- See [api/component-api.md](../api/component-api.md) for Button / Cell / Form / Dialog / Toast / Popup / NavBar / Tabbar props and events.

## 4. Invariants

- **Use framework components when available**: Card-like blocks → **van-cell-group** (inset) + **van-cell**; form hints → **van-field** label/label slot. No custom .card, .card-header, .card-title, .tips-text when van-* components exist.
- Page background: `#f7f8fa`.
- Prefer `<van-cell-group inset>` for grouped lists.
- Wrap block submit buttons in `<div style="margin: 16px;">` at form bottom.
- NavBar at top (fixed if needed); Tabbar at bottom for main entry.
- Do not use raw `<button>` when `<van-button>` applies; do not use `<div class="card">` when `<van-cell-group>` applies.
- Form: use `van-field` with `name` and `:rules`; submit via `<van-form @submit>`.
