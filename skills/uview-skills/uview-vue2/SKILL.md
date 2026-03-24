---
name: uview-vue2
description: Provides comprehensive guidance for uView Vue 2 component library including components, tools, and layouts. Use when the user asks about uView for Vue 2, needs to build Vue 2 applications with uView, or use uView components.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build uni-app applications with uView UI components
- Use uView UI components (Button, Input, Form, Table, Modal, etc.)
- Use uView UI tools ($u.toast, $u.http, etc.)
- Customize uView UI theme
- Integrate uView UI with uni-app
- Create responsive layouts with uView UI
- Use uView UI form components
- Display data with uView UI components
- Handle navigation with uView UI
- Use uView UI utilities and helpers

## How to use this skill

This skill is organized to match the uView UI official documentation structure (https://www.uviewui.com/guide/demo.html, https://www.uviewui.com/components/intro.html). When working with uView UI:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/basic-usage.md`
   - Button/按钮 → `examples/components/button.md`
   - Input/输入框 → `examples/components/input.md`
   - Form/表单 → `examples/components/form.md`
   - Table/表格 → `examples/components/table.md`
   - Modal/模态框 → `examples/components/modal.md`
   - Toast/提示 → `examples/tools/toast.md`
   - Http/请求 → `examples/tools/http.md`
   - Theme/主题 → `examples/advanced/theme-customization.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing uView UI and basic setup
   - `examples/getting-started/basic-usage.md` - Basic component usage
   - `examples/getting-started/design-principles.md` - Design principles and best practices

   **Components (组件) - `examples/components/`**:
   - `examples/components/button.md` - Button component
   - `examples/components/input.md` - Input component
   - `examples/components/form.md` - Form component
   - `examples/components/table.md` - Table component
   - `examples/components/modal.md` - Modal component
   - `examples/components/toast.md` - Toast component
   - `examples/components/loading.md` - Loading component
   - `examples/components/picker.md` - Picker component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/navbar.md` - Navbar component
   - `examples/components/grid.md` - Grid component
   - `examples/components/card.md` - Card component
   - `examples/components/badge.md` - Badge component
   - `examples/components/swiper.md` - Swiper component
   - `examples/components/list.md` - List component

   **Tools (工具) - `examples/tools/`**:
   - `examples/tools/toast.md` - Toast tool ($u.toast)
   - `examples/tools/http.md` - Http tool ($u.http)
   - `examples/tools/storage.md` - Storage tool ($u.storage)
   - `examples/tools/route.md` - Route tool ($u.route)
   - `examples/tools/debounce.md` - Debounce tool
   - `examples/tools/throttle.md` - Throttle tool

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/theme-customization.md` - Customizing uView UI theme
   - `examples/advanced/uniapp-integration.md` - UniApp integration

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow uView UI Vue 2.0 API
   - Examples use uni-app syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns
   - uView UI is designed for uni-app (H5, 小程序, App)

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/components.md` - Component API reference
   - `api/tools.md` - Tools API reference ($u methods)
   - `api/theme-variables.md` - Theme variables API

5. **Use templates** from the `templates/` directory:
   - `templates/project-setup.md` - Project setup templates
   - `templates/component-template.md` - Component usage templates


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://www.uviewui.com/guide/demo.html

**Components (组件)**:
- See component files in `examples/components/` → https://www.uviewui.com/components/intro.html

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

Detailed API documentation is available in the `api/` directory, organized to match the official uView UI API documentation structure:

### Components API (`api/components.md`)
- All component props and APIs
- Component events and slots
- Component types and interfaces

### Tools API (`api/tools.md`)
- $u object methods
- Toast, Http, Storage, Route tools
- Utility functions

### Theme Variables API (`api/theme-variables.md`)
- SCSS variables
- Theme customization variables
- Color variables

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Import uView UI**: Import uView UI in main.js with Vue.use()
2. **Import styles**: Import uView UI styles in App.vue
3. **Use easycom**: Configure easycom in pages.json for automatic component registration
4. **Use $u tools**: Use $u object for utility functions
5. **Theme customization**: Customize theme via SCSS variables
6. **UniApp compatibility**: Test on multiple platforms (H5, 小程序, App)
7. **Responsive design**: Use rpx units for responsive layouts
8. **Component composition**: Compose components for complex UIs
9. **Performance**: Optimize for uni-app performance
10. **Accessibility**: Follow uni-app accessibility guidelines

## Resources

- **Official Website**: https://www.uviewui.com/
- **Getting Started**: https://www.uviewui.com/guide/demo.html
- **Components**: https://www.uviewui.com/components/intro.html
- **UniApp Plugin**: https://ext.dcloud.net.cn/plugin?id=1593
- **GitHub Repository**: https://github.com/umicro/uView

## Keywords

uView UI, uView, uni-app, Vue 2, components, Button, Input, Form, Table, Modal, Toast, $u, tools, theme, customization, 组件库, 按钮, 输入框, 表单, 表格, 模态框, 提示, 工具函数, 主题定制
