---
name: ant-design-mini
description: "Builds mini-program UIs with Ant Design Mini components for Alipay and WeChat mini-programs. Covers Button, Form, List, Modal, Tabs, NavBar, and 60+ components with theme customization and CSS variable theming. Use when the user needs to create mini-program interfaces with Ant Design Mini, configure themes, or implement mini-program-specific UI patterns."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Alipay or WeChat mini-program UIs with Ant Design Mini components
- Use form, data display, feedback, or navigation components in mini-programs
- Customize the Ant Design Mini theme via CSS variables
- Handle component events and lifecycle in mini-program contexts

## How to use this skill

### Quick-Start Example: Button and Form in Mini-Program

```xml
<!-- pages/index/index.axml -->
<ant-button type="primary" onTap="handleClick">Submit</ant-button>

<ant-form onFinish="onFormFinish">
  <ant-form-item label="Name" name="name" required="{{true}}">
    <ant-input placeholder="Enter your name" />
  </ant-form-item>
  <ant-form-item label="Phone" name="phone">
    <ant-input type="number" placeholder="Enter phone" />
  </ant-form-item>
  <ant-button type="primary" form-type="submit">Submit</ant-button>
</ant-form>
```

```javascript
// pages/index/index.js
Page({
  handleClick() { my.showToast({ content: 'Clicked!' }); },
  onFormFinish(values) { console.log('Form values:', values); }
});
```

This skill is organized to match the Ant Design Mini official documentation structure (https://ant-design-mini.antgroup.com/guide/quick-start, https://ant-design-mini.antgroup.com/components/overview). When working with Ant Design Mini:

1. **Identify the topic** from the user's request:
   - Getting started/快速开始 → `examples/getting-started.md`
   - Components/组件 → `examples/components/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Getting Started (快速开始)**:
   - `examples/getting-started.md` - Installation and setup
   - `examples/quick-start.md` - Quick start guide

   **Components (组件)**:
   - `examples/components/overview.md` - Components overview
   - `examples/components/button.md` - Button component
   - `examples/components/input.md` - Input component
   - `examples/components/form.md` - Form component
   - `examples/components/list.md` - List component
   - `examples/components/card.md` - Card component
   - `examples/components/toast.md` - Toast component
   - `examples/components/modal.md` - Modal component
   - `examples/components/tabs.md` - Tabs component
   - `examples/components/nav-bar.md` - NavBar component
   - `examples/components/picker.md` - Picker component
   - `examples/components/date-picker.md` - DatePicker component
   - `examples/components/switch.md` - Switch component
   - `examples/components/checkbox.md` - Checkbox component
   - `examples/components/radio.md` - Radio component
   - `examples/components/stepper.md` - Stepper component
   - `examples/components/avatar.md` - Avatar component
   - `examples/components/badge.md` - Badge component
   - `examples/components/tag.md` - Tag component
   - `examples/components/empty.md` - Empty component
   - `examples/components/loading.md` - Loading component
   - `examples/components/popup.md` - Popup component
   - `examples/components/action-sheet.md` - ActionSheet component

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Ant Design Mini is for Alipay Mini Program and WeChat Mini Program
   - Components use mini-program syntax (axml/json)
   - Examples include both Alipay and WeChat syntax
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/component-api.md` - Component API reference
   - `api/props-and-events.md` - Props and events reference

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/component-usage.md` - Component usage templates

### 1. Understanding Ant Design Mini

Ant Design Mini is a UI component library for Alipay Mini Program and WeChat Mini Program, following Ant Design design specifications.

**Key Concepts**:
- **Mini Program Support**: Alipay and WeChat Mini Programs
- **Design System**: Follows Ant Design design language
- **Rich Components**: Button, Form, List, Modal, etc.
- **Theme Customization**: Support for theme customization
- **i18n**: Internationalization support

### 2. Installation

**Using npm**:

```bash
npm install antd-mini
```

**Using yarn**:

```bash
yarn add antd-mini
```

**Using pnpm**:

```bash
pnpm add antd-mini
```

### 3. Basic Setup

```json
// app.json (Alipay Mini Program)
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index"
  }
}
```

```xml
<!-- page.axml -->
<ant-button type="primary" onTap="handleTap">Button</ant-button>
```


### Doc mapping (one-to-one with official documentation)

**Guide (指南)**:
- See guide files in `examples/guide/` or `examples/getting-started/` → https://ant-design-mini.antgroup.com/guide/quick-start

**Components (组件)**:
- See component files in `examples/components/` → https://ant-design-mini.antgroup.com/components/overview

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

Detailed API documentation is available in the `api/` directory, organized to match the official Ant Design Mini API documentation structure:

### Component API (`api/component-api.md`)
- Component props and events
- Component methods
- Component slots

### Props and Events (`api/props-and-events.md`)
- Common props
- Common events
- Event handling

**To use API reference:**
1. Identify the API you need help with
2. Load the corresponding API file from the `api/` directory
3. Find the API signature, parameters, return type, and examples
4. Reference the linked example files for detailed usage patterns
5. All API files include links to relevant example files in the `examples/` directory

## Best Practices

1. **Register components**: Register components in app.json or page.json
2. **Use correct syntax**: Use axml for Alipay, wxml for WeChat
3. **Handle events**: Use onTap for Alipay, bindtap for WeChat
4. **Customize theme**: Use theme variables for customization
5. **Follow design specs**: Follow Ant Design design specifications

## Resources

- **Official Documentation**: https://ant-design-mini.antgroup.com/
- **Quick Start**: https://ant-design-mini.antgroup.com/guide/quick-start
- **Components**: https://ant-design-mini.antgroup.com/components/overview
- **GitHub Repository**: https://github.com/ant-design/ant-design-mini

## Keywords

Ant Design Mini, ant-design-mini, antd-mini, mini program, Alipay Mini Program, WeChat Mini Program, 小程序, 支付宝小程序, 微信小程序, 组件库, UI components, Button, Form, List, Modal, Toast, Tabs, NavBar, 按钮, 表单, 列表, 弹窗, 提示, 标签页, 导航栏
