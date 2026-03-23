# Grid | 宫格

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Grid component in Ant Design Mobile.

### Key Concepts

- Basic grid
- Grid with columns
- Grid with gap
- Grid with custom content
- Grid with icons

### Example: Basic Grid

```javascript
import React from 'react';
import { Grid } from 'antd-mobile';

const data = Array.from(new Array(4)).map((_, i) => ({
  icon: 'https://via.placeholder.com/50',
  text: `选项${i + 1}`,
}));

function App() {
  return (
    <Grid columns={2} gap={8}>
      {data.map((item, index) => (
        <Grid.Item key={index}>
          <div style={{ textAlign: 'center' }}>
            <img
              src={item.icon}
              alt={item.text}
              style={{ width: 50, height: 50 }}
            />
            <div>{item.text}</div>
          </div>
        </Grid.Item>
      ))}
    </Grid>
  );
}
```

### Example: Grid with Columns

```javascript
import React from 'react';
import { Grid } from 'antd-mobile';

const data = Array.from(new Array(6)).map((_, i) => ({
  text: `选项${i + 1}`,
}));

function App() {
  return (
    <>
      <Grid columns={2} gap={8}>
        {data.map((item, index) => (
          <Grid.Item key={index}>
            <div style={{ textAlign: 'center', padding: '20px' }}>
              {item.text}
            </div>
          </Grid.Item>
        ))}
      </Grid>
      <Grid columns={3} gap={8}>
        {data.map((item, index) => (
          <Grid.Item key={index}>
            <div style={{ textAlign: 'center', padding: '20px' }}>
              {item.text}
            </div>
          </Grid.Item>
        ))}
      </Grid>
    </>
  );
}
```

### Example: Grid with Icons

```javascript
import React from 'react';
import { Grid } from 'antd-mobile';
import { AppOutline, UserOutline, SearchOutline } from 'antd-mobile-icons';

const data = [
  { icon: <AppOutline />, text: '应用' },
  { icon: <UserOutline />, text: '用户' },
  { icon: <SearchOutline />, text: '搜索' },
];

function App() {
  return (
    <Grid columns={3} gap={8}>
      {data.map((item, index) => (
        <Grid.Item key={index}>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: 24, marginBottom: 8 }}>
              {item.icon}
            </div>
            <div>{item.text}</div>
          </div>
        </Grid.Item>
      ))}
    </Grid>
  );
}
```

### Example: Grid with Click

```javascript
import React from 'react';
import { Grid, Toast } from 'antd-mobile';

const data = Array.from(new Array(4)).map((_, i) => ({
  text: `选项${i + 1}`,
}));

function App() {
  return (
    <Grid columns={2} gap={8}>
      {data.map((item, index) => (
        <Grid.Item
          key={index}
          onClick={() => {
            Toast.show(`点击了${item.text}`);
          }}
        >
          <div style={{ textAlign: 'center', padding: '20px' }}>
            {item.text}
          </div>
        </Grid.Item>
      ))}
    </Grid>
  );
}
```

### Key Points

- Use `columns` prop for column count
- Use `gap` prop for gap between items
- Use `Grid.Item` for grid items
- Grid items can have custom content
- Grid supports click events
- Grid is optimized for mobile display
