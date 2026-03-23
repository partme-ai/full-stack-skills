# Divider | 分割线

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Divider component in Ant Design Mobile.

### Key Concepts

- Horizontal divider
- Vertical divider
- Divider with text
- Divider styles

### Example: Basic Divider

```javascript
import React from 'react';
import { Divider } from 'antd-mobile';

function App() {
  return (
    <>
      <div>内容1</div>
      <Divider />
      <div>内容2</div>
    </>
  );
}
```

### Example: Divider with Text

```javascript
import React from 'react';
import { Divider } from 'antd-mobile';

function App() {
  return (
    <>
      <div>内容1</div>
      <Divider>分割线</Divider>
      <div>内容2</div>
    </>
  );
}
```

### Example: Divider Positions

```javascript
import React from 'react';
import { Divider } from 'antd-mobile';

function App() {
  return (
    <>
      <Divider contentPosition="left">左侧</Divider>
      <Divider contentPosition="center">居中</Divider>
      <Divider contentPosition="right">右侧</Divider>
    </>
  );
}
```

### Example: Vertical Divider

```javascript
import React from 'react';
import { Divider } from 'antd-mobile';

function App() {
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <span>左侧</span>
      <Divider direction="vertical" />
      <span>右侧</span>
    </div>
  );
}
```

### Key Points

- Use `Divider` for horizontal divider
- Use `direction="vertical"` for vertical divider
- Use children for divider text
- Use `contentPosition` prop for text position (left, center, right)
- Divider is optimized for mobile display
