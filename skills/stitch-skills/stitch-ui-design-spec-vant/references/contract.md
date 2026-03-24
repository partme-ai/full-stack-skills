# Vant Design Contract (Vant 4 / Vue 3)

This reference contains:

- Hard constraints prefix (paste-ready)
- Layout invariants for beautify mode
- Component snippets (Vant look & feel)

---

## Trigger Keywords

Use this contract when the request mentions **Stitch** and any of the following keywords:

- `vant`
- `vant4`
- `vant-ui`

---

## Hard Constraints (Must Follow)

### Design Tokens (Vant 4 Defaults)

**Colors**:
- **Primary**: `#1989fa` (Blue)
- **Success**: `#07c160` (Green)
- **Warning**: `#ff976a` (Orange)
- **Danger**: `#ee0a24` (Red)
- **Text Main**: `#323233`
- **Text Regular**: `#969799`
- **Border**: `#ebedf0`
- **Background**: `#f7f8fa` (Page background) / `#ffffff` (Card background)

**Typography**:
- Font Family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Segoe UI, Arial, Roboto, 'PingFang SC', 'miui', 'Hiragino Sans GB', 'Microsoft Yahei', sans-serif.
- Base Size: 14px (root), 16px (large buttons/titles).

**Spacing & Radius**:
- **Padding**: `van-padding-base` (4px), `van-padding-xs` (8px), `van-padding-sm` (12px), `van-padding-md` (16px).
- **Radius**: `van-radius-sm` (2px), `van-radius-md` (4px), `van-radius-lg` (8px), `van-radius-max` (999px).

### Layout Invariants

- **Mobile First**: Design for narrow screens (375px width base).
- **Flexbox**: Use Flexbox for alignment (`display: flex`, `justify-content`, `align-items`).
- **Safe Area**: Respect top and bottom safe areas for mobile devices.

---

## Component Contracts (Vant 4 Specifics)

### Layout Components
- **Container**: `<div class="container">` or `<van-config-provider>`.
- **Grid**: `<van-row>` and `<van-col span="12">`.
- **Cell Group**: `<van-cell-group inset>` (Card style) or `<van-cell-group>` (Full width).

### Basic Components
- **Button**: `<van-button type="primary" size="large" round>`
    - Types: `primary`, `success`, `warning`, `danger`, `default`.
    - Sizes: `large`, `normal`, `small`, `mini`.
    - Props: `plain`, `hairline`, `disabled`, `loading`, `round`, `block`.
- **Cell**: `<van-cell title="Title" value="Content" label="Description" is-link />`
- **Icon**: `<van-icon name="chat-o" />`
- **Image**: `<van-image width="100" height="100" src="..." radius="4" />`

### Form Components
- **Form**: `<van-form @submit="onSubmit">`
- **Field**: `<van-field v-model="value" label="Label" placeholder="Placeholder" :rules="[{ required: true }]" />`
- **Search**: `<van-search v-model="value" placeholder="Search..." />`
- **Checkbox/Radio**: `<van-checkbox v-model="checked">Label</van-checkbox>`
- **Picker**: `<van-picker :columns="columns" />` (or `<van-popup position="bottom"><van-picker ... /></van-popup>`)
- **Date/Time**: `<van-date-picker>` / `<van-time-picker>`.

### Business Components (E-commerce)
- **Product Card**: `<van-card num="2" price="2.00" desc="Desc" title="Title" thumb="..." />`
- **Submit Bar**: `<van-submit-bar :price="3050" button-text="Submit" @submit="onSubmit" />`
- **Address**: `<van-address-list v-model="chosenAddressId" :list="list" />` / `<van-address-edit ... />`
- **Coupon**: `<van-coupon-list ... />`
- **Cart**: Use `<van-swipe-cell>` wrapping `<van-card>` for delete actions.

### Feedback & Navigation
- **NavBar**: `<van-nav-bar title="Title" left-text="Back" left-arrow />`
- **Tabbar**: `<van-tabbar v-model="active"><van-tabbar-item icon="home-o">Home</van-tabbar-item></van-tabbar>`
- **Sidebar**: `<van-sidebar v-model="active"><van-sidebar-item title="Label" /></van-sidebar>` (Category pages)
- **Tabs**: `<van-tabs v-model="active"><van-tab title="Tab 1">...</van-tab></van-tabs>`
- **ActionSheet**: `<van-action-sheet v-model:show="show" :actions="actions" />`
- **Empty**: `<van-empty description="No Data" />`

---

## Layout Rules

1.  **Page Background**: Always set the page background to `#f7f8fa` (Vant gray).
2.  **Card Style**: Prefer `<van-cell-group inset>` for grouped lists to give a modern card look.
3.  **Submit Buttons**: Use `<div style="margin: 16px;">` to wrap block-level submit buttons at the bottom of forms.
4.  **Navigation**: Ensure `<van-nav-bar>` is at the top (fixed if needed) and `<van-tabbar>` at the bottom (if main entry).
