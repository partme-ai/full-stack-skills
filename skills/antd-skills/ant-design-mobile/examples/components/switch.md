# Switch | 开关

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Switch component in Ant Design Mobile.

### Key Concepts

- Basic switch
- Switch with label
- Switch states
- Switch colors
- Switch sizes

### Example: Basic Switch

```javascript
import React, { useState } from 'react';
import { Switch } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);

  return (
    <Switch
      checked={checked}
      onChange={(checked) => setChecked(checked)}
    />
  );
}
```

### Example: Switch with Label

```javascript
import React, { useState } from 'react';
import { Switch, List } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);

  return (
    <List>
      <List.Item
        extra={
          <Switch
            checked={checked}
            onChange={(checked) => setChecked(checked)}
          />
        }
      >
        开关
      </List.Item>
    </List>
  );
}
```

### Example: Switch States

```javascript
import React from 'react';
import { Switch } from 'antd-mobile';

function App() {
  return (
    <>
      <Switch defaultChecked />
      <Switch disabled />
      <Switch checked disabled />
    </>
  );
}
```

### Example: Switch Colors

```javascript
import React, { useState } from 'react';
import { Switch } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);

  return (
    <>
      <Switch
        checked={checked}
        onChange={(checked) => setChecked(checked)}
      />
      <Switch
        checked={checked}
        onChange={(checked) => setChecked(checked)}
        color="primary"
      />
      <Switch
        checked={checked}
        onChange={(checked) => setChecked(checked)}
        color="#ff6b6b"
      />
    </>
  );
}
```

### Example: Switch with Loading

```javascript
import React, { useState } from 'react';
import { Switch } from 'antd-mobile';

function App() {
  const [checked, setChecked] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleChange = (val) => {
    setLoading(true);
    setTimeout(() => {
      setChecked(val);
      setLoading(false);
    }, 1000);
  };

  return (
    <Switch
      checked={checked}
      onChange={handleChange}
      loading={loading}
    />
  );
}
```

### Key Points

- Use `checked` prop for switch state
- Use `onChange` callback for state change
- Use `disabled` prop to disable switch
- Use `color` prop for switch color
- Use `loading` prop for loading state
- Switch is optimized for mobile touch interactions
