# VirtualInput | 虚拟键盘

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the VirtualInput component in Ant Design Mobile.

### Key Concepts

- Basic virtual input
- Virtual input with type
- Virtual input with confirm
- Virtual input with custom keyboard

### Example: Basic VirtualInput

```javascript
import React, { useState } from 'react';
import { VirtualInput } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <VirtualInput
      value={value}
      onChange={setValue}
      placeholder="请输入"
    />
  );
}
```

### Example: VirtualInput with Type

```javascript
import React, { useState } from 'react';
import { VirtualInput } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <>
      <VirtualInput
        value={value}
        onChange={setValue}
        type="number"
        placeholder="数字键盘"
      />
      <VirtualInput
        value={value}
        onChange={setValue}
        type="password"
        placeholder="密码键盘"
      />
    </>
  );
}
```

### Example: VirtualInput with Confirm

```javascript
import React, { useState } from 'react';
import { VirtualInput } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <VirtualInput
      value={value}
      onChange={setValue}
      placeholder="请输入"
      confirmText="确定"
      onConfirm={(val) => {
        console.log('确认:', val);
      }}
    />
  );
}
```

### Key Points

- Use `value` prop for input value
- Use `onChange` callback for value change
- Use `type` prop for keyboard type (number, password, etc.)
- Use `confirmText` prop for confirm button text
- Use `onConfirm` callback for confirm event
- VirtualInput is optimized for mobile virtual keyboards
