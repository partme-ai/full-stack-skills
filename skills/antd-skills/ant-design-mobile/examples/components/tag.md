# Tag | 标签

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Tag component in Ant Design Mobile.

### Key Concepts

- Tag colors
- Tag sizes
- Tag shapes
- Closable tags
- Tag with icons

### Example: Basic Tag

```javascript
import React from 'react';
import { Tag } from 'antd-mobile';

function App() {
  return (
    <>
      <Tag>标签</Tag>
      <Tag color="primary">主要</Tag>
      <Tag color="success">成功</Tag>
      <Tag color="warning">警告</Tag>
      <Tag color="danger">危险</Tag>
    </>
  );
}
```

### Example: Tag Sizes

```javascript
import React from 'react';
import { Tag } from 'antd-mobile';

function App() {
  return (
    <>
      <Tag size="small">小标签</Tag>
      <Tag size="middle">中标签</Tag>
      <Tag size="large">大标签</Tag>
    </>
  );
}
```

### Example: Tag Shapes

```javascript
import React from 'react';
import { Tag } from 'antd-mobile';

function App() {
  return (
    <>
      <Tag>默认</Tag>
      <Tag round>圆角</Tag>
    </>
  );
}
```

### Example: Closable Tag

```javascript
import React, { useState } from 'react';
import { Tag } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(true);

  return (
    <>
      {visible && (
        <Tag
          closable
          onClose={() => {
            setVisible(false);
          }}
        >
          可关闭标签
        </Tag>
      )}
    </>
  );
}
```

### Example: Tag with Icon

```javascript
import React from 'react';
import { Tag } from 'antd-mobile';
import { CheckCircleOutline } from 'antd-mobile-icons';

function App() {
  return (
    <Tag icon={<CheckCircleOutline />}>
      带图标标签
    </Tag>
  );
}
```

### Example: Tag Colors

```javascript
import React from 'react';
import { Tag } from 'antd-mobile';

function App() {
  return (
    <>
      <Tag color="default">默认</Tag>
      <Tag color="primary">主要</Tag>
      <Tag color="success">成功</Tag>
      <Tag color="warning">警告</Tag>
      <Tag color="danger">危险</Tag>
      <Tag color="#ff6b6b">自定义颜色</Tag>
    </>
  );
}
```

### Key Points

- Use `color` prop for tag color
- Use `size` prop for tag size (small, middle, large)
- Use `round` prop for rounded corners
- Use `closable` prop for closable tag
- Use `onClose` callback for close event
- Use `icon` prop for tag icon
- Tag is optimized for mobile display
