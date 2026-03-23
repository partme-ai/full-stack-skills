# Button | 按钮

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Button component in Ant Design Mobile.

### Key Concepts

- Button colors (primary, success, warning, danger)
- Button sizes (large, middle, small, mini)
- Button shapes (rectangular, rounded, square)
- Button states (loading, disabled)
- Button with icons
- Block buttons

### Example: Button Colors

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <>
      <Button color="primary">Primary</Button>
      <Button color="success">Success</Button>
      <Button color="warning">Warning</Button>
      <Button color="danger">Danger</Button>
      <Button>Default</Button>
    </>
  );
}
```

### Example: Button Sizes

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <>
      <Button color="primary" size="large">Large</Button>
      <Button color="primary" size="middle">Middle</Button>
      <Button color="primary" size="small">Small</Button>
      <Button color="primary" size="mini">Mini</Button>
    </>
  );
}
```

### Example: Button with Icon

```javascript
import React from 'react';
import { Button } from 'antd-mobile';
import { SearchOutline } from 'antd-mobile-icons';

function App() {
  return (
    <Button color="primary" fill="outline">
      <SearchOutline />
      Search
    </Button>
  );
}
```

### Example: Loading State

```javascript
import React, { useState } from 'react';
import { Button } from 'antd-mobile';

function App() {
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  };

  return (
    <Button color="primary" loading={loading} onClick={handleClick}>
      Click Me
    </Button>
  );
}
```

### Example: Block Button

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <Button color="primary" block>
      Block Button
    </Button>
  );
}
```

### Example: Disabled Button

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <>
      <Button color="primary" disabled>Disabled Primary</Button>
      <Button disabled>Disabled Default</Button>
    </>
  );
}
```

### Key Points

- Use `color` prop for button style (primary, success, warning, danger)
- Use `size` prop for button size (large, middle, small, mini)
- Use `fill` prop for button fill style (solid, outline, none)
- Use `icon` or icon components for icon buttons
- Use `loading` prop for loading state
- Use `disabled` prop to disable button
- Use `block` prop for full-width button
- Button is optimized for mobile touch interactions
