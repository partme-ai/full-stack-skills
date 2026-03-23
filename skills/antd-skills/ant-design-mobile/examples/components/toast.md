# Toast | 轻提示

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Toast component in Ant Design Mobile.

### Key Concepts

- Basic toast
- Toast with success
- Toast with error
- Toast with loading
- Toast with duration

### Example: Basic Toast

```javascript
import React from 'react';
import { Toast, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Toast.show('提示信息');
      }}
    >
      显示提示
    </Button>
  );
}
```

### Example: Toast with Success

```javascript
import React from 'react';
import { Toast, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Toast.show({
          icon: 'success',
          content: '操作成功',
        });
      }}
    >
      成功提示
    </Button>
  );
}
```

### Example: Toast with Error

```javascript
import React from 'react';
import { Toast, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Toast.show({
          icon: 'fail',
          content: '操作失败',
        });
      }}
    >
      错误提示
    </Button>
  );
}
```

### Example: Toast with Loading

```javascript
import React from 'react';
import { Toast, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        const handler = Toast.show({
          icon: 'loading',
          content: '加载中...',
          duration: 0,
        });
        
        setTimeout(() => {
          Toast.clear();
        }, 2000);
      }}
    >
      加载提示
    </Button>
  );
}
```

### Example: Toast with Duration

```javascript
import React from 'react';
import { Toast, Button } from 'antd-mobile';

function App() {
  return (
    <Button
      onClick={() => {
        Toast.show({
          content: '提示信息',
          duration: 3000,
        });
      }}
    >
      显示提示
    </Button>
  );
}
```

### Key Points

- Use `Toast.show` to show toast
- Use `Toast.clear` to clear toast
- Use `icon` prop for toast icon (success, fail, loading)
- Use `content` prop for toast content
- Use `duration` prop for display duration (0 for infinite)
- Toast is optimized for mobile display
