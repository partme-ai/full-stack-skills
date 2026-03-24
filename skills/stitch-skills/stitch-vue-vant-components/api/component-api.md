# Vant Vue 3 Component API (Stitch conversion reference)

Aligned with [full-stack-skills/vant-vue3](https://github.com/partme-ai/full-stack-skills/tree/main/skills/vant-vue3) and [Vant docs](https://vant-ui.github.io/vant/#/zh-CN). Stitch HTML → Vue 3 + Vant 4 uses component prefix `van-`. **Mobile-first** (375px base).

## Common conventions

- Common props: custom-style, custom-class, disabled, loading.
- Overlay components use v-model:show for visibility (Vue 3).

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Type | `type="primary" \| success \| warning \| danger \| default"` | primary / success / warning / danger / default |
| Size | `size="large" \| normal \| small \| mini"` | large / normal / small / mini |
| Shape | `shape="square" \| round"` | square / round |
| Style | `plain`, `hairline` | plain / hairline |
| State | `disabled`, `loading` | disabled / loading |
| Block | `block` | full width |
| Icon | `icon="plus"`, `icon="search"` | icon name |
| Event | `@click` | click |

Do not use `<button>`; use `<van-button>` only.

## Cell

| Use | Syntax | Notes |
|-----|--------|-------|
| Title/Value | `title="..."`, `value="..."` | left title, right content |
| Label | `label="..."` | description below title |
| Arrow | `is-link`, `arrow-direction="left" \| up \| down"` | show arrow, direction |
| Icon | `icon="..."` | left icon |
| Event | `@click` | click |

## Form

| Use | Syntax | Notes |
|-----|--------|-------|
| Form | `<van-form @submit="onSubmit" @failed="onFailed">` | submit / validation failed |
| Field | `<van-field v-model="val" name="fieldName" label="Label" placeholder="..." :rules="[{ required: true }]" />` | name required for validation |
| Validation | :rules on field; van-form validates on submit | validate(), resetValidation() |
| Search | `<van-search v-model="keyword" placeholder="Search..." />` | search input |

## Dialog

| Use | Syntax | Notes |
|-----|--------|-------|
| Show | `<van-dialog v-model:show="show" title="Title" message="Content" show-cancel-button @confirm="onConfirm" @cancel="onCancel">` | v-model:show controls visibility |
| Methods | `showDialog(options)`, `showConfirmDialog(options)` | call via methods |

## Toast

| Use | Syntax | Notes |
|-----|--------|-------|
| Call | `showToast(message \| options)` | global method |
| Shortcuts | `showSuccessToast(message)`, `showFailToast(message)`, `showLoadingToast(message)` | success / fail / loading |
| Options | type, message, duration, position (top/middle/bottom) | config |

## Popup

| Use | Syntax | Notes |
|-----|--------|-------|
| Show | `<van-popup v-model:show="show" position="bottom" round closeable>` | position: top, bottom, left, right, center |
| Props | round, closeable, close-icon-position, overlay | round, close button, overlay |
| Event | `@close` | close |

## Navigation and layout

| Component | Syntax | Notes |
|-----------|--------|-------|
| NavBar | `<van-nav-bar title="Title" left-text="Back" left-arrow @click-left="onBack" />` | top nav |
| Tabbar | `<van-tabbar v-model="active"><van-tabbar-item icon="home-o">Home</van-tabbar-item></van-tabbar>` | bottom tabs |
| Tabs | `<van-tabs v-model="active"><van-tab title="Tab 1">...</van-tab></van-tabs>` | tabs |
| Grid | `<van-row>`, `<van-col span="12">` | grid |
| Cell Group | `<van-cell-group>`, `<van-cell-group inset>` | list group (inset = card style) |

## Business components (e-commerce etc.)

| Component | Syntax | Notes |
|-----------|--------|-------|
| Card | `<van-card num="2" price="2.00" desc="Desc" title="Title" thumb="..." />` | product card |
| SubmitBar | `<van-submit-bar :price="3050" button-text="Submit" @submit="onSubmit" />` | submit bar (price in cents) |
| Empty | `<van-empty description="No Data" />` | empty state |
| SwipeCell | `<van-swipe-cell>` wrapping list item, right slide for actions | swipe to delete etc. |

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
