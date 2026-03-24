# Slider | 滑动输入条

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Slider component in Ant Design Mobile.

### Key Concepts

- Basic slider
- Slider with min/max
- Slider with step
- Slider with marks
- Slider with range

### Example: Basic Slider

```javascript
import React, { useState } from 'react';
import { Slider } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(50);

  return (
    <Slider
      value={value}
      onChange={(val) => setValue(val)}
    />
  );
}
```

### Example: Slider with Min/Max

```javascript
import React, { useState } from 'react';
import { Slider } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(50);

  return (
    <Slider
      value={value}
      onChange={(val) => setValue(val)}
      min={0}
      max={100}
    />
  );
}
```

### Example: Slider with Step

```javascript
import React, { useState } from 'react';
import { Slider } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(50);

  return (
    <Slider
      value={value}
      onChange={(val) => setValue(val)}
      min={0}
      max={100}
      step={10}
    />
  );
}
```

### Example: Slider with Marks

```javascript
import React, { useState } from 'react';
import { Slider } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(50);

  return (
    <Slider
      value={value}
      onChange={(val) => setValue(val)}
      min={0}
      max={100}
      marks={{
        0: '0',
        50: '50',
        100: '100',
      }}
    />
  );
}
```

### Example: Slider Range

```javascript
import React, { useState } from 'react';
import { Slider } from 'antd-mobile';

function App() {
  const [value, setValue] = useState([20, 80]);

  return (
    <Slider
      value={value}
      onChange={(val) => setValue(val)}
      min={0}
      max={100}
      range
    />
  );
}
```

### Example: Slider with Form

```javascript
import React from 'react';
import { Form, Slider } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="volume" label="音量">
        <Slider min={0} max={100} />
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `value` prop for slider value
- Use `onChange` callback for value change
- Use `min` and `max` props to limit value range
- Use `step` prop for step increment
- Use `marks` prop for marks display
- Use `range` prop for range selection
- Slider works well with Form component
- Slider is optimized for mobile touch interactions
