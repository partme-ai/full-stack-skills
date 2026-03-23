# Vant Vue 3 Official Mapping

This file maps the local skill content to the official Vant documentation entry points.

## Official entry points

- Official website: https://vant-ui.github.io/
- Official guide: https://vant-ui.github.io/vant/#/zh-CN

## Local coverage map

| Official area | Official section name | Local file | Coverage |
|---|---|---|---|
| Guide | Quickstart / 快速开始 | `examples/getting-started/installation.md` | Local setup instructions |
| Guide | Basic Usage / 基本用法 | `examples/getting-started/basic-usage.md` | Local starter usage |
| Guide | Project setup patterns | `templates/project-setup.md` | Local scaffold template |
| Component | Button / 按钮 | `examples/components/button.md` | Local example |
| Component | Cell / 单元格 | `examples/components/cell.md` | Local example |
| Component | Form / 表单 | `examples/components/form.md` | Local example |
| Component | Dialog / 弹出层中的对话交互 | `examples/components/dialog.md` | Local example |
| Component | Popup / 弹出层 | `examples/components/popup.md` | Local example |
| Component | Toast / 轻提示 | `examples/components/toast.md` | Local example |
| Global config | ConfigProvider | `api/config-provider.md` | Local API guidance |
| Theme | Theme customization / 主题定制 | `examples/advanced/theme-customization.md` | Local example |
| API summary | Common component APIs | `api/components.md` | Local summary |

## Coverage boundary

This skill does **not** provide local example files for every Vant component.

Examples of components not covered locally include:

- Tabs
- Tabbar
- NavBar
- Icon
- Image
- Calendar
- Picker
- Grid
- Card
- Badge
- Loading
- ActionSheet

When the user requests one of these:

1. Use the official guide as the primary reference.
2. State clearly that the skill has no dedicated local example file for that component.
3. Follow the coding style already used in this skill:
   - Vue 3 `script setup`
   - imports from `vant`
   - mobile-first examples
   - concise prop/event explanation

## Navigation rule

Only reference local files that actually exist in:

- `examples/getting-started/`
- `examples/components/`
- `examples/advanced/`
- `api/`
- `templates/`

Do not mention local files that are not present in the skill directory.
