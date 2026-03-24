# Tag Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Tag component in Ant Design Mini.

### Key Concepts

- Tag types
- Tag sizes
- Tag closable
- Tag events

### Example: Basic Tag

```xml
<ant-tag>Tag</ant-tag>
<ant-tag type="primary">Primary</ant-tag>
<ant-tag type="success">Success</ant-tag>
<ant-tag type="warning">Warning</ant-tag>
<ant-tag type="error">Error</ant-tag>
```

### Example: Tag Sizes

```xml
<ant-tag size="large">Large</ant-tag>
<ant-tag size="medium">Medium</ant-tag>
<ant-tag size="small">Small</ant-tag>
```

### Example: Closable Tag

```xml
<ant-tag 
  closable
  onClose="handleClose"
>
  Closable Tag
</ant-tag>
```

```javascript
// page.js
Page({
  handleClose() {
    // Remove tag
  }
})
```

### Key Points

- Multiple types: primary, success, warning, error
- Multiple sizes: large, medium, small
- Support closable
- Handle onClose event
- Customize tag appearance
