# Empty | 空状态

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Empty component in Ant Design Mobile.

### Key Concepts

- Basic empty
- Empty with image
- Empty with title
- Empty with description
- Empty with action

### Example: Basic Empty

```javascript
import React from 'react';
import { Empty } from 'antd-mobile';

function App() {
  return (
    <Empty />
  );
}
```

### Example: Empty with Title

```javascript
import React from 'react';
import { Empty } from 'antd-mobile';

function App() {
  return (
    <Empty
      title="暂无数据"
      description="请稍后再试"
    />
  );
}
```

### Example: Empty with Image

```javascript
import React from 'react';
import { Empty } from 'antd-mobile';

function App() {
  return (
    <Empty
      image="https://via.placeholder.com/200"
      title="暂无数据"
    />
  );
}
```

### Example: Empty with Action

```javascript
import React from 'react';
import { Empty, Button } from 'antd-mobile';

function App() {
  return (
    <Empty
      title="暂无数据"
      description="请稍后再试"
      actions={
        <Button color="primary" onClick={() => {}}>
          刷新
        </Button>
      }
    />
  );
}
```

### Key Points

- Use `title` prop for empty title
- Use `description` prop for empty description
- Use `image` prop for custom image
- Use `actions` prop for action buttons
- Empty is optimized for mobile display
