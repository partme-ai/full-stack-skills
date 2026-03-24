---
name: ant-design-react
description: Provides comprehensive guidance for Ant Design React component library including components, design system, themes, and TypeScript support. Use when the user asks about Ant Design for React, needs to build React applications with Ant Design, or implement design system patterns.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build React applications with Ant Design components
- Use Ant Design UI components (Button, Form, Table, Input, Select, etc.)
- Customize Ant Design theme and styles
- Implement internationalization (i18n) with Ant Design
- Use Ant Design with TypeScript
- Create forms with validation
- Display data in tables and lists
- Implement navigation and layout
- Use Ant Design icons
- Handle user feedback (Modal, Message, Notification)
- Implement data visualization components
- Use Ant Design design tokens and design system

## How to use this skill

This skill is organized to match the Ant Design React official documentation structure (https://4x-ant-design.antgroup.com/docs/react/introduce-cn, https://4x-ant-design.antgroup.com/components/overview-cn/). When working with Ant Design React:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started/installation.md` or `examples/getting-started/basic-usage.md`
   - Button/按钮 → `examples/components/button.md`
   - Form/表单 → `examples/components/form.md`
   - Table/表格 → `examples/components/table.md`
   - Input/输入框 → `examples/components/input.md`
   - Select/选择器 → `examples/components/select.md`
   - DatePicker/日期选择器 → `examples/components/date-picker.md`
   - Modal/对话框 → `examples/components/modal.md`
   - Layout/布局 → `examples/components/layout.md`
   - Menu/菜单 → `examples/components/menu.md`
   - Theme customization/主题定制 → `examples/advanced/theme-customization.md`
   - Internationalization/国际化 → `examples/advanced/internationalization.md`
   - TypeScript/类型支持 → `examples/advanced/typescript.md`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始) - `examples/getting-started/`**:
   - `examples/getting-started/installation.md` - Installing Ant Design and basic setup
   - `examples/getting-started/basic-usage.md` - Basic component usage

   **Components (组件) - `examples/components/`**:
   - `examples/components/button.md` - Button component
   - `examples/components/input.md` - Input component
   - `examples/components/form.md` - Form component with validation
   - `examples/components/table.md` - Table component
   - `examples/components/select.md` - Select component
   - `examples/components/date-picker.md` - DatePicker component
   - `examples/components/modal.md` - Modal component
   - `examples/components/layout.md` - Layout component
   - `examples/components/menu.md` - Menu component
   - `examples/components/icon.md` - Icon component
   - `examples/components/typography.md` - Typography component
   - `examples/components/grid.md` - Grid component
   - `examples/components/space.md` - Space component
   - `examples/components/card.md` - Card component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/pagination.md` - Pagination component
   - `examples/components/upload.md` - Upload component
   - `examples/components/upload.md` - Upload component
   - `examples/components/message.md` - Message component
   - `examples/components/notification.md` - Notification component
   - `examples/components/alert.md` - Alert component
   - `examples/components/spin.md` - Spin component
   - `examples/components/progress.md` - Progress component

   **Advanced (高级) - `examples/advanced/`**:
   - `examples/advanced/theme-customization.md` - Customizing theme
   - `examples/advanced/internationalization.md` - Internationalization setup
   - `examples/advanced/typescript.md` - TypeScript support

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - All examples follow Ant Design React 4.x API
   - Examples include both JavaScript and TypeScript versions where applicable
   - Each example file includes key concepts, code examples, and key points
   - Always check the example file for best practices and common patterns

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/components.md` - Component API reference
   - `api/config-provider.md` - ConfigProvider API
   - `api/design-tokens.md` - Design tokens API

5. **Use templates** from the `templates/` directory:
   - `templates/project-setup.md` - Project setup templates
   - `templates/component-template.md` - Component usage templates


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://4x-ant-design.antgroup.com/docs/react/introduce-cn

**Components (组件)**:
- See component files in `examples/components/` → https://4x-ant-design.antgroup.com/components/overview-cn/

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

Detailed API documentation is available in the `api/` directory, organized to match the official Ant Design React API documentation structure:

### Components API (`api/components.md`)
- All component props and APIs
- Component methods and events
- Component types and interfaces

### ConfigProvider API (`api/config-provider.md`)
- ConfigProvider component API
- Global configuration options
- Locale configuration

### Design Tokens API (`api/design-tokens.md`)
- Design tokens reference
- Theme customization tokens
- CSS variables

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Import styles**: Import Ant Design CSS in your entry file
2. **Use ConfigProvider**: Wrap your app with ConfigProvider for global configuration
3. **Form validation**: Use Form component with validation rules
4. **TypeScript**: Use TypeScript for better type safety
5. **Theme customization**: Use design tokens for consistent theming
6. **Internationalization**: Use ConfigProvider with locale for i18n
7. **Component composition**: Compose components for complex UIs
8. **Performance**: Use React.memo and useMemo for optimization
9. **Accessibility**: Follow Ant Design accessibility guidelines
10. **Responsive design**: Use Grid and responsive utilities

## Resources

- **Official Website**: https://4x-ant-design.antgroup.com/index-cn
- **Getting Started**: https://4x-ant-design.antgroup.com/docs/react/introduce-cn
- **Components**: https://4x-ant-design.antgroup.com/components/overview-cn/
- **GitHub Repository**: https://github.com/ant-design/ant-design

## Keywords

Ant Design, Ant Design React, antd, React UI library, components, Button, Form, Table, Input, Select, DatePicker, Modal, Layout, Menu, theme, customization, internationalization, i18n, TypeScript, design system, 组件库, 按钮, 表单, 表格, 输入框, 选择器, 日期选择器, 对话框, 布局, 菜单, 主题, 国际化, 类型支持
