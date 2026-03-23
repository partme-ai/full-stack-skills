# Loading | 加载

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Loading component in Ant Design Mobile.

### Key Concepts

- Basic loading
- Loading with text
- Loading with spinner
- Loading with mask
- Loading with full screen

### Example: Basic Loading

```javascript
import React, { useState } from 'react';
import { Loading, Button } from 'antd-mobile';

function App() {
  const [loading, setLoading] = useState(false);

  return (
    <>
      <Button onClick={() => setLoading(true)}>显示加载</Button>
      <Loading visible={loading} />
    </>
  );
}
```

### Example: Loading with Text

```javascript
import React, { useState } from 'react';
import { Loading, Button } from 'antd-mobile';

function App() {
  const [loading, setLoading] = useState(false);

  return (
    <>
      <Button onClick={() => setLoading(true)}>显示加载</Button>
      <Loading visible={loading}>加载中...</Loading>
    </>
  );
}
```

### Example: Loading with Mask

```javascript
import React, { useState } from 'react';
import { Loading, Button } from 'antd-mobile';

function App() {
  const [loading, setLoading] = useState(false);

  return (
    <>
      <Button onClick={() => setLoading(true)}>显示加载</Button>
      <Loading visible={loading} mask />
    </>
  );
}
```

### Example: Loading with Full Screen

```javascript
import React, { useState } from 'react';
import { Loading, Button } from 'antd-mobile';

function App() {
  const [loading, setLoading] = useState(false);

  return (
    <>
      <Button onClick={() => setLoading(true)}>显示加载</Button>
      <Loading visible={loading} mask fullScreen>
        加载中...
      </Loading>
    </>
  );
}
```

### Key Points

- Use `visible` prop to control visibility
- Use children for loading text
- Use `mask` prop for mask overlay
- Use `fullScreen` prop for full screen loading
- Loading is optimized for mobile display
