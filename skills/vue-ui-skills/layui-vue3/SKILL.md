---
name: layui-vue3
description: Provides comprehensive guidance for Layui Vue component library including components, layer dialogs, and utilities. Use when the user asks about Layui Vue, needs to use Layui components in Vue 3, or implement UI components.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Layui Vue in a Vue 3 project
- Use Layui Vue components (Button, Table, DatePicker, etc.)
- Configure Layui Vue (theme, i18n, etc.)
- Use Layer component for modals and dialogs
- Implement forms with Layui Vue components
- Use data tables with sorting and pagination
- Handle file uploads
- Create dropdowns and tooltips
- Use date and time pickers
- Customize component styles
- Understand Layui Vue API and methods
- Troubleshoot Layui Vue issues

## How to use this skill

1. **Identify the topic** from the user's request and find the corresponding example file in the mapping below

2. **Load the appropriate example file** from the `examples/` directory

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

### Doc mapping (one-to-one with https://www.layui-vue.com/zh-CN/)

**Guide (指南)**:
- `examples/getting-started.md` → https://www.layui-vue.com/zh-CN/index
- `examples/introduce.md` → https://www.layui-vue.com/zh-CN/guide/introduce

**Components (组件)** - `examples/components/`:
- See component files in `examples/components/` directory
- Each component file maps to https://www.layui-vue.com/zh-CN/components/[component-name]

   **Important Notes**:
   - Layui Vue is built for Vue 3
   - Components use Composition API
   - Supports TypeScript
   - Examples include both JavaScript and TypeScript versions
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/layer-api.md` - Layer API methods
   - `api/component-api.md` - Component API reference

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/component-usage.md` - Component usage templates

### 1. Understanding Layui Vue

Layui Vue is a Vue 3 component library that provides a rich set of UI components, following the design philosophy of Layui.

**Key Concepts**:
- **Vue 3 Support**: Built with Vue 3 Composition API
- **Rich Components**: Button, Table, DatePicker, Layer, etc.
- **TypeScript**: Full TypeScript support
- **Theme Customization**: Support for theme customization
- **i18n**: Internationalization support

### 2. Installation

**Using npm**:

```bash
npm install @layui/layui-vue
```

**Using yarn**:

```bash
yarn add @layui/layui-vue
```

**Using pnpm**:

```bash
pnpm add @layui/layui-vue
```

### 3. Basic Setup

```javascript
// main.js
import { createApp } from 'vue'
import LayuiVue from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(LayuiVue)
app.mount('#app')
```

### 4. Basic Component Usage

```vue
<template>
  <lay-button type="primary">Button</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
</script>
```

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

Detailed API documentation is available in the `api/` directory, organized to match the official Layui Vue API documentation structure:

### Layer API (`api/layer-api.md`)
- `layer.open()` - Open modal/dialog
- `layer.close()` - Close layer
- `layer.msg()` - Show message
- `layer.confirm()` - Show confirmation dialog
- `layer.load()` - Show loading
- `layer.drawer()` - Show drawer

### Component API (`api/component-api.md`)
- Component props and events
- Component methods
- Component slots

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Use TypeScript**: Take advantage of TypeScript support
2. **Import on demand**: Import only needed components
3. **Follow component API**: Use props and events correctly
4. **Customize theme**: Use theme variables for customization
5. **Handle events**: Properly handle component events
6. **Use Layer API**: Use Layer API for modals and dialogs

## Resources

- **Official Documentation**: https://www.layui-vue.com/zh-CN/index
- **Getting Started**: https://www.layui-vue.com/zh-CN/guide/introduce
- **Components**: https://www.layui-vue.com/zh-CN/components
- **GitHub Repository**: https://github.com/layui-vue/layui-vue

## Keywords

Layui Vue, layui-vue, Vue 3, component library, UI components, Button, Table, DatePicker, Layer, Dropdown, Tooltip, Form, Input, Select, Checkbox, Radio, Switch, Upload, 组件库, 按钮, 表格, 日期选择器, 弹层, 下拉菜单, 提示, 表单, 输入框, 选择器, 复选框, 单选框, 开关, 上传
