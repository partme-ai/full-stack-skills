# Mask | 遮罩层

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Mask component in Ant Design Mobile.

### Key Concepts

- Basic mask
- Mask with visible
- Mask with opacity
- Mask with clickable
- Mask with content

### Example: Basic Mask

```javascript
import React, { useState } from 'react';
import { Mask, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示遮罩</Button>
      <Mask visible={visible} onMaskClick={() => setVisible(false)} />
    </>
  );
}
```

### Example: Mask with Opacity

```javascript
import React, { useState } from 'react';
import { Mask, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示遮罩</Button>
      <Mask
        visible={visible}
        onMaskClick={() => setVisible(false)}
        opacity={0.5}
      />
    </>
  );
}
```

### Example: Mask with Content

```javascript
import React, { useState } from 'react';
import { Mask, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示遮罩</Button>
      <Mask
        visible={visible}
        onMaskClick={() => setVisible(false)}
      >
        <div style={{ padding: '20px', background: '#fff', borderRadius: '8px' }}>
          内容
        </div>
      </Mask>
    </>
  );
}
```

### Example: Mask with Clickable

```javascript
import React, { useState } from 'react';
import { Mask, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示遮罩</Button>
      <Mask
        visible={visible}
        onMaskClick={() => setVisible(false)}
        disableBodyScroll={false}
      />
    </>
  );
}
```

### Key Points

- Use `visible` prop to control visibility
- Use `onMaskClick` callback for mask click
- Use `opacity` prop for mask opacity
- Use `disableBodyScroll` prop to disable body scroll
- Use children for mask content
- Mask is optimized for mobile display
