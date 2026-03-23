# Component Template | 组件模板

## Basic Component Usage

```javascript
import React from 'react';
import { ComponentName } from 'antd-mobile';

function App() {
  return (
    <ComponentName
      prop1="value1"
      prop2="value2"
      onChange={(value) => console.log(value)}
    />
  );
}
```

## Component with State

```javascript
import React, { useState } from 'react';
import { ComponentName } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <ComponentName
      value={value}
      onChange={(val) => setValue(val)}
    />
  );
}
```

## Component in Form

```javascript
import React from 'react';
import { Form, ComponentName } from 'antd-mobile';

function App() {
  return (
    <Form>
      <Form.Item name="field" label="Label">
        <ComponentName />
      </Form.Item>
    </Form>
  );
}
```
