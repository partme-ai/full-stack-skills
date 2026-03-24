# DatePicker | 日期选择器

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the DatePicker component in Ant Design Mobile.

### Key Concepts

- Date selection
- Date range selection
- Date format
- Date picker modes
- Date picker with time

### Example: Basic DatePicker

```javascript
import React, { useState } from 'react';
import { DatePicker } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  return (
    <>
      <div onClick={() => setVisible(true)}>
        {value ? value.toLocaleDateString() : '选择日期'}
      </div>
      <DatePicker
        visible={visible}
        onClose={() => setVisible(false)}
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

### Example: DatePicker with Format

```javascript
import React, { useState } from 'react';
import { DatePicker } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  return (
    <>
      <div onClick={() => setVisible(true)}>
        {value ? value.toLocaleDateString() : '选择日期'}
      </div>
      <DatePicker
        visible={visible}
        onClose={() => setVisible(false)}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        precision="day"
      />
    </>
  );
}
```

### Example: DatePicker with Time

```javascript
import React, { useState } from 'react';
import { DatePicker } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  return (
    <>
      <div onClick={() => setVisible(true)}>
        {value ? value.toLocaleString() : '选择日期时间'}
      </div>
      <DatePicker
        visible={visible}
        onClose={() => setVisible(false)}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        precision="minute"
      />
    </>
  );
}
```

### Example: DatePicker with Min/Max

```javascript
import React, { useState } from 'react';
import { DatePicker } from 'antd-mobile';

function App() {
  const [visible, setVisible] = useState(false);
  const [value, setValue] = useState(null);

  return (
    <>
      <div onClick={() => setVisible(true)}>
        {value ? value.toLocaleDateString() : '选择日期'}
      </div>
      <DatePicker
        visible={visible}
        onClose={() => setVisible(false)}
        value={value}
        onConfirm={(val) => {
          setValue(val);
          setVisible(false);
        }}
        min={new Date('2020-01-01')}
        max={new Date('2030-12-31')}
      />
    </>
  );
}
```

### Example: DatePicker with Form

```javascript
import React from 'react';
import { Form, DatePicker } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="date" label="日期">
        <DatePicker precision="day">
          {(value) => value?.toLocaleDateString() || '请选择日期'}
        </DatePicker>
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `visible` prop to control picker visibility
- Use `value` prop for selected date
- Use `onConfirm` callback for confirm event
- Use `onClose` callback for close event
- Use `precision` prop for date precision (year, month, day, hour, minute, second)
- Use `min` and `max` props to limit date range
- DatePicker works well with Form component
- DatePicker is optimized for mobile display
