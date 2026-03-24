# Layui-Vue Component API (Stitch conversion reference)

Aligned with [full-stack-skills/layui-vue3](https://github.com/partme-ai/full-stack-skills/tree/main/skills/layui-vue3) and [Layui-Vue docs](https://www.layui-vue.com/zh-CN/components). Stitch HTML → Vue 3 + Layui-Vue uses component prefix `lay-` (e.g. `<lay-button>`, `<lay-input>`).

## Common conventions

- Components: lay-button, lay-input, lay-table, lay-card etc.; package `@layui/layui-vue`; import on demand or register globally.
- Common props: size (lg/md/sm/xs), disabled, loading.
- Events: @click, @change, @input.

## Button

| Use | Syntax | Notes |
|-----|--------|-------|
| Type | `type="primary" \| normal \| warm \| danger"` | primary / normal / warm / danger |
| Size | `size="lg" \| md \| sm \| xs"` | large / medium / small / extra small |
| State | `disabled`, `loading` | disabled / loading |
| Icon | `icon="layui-icon-search"` | layui icon class name |
| Event | `@click="handler"` | click |

Do not use `<button class="layui-btn">`; use `<lay-button>`.

## Input

| Use | Syntax | Notes |
|-----|--------|-------|
| Binding | `v-model="value"` | two-way |
| Placeholder | `placeholder="..."` | placeholder text |
| State | `disabled`, `readonly` | disabled / readonly |
| Icons | `prefixIcon`, `suffixIcon` | prefix / suffix icon |
| Events | `@input`, `@change`, `@blur`, `@focus` | input / change / blur / focus |

## Table

| Use | Syntax | Notes |
|-----|--------|-------|
| Columns | `columns` | column definition array |
| Data | `dataSource` | data array |
| Pagination | `pagination` | pagination config |
| Sort | `sortable` | enable sort |
| Checkbox | `checkbox` | show row checkbox |
| Events | `@change` (pagination/sort), `@select` (row select) | change and select |

## DatePicker

| Use | Syntax | Notes |
|-----|--------|-------|
| Binding | `v-model="date"` | selected date |
| Type | `type="date" \| datetime \| year \| month \| daterange"` | picker type |
| Format | `format="YYYY-MM-DD"` | display format |
| Event | `@change` | value change |

## Other components

| Component | Syntax | Notes |
|-----------|--------|-------|
| PageHeader | `<lay-page-header content="Detail" @back="onBack" />` | page header with back |
| Result | `<lay-result status="success" title="Success" describe="..." />` | result page |
| Skeleton | `<lay-skeleton :rows="4" />` | skeleton |
| Timeline | `<lay-timeline>` + `<lay-timeline-item title="Step 1">` | timeline |
| Space | `<lay-space direction="vertical" size="md">` | spacing wrapper |
| Form | `<lay-form>` + `<lay-form-item>` + `<lay-input>` etc. | form structure |
| Select | `<lay-select v-model="val" :options="options">` | select (per official API) |
| Checkbox / Radio | `<lay-checkbox>`, `<lay-radio>` | checkbox / radio (per official API) |

## Design tokens (align when converting)

- Primary: #16baaa; Danger: #FF5722; Border: #e2e2e2; Radius: 2px / 4px.
- Button height: normal 38px, small 30px, large 44px.

## References

- [references/contract.md](../references/contract.md) — design tokens and mapping rules
- [references/official.md](../references/official.md) — official docs
