# Rate | 评分

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Rate component in Ant Design Mobile.

### Key Concepts

- Basic rate
- Rate with count
- Rate with allow half
- Rate with readonly
- Rate with custom character

### Example: Basic Rate

```javascript
import React, { useState } from 'react';
import { Rate } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(3);

  return (
    <Rate
      value={value}
      onChange={(val) => setValue(val)}
    />
  );
}
```

### Example: Rate with Count

```javascript
import React, { useState } from 'react';
import { Rate } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(3);

  return (
    <>
      <Rate
        value={value}
        onChange={(val) => setValue(val)}
        count={5}
      />
      <Rate
        value={value}
        onChange={(val) => setValue(val)}
        count={10}
      />
    </>
  );
}
```

### Example: Rate with Allow Half

```javascript
import React, { useState } from 'react';
import { Rate } from 'antd-mobile';

function App() {
  const [value, setValue] = useState(3.5);

  return (
    <Rate
      value={value}
      onChange={(val) => setValue(val)}
      allowHalf
    />
  );
}
```

### Example: Rate Readonly

```javascript
import React from 'react';
import { Rate } from 'antd-mobile';

function App() {
  return (
    <>
      <Rate value={3} readonly />
      <Rate value={4.5} readonly allowHalf />
    </>
  );
}
```

### Example: Rate with Custom Character

```javascript
import React, { useState } from 'react';
import { Rate } from 'antd-mobile';
import { HeartFill } from 'antd-mobile-icons';

function App() {
  const [value, setValue] = useState(3);

  return (
    <Rate
      value={value}
      onChange={(val) => setValue(val)}
      character={<HeartFill />}
    />
  );
}
```

### Example: Rate with Form

```javascript
import React from 'react';
import { Form, Rate } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="rating" label="评分">
        <Rate />
      </Form.Item>
    </Form>
  );
}
```

### Key Points

- Use `value` prop for rate value
- Use `onChange` callback for value change
- Use `count` prop for star count
- Use `allowHalf` prop for half star selection
- Use `readonly` prop for readonly rate
- Use `character` prop for custom character
- Rate works well with Form component
- Rate is optimized for mobile touch interactions
