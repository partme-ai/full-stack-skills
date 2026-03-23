# TabBar | 标签栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the TabBar component in Ant Design Mobile.

### Key Concepts

- Basic tabbar
- TabBar with icons
- TabBar with badges
- TabBar with active key
- TabBar with custom styles

### Example: Basic TabBar

```javascript
import React, { useState } from 'react';
import { TabBar } from 'antd-mobile';
import { AppOutline, UserOutline } from 'antd-mobile-icons';

const tabs = [
  {
    key: 'home',
    title: '首页',
    icon: <AppOutline />,
  },
  {
    key: 'user',
    title: '我的',
    icon: <UserOutline />,
  },
];

function App() {
  const [activeKey, setActiveKey] = useState('home');

  return (
    <TabBar
      activeKey={activeKey}
      onChange={setActiveKey}
    >
      {tabs.map(item => (
        <TabBar.Item key={item.key} icon={item.icon} title={item.title} />
      ))}
    </TabBar>
  );
}
```

### Example: TabBar with Badges

```javascript
import React, { useState } from 'react';
import { TabBar, Badge } from 'antd-mobile';
import { AppOutline, UserOutline } from 'antd-mobile-icons';

const tabs = [
  {
    key: 'home',
    title: '首页',
    icon: <AppOutline />,
    badge: '5',
  },
  {
    key: 'user',
    title: '我的',
    icon: <UserOutline />,
    badge: Badge.dot,
  },
];

function App() {
  const [activeKey, setActiveKey] = useState('home');

  return (
    <TabBar
      activeKey={activeKey}
      onChange={setActiveKey}
    >
      {tabs.map(item => (
        <TabBar.Item
          key={item.key}
          icon={item.icon}
          title={item.title}
          badge={item.badge}
        />
      ))}
    </TabBar>
  );
}
```

### Example: TabBar with Safe Area

```javascript
import React, { useState } from 'react';
import { TabBar, SafeArea } from 'antd-mobile';
import { AppOutline, UserOutline } from 'antd-mobile-icons';

const tabs = [
  {
    key: 'home',
    title: '首页',
    icon: <AppOutline />,
  },
  {
    key: 'user',
    title: '我的',
    icon: <UserOutline />,
  },
];

function App() {
  const [activeKey, setActiveKey] = useState('home');

  return (
    <>
      <TabBar
        activeKey={activeKey}
        onChange={setActiveKey}
      >
        {tabs.map(item => (
          <TabBar.Item key={item.key} icon={item.icon} title={item.title} />
        ))}
      </TabBar>
      <SafeArea position="bottom" />
    </>
  );
}
```

### Key Points

- Use `activeKey` prop for active tab
- Use `onChange` callback for tab change
- Use `TabBar.Item` for tab items
- Use `icon` prop for tab icon
- Use `title` prop for tab title
- Use `badge` prop for tab badge
- TabBar is optimized for mobile display
- TabBar supports safe area insets
