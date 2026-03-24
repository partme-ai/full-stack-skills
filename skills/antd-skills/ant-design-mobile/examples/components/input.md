# Input | 输入框

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Input component in Ant Design Mobile.

### Key Concepts

- Basic Input
- Input types
- Input with clear button
- Input with prefix/suffix
- Input validation
- Virtual keyboard

### Example: Basic Input

```javascript
import React, { useState } from 'react';
import { Input } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <Input
      placeholder="Enter text"
      value={value}
      onChange={(val) => setValue(val)}
    />
  );
}
```

### Example: Input Types

```javascript
import React from 'react';
import { Input } from 'antd-mobile';

function App() {
  return (
    <>
      <Input type="text" placeholder="Text input" />
      <Input type="number" placeholder="Number input" />
      <Input type="password" placeholder="Password input" />
      <Input type="tel" placeholder="Phone input" />
    </>
  );
}
```

### Example: Input with Clear Button

```javascript
import React, { useState } from 'react';
import { Input } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <Input
      placeholder="Enter text"
      value={value}
      onChange={(val) => setValue(val)}
      clearable
    />
  );
}
```

### Example: Input with Prefix/Suffix

```javascript
import React from 'react';
import { Input } from 'antd-mobile';
import { SearchOutline } from 'antd-mobile-icons';

function App() {
  return (
    <Input
      placeholder="Search"
      prefix={<SearchOutline />}
    />
  );
}
```

### Example: Input Validation

```javascript
import React, { useState } from 'react';
import { Input } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');
  const [error, setError] = useState('');

  const handleChange = (val) => {
    setValue(val);
    if (val.length < 6) {
      setError('At least 6 characters');
    } else {
      setError('');
    }
  };

  return (
    <Input
      placeholder="Enter text"
      value={value}
      onChange={handleChange}
      error={error}
    />
  );
}
```

### Key Points

- Use `Input` for text input
- Use `type` prop for input type (text, number, password, tel, etc.)
- Use `clearable` prop for clear button
- Use `prefix` and `suffix` for icons
- Use `error` prop for validation errors
- Use `onChange` handler receives value directly
- Optimized for mobile virtual keyboard
