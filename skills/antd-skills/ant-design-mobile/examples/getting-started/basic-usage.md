# Basic Usage | 基本用法

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates basic Ant Design Mobile component usage in React.

### Key Concepts

- Importing components
- Using component props
- Component composition
- Event handling
- Mobile-specific considerations

### Example: Button Component

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <div>
      <Button color="primary">Primary</Button>
      <Button color="success">Success</Button>
      <Button color="warning">Warning</Button>
      <Button color="danger">Danger</Button>
    </div>
  );
}
```

### Example: Button with Events

```javascript
import React from 'react';
import { Button, Toast } from 'antd-mobile';

function App() {
  const handleClick = () => {
    Toast.show('Button clicked!');
  };

  return (
    <Button color="primary" onClick={handleClick}>
      Click Me
    </Button>
  );
}
```

### Example: Input Component

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

### Example: Multiple Components

```javascript
import React from 'react';
import { Button, Input, Card } from 'antd-mobile';

function App() {
  return (
    <Card title="Example Card">
      <Input placeholder="Enter text" />
      <Button color="primary" style={{ marginTop: 16 }}>
        Submit
      </Button>
    </Card>
  );
}
```

### Key Points

- Import components from 'antd-mobile'
- Use component props to configure behavior
- Components are optimized for mobile
- Handle events with React event handlers
- Use style prop for inline styles
- Follow React patterns for state management
- Consider touch interactions and mobile UX
