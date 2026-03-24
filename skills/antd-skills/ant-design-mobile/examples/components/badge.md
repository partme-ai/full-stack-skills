# Badge | 徽标

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Badge component in Ant Design Mobile.

### Key Concepts

- Badge with number
- Badge with text
- Badge with dot
- Badge colors
- Badge positions

### Example: Basic Badge

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <Badge content="5">
      <div style={{ width: 40, height: 40, background: '#ddd' }} />
    </Badge>
  );
}
```

### Example: Badge with Number

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <>
      <Badge content={5}>
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
      <Badge content={99}>
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
      <Badge content={100}>
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
    </>
  );
}
```

### Example: Badge with Dot

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <Badge dot>
      <div style={{ width: 40, height: 40, background: '#ddd' }} />
    </Badge>
  );
}
```

### Example: Badge Colors

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <>
      <Badge content="5" color="red">
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
      <Badge content="5" color="blue">
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
      <Badge content="5" color="green">
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
    </>
  );
}
```

### Example: Badge Positions

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <>
      <Badge content="5" position="top-right">
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
      <Badge content="5" position="bottom-right">
        <div style={{ width: 40, height: 40, background: '#ddd' }} />
      </Badge>
    </>
  );
}
```

### Example: Badge with Max Count

```javascript
import React from 'react';
import { Badge } from 'antd-mobile';

function App() {
  return (
    <Badge content={100} max={99}>
      <div style={{ width: 40, height: 40, background: '#ddd' }} />
    </Badge>
  );
}
```

### Key Points

- Use `content` prop for badge content (number or string)
- Use `dot` prop for dot badge
- Use `color` prop for badge color
- Use `position` prop for badge position
- Use `max` prop to limit displayed number
- Badge wraps children element
- Badge is optimized for mobile display
