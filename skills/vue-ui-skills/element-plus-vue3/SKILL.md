---
name: element-plus-vue3
description: Provides comprehensive guidance for Element Plus Vue 3 component library including installation, components, themes, internationalization, and API reference. Use when the user asks about Element Plus for Vue 3, needs to build Vue 3 applications with Element Plus, or customize component styles.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Element Plus in a Vue 3 project
- Use Element Plus components in Vue 3 applications
- Configure Element Plus (global config, i18n, theme, etc.)
- Use form components (Button, Input, Form, etc.)
- Use data display components (Table, Card, etc.)
- Use feedback components (Message, Notification, Dialog, etc.)
- Use navigation components (Menu, Tabs, etc.)
- Customize component styles and themes
- Handle component events
- Understand Element Plus API and methods
- Troubleshoot Element Plus issues

## How to use this skill

This skill is organized to match the Element Plus official documentation structure (https://element-plus.org/zh-CN/, https://element-plus.org/en-US/guide/design, https://element-plus.org/en-US/component/overview). When working with Element Plus:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/guide/installation.md`
   - Quick Start/快速开始 → `examples/guide/quick-start.md`
   - Design/设计 → `examples/guide/design.md`
   - Components/组件 → `examples/components/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (使用指南)**:
   - `examples/guide/installation.md` - Installation guide
   - `examples/guide/quick-start.md` - Quick start guide
   - `examples/guide/design.md` - Design guidelines
   - `examples/guide/i18n.md` - Internationalization
   - `examples/guide/theme.md` - Theme customization
   - `examples/guide/global-config.md` - Global configuration

   **Components (组件)**:
   - `examples/components/overview.md` - Components overview
   - `examples/components/button.md` - Button component
   - `examples/components/input.md` - Input component
   - `examples/components/form.md` - Form component
   - `examples/components/table.md` - Table component
   - `examples/components/card.md` - Card component
   - `examples/components/dialog.md` - Dialog component
   - `examples/components/message.md` - Message component
   - `examples/components/notification.md` - Notification component
   - `examples/components/menu.md` - Menu component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/date-picker.md` - DatePicker component
   - `examples/components/select.md` - Select component
   - `examples/components/switch.md` - Switch component
   - `examples/components/checkbox.md` - Checkbox component
   - `examples/components/radio.md` - Radio component
   - `examples/components/upload.md` - Upload component
   - `examples/components/pagination.md` - Pagination component
   - `examples/components/tree.md` - Tree component
   - `examples/components/tree-select.md` - TreeSelect component
   - `examples/components/transfer.md` - Transfer component
   - `examples/components/descriptions.md` - Descriptions component
   - `examples/components/avatar.md` - Avatar component
   - `examples/components/badge.md` - Badge component
   - `examples/components/tag.md` - Tag component
   - `examples/components/empty.md` - Empty component
   - `examples/components/loading.md` - Loading component
   - `examples/components/popover.md` - Popover component
   - `examples/components/tooltip.md` - Tooltip component
   - `examples/components/dropdown.md` - Dropdown component
   - `examples/components/drawer.md` - Drawer component
   - `examples/components/popconfirm.md` - Popconfirm component

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Element Plus is for Vue 3 only
   - Components use Vue 3 Composition API
   - Examples include both Options API and Composition API
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/component-api.md` - Component API reference
   - `api/props-and-events.md` - Props and events reference
   - `api/global-config.md` - Global configuration API

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/component-usage.md` - Component usage templates
   - `templates/project-setup.md` - Project setup templates

### 1. Understanding Element Plus

Element Plus is a Vue 3 component library that provides a rich set of UI components following Element Design principles.

**Key Concepts**:
- **Vue 3 Support**: Built for Vue 3 with Composition API
- **Design System**: Follows Element Design language
- **Rich Components**: 60+ components for various use cases
- **Theme Customization**: Support for theme customization
- **i18n**: Internationalization support
- **TypeScript**: Full TypeScript support

### 2. Installation

**Using npm**:

```bash
npm install element-plus
```

**Using yarn**:

```bash
yarn add element-plus
```

**Using pnpm**:

```bash
pnpm add element-plus
```

### 3. Basic Setup

**Full Import**:

```javascript
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
```

**On-Demand Import**:

```javascript
import { ElButton, ElInput } from 'element-plus'
import 'element-plus/es/components/button/style/css'
import 'element-plus/es/components/input/style/css'
```


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://element-plus.org/en-US/guide/design

**Components (组件)**:
- See component files in `examples/components/` → https://element-plus.org/en-US/component/overview

## Examples and Templates

This skill includes detailed examples organized to match the official documentation structure. All examples are in the `examples/` directory (see mapping above).

**To use examples:**
- Identify the topic from the user's request
- Load the appropriate example file from the mapping above
- Follow the instructions, syntax, and best practices in that file
- Adapt the code examples to your specific use case

**To use templates:**
- Reference templates in `templates/` directory for common scaffolding
- Adapt templates to your specific needs and coding style

## API Reference

Detailed API documentation is available in the `api/` directory, organized to match the official Element Plus API documentation structure:

### Component API (`api/component-api.md`)
- Component props and events
- Component methods
- Component slots

### Props and Events (`api/props-and-events.md`)
- Common props
- Common events
- Event handling

### Global Configuration (`api/global-config.md`)
- Global configuration options
- ConfigProvider usage
- Theme configuration

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use on-demand import**: Import only the components you need to reduce bundle size
2. **Use Composition API**: Prefer Composition API for better code organization
3. **Handle events properly**: Use proper event handlers for component interactions
4. **Customize theme**: Use theme variables for customization
5. **Follow design specs**: Follow Element Design specifications
6. **Use TypeScript**: Leverage TypeScript for better type safety

## Resources

- **Official Documentation**: https://element-plus.org/zh-CN/
- **English Documentation**: https://element-plus.org/en-US/
- **Design Guide**: https://element-plus.org/en-US/guide/design
- **Component Overview**: https://element-plus.org/en-US/component/overview
- **GitHub Repository**: https://github.com/element-plus/element-plus

## Keywords

Element Plus, element-plus, Vue 3, Vue3, UI components, component library, 组件库, 按钮, 表单, 表格, 弹窗, 消息, 通知, 菜单, 标签页, 日期选择器, 选择器, 开关, 复选框, 单选框, 上传, 分页, 树形控件, 穿梭框, 描述列表, 头像, 徽标, 标签, 空状态, 加载, 弹出框, 提示, 下拉菜单, 抽屉, 气泡确认框, Button, Form, Table, Dialog, Message, Notification, Menu, Tabs, DatePicker, Select, Switch, Checkbox, Radio, Upload, Pagination, Tree, Transfer, Descriptions, Avatar, Badge, Tag, Empty, Loading, Popover, Tooltip, Dropdown, Drawer, Popconfirm
