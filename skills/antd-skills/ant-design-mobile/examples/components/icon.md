# Icon | 图标

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Icon component in Ant Design Mobile.

### Key Concepts

- Icon types and names
- Icon sizes
- Icon colors
- Custom icons
- Icon with text

### Example: Basic Icon

```javascript
import React from 'react';
import { SearchOutline, HeartFill, StarOutline } from 'antd-mobile-icons';

function App() {
  return (
    <>
      <SearchOutline />
      <HeartFill />
      <StarOutline />
    </>
  );
}
```

### Example: Icon Sizes

```javascript
import React from 'react';
import { SearchOutline } from 'antd-mobile-icons';

function App() {
  return (
    <>
      <SearchOutline fontSize={16} />
      <SearchOutline fontSize={24} />
      <SearchOutline fontSize={32} />
    </>
  );
}
```

### Example: Icon Colors

```javascript
import React from 'react';
import { HeartFill } from 'antd-mobile-icons';

function App() {
  return (
    <>
      <HeartFill color="red" />
      <HeartFill color="#409EFF" />
      <HeartFill color="rgb(64, 158, 255)" />
    </>
  );
}
```

### Example: Icon with Button

```javascript
import React from 'react';
import { Button } from 'antd-mobile';
import { SearchOutline } from 'antd-mobile-icons';

function App() {
  return (
    <Button color="primary">
      <SearchOutline />
      <span style={{ marginLeft: 4 }}>搜索</span>
    </Button>
  );
}
```

### Example: Icon in List

```javascript
import React from 'react';
import { List } from 'antd-mobile';
import { RightOutline } from 'antd-mobile-icons';

function App() {
  return (
    <List>
      <List.Item
        prefix={<RightOutline />}
        onClick={() => {}}
      >
        列表项
      </List.Item>
    </List>
  );
}
```

### Key Points

- Import icons from `antd-mobile-icons` package
- Use `fontSize` prop for icon size
- Use `color` prop for icon color
- Icons can be used standalone or with other components
- Icon names follow the pattern: `NameOutline` or `NameFill`
- Icons are optimized for mobile display
