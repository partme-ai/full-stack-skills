# uView 2.0 Component API (Stitch conversion reference)

Aligned with [full-stack-skills/uview-vue2](https://github.com/partme-ai/full-stack-skills/tree/main/skills/uview-vue2) and [uView 2.0 docs](https://www.uviewui.com/components/intro.html). Stitch HTML → uni-app + Vue 2 + uView 2 uses component prefix `u-`. Runs in **uni-app pages** (`<view>` root).

## Common conventions

- Common props: custom-style, custom-class, disabled, loading.
- Page root: `<view>`; components: u-*; forms: v-model binding.

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Type | `type="primary" \| success \| error \| warning \| info"` | primary / success / error / warning / info |
| Size | `size="default" \| medium \| mini"` | default / medium / mini |
| Shape | `shape="square" \| circle"` | square / circle |
| Style | `plain` | plain |
| State | `disabled`, `:loading="loading"` | disabled / loading |
| Icon | `icon="search"` | icon name |
| Text | `text="Submit"` or default slot | button text |
| Event | `@click="handler"` | click |

Do not use `<button>`; use `<u-button>`.

## Input

| Use | Syntax | Notes |
|-----|--------|-------|
| Binding | `v-model="value"` | two-way |
| Type | `type="text" \| number \| password"` etc. | input type |
| Placeholder | `placeholder="..."` | placeholder |
| State | `clearable`, `disabled`, `error`, `error-message` | clear / disabled / error |
| Icons | `prefix-icon`, `suffix-icon` | prefix / suffix icon |
| Events | `@input`, `@change` | input / change |

## Form

| Use | Syntax | Notes |
|-----|--------|-------|
| Form | `<u--form :model="form" :rules="rules" ref="uForm">` or `<u-form>` | model and rules |
| Item | `<u-form-item label="Name" prop="name" required>` | label, prop for model key |
| Input | `<u--input v-model="form.name" />` or `<u-input border="surround">` | inside form-item |
| Methods | `this.$refs.uForm.validate()`, `resetFields()` | validate / reset |

## Modal

| Use | Syntax | Notes |
|-----|--------|-------|
| Show | `<u-modal v-model="show" title="Title" content="Content" show-cancel-button @confirm="onConfirm" @cancel="onCancel">` | v-model controls visibility |
| Props | `confirm-text`, `cancel-text` | confirm / cancel text |
| Events | `@confirm`, `@cancel` | confirm / cancel |

## Toast

| Use | Syntax | Notes |
|-----|--------|-------|
| Call | `this.$refs.uToast.show({ type: 'success', message: 'Success' })` | via ref |
| Options | type (success/error/warning/loading), message, duration, position | config |

## Layout and navigation

| Component | Syntax | Notes |
|-----------|--------|-------|
| Grid | `<u-row justify="space-between" gutter="10">`, `<u-col span="6">` | grid |
| Cell | `<u-cell-group>`, `<u-cell title="Title" value="Content" />` | list group / cell |
| Navbar | `<u-navbar title="Title" @leftClick="leftClick" :autoBack="true">` | navbar |
| Tabs | `<u-tabs :list="list1"></u-tabs>` | list = { name, ... }[] |
| Steps | `<u-steps :current="1">...</u-steps>` | steps |

## List and feedback

| Component | Syntax | Notes |
|-----------|--------|-------|
| SwipeAction | `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>` | swipe actions |
| IndexList | `<u-index-list :indexList="indexList">...</u-index-list>` | index list (contacts) |
| Waterfall | `<u-waterfall v-model="flowList">...</u-waterfall>` | waterfall |
| Code | `<u-code :seconds="60" ref="uCode" @change="codeChange"></u-code>` | SMS countdown |

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
