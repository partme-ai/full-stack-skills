---
name: ant-design-mobile
description: "Builds React mobile UIs with Ant Design Mobile (antd-mobile) components including Button, Form, List, Modal, Picker, Tabs, PullToRefresh, InfiniteScroll, and 50+ mobile-optimized components. Use when the user needs to create mobile-first React interfaces, implement mobile navigation, forms, or data display with Ant Design Mobile."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build React mobile applications with Ant Design Mobile components
- Use mobile UI components (Button, Form, List, Card, Modal, Tabs, etc.)
- Implement mobile-specific features (pull-to-refresh, infinite scroll, gestures)
- Customize the Ant Design Mobile theme with CSS variables
- Set up internationalization with ConfigProvider

## How to use this skill

### Workflow

1. **Install** - `npm install antd-mobile` and import CSS
2. **Choose components** - Match the UI need to the component from the reference below
3. **Load the example file** - Each component has a detailed example in `examples/components/`
4. **Customize theme** - Use ConfigProvider or CSS variables for theming

### Quick-Start Example: Mobile Form with Validation

```tsx
import { Button, Form, Input, Toast } from 'antd-mobile';

function LoginForm() {
  const [form] = Form.useForm();

  const onSubmit = async () => {
    const values = await form.validateFields();
    Toast.show({ content: `Welcome, ${values.username}!` });
  };

  return (
    <Form form={form} layout="horizontal" footer={
      <Button block type="submit" color="primary" onClick={onSubmit}>
        Login
      </Button>
    }>
      <Form.Item name="username" label="Username" rules={[{ required: true }]}>
        <Input placeholder="Enter username" />
      </Form.Item>
      <Form.Item name="password" label="Password" rules={[{ required: true }]}>
        <Input type="password" placeholder="Enter password" />
      </Form.Item>
    </Form>
  );
}
```

### Component Categories

| Category | Components | Example Files |
|----------|-----------|---------------|
| Navigation | NavBar, TabBar, Tabs, SideBar | `examples/components/nav-bar.md`, `tabs.md` |
| Data Entry | Input, Form, Picker, DatePicker, Switch, Checkbox | `examples/components/form.md`, `picker.md` |
| Data Display | List, Card, Badge, Tag, Avatar, Image | `examples/components/list.md`, `card.md` |
| Feedback | Modal, Toast, Dialog, ActionSheet, Loading | `examples/components/modal.md`, `toast.md` |
| Gestures | PullToRefresh, InfiniteScroll, Swiper | `examples/components/pull-to-refresh.md` |

### API Reference

- `api/components.md` - All component props and APIs
- `api/config-provider.md` - Global configuration and theming

## Best Practices

1. **Import CSS first** - Add `import 'antd-mobile/es/global'` in your entry file
2. **Wrap with ConfigProvider** - Set locale and theme at the app root
3. **Use CSS variables for theming** - Override `--adm-color-primary` etc. for custom branding
4. **Tree-shake imports** - Import individual components (`import { Button } from 'antd-mobile'`) for smaller bundles
5. **Test on real devices** - Mobile touch behavior differs from desktop browser emulation

## Resources

- **Official Website**: https://ant-design-mobile.antgroup.com/
- **GitHub**: https://github.com/ant-design/ant-design-mobile

## Keywords

antd-mobile, Ant Design Mobile, React mobile, mobile UI, 移动端, 组件库, Button, Form, List, Modal, Tabs, PullToRefresh, InfiniteScroll, Toast, NavBar, TabBar, mobile components
