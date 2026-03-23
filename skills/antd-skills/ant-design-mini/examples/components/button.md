# Button Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Button component in Ant Design Mini.

### Key Concepts

- Button types
- Button sizes
- Button states
- Button events

### Example: Basic Button

```xml
<!-- Alipay -->
<ant-button type="primary">Primary</ant-button>
<ant-button type="default">Default</ant-button>
<ant-button type="text">Text</ant-button>
```

```xml
<!-- WeChat -->
<ant-button type="primary">Primary</ant-button>
<ant-button type="default">Default</ant-button>
<ant-button type="text">Text</ant-button>
```

### Example: Button Sizes

```xml
<ant-button size="large">Large</ant-button>
<ant-button size="medium">Medium</ant-button>
<ant-button size="small">Small</ant-button>
```

### Example: Button States

```xml
<ant-button disabled>Disabled</ant-button>
<ant-button loading>Loading</ant-button>
```

### Example: Button Events

```xml
<!-- Alipay -->
<ant-button type="primary" onTap="handleTap">Click Me</ant-button>
```

```xml
<!-- WeChat -->
<ant-button type="primary" bindtap="handleTap">Click Me</ant-button>
```

```javascript
// page.js
Page({
  handleTap() {
    console.log('Button clicked')
  }
})
```

### Example: Button with Icon

```xml
<ant-button icon="user">With Icon</ant-button>
```

### Key Points

- Multiple types: primary, default, text
- Multiple sizes: large, medium, small
- Support disabled and loading states
- Icon support
- Use onTap (Alipay) or bindtap (WeChat)
