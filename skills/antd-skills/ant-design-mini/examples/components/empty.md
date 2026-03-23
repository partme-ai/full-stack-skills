# Empty Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Empty component in Ant Design Mini.

### Key Concepts

- Empty state
- Empty description
- Empty image
- Empty actions

### Example: Basic Empty

```xml
<ant-empty description="No Data" />
```

### Example: Empty with Image

```xml
<ant-empty 
  image="{{imageUrl}}"
  description="No Data"
/>
```

### Example: Empty with Actions

```xml
<ant-empty description="No Data">
  <ant-button type="primary" onTap="handleAction">
    Refresh
  </ant-button>
</ant-empty>
```

### Example: Empty Types

```xml
<ant-empty type="empty" description="Empty" />
<ant-empty type="error" description="Error" />
<ant-empty type="network" description="Network Error" />
```

### Key Points

- Use description for text
- Customize image
- Add action buttons
- Multiple empty types
- Simple empty state display
