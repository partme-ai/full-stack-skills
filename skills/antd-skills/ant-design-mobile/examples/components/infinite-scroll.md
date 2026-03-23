# InfiniteScroll | 无限滚动

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the InfiniteScroll component in Ant Design Mobile.

### Key Concepts

- Basic InfiniteScroll
- InfiniteScroll with data loading
- InfiniteScroll with hasMore
- InfiniteScroll callbacks

### Example: Basic InfiniteScroll

```javascript
import React, { useState } from 'react';
import { InfiniteScroll, List } from 'antd-mobile';

function App() {
  const [data, setData] = useState(Array.from({ length: 10 }, (_, i) => `Item ${i + 1}`));
  const [hasMore, setHasMore] = useState(true);

  const loadMore = async () => {
    await new Promise(resolve => setTimeout(resolve, 1000));
    const newData = Array.from({ length: 10 }, (_, i) => `Item ${data.length + i + 1}`);
    setData([...data, ...newData]);
    setHasMore(data.length < 50);
  };

  return (
    <>
      <List>
        {data.map((item, index) => (
          <List.Item key={index}>{item}</List.Item>
        ))}
      </List>
      <InfiniteScroll loadMore={loadMore} hasMore={hasMore} />
    </>
  );
}
```

### Example: InfiniteScroll with Loading

```javascript
import React, { useState } from 'react';
import { InfiniteScroll, List } from 'antd-mobile';

function App() {
  const [data, setData] = useState(Array.from({ length: 10 }, (_, i) => `Item ${i + 1}`));
  const [hasMore, setHasMore] = useState(true);

  const loadMore = async () => {
    await new Promise(resolve => setTimeout(resolve, 2000));
    const newData = Array.from({ length: 10 }, (_, i) => `Item ${data.length + i + 1}`);
    setData([...data, ...newData]);
    setHasMore(data.length < 50);
  };

  return (
    <>
      <List>
        {data.map((item, index) => (
          <List.Item key={index}>{item}</List.Item>
        ))}
      </List>
      <InfiniteScroll
        loadMore={loadMore}
        hasMore={hasMore}
        threshold={10}
      />
    </>
  );
}
```

### Key Points

- Use `InfiniteScroll` after scrollable content
- Use `loadMore` for loading handler (async function)
- Use `hasMore` prop to control if more data available
- Use `threshold` prop to set trigger distance
- Load handler should return a Promise
- Optimized for mobile scrolling
- Works with List, ScrollView, etc.
