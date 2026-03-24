# Radio | 单选框

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Radio component in Ant Design Mobile.

### Key Concepts

- Basic radio
- Radio group
- Radio with label
- Radio states
- Radio shapes

### Example: Basic Radio

```javascript
import React, { useState } from 'react';
import { Radio } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('1');

  return (
    <>
      <Radio
        checked={value === '1'}
        onChange={() => setValue('1')}
      >
        选项1
      </Radio>
      <Radio
        checked={value === '2'}
        onChange={() => setValue('2')}
      >
        选项2
      </Radio>
    </>
  );
}
```

### Example: Radio Group

```javascript
import React, { useState } from 'react';
import { Radio } from 'antd-mobile';

const options = [
  { label: '选项1', value: '1' },
  { label: '选项2', value: '2' },
  { label: '选项3', value: '3' },
];

function App() {
  const [value, setValue] = useState('1');

  return (
    <Radio.Group
      value={value}
      onChange={(val) => setValue(val)}
    >
      {options.map(option => (
        <Radio key={option.value} value={option.value}>
          {option.label}
        </Radio>
      ))}
    </Radio.Group>
  );
}
```

### Example: Radio States

```javascript
import React from 'react';
import { Radio } from 'antd-mobile';

function App() {
  return (
    <>
      <Radio defaultChecked>默认选中</Radio>
      <Radio disabled>禁用</Radio>
      <Radio checked disabled>禁用且选中</Radio>
    </>
  );
}
```

### Example: Radio Shapes

```javascript
import React, { useState } from 'react';
import { Radio } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('1');

  return (
    <>
      <Radio.Group value={value} onChange={setValue}>
        <Radio value="1" shape="square">方形</Radio>
        <Radio value="2" shape="round">圆形</Radio>
      </Radio.Group>
    </>
  );
}
```

### Example: Radio with Form

```javascript
import React from 'react';
import { Form, Radio } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="gender" label="性别">
        <Radio.Group>
          <Radio value="male">男</Radio>
          <Radio value="female">女</Radio>
        </Radio.Group>
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `checked` prop for radio state
- Use `onChange` callback for state change
- Use `Radio.Group` for radio group
- Use `disabled` prop to disable radio
- Use `shape` prop for radio shape (square, round)
- Radio works well with Form component
- Radio is optimized for mobile touch interactions
