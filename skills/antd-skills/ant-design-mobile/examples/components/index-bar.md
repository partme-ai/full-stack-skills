# IndexBar | 索引栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the IndexBar component in Ant Design Mobile.

### Key Concepts

- Basic index bar
- Index bar with sections
- Index bar with sticky
- Index bar with custom index

### Example: Basic IndexBar

```javascript
import React from 'react';
import { IndexBar } from 'antd-mobile';

const charCodeOfA = 'A'.charCodeAt(0);
const groups = Array(26)
  .fill('')
  .map((_, i) => ({
    title: String.fromCharCode(charCodeOfA + i),
    items: Array(Math.floor(Math.random() * 5) + 3)
      .fill('')
      .map((_, j) => ({
        name: `${String.fromCharCode(charCodeOfA + i)}${j + 1}`,
      })),
  }));

function App() {
  return (
    <IndexBar>
      {groups.map(group => (
        <IndexBar.Panel
          key={group.title}
          index={group.title}
          title={`标题 ${group.title}`}
        >
          {group.items.map(item => (
            <div key={item.name} style={{ padding: '10px' }}>
              {item.name}
            </div>
          ))}
        </IndexBar.Panel>
      ))}
    </IndexBar>
  );
}
```

### Example: IndexBar with Sticky

```javascript
import React from 'react';
import { IndexBar } from 'antd-mobile';

const charCodeOfA = 'A'.charCodeAt(0);
const groups = Array(26)
  .fill('')
  .map((_, i) => ({
    title: String.fromCharCode(charCodeOfA + i),
    items: Array(Math.floor(Math.random() * 5) + 3)
      .fill('')
      .map((_, j) => ({
        name: `${String.fromCharCode(charCodeOfA + i)}${j + 1}`,
      })),
  }));

function App() {
  return (
    <IndexBar sticky>
      {groups.map(group => (
        <IndexBar.Panel
          key={group.title}
          index={group.title}
          title={`标题 ${group.title}`}
        >
          {group.items.map(item => (
            <div key={item.name} style={{ padding: '10px' }}>
              {item.name}
            </div>
          ))}
        </IndexBar.Panel>
      ))}
    </IndexBar>
  );
}
```

### Example: IndexBar with Custom Index

```javascript
import React from 'react';
import { IndexBar } from 'antd-mobile';

const groups = [
  {
    title: '#',
    items: [
      { name: '123' },
      { name: '456' },
    ],
  },
  {
    title: 'A',
    items: [
      { name: 'Apple' },
      { name: 'Ant' },
    ],
  },
];

function App() {
  return (
    <IndexBar>
      {groups.map(group => (
        <IndexBar.Panel
          key={group.title}
          index={group.title}
          title={`标题 ${group.title}`}
        >
          {group.items.map(item => (
            <div key={item.name} style={{ padding: '10px' }}>
              {item.name}
            </div>
          ))}
        </IndexBar.Panel>
      ))}
    </IndexBar>
  );
}
```

### Key Points

- Use `IndexBar` for index bar container
- Use `IndexBar.Panel` for index sections
- Use `index` prop for index value
- Use `title` prop for section title
- Use `sticky` prop for sticky header
- IndexBar is optimized for mobile display
- IndexBar supports touch scrolling
