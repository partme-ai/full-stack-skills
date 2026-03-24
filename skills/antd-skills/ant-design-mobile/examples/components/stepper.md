# Stepper | 步进器

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Stepper component in Ant Design Mobile.

### Key Concepts

- Basic stepper
- Stepper with min/max
- Stepper with step
- Stepper with disabled
- Stepper with formatter

### Example: Basic Stepper

```javascript
import React, { useState } from 'react';
import { Stepper } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(1);

  return (
    <Stepper
      value={value}
      onChange={(val) => setValue(val)}
    />
  );
}
```

### Example: Stepper with Min/Max

```javascript
import React, { useState } from 'react';
import { Stepper } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(1);

  return (
    <Stepper
      value={value}
      onChange={(val) => setValue(val)}
      min={0}
      max={10}
    />
  );
}
```

### Example: Stepper with Step

```javascript
import React, { useState } from 'react';
import { Stepper } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(1);

  return (
    <Stepper
      value={value}
      onChange={(val) => setValue(val)}
      step={2}
    />
  );
}
```

### Example: Stepper with Disabled

```javascript
import React, { useState } from 'react';
import { Stepper } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(1);

  return (
    <>
      <Stepper
        value={value}
        onChange={(val) => setValue(val)}
        disabled
      />
      <Stepper
        value={value}
        onChange={(val) => setValue(val)}
        min={0}
        max={10}
      />
    </>
  );
}
```

### Example: Stepper with Formatter

```javascript
import React, { useState } from 'react';
import { Stepper } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(1);

  return (
    <Stepper
      value={value}
      onChange={(val) => setValue(val)}
      formatter={(value) => `${value}件`}
    />
  );
}
```

### Example: Stepper with Form

```javascript
import React from 'react';
import { Form, Stepper } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="quantity" label="数量">
        <Stepper min={1} max={99} />
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `value` prop for stepper value
- Use `onChange` callback for value change
- Use `min` and `max` props to limit value range
- Use `step` prop for step increment
- Use `disabled` prop to disable stepper
- Use `formatter` prop to format displayed value
- Stepper works well with Form component
- Stepper is optimized for mobile touch interactions
