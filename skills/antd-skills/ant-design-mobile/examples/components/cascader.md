# Cascader | 级联选择

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Cascader component in Ant Design Mobile.

### Key Concepts

- Basic cascader
- Cascader with options
- Cascader with value
- Cascader with visible
- Cascader with form

### Example: Basic Cascader

```javascript
import React, { useState } from 'react';
import { Cascader } from 'antd-mobile';

const options = [
  {
    label: '浙江',
    value: 'zhejiang',
    children: [
      {
        label: '杭州',
        value: 'hangzhou',
        children: [
          { label: '西湖区', value: 'xihu' },
          { label: '余杭区', value: 'yuhang' },
        ],
      },
    ],
  },
  {
    label: '江苏',
    value: 'jiangsu',
    children: [
      {
        label: '南京',
        value: 'nanjing',
        children: [
          { label: '玄武区', value: 'xuanwu' },
        ],
      },
    ],
  },
];

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState([]);

  return (
    <>
      <div onClick={() => setVisible(true)}>
        {value.length ? value.join('/') : '请选择'}
      </div>
      <Cascader
        visible={visible}
        onClose={() => setVisible(false)}
        options={options}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
      />
    </>
  );
}
```

### Example: Cascader with Form

```javascript
import React from 'react';
import { Form, Cascader } from 'antd-mobile';

const options = [
  {
    label: '浙江',
    value: 'zhejiang',
    children: [
      {
        label: '杭州',
        value: 'hangzhou',
        children: [
          { label: '西湖区', value: 'xihu' },
        ],
      },
    ],
  },
];

function App() {
  return (
    <Form>
      <Form.Item name="area" label="地区">
        <Cascader options={options}>
          {(value) => value?.join('/') || '请选择'}
        </Cascader>
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `visible` prop to control visibility
- Use `options` prop for cascader options
- Use `value` prop for selected value
- Use `onConfirm` callback for confirm event
- Use `onClose` callback for close event
- Cascader works well with Form component
- Cascader is optimized for mobile display
