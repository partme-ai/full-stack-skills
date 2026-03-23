# ErrorBlock | 错误区块

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the ErrorBlock component in Ant Design Mobile.

### Key Concepts

- Basic error block
- Error block with status
- Error block with title
- Error block with description
- Error block with action

### Example: Basic ErrorBlock

```javascript
import React from 'react';
import { ErrorBlock } from 'antd-mobile';

function App() {
  return (
    <ErrorBlock status="default" />
  );
}
```

### Example: ErrorBlock with Status

```javascript
import React from 'react';
import { ErrorBlock } from 'antd-mobile';

function App() {
  return (
    <>
      <ErrorBlock status="default" />
      <ErrorBlock status="network" />
      <ErrorBlock status="busy" />
      <ErrorBlock status="empty" />
    </>
  );
}
```

### Example: ErrorBlock with Title

```javascript
import React from 'react';
import { ErrorBlock } from 'antd-mobile';

function App() {
  return (
    <ErrorBlock
      status="default"
      title="出错了"
      description="请稍后重试"
    />
  );
}
```

### Example: ErrorBlock with Action

```javascript
import React from 'react';
import { ErrorBlock, Button } from 'antd-mobile';

function App() {
  return (
    <ErrorBlock
      status="default"
      title="出错了"
      description="请稍后重试"
      actions={
        <Button color="primary" onClick={() => window.location.reload()}>
          重试
        </Button>
      }
    />
  );
}
```

### Key Points

- Use `status` prop for error status (default, network, busy, empty)
- Use `title` prop for error title
- Use `description` prop for error description
- Use `actions` prop for action buttons
- ErrorBlock is optimized for mobile display
