# SearchBar | 搜索栏

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to use the SearchBar component in Ant Design Mobile.

### Key Concepts

- Basic search bar
- Search bar with placeholder
- Search bar with cancel
- Search bar with onSearch
- Search bar with clear

### Example: Basic SearchBar

```javascript
import React, { useState } from 'react';
import { SearchBar } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <SearchBar
      value={value}
      onChange={setValue}
      placeholder="搜索"
    />
  );
}
```

### Example: SearchBar with Cancel

```javascript
import React, { useState } from 'react';
import { SearchBar } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <SearchBar
      value={value}
      onChange={setValue}
      placeholder="搜索"
      showCancelButton
      onCancel={() => {
        setValue('');
      }}
    />
  );
}
```

### Example: SearchBar with onSearch

```javascript
import React, { useState } from 'react';
import { SearchBar, Toast } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <SearchBar
      value={value}
      onChange={setValue}
      placeholder="搜索"
      onSearch={(val) => {
        Toast.show(`搜索: ${val}`);
      }}
    />
  );
}
```

### Example: SearchBar with Clear

```javascript
import React, { useState } from 'react';
import { SearchBar } from 'antd-mobile';

function App() {
  const [value, setValue] = useState('');

  return (
    <SearchBar
      value={value}
      onChange={setValue}
      placeholder="搜索"
      clearable
    />
  );
}
```

### Key Points

- Use `value` prop for search value
- Use `onChange` callback for value change
- Use `placeholder` prop for placeholder text
- Use `showCancelButton` prop for cancel button
- Use `onCancel` callback for cancel event
- Use `onSearch` callback for search event
- Use `clearable` prop for clear button
- SearchBar is optimized for mobile display
