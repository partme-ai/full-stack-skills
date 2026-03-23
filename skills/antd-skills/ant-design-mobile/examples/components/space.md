# Space | 间距

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Space component in Ant Design Mobile.

### Key Concepts

- Horizontal spacing
- Vertical spacing
- Spacing sizes
- Spacing with wrap

### Example: Basic Space

```javascript
import React from 'react';
import { Space, Button } from 'antd-mobile';

function App() {
  return (
    <Space>
      <Button>按钮1</Button>
      <Button>按钮2</Button>
      <Button>按钮3</Button>
    </Space>
  );
}
```

### Example: Vertical Space

```javascript
import React from 'react';
import { Space, Button } from 'antd-mobile';

function App() {
  return (
    <Space direction="vertical">
      <Button>按钮1</Button>
      <Button>按钮2</Button>
      <Button>按钮3</Button>
    </Space>
  );
}
```

### Example: Space Sizes

```javascript
import React from 'react';
import { Space, Button } from 'antd-mobile';

function App() {
  return (
    <>
      <Space size="small">
        <Button>小间距</Button>
        <Button>小间距</Button>
      </Space>
      <Space size="middle">
        <Button>中间距</Button>
        <Button>中间距</Button>
      </Space>
      <Space size="large">
        <Button>大间距</Button>
        <Button>大间距</Button>
      </Space>
    </>
  );
}
```

### Example: Space with Wrap

```javascript
import React from 'react';
import { Space, Button } from 'antd-mobile';

function App() {
  return (
    <Space wrap>
      <Button>按钮1</Button>
      <Button>按钮2</Button>
      <Button>按钮3</Button>
      <Button>按钮4</Button>
      <Button>按钮5</Button>
    </Space>
  );
}
```

### Key Points

- Use `Space` to add spacing between components
- Use `direction` prop for direction (horizontal, vertical)
- Use `size` prop for spacing size (small, middle, large)
- Use `wrap` prop for wrapping
- Space is optimized for mobile display
