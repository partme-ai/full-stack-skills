# Menu | 菜单

**官方文档**: https://4x-ant-design.antgroup.com/components/menu-cn


## Instructions

This example demonstrates how to use the Menu component in Ant Design React.

### Key Concepts

- Basic Menu
- Menu with icons
- Menu with submenus
- Menu modes (vertical, horizontal, inline)
- Menu selection
- Menu with router

### Example: Basic Menu

```javascript
import React, { useState } from 'react';
import { Menu } from 'antd';

function App() {
  const [current, setCurrent] = useState('mail');

  const onClick = (e) => {
    setCurrent(e.key);
  };

  const items = [
    {
      label: 'Navigation One',
      key: 'mail',
    },
    {
      label: 'Navigation Two',
      key: 'app',
    },
    {
      label: 'Navigation Three',
      key: 'submenu',
      children: [
        {
          type: 'group',
          label: 'Item 1',
          children: [
            { label: 'Option 1', key: 'setting:1' },
            { label: 'Option 2', key: 'setting:2' },
          ],
        },
      ],
    },
  ];

  return (
    <Menu
      onClick={onClick}
      selectedKeys={[current]}
      mode="horizontal"
      items={items}
    />
  );
}
```

### Example: Vertical Menu

```javascript
import React, { useState } from 'react';
import { Menu } from 'antd';
import {
  AppstoreOutlined,
  MailOutlined,
  SettingOutlined,
} from '@ant-design/icons';

function App() {
  const [current, setCurrent] = useState('mail');

  const items = [
    {
      label: 'Navigation One',
      key: 'mail',
      icon: <MailOutlined />,
    },
    {
      label: 'Navigation Two',
      key: 'app',
      icon: <AppstoreOutlined />,
    },
    {
      label: 'Navigation Three',
      key: 'sub1',
      icon: <SettingOutlined />,
      children: [
        { label: 'Option 1', key: '1' },
        { label: 'Option 2', key: '2' },
      ],
    },
  ];

  return (
    <Menu
      onClick={(e) => setCurrent(e.key)}
      selectedKeys={[current]}
      mode="vertical"
      items={items}
    />
  );
}
```

### Example: Inline Menu

```javascript
import React, { useState } from 'react';
import { Menu } from 'antd';

function App() {
  const [openKeys, setOpenKeys] = useState(['sub1']);

  const items = [
    {
      label: 'Navigation One',
      key: 'sub1',
      children: [
        { label: 'Option 1', key: '1' },
        { label: 'Option 2', key: '2' },
      ],
    },
  ];

  const onOpenChange = (keys) => {
    setOpenKeys(keys);
  };

  return (
    <Menu
      mode="inline"
      openKeys={openKeys}
      onOpenChange={onOpenChange}
      items={items}
    />
  );
}
```

### Key Points

- Use `items` prop for menu items (v4+)
- Use `mode` prop for menu direction (horizontal, vertical, inline)
- Use `selectedKeys` for selected menu items
- Use `onClick` to handle menu item clicks
- Use `openKeys` and `onOpenChange` for submenu control
- Use icons in menu items
- Support nested submenus
