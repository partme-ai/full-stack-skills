# Badge Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Badge component in Ant Design Mini.

### Key Concepts

- Badge count
- Badge dot
- Badge position
- Badge styling

### Example: Basic Badge

```xml
<ant-badge count="{{count}}">
  <ant-button>Button</ant-button>
</ant-badge>
```

### Example: Badge Dot

```xml
<ant-badge dot>
  <ant-button>Button</ant-button>
</ant-badge>
```

### Example: Badge Position

```xml
<ant-badge 
  count="{{count}}"
  position="topRight"
>
  <ant-button>Button</ant-button>
</ant-badge>
```

### Example: Badge with Max

```xml
<ant-badge 
  count="{{count}}"
  max="99"
>
  <ant-button>Button</ant-button>
</ant-badge>
```

### Key Points

- Wrap content with badge
- Set count for number badge
- Use dot for dot badge
- Configure position
- Set max for overflow
