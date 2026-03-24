# Input | 输入框

**官方文档**: https://4x-ant-design.antgroup.com/components/input-cn


## Instructions

This example demonstrates how to use the Input component in Ant Design React.

### Key Concepts

- Basic Input
- Input with prefix/suffix
- Input sizes
- Input types (text, password, search, textarea)
- Input with addon
- Input validation

### Example: Basic Input

```javascript
import React, { useState } from 'react';
import { Input } from 'antd';

function App() {
  const [value, setValue] = useState('');

  return (
    <Input
      placeholder="Enter text"
      value={value}
      onChange={(e) => setValue(e.target.value)}
    />
  );
}
```

### Example: Input Sizes

```javascript
import React from 'react';
import { Input } from 'antd';

function App() {
  return (
    <>
      <Input size="large" placeholder="Large size" />
      <Input placeholder="Default size" />
      <Input size="small" placeholder="Small size" />
    </>
  );
}
```

### Example: Input with Prefix/Suffix

```javascript
import React from 'react';
import { Input } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <Input
        prefix={<UserOutlined />}
        placeholder="Username"
      />
      <Input
        prefix={<LockOutlined />}
        type="password"
        placeholder="Password"
      />
    </>
  );
}
```

### Example: Input.Password

```javascript
import React from 'react';
import { Input } from 'antd';

function App() {
  return <Input.Password placeholder="Enter password" />;
}
```

### Example: Input.Search

```javascript
import React from 'react';
import { Input } from 'antd';

const { Search } = Input;

function App() {
  const onSearch = (value) => {
    console.log('Search:', value);
  };

  return (
    <Search
      placeholder="Search"
      onSearch={onSearch}
      enterButton
    />
  );
}
```

### Example: Input.TextArea

```javascript
import React from 'react';
import { Input } from 'antd';

const { TextArea } = Input;

function App() {
  return (
    <TextArea
      rows={4}
      placeholder="Enter text"
      showCount
      maxLength={100}
    />
  );
}
```

### Example: Input with Addon

```javascript
import React from 'react';
import { Input } from 'antd';

const { Group, Addon } = Input;

function App() {
  return (
    <>
      <Input.Group compact>
        <Input style={{ width: '20%' }} defaultValue="0571" />
        <Input style={{ width: '80%' }} defaultValue="26888888" />
      </Input.Group>
    </>
  );
}
```

### Key Points

- Use `Input` for text input
- Use `Input.Password` for password input
- Use `Input.Search` for search input
- Use `Input.TextArea` for multi-line input
- Use `prefix` and `suffix` for icons
- Use `size` prop for input size
- Use `showCount` for character count
- Use `maxLength` to limit input length
