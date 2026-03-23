# NavBar | 导航栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the NavBar component in Ant Design Mobile.

### Key Concepts

- Basic navbar
- Navbar with back button
- Navbar with title
- Navbar with right content
- Navbar with custom styles

### Example: Basic NavBar

```javascript
import React from 'react';
import { NavBar } from 'antd-mobile';

function App() {
  return (
    <NavBar>标题</NavBar>
  );
}
```

### Example: NavBar with Back Button

```javascript
import React from 'react';
import { NavBar } from 'antd-mobile';

function App() {
  return (
    <NavBar
      onBack={() => {
        console.log('返回');
      }}
    >
      标题
    </NavBar>
  );
}
```

### Example: NavBar with Right Content

```javascript
import React from 'react';
import { NavBar, Button } from 'antd-mobile';

function App() {
  return (
    <NavBar
      right={
        <Button size="small" color="primary">
          操作
        </Button>
      }
    >
      标题
    </NavBar>
  );
}
```

### Example: NavBar with Left Content

```javascript
import React from 'react';
import { NavBar } from 'antd-mobile';
import { LeftOutline } from 'antd-mobile-icons';

function App() {
  return (
    <NavBar
      left={<LeftOutline />}
      right="操作"
    >
      标题
    </NavBar>
  );
}
```

### Example: NavBar with Custom Styles

```javascript
import React from 'react';
import { NavBar } from 'antd-mobile';

function App() {
  return (
    <NavBar
      style={{
        background: '#409EFF',
        color: '#fff',
      }}
    >
      标题
    </NavBar>
  );
}
```

### Key Points

- Use children for navbar title
- Use `onBack` callback for back button
- Use `left` prop for left content
- Use `right` prop for right content
- Use `style` prop for custom styles
- NavBar is optimized for mobile display
- NavBar supports safe area insets
