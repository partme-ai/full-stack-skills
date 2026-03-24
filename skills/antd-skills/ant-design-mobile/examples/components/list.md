# List | 列表

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the List component in Ant Design Mobile.

### Key Concepts

- Basic List
- List with items
- List with click handlers
- List with icons
- List with descriptions
- List with arrows

### Example: Basic List

```javascript
import React from 'react';
import { List } from 'antd-mobile';

function App() {
  return (
    <List>
      <List.Item>Item 1</List.Item>
      <List.Item>Item 2</List.Item>
      <List.Item>Item 3</List.Item>
    </List>
  );
}
```

### Example: List with Click Handlers

```javascript
import React from 'react';
import { List, Toast } from 'antd-mobile';

function App() {
  const handleClick = (item) => {
    Toast.show(`Clicked: ${item}`);
  };

  return (
    <List>
      <List.Item onClick={() => handleClick('Item 1')}>
        Item 1
      </List.Item>
      <List.Item onClick={() => handleClick('Item 2')}>
        Item 2
      </List.Item>
    </List>
  );
}
```

### Example: List with Icons and Descriptions

```javascript
import React from 'react';
import { List } from 'antd-mobile';
import { RightOutline } from 'antd-mobile-icons';

function App() {
  return (
    <List>
      <List.Item
        prefix="Prefix"
        description="Description text"
        extra={<RightOutline />}
        onClick={() => {}}
      >
        Title
      </List.Item>
    </List>
  );
}
```

### Example: List with Arrow

```javascript
import React from 'react';
import { List } from 'antd-mobile';

function App() {
  return (
    <List>
      <List.Item arrow>Item with arrow</List.Item>
      <List.Item arrow="right">Item with right arrow</List.Item>
      <List.Item arrow="down">Item with down arrow</List.Item>
    </List>
  );
}
```

### Key Points

- Use `List` component to wrap list items
- Use `List.Item` for each list item
- Use `onClick` for item click handlers
- Use `prefix` and `description` for item content
- Use `extra` for additional content (icons, etc.)
- Use `arrow` prop for navigation indicators
- List is optimized for mobile scrolling
