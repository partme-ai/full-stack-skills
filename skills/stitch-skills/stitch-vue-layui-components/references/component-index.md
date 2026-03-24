# Layui-Vue Component Index (with official doc links)

**Use framework components when available; do not replace with generic div/span + custom class.** Use **lay-card** for cards, **lay-divider** for dividers. When generating pages **prefer lay-\* components from this table**; avoid raw `<button class="layui-btn">` or `<div class="card">` when a Layui-Vue component exists. Official (zh-CN): https://www.layui-vue.com/zh-CN/components

Each component links to its official doc (Doc column). Base: https://www.layui-vue.com/zh-CN/components

| Component | Tag | Doc |
|-----------|-----|-----|
| Button | `<lay-button type="primary" size="md">` | [button](https://www.layui-vue.com/zh-CN/components/button) |
| Input | `<lay-input v-model="val" placeholder="...">` | [input](https://www.layui-vue.com/zh-CN/components/input) |
| Table | columns, dataSource, pagination | [table](https://www.layui-vue.com/zh-CN/components/table) |
| DatePicker | `<lay-date-picker v-model="date" type="date">` | [datePicker](https://www.layui-vue.com/zh-CN/components/datePicker) |
| Card | `<lay-card>` or card-style layout | [card](https://www.layui-vue.com/zh-CN/components/card) |
| PageHeader | `<lay-page-header content="Detail" @back="onBack">` | [pageheader](https://www.layui-vue.com/zh-CN/components/pageheader) |
| Result | `<lay-result status="success" title="Success" describe="...">` | [result](https://www.layui-vue.com/zh-CN/components/result) |
| Skeleton | `<lay-skeleton :rows="4">` | [skeleton](https://www.layui-vue.com/zh-CN/components/skeleton) |
| Timeline | `<lay-timeline>`, `<lay-timeline-item>` | [timeline](https://www.layui-vue.com/zh-CN/components/timeline) |
| Space | `<lay-space direction="vertical" size="md">` | [space](https://www.layui-vue.com/zh-CN/components/space) |
| Form | Layui-Vue form components | [form](https://www.layui-vue.com/zh-CN/components/form) |
| Tag | `<lay-tag>` | [tag](https://www.layui-vue.com/zh-CN/components/tag) |
| Divider | `<lay-divider>` | [divider](https://www.layui-vue.com/zh-CN/components/divider) |
| Dropdown | `<lay-dropdown>` | [dropdown](https://www.layui-vue.com/zh-CN/components/dropdown) |
| Modal / Message | Layui-Vue feedback | [message](https://www.layui-vue.com/zh-CN/components/message) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card / section block | **lay-card** | div.card + custom header/title |
| Divider line | **lay-divider** | div with border only |
| Button, Input, Table, etc. | lay-button, lay-input, lay-table, etc. | raw button, input, table |

Consult this table and [contract.md](contract.md) when mapping Stitch HTML to Layui-Vue components. Use radius 2px/4px only; flat, minimalist style.
