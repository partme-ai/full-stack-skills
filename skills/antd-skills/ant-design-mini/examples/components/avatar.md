# Avatar Component

**官方文档**: https://ant-design-mini.antgroup.com


## Instructions

This example demonstrates the Avatar component in Ant Design Mini.

### Key Concepts

- Avatar image
- Avatar size
- Avatar shape
- Avatar fallback

### Example: Basic Avatar

```xml
<ant-avatar src="{{avatarUrl}}" />
```

### Example: Avatar Sizes

```xml
<ant-avatar src="{{avatarUrl}}" size="large" />
<ant-avatar src="{{avatarUrl}}" size="medium" />
<ant-avatar src="{{avatarUrl}}" size="small" />
```

### Example: Avatar Shape

```xml
<ant-avatar src="{{avatarUrl}}" shape="circle" />
<ant-avatar src="{{avatarUrl}}" shape="square" />
```

### Example: Avatar with Fallback

```xml
<ant-avatar 
  src="{{avatarUrl}}"
  onError="handleError"
>
  <text>User</text>
</ant-avatar>
```

### Key Points

- Use src for image URL
- Configure size (large, medium, small)
- Set shape (circle, square)
- Handle image error
- Support text fallback
