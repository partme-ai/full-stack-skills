# Basic Usage | 基本用法

**官方文档**: https://4x-ant-design.antgroup.com/docs/react/introduce-cn


## Instructions

This example demonstrates basic Ant Design component usage in React.

### Key Concepts

- Importing components
- Using component props
- Component composition
- Event handling

### Example: Button Component

```javascript
import React from 'react';
import { Button } from 'antd';

function App() {
  return (
    <div>
      <Button type="primary">Primary</Button>
      <Button>Default</Button>
      <Button type="dashed">Dashed</Button>
      <Button type="text">Text</Button>
      <Button type="link">Link</Button>
    </div>
  );
}
```

### Example: Button with Events

```javascript
import React from 'react';
import { Button, message } from 'antd';

function App() {
  const handleClick = () => {
    message.success('Button clicked!');
  };

  return (
    <Button type="primary" onClick={handleClick}>
      Click Me
    </Button>
  );
}
```

### Example: Input Component

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

### Example: Multiple Components

```javascript
import React from 'react';
import { Button, Input, Card } from 'antd';

function App() {
  return (
    <Card title="Example Card">
      <Input placeholder="Enter text" />
      <Button type="primary" style={{ marginTop: 16 }}>
        Submit
      </Button>
    </Card>
  );
}
```

### Key Points

- Import components from 'antd'
- Use component props to configure behavior
- Components are composable
- Handle events with React event handlers
- Use style prop for inline styles
- Follow React patterns for state management
