# Checkbox | 复选框

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Checkbox component in Ant Design Mobile.

### Key Concepts

- Basic checkbox
- Checkbox group
- Checkbox with label
- Checkbox states
- Checkbox shapes

### Example: Basic Checkbox

```javascript
import React, { useState } from 'react';
import { Checkbox } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);

  return (
    <Checkbox
      checked={checked}
      onChange={(checked) => setChecked(checked)}
    >
      选项
    </Checkbox>
  );
}
```

### Example: Checkbox Group

```javascript
import React, { useState } from 'react';
import { Checkbox } from 'antd-mobile';

const options = [
  { label: '选项1', value: '1' },
  { label: '选项2', value: '2' },
  { label: '选项3', value: '3' },
];

function App() {
  const [value, setValue] = useState([]);

  return (
    <Checkbox.Group
      value={value}
      onChange={(val) => setValue(val)}
    >
      {options.map(option => (
        <Checkbox key={option.value} value={option.value}>
          {option.label}
        </Checkbox>
      ))}
    </Checkbox.Group>
  );
}
```

### Example: Checkbox States

```javascript
import React from 'react';
import { Checkbox } from 'antd-mobile';

function App() {
  return (
    <>
      <Checkbox defaultChecked>默认选中</Checkbox>
      <Checkbox disabled>禁用</Checkbox>
      <Checkbox checked disabled>禁用且选中</Checkbox>
    </>
  );
}
```

### Example: Checkbox Shapes

```javascript
import React, { useState } from 'react';
import { Checkbox } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);

  return (
    <>
      <Checkbox
        checked={checked}
        onChange={(checked) => setChecked(checked)}
      >
        默认形状
      </Checkbox>
      <Checkbox
        checked={checked}
        onChange={(checked) => setChecked(checked)}
        shape="round"
      >
        圆形
      </Checkbox>
    </>
  );
}
```

### Example: Checkbox with Form

```javascript
import React from 'react';
import { Form, Checkbox } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="agree" label="同意协议">
        <Checkbox>我已阅读并同意</Checkbox>
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `checked` prop for checkbox state
- Use `onChange` callback for state change
- Use `Checkbox.Group` for multiple checkboxes
- Use `disabled` prop to disable checkbox
- Use `shape` prop for checkbox shape (square, round)
- Checkbox works well with Form component
- Checkbox is optimized for mobile touch interactions
