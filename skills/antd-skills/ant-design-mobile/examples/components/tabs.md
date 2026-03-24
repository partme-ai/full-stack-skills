# Tabs | 标签页

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Tabs component in Ant Design Mobile.

### Key Concepts

- Basic Tabs
- Tabs with content
- Tabs with icons
- Tabs with badges
- Tabs switching

### Example: Basic Tabs

```javascript
import React, { useState } from 'react';
import { Tabs } from 'antd-mobile';

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <Tabs activeKey={activeKey} onChange={setActiveKey}>
      <Tabs.Tab title="Tab 1" key="1">
        Content 1
      </Tabs.Tab>
      <Tabs.Tab title="Tab 2" key="2">
        Content 2
      </Tabs.Tab>
      <Tabs.Tab title="Tab 3" key="3">
        Content 3
      </Tabs.Tab>
    </Tabs>
  );
}
```

### Example: Tabs with Icons

```javascript
import React, { useState } from 'react';
import { Tabs } from 'antd-mobile';
import { AppOutline, UserOutline } from 'antd-mobile-icons';

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <Tabs activeKey={activeKey} onChange={setActiveKey}>
      <Tabs.Tab
        title={
          <span>
            <AppOutline />
            Tab 1
          </span>
        }
        key="1"
      >
        Content 1
      </Tabs.Tab>
      <Tabs.Tab
        title={
          <span>
            <UserOutline />
            Tab 2
          </span>
        }
        key="2"
      >
        Content 2
      </Tabs.Tab>
    </Tabs>
  );
}
```

### Example: Tabs with Badges

```javascript
import React, { useState } from 'react';
import { Tabs, Badge } from 'antd-mobile';

function App() {
  const [activeKey, setActiveKey] = useState('1');

  return (
    <Tabs activeKey={activeKey} onChange={setActiveKey}>
      <Tabs.Tab
        title={
          <Badge content="5">
            Tab 1
          </Badge>
        }
        key="1"
      >
        Content 1
      </Tabs.Tab>
      <Tabs.Tab title="Tab 2" key="2">
        Content 2
      </Tabs.Tab>
    </Tabs>
  );
}
```

### Key Points

- Use `Tabs` component with `Tabs.Tab` children
- Use `activeKey` to control active tab
- Use `onChange` to handle tab switching
- Use `title` prop for tab label
- Use `key` prop for unique tab identifier
- Tabs support icons and badges
- Optimized for mobile swipe gestures
