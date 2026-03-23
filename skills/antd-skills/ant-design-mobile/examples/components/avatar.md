# Avatar | 头像

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Avatar component in Ant Design Mobile.

### Key Concepts

- Avatar with image
- Avatar with text
- Avatar with icon
- Avatar sizes
- Avatar shapes

### Example: Basic Avatar

```javascript
import React from 'react';
import { Avatar } from 'antd-mobile';

function App() {
  return (
    <>
      <Avatar src="https://via.placeholder.com/100" />
      <Avatar>U</Avatar>
      <Avatar style={{ background: '#87d068' }}>U</Avatar>
    </>
  );
}
```

### Example: Avatar Sizes

```javascript
import React from 'react';
import { Avatar } from 'antd-mobile';

function App() {
  return (
    <>
      <Avatar size="small" src="https://via.placeholder.com/100" />
      <Avatar size="middle" src="https://via.placeholder.com/100" />
      <Avatar size="large" src="https://via.placeholder.com/100" />
    </>
  );
}
```

### Example: Avatar Shapes

```javascript
import React from 'react';
import { Avatar } from 'antd-mobile';

function App() {
  return (
    <>
      <Avatar src="https://via.placeholder.com/100" />
      <Avatar shape="square" src="https://via.placeholder.com/100" />
      <Avatar shape="rounded" src="https://via.placeholder.com/100" />
    </>
  );
}
```

### Example: Avatar with Badge

```javascript
import React from 'react';
import { Avatar, Badge } from 'antd-mobile';

function App() {
  return (
    <Badge content="5">
      <Avatar src="https://via.placeholder.com/100" />
    </Badge>
  );
}
```

### Example: Avatar Group

```javascript
import React from 'react';
import { Avatar } from 'antd-mobile';

function App() {
  return (
    <Avatar.Group>
      <Avatar src="https://via.placeholder.com/100" />
      <Avatar src="https://via.placeholder.com/100" />
      <Avatar src="https://via.placeholder.com/100" />
      <Avatar>+5</Avatar>
    </Avatar.Group>
  );
}
```

### Key Points

- Use `src` prop for image URL
- Use `size` prop for avatar size (small, middle, large)
- Use `shape` prop for avatar shape (circle, square, rounded)
- Use children for text avatar
- Use `style` prop for custom styles
- Avatar can be used with Badge
- Avatar.Group for multiple avatars
- Avatar is optimized for mobile display
