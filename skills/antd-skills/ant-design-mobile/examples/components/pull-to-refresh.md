# PullToRefresh | 下拉刷新

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the PullToRefresh component in Ant Design Mobile.

### Key Concepts

- Basic PullToRefresh
- PullToRefresh with data loading
- Custom refresh indicator
- PullToRefresh callbacks

### Example: Basic PullToRefresh

```javascript
import React, { useState } from 'react';
import { PullToRefresh, List } from 'antd-mobile';

function App() {
  const [data, setData] = useState(['Item 1', 'Item 2', 'Item 3']);

  const onRefresh = async () => {
    await new Promise(resolve => setTimeout(resolve, 1000));
    setData(['New Item 1', 'New Item 2', 'New Item 3']);
  };

  return (
    <PullToRefresh onRefresh={onRefresh}>
      <List>
        {data.map((item, index) => (
          <List.Item key={index}>{item}</List.Item>
        ))}
      </List>
    </PullToRefresh>
  );
}
```

### Example: PullToRefresh with Loading State

```javascript
import React, { useState } from 'react';
import { PullToRefresh, List } from 'antd-mobile';

function App() {
  const [data, setData] = useState(['Item 1', 'Item 2']);
  const [refreshing, setRefreshing] = useState(false);

  const onRefresh = async () => {
    setRefreshing(true);
    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      setData(['Updated Item 1', 'Updated Item 2']);
    } finally {
      setRefreshing(false);
    }
  };

  return (
    <PullToRefresh
      onRefresh={onRefresh}
      refreshing={refreshing}
    >
      <List>
        {data.map((item, index) => (
          <List.Item key={index}>{item}</List.Item>
        ))}
      </List>
    </PullToRefresh>
  );
}
```

### Key Points

- Use `PullToRefresh` to wrap scrollable content
- Use `onRefresh` for refresh handler (async function)
- Use `refreshing` prop to control loading state
- Refresh handler should return a Promise
- Optimized for mobile pull gesture
- Works with List, ScrollView, etc.
