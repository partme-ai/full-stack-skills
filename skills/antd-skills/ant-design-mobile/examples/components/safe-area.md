# SafeArea | 安全区域

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the SafeArea component in Ant Design Mobile.

### Key Concepts

- Safe area insets
- Top safe area
- Bottom safe area
- Left/Right safe area

### Example: Basic SafeArea

```javascript
import React from 'react';
import { SafeArea } from 'antd-mobile';

function App() {
  return (
    <SafeArea position="bottom">
      <div>内容区域</div>
    </SafeArea>
  );
}
```

### Example: Top SafeArea

```javascript
import React from 'react';
import { SafeArea } from 'antd-mobile';

function App() {
  return (
    <SafeArea position="top">
      <div>顶部内容</div>
    </SafeArea>
  );
}
```

### Example: Bottom SafeArea

```javascript
import React from 'react';
import { SafeArea } from 'antd-mobile';

function App() {
  return (
    <SafeArea position="bottom">
      <div>底部内容</div>
    </SafeArea>
  );
}
```

### Example: All Sides SafeArea

```javascript
import React from 'react';
import { SafeArea } from 'antd-mobile';

function App() {
  return (
    <>
      <SafeArea position="top" />
      <div>内容区域</div>
      <SafeArea position="bottom" />
    </>
  );
}
```

### Key Points

- Use `SafeArea` to handle safe area insets
- Use `position` prop for position (top, bottom, left, right)
- SafeArea prevents content from being obscured by notches or system UI
- SafeArea is essential for modern mobile devices
- SafeArea is optimized for mobile display
