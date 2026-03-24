# SideBar | 侧边栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the SideBar component in Ant Design Mobile.

### Key Concepts

- Basic sidebar
- Sidebar with active key
- Sidebar with content
- Sidebar with custom styles

### Example: Basic SideBar

```javascript
import React, { useState } from 'react';
import { SideBar } from 'antd-mobile';

const items = [
  { key: '1', title: '选项1' },
  { key: '2', title: '选项2' },
  { key: '3', title: '选项3' },
];

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <SideBar activeKey={activeKey} onChange={setActiveKey}>
      {items.map(item => (
        <SideBar.Item key={item.key} title={item.title} />
      ))}
    </SideBar>
  );
}
```

### Example: SideBar with Content

```javascript
import React, { useState } from 'react';
import { SideBar } from 'antd-mobile';

const items = [
  { key: '1', title: '选项1', content: '内容1' },
  { key: '2', title: '选项2', content: '内容2' },
  { key: '3', title: '选项3', content: '内容3' },
];

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <div style={{ display: 'flex', height: '100vh' }}>
      <SideBar activeKey={activeKey} onChange={setActiveKey}>
        {items.map(item => (
          <SideBar.Item key={item.key} title={item.title} />
        ))}
      </SideBar>
      <div style={{ flex: 1, padding: '20px' }}>
        {items.find(item => item.key === activeKey)?.content}
      </div>
    </div>
  );
}
```

### Example: SideBar with Badge

```javascript
import React, { useState } from 'react';
import { SideBar, Badge } from 'antd-mobile';

const items = [
  { key: '1', title: '选项1', badge: '5' },
  { key: '2', title: '选项2', badge: Badge.dot },
  { key: '3', title: '选项3' },
];

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <SideBar activeKey={activeKey} onChange={setActiveKey}>
      {items.map(item => (
        <SideBar.Item
          key={item.key}
          title={item.title}
          badge={item.badge}
        />
      ))}
    </SideBar>
  );
}
```

### Key Points

- Use `activeKey` prop for active item
- Use `onChange` callback for item change
- Use `SideBar.Item` for sidebar items
- Use `title` prop for item title
- Use `badge` prop for item badge
- SideBar is optimized for mobile display
- SideBar supports touch interactions
