# Element Plus Official References

- **Official (zh-CN)**: https://element-plus.org/zh-CN
- **Official (en-US)**: https://element-plus.org/en-US/
- **Design Guide**: https://element-plus.org/en-US/guide/design
- **Component Overview**: https://element-plus.org/en-US/component/overview
- **GitHub**: https://github.com/element-plus/element-plus

## Per-component doc links (each component → official doc)

Base URL: `https://cn.element-plus.org/zh-CN/component/` + `{name}.html`

| Component | Doc |
|-----------|-----|
| Button | https://cn.element-plus.org/zh-CN/component/button.html |
| Layout (Row, Col) | https://cn.element-plus.org/zh-CN/component/layout.html |
| Container | https://cn.element-plus.org/zh-CN/component/container.html |
| Form | https://cn.element-plus.org/zh-CN/component/form.html |
| Input | https://cn.element-plus.org/zh-CN/component/input.html |
| Select | https://cn.element-plus.org/zh-CN/component/select.html |
| Switch | https://cn.element-plus.org/zh-CN/component/switch.html |
| Checkbox | https://cn.element-plus.org/zh-CN/component/checkbox.html |
| Radio | https://cn.element-plus.org/zh-CN/component/radio.html |
| Table | https://cn.element-plus.org/zh-CN/component/table.html |
| Card | https://cn.element-plus.org/zh-CN/component/card.html |
| Tag | https://cn.element-plus.org/zh-CN/component/tag.html |
| Empty | https://cn.element-plus.org/zh-CN/component/empty.html |
| Menu | https://cn.element-plus.org/zh-CN/component/menu.html |
| Breadcrumb | https://cn.element-plus.org/zh-CN/component/breadcrumb.html |
| Tabs | https://cn.element-plus.org/zh-CN/component/tabs.html |
| Dialog | https://cn.element-plus.org/zh-CN/component/dialog.html |
| Drawer | https://cn.element-plus.org/zh-CN/component/drawer.html |
| Alert | https://cn.element-plus.org/zh-CN/component/alert.html |
| Icon | https://cn.element-plus.org/zh-CN/component/icon.html |

Full table with tags: [component-index.md](component-index.md).

## Usage in This Skill

1. Map Stitch HTML to Element Plus components (`el-row`, `el-col`, `el-button`, `el-form`, `el-input`, etc.) per [references/contract.md](contract.md).
2. Use design tokens (primary, success, typography, radius) from the Design Guide.
3. Prefer prop-driven configuration (e.g. `el-table :data`, `el-table-column`) over raw HTML.
