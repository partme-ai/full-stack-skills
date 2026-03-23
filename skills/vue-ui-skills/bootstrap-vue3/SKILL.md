---
name: bootstrap-vue3
description: Provides comprehensive guidance for Bootstrap Vue 3 component library including Bootstrap components, grid system, utilities, and Vue 3 integration. Use when the user asks about Bootstrap Vue 3, needs to use Bootstrap components in Vue 3, or implement responsive layouts.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Vue 3 applications with Bootstrap Vue components
- Use Bootstrap UI components (Button, Form, Table, Modal, etc.)
- Create responsive layouts with Bootstrap grid
- Use Bootstrap Vue directives (v-b-tooltip, v-b-popover, v-b-modal)
- Implement forms with Bootstrap styling
- Display data in Bootstrap tables
- Create modals and alerts
- Use Bootstrap navigation components
- Customize Bootstrap themes
- Migrate from Bootstrap Vue 2.x to 3.0

## How to use this skill

This skill is organized to match the Bootstrap Vue 3.0 official documentation structure (https://bootstrap-vue.org/docs, https://bootstrap-vue.org/docs/components). When working with Bootstrap Vue 3.0:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/basic-usage.md`
   - Button/按钮 → `examples/components/button.md`
   - Form/表单 → `examples/components/form.md`
   - Table/表格 → `examples/components/table.md`
   - Modal/模态框 → `examples/components/modal.md`
   - Alert/警告框 → `examples/components/alert.md`
   - Navbar/导航栏 → `examples/components/navbar.md`
   - Grid/栅格 → `examples/components/grid.md`
   - Directives/指令 → `examples/directives/tooltip.md` or `examples/directives/modal.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Bootstrap Vue and basic setup
   - `examples/getting-started/basic-usage.md` - Basic component usage

   **Components (组件) - `examples/components/`**:
   - `examples/components/button.md` - Button component
   - `examples/components/form.md` - Form components
   - `examples/components/input.md` - Input component
   - `examples/components/table.md` - Table component
   - `examples/components/modal.md` - Modal component
   - `examples/components/alert.md` - Alert component
   - `examples/components/navbar.md` - Navbar component
   - `examples/components/grid.md` - Grid system (Container, Row, Col)
   - `examples/components/card.md` - Card component
   - `examples/components/badge.md` - Badge component
   - `examples/components/dropdown.md` - Dropdown component
   - `examples/components/pagination.md` - Pagination component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/collapse.md` - Collapse component
   - `examples/components/popover.md` - Popover component
   - `examples/components/tooltip.md` - Tooltip component

   **Directives (指令) - `examples/directives/`**:
   - `examples/directives/tooltip.md` - v-b-tooltip directive
   - `examples/directives/popover.md` - v-b-popover directive
   - `examples/directives/modal.md` - v-b-modal directive
   - `examples/directives/toggle.md` - v-b-toggle directive

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/theme-customization.md` - Customizing Bootstrap theme
   - `examples/advanced/composables.md` - Using composables (useToast, useModal)

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Bootstrap Vue 3.0 API (Vue 3 + Bootstrap 5)
   - Examples use Composition API syntax
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/components.md` - Component API reference
   - `api/directives.md` - Directives API reference
   - `api/composables.md` - Composables API reference

5. **Use templates** from the `templates/` directory:
   - `templates/project-setup.md` - Project setup templates
   - `templates/component-template.md` - Component usage templates


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://bootstrap-vue.org/docs

**Components (组件)**:
- See component files in `examples/components/` → https://bootstrap-vue.org/docs/components

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

Detailed API documentation is available in the `api/` directory, organized to match the official Bootstrap Vue 3.0 API documentation structure:

### Components API (`api/components.md`)
- All component props and APIs
- Component events and slots
- Component types and interfaces

### Directives API (`api/directives.md`)
- Directive syntax and usage
- Directive modifiers
- Directive options

### Composables API (`api/composables.md`)
- useToast composable
- useModal composable
- usePopover composable

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Import Bootstrap CSS**: Import Bootstrap CSS in your entry file
2. **Use Composition API**: Prefer Composition API for Vue 3 projects
3. **Tree-shaking**: Import components individually for better tree-shaking
4. **Responsive design**: Use Bootstrap grid system for responsive layouts
5. **Accessibility**: Follow Bootstrap accessibility guidelines
6. **Theme customization**: Use Bootstrap variables for consistent theming
7. **Directives**: Use directives for programmatic component control
8. **Composables**: Use composables for programmatic API access
9. **Component composition**: Compose components for complex UIs
10. **Performance**: Optimize bundle size with tree-shaking

## Resources

- **Official Website**: https://bootstrap-vue.org
- **Documentation**: https://bootstrap-vue.org/docs
- **Components**: https://bootstrap-vue.org/docs/components
- **GitHub Repository**: https://github.com/bootstrap-vue/bootstrap-vue-next

## Keywords

Bootstrap Vue, Bootstrap Vue 3.0, Vue 3, Bootstrap 5, components, Button, Form, Table, Modal, Alert, Navbar, Grid, directives, v-b-tooltip, v-b-popover, v-b-modal, composables, useToast, useModal, 组件库, 按钮, 表单, 表格, 模态框, 警告框, 导航栏, 栅格, 指令
