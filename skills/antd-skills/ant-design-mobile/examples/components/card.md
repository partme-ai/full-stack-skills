# Card | 卡片

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the Card component in Ant Design Mobile.

### Key Concepts

- Card with title
- Card with body
- Card with actions
- Card with images
- Card styles

### Example: Basic Card

```javascript
import React from 'react';
import { Card } from 'antd-mobile';

function App() {
  return (
    <Card title="卡片标题">
      <div>卡片内容</div>
    </Card>
  );
}
```

### Example: Card with Body

```javascript
import React from 'react';
import { Card } from 'antd-mobile';

function App() {
  return (
    <Card title="卡片标题" bodyStyle={{ padding: '20px' }}>
      <div>这是卡片的内容区域</div>
    </Card>
  );
}
```

### Example: Card with Actions

```javascript
import React from 'react';
import { Card, Button } from 'antd-mobile';

function App() {
  return (
    <Card
      title="卡片标题"
      extra={<Button size="small">更多</Button>}
    >
      <div>卡片内容</div>
    </Card>
  );
}
```

### Example: Card with Image

```javascript
import React from 'react';
import { Card } from 'antd-mobile';

function App() {
  return (
    <Card
      title="卡片标题"
      cover={
        <img
          alt="example"
          src="https://via.placeholder.com/300x200"
          style={{ width: '100%' }}
        />
      }
    >
      <div>卡片内容</div>
    </Card>
  );
}
```

### Example: Card Styles

```javascript
import React from 'react';
import { Card } from 'antd-mobile';

function App() {
  return (
    <>
      <Card title="默认卡片">内容</Card>
      <Card title="无边框卡片" bordered={false}>内容</Card>
    </>
  );
}
```

### Key Points

- Use `title` prop for card title
- Use `bodyStyle` prop to customize body styles
- Use `extra` prop for additional content in header
- Use `cover` prop for card cover image
- Use `bordered` prop to control border display
- Card is optimized for mobile display
