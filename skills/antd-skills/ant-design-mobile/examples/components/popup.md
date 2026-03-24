# Popup | 弹出层

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Popup component in Ant Design Mobile.

### Key Concepts

- Basic popup
- Popup with position
- Popup with mask
- Popup with close button
- Popup with content

### Example: Basic Popup

```javascript
import React, { useState } from 'react';
import { Popup, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示弹出层</Button>
      <Popup
        visible={visible}
        onMaskClick={() => setVisible(false)}
      >
        <div style={{ padding: '20px' }}>内容</div>
      </Popup>
    </>
  );
}
```

### Example: Popup with Position

```javascript
import React, { useState } from 'react';
import { Popup, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示弹出层</Button>
      <Popup
        visible={visible}
        onMaskClick={() => setVisible(false)}
        position="bottom"
      >
        <div style={{ padding: '20px' }}>内容</div>
      </Popup>
    </>
  );
}
```

### Example: Popup with Close Button

```javascript
import React, { useState } from 'react';
import { Popup, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示弹出层</Button>
      <Popup
        visible={visible}
        onMaskClick={() => setVisible(false)}
        showCloseButton
        onClose={() => setVisible(false)}
      >
        <div style={{ padding: '20px' }}>内容</div>
      </Popup>
    </>
  );
}
```

### Example: Popup with Title

```javascript
import React, { useState } from 'react';
import { Popup, Button } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <Button onClick={() => setVisible(true)}>显示弹出层</Button>
      <Popup
        visible={visible}
        onMaskClick={() => setVisible(false)}
        title="标题"
      >
        <div style={{ padding: '20px' }}>内容</div>
      </Popup>
    </>
  );
}
```

### Key Points

- Use `visible` prop to control visibility
- Use `onMaskClick` callback for mask click
- Use `position` prop for popup position (top, bottom, left, right, center)
- Use `showCloseButton` prop for close button
- Use `onClose` callback for close event
- Use `title` prop for popup title
- Popup is optimized for mobile display
