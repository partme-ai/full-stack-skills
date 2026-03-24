# Button | 按钮

**官方文档**: https://4x-ant-design.antgroup.com/components/button-cn


## Instructions

This example demonstrates how to use the Button component in Ant Design React.

### Key Concepts

- Button types (primary, default, dashed, text, link)
- Button sizes (large, middle, small)
- Button shapes (default, round, circle)
- Button states (loading, disabled)
- Button groups
- Icon buttons

### Example: Button Types

```javascript
import React from 'react';
import { Button } from 'antd';

function App() {
  return (
    <>
      <Button type="primary">Primary</Button>
      <Button>Default</Button>
      <Button type="dashed">Dashed</Button>
      <Button type="text">Text</Button>
      <Button type="link">Link</Button>
    </>
  );
}
```

### Example: Button Sizes

```javascript
import React from 'react';
import { Button } from 'antd';

function App() {
  return (
    <>
      <Button type="primary" size="large">Large</Button>
      <Button type="primary" size="middle">Middle</Button>
      <Button type="primary" size="small">Small</Button>
    </>
  );
}
```

### Example: Button with Icon

```javascript
import React from 'react';
import { Button } from 'antd';
import { DownloadOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <Button type="primary" icon={<DownloadOutlined />}>
        Download
      </Button>
      <Button icon={<DownloadOutlined />}>Download</Button>
    </>
  );
}
```

### Example: Loading State

```javascript
import React, { useState } from 'react';
import { Button } from 'antd';

function App() {
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 2000);
  };

  return (
    <Button type="primary" loading={loading} onClick={handleClick}>
      Click Me
    </Button>
  );
}
```

### Example: Button Group

```javascript
import React from 'react';
import { Button } from 'antd';

const { ButtonGroup } = Button;

function App() {
  return (
    <ButtonGroup>
      <Button>Left</Button>
      <Button>Middle</Button>
      <Button>Right</Button>
    </ButtonGroup>
  );
}
```

### Example: Disabled Button

```javascript
import React from 'react';
import { Button } from 'antd';

function App() {
  return (
    <>
      <Button type="primary" disabled>Disabled Primary</Button>
      <Button disabled>Disabled Default</Button>
    </>
  );
}
```

### Key Points

- Use `type` prop for button style (primary, default, dashed, text, link)
- Use `size` prop for button size (large, middle, small)
- Use `icon` prop for icon buttons
- Use `loading` prop for loading state
- Use `disabled` prop to disable button
- Use ButtonGroup for button groups
- Button supports all standard HTML button attributes
