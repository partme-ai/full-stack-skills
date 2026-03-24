# Element Plus Component Index (with official doc links)

**Use framework components when available; do not replace with generic div/span + custom class.** Use **el-card** for cards, **el-alert** for tips/notices. When generating pages **prefer el-\* components from this table**; avoid raw `<button>`, `<input>`, or `<div class="card">` when an Element Plus component exists. Overview: https://cn.element-plus.org/zh-CN/component/overview.html

Each row links to the official doc (Doc column). Base: https://cn.element-plus.org/zh-CN/component/

| Component | Tag | Doc |
|-----------|-----|-----|
| Button | `<el-button type="primary">` | [button](https://cn.element-plus.org/zh-CN/component/button.html) |
| Row, Col | `<el-row :gutter="20">`, `<el-col :span="12">` | [layout](https://cn.element-plus.org/zh-CN/component/layout.html) |
| Container | `<el-container>`, `<el-header>`, `<el-main>` | [container](https://cn.element-plus.org/zh-CN/component/container.html) |
| Form | `<el-form :model="form">` | [form](https://cn.element-plus.org/zh-CN/component/form.html) |
| Input | `<el-input v-model="form.name">` | [input](https://cn.element-plus.org/zh-CN/component/input.html) |
| Select | `<el-select>` + `<el-option>` | [select](https://cn.element-plus.org/zh-CN/component/select.html) |
| Switch | `<el-switch v-model="form.delivery">` | [switch](https://cn.element-plus.org/zh-CN/component/switch.html) |
| Checkbox | `<el-checkbox>`, `<el-checkbox-group>` | [checkbox](https://cn.element-plus.org/zh-CN/component/checkbox.html) |
| Radio | `<el-radio>`, `<el-radio-group>` | [radio](https://cn.element-plus.org/zh-CN/component/radio.html) |
| Table | `<el-table :data="tableData">` + `<el-table-column>` | [table](https://cn.element-plus.org/zh-CN/component/table.html) |
| Card | `<el-card shadow="hover">` | [card](https://cn.element-plus.org/zh-CN/component/card.html) |
| Tag | `<el-tag type="success">` | [tag](https://cn.element-plus.org/zh-CN/component/tag.html) |
| Empty | `<el-empty description="No Data">` | [empty](https://cn.element-plus.org/zh-CN/component/empty.html) |
| Menu | `<el-menu>`, `<el-sub-menu>`, `<el-menu-item>` | [menu](https://cn.element-plus.org/zh-CN/component/menu.html) |
| Breadcrumb | `<el-breadcrumb>`, `<el-breadcrumb-item>` | [breadcrumb](https://cn.element-plus.org/zh-CN/component/breadcrumb.html) |
| Tabs | `<el-tabs v-model="activeName">` + `<el-tab-pane>` | [tabs](https://cn.element-plus.org/zh-CN/component/tabs.html) |
| Dialog | `<el-dialog v-model="visible" title="...">` | [dialog](https://cn.element-plus.org/zh-CN/component/dialog.html) |
| Drawer | `<el-drawer v-model="drawer" title="...">` | [drawer](https://cn.element-plus.org/zh-CN/component/drawer.html) |
| Alert | `<el-alert title="..." type="info">` | [alert](https://cn.element-plus.org/zh-CN/component/alert.html) |
| Icon | `<el-icon><Component /></el-icon>` | [icon](https://cn.element-plus.org/zh-CN/component/icon.html) |

## Design element → Component mapping (MUST use these)

| What you see in design | Use component | Do not use |
|------------------------|---------------|------------|
| Card / section block | **el-card** (shadow, #header slot) | div.card + custom header/title |
| Tips / notice text | **el-alert** (type="info"|warning|success) | div + .tips-text / custom alert class |
| Button, Form, Table, etc. | el-button, el-form, el-table, etc. | raw button, input, table |

Consult this table and [contract.md](contract.md) when mapping Stitch HTML to Element Plus.
