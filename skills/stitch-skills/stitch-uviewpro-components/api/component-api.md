# uView Pro Component API (Stitch conversion reference)

Aligned with [full-stack-skills/uview-pro-vue3](https://github.com/partme-ai/full-stack-skills/tree/main/skills/uview-pro-vue3) and [uView Pro docs](https://uviewpro.cn/zh/components/intro.html). uView Pro uses the **u-** prefix (same as uView 2; package is `uview-pro`, Vue 3). Use **rpx** for typography/spacing and **&lt;script setup&gt;**.

## Common conventions

- Common props: custom-class, custom-style, disabled, loading.
- Tools: `uni.$u.toast()`, `uni.$u.route()`, etc.

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Type | `type="primary" \| success \| info \| warning \| error"` | primary / success / info / warning / error |
| Size | `size="large" \| normal \| small \| mini"` | large / normal / small / mini |
| Shape | `shape="circle" \| round"` | circle / round |
| Style | `plain` | plain style |
| State | `disabled`, `loading` | disabled / loading |
| Icon | `icon="search"` | icon name |
| Event | `@click` | click |

Do not use raw `<button>`; use `<u-button>`.

## Input

| Use | Syntax | Notes |
|-----|--------|-------|
| Binding | `v-model="form.name"` | two-way |
| Type | `type="text" \| number \| password \| textarea"` | input type |
| Size | `size="large" \| normal \| small"` | size |
| State | `disabled`, `readonly`, `clearable` | disabled / readonly / clear |
| Border | `border="none" \| surround"` etc. | border style |
| Icons | `prefix-icon`, `suffix-icon` | prefix / suffix icon |
| Events | `@input`, `@change`, `@focus`, `@blur` | input / change / focus / blur |

## Form

| Use | Syntax | Notes |
|-----|--------|-------|
| Form | `<u-form :model="form" ref="uForm">` | model binds data |
| Item | `<u-form-item label="Name" prop="name" borderBottom>` | custom label: use #label or v-slot:label (Vue 3), not slot="label" |
| Input | `<u-input v-model="form.name" border="none" placeholder="Please input">` | inside form-item |
| Methods | `validate()`, `validateField()`, `resetFields()`, `clearValidate()` | validate / reset |
| Event | `@validate` | validation event |

## Toast

| Use | Syntax | Notes |
|-----|--------|-------|
| Template | `<u-toast ref="uToast"></u-toast>` | mount in page |
| Call | `uni.$u.toast('message')` or ref.show({ ... }) | global or ref |
| Options | type, message, duration, etc. | per official API |

## Layout and navigation

| Component | Syntax | Notes |
|-----------|--------|-------|
| Grid | `<u-row>`, `<u-col span="6">` | grid |
| Gap | `<u-gap height="20" bgColor="#f3f4f6"></u-gap>` | vertical gap |
| Divider | `<u-divider text="End"></u-divider>` | divider |
| Navbar | `<u-navbar title="Home" @leftClick="leftClick" :autoBack="true">` | navbar |
| Tabs | `<u-tabs :list="list1" :current="current" @change="(i)=>current=i" active-color="#2979ff" inactive-color="#606266">` | list=[{name:'A'},...]; @change(index: number); do not use lineColor/activeStyle/itemStyle |
| Picker (single) | `<u-picker v-model="show" mode="selector" :range="options" @confirm="onConfirm">` | v-model=show; :range=1D array; @confirm(e) per official doc |
| Radio | `<u-radio-group v-model="val"><u-radio label="A" value="a"></u-radio></u-radio-group>` | value + label; no name/customStyle |
| IndexList | `<u-index-list :indexList="indexList">...</u-index-list>` | index list |

## List and feedback

| Component | Syntax | Notes |
|-----------|--------|-------|
| SwipeAction | `<u-swipe-action><u-swipe-action-item ...>...</u-swipe-action-item></u-swipe-action>` | swipe actions |
| List | `<u-list @scrolltolower="scrolltolower">...</u-list>` | list with load more |
| Grid | `<u-grid :col="3">...</u-grid>` | grid menu |
| Waterfall | `<u-waterfall v-model="flowList">...</u-waterfall>` | waterfall |
| Upload | `<u-upload :fileList="fileList1" @afterRead="afterRead" ...></u-upload>` | upload |
| Code | `<u-code :seconds="60" @end="end"></u-code>` | SMS countdown |
| Icon | `<u-icon name="photo" color="#2979ff" size="28"></u-icon>` | icon |

## Script Setup (Vue 3)

- Use `<script setup lang="ts">`; reactive with ref, reactive.
- Route: `uni.$u.route('/pages/xxx/xxx')`; request: `uni.$u.http.post(...)`; validation: `uni.$u.test.mobile(str)` etc.

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
