# Components Overview

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example provides an overview of Ant Design Mini components.

### Key Concepts

- Component categories
- Component list
- Component usage
- Platform compatibility

### Example: Component Categories

**Form Components (表单组件)**:
- Button, Input, Form, FormItem
- Switch, Checkbox, Radio
- Picker, DatePicker, Stepper

**Data Display (数据展示)**:
- List, ListItem
- Card
- Avatar, Badge, Tag
- Empty

**Feedback (反馈)**:
- Toast, Modal
- Loading
- Popup, ActionSheet

**Navigation (导航)**:
- Tabs, TabItem
- NavBar

### Example: Component Registration

```json
// app.json
{
  "usingComponents": {
    "ant-button": "antd-mini/es/Button/index",
    "ant-input": "antd-mini/es/Input/index",
    "ant-form": "antd-mini/es/Form/index",
    "ant-list": "antd-mini/es/List/index",
    "ant-modal": "antd-mini/es/Modal/index"
  }
}
```

### Key Points

- Components organized by category
- Register components before use
- Compatible with Alipay and WeChat
- Follow Ant Design design specs
- Rich component ecosystem
