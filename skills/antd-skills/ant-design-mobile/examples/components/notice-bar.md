# NoticeBar | 通告栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the NoticeBar component in Ant Design Mobile.

### Key Concepts

- Basic notice bar
- Notice bar with icon
- Notice bar with close
- Notice bar with action
- Notice bar with scroll

### Example: Basic NoticeBar

```javascript
import React from 'react';
import { NoticeBar } from 'antd-mobile';

function App() {
  return (
    <NoticeBar content="这是一条通知消息" />
  );
}
```

### Example: NoticeBar with Icon

```javascript
import React from 'react';
import { NoticeBar } from 'antd-mobile';
import { InfoCircleOutline } from 'antd-mobile-icons';

function App() {
  return (
    <NoticeBar
      content="这是一条通知消息"
      icon={<InfoCircleOutline />}
    />
  );
}
```

### Example: NoticeBar with Close

```javascript
import React, { useState } from 'react';
import { NoticeBar } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(true);

  return (
    <>
      {visible && (
        <NoticeBar
          content="这是一条通知消息"
          closeable
          onClose={() => setVisible(false)}
        />
      )}
    </>
  );
}
```

### Example: NoticeBar with Action

```javascript
import React from 'react';
import { NoticeBar } from 'antd-mobile';

function App() {
  return (
    <NoticeBar
      content="这是一条通知消息"
      extra={<span>查看</span>}
      onExtraClick={() => {
        console.log('点击了查看');
      }}
    />
  );
}
```

### Example: NoticeBar with Scroll

```javascript
import React from 'react';
import { NoticeBar } from 'antd-mobile';

function App() {
  return (
    <NoticeBar
      content="这是一条很长的通知消息，会自动滚动显示"
      color="alert"
      wrap
    />
  );
}
```

### Key Points

- Use `content` prop for notice content
- Use `icon` prop for notice icon
- Use `closeable` prop for close button
- Use `onClose` callback for close event
- Use `extra` prop for extra content
- Use `onExtraClick` callback for extra click
- Use `wrap` prop for text wrapping
- Use `color` prop for notice color (default, alert)
- NoticeBar is optimized for mobile display
