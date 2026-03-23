# Icon | 图标

**官方文档**: https://4x-ant-design.antgroup.com/components/icon-cn


## Instructions

This example demonstrates how to use icons in Ant Design React.

### Key Concepts

- Importing icons from @ant-design/icons
- Using icons in components
- Icon sizes
- Icon colors
- Custom icons

### Example: Basic Icon Usage

```javascript
import React from 'react';
import { HomeOutlined, UserOutlined, SettingOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <HomeOutlined />
      <UserOutlined />
      <SettingOutlined />
    </>
  );
}
```

### Example: Icon with Button

```javascript
import React from 'react';
import { Button } from 'antd';
import { DownloadOutlined, SearchOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <Button type="primary" icon={<DownloadOutlined />}>
        Download
      </Button>
      <Button icon={<SearchOutlined />}>Search</Button>
    </>
  );
}
```

### Example: Icon Sizes

```javascript
import React from 'react';
import { HomeOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <HomeOutlined style={{ fontSize: '16px' }} />
      <HomeOutlined style={{ fontSize: '24px' }} />
      <HomeOutlined style={{ fontSize: '32px' }} />
    </>
  );
}
```

### Example: Icon Colors

```javascript
import React from 'react';
import { HeartOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <HeartOutlined style={{ color: '#ff4d4f' }} />
      <HeartOutlined style={{ color: '#52c41a' }} />
      <HeartOutlined style={{ color: '#1890ff' }} />
    </>
  );
}
```

### Key Points

- Import icons from '@ant-design/icons'
- Icons are React components
- Use style prop for size and color
- Icons can be used in buttons, menus, etc.
- Icon names follow Outlined, Filled, TwoTone pattern
- Use appropriate icon variant (Outlined, Filled, TwoTone)
