# Theme Customization | 主题定制

## Instructions

This example demonstrates how to customize Ant Design theme.

### Key Concepts

- Using ConfigProvider
- Customizing design tokens
- Less variables
- CSS variables
- Theme switching

### Example: Basic Theme Customization

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';

function App() {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#00b96b',
          borderRadius: 2,
        },
      }}
    >
      <YourApp />
    </ConfigProvider>
  );
}
```

### Example: Customizing Multiple Tokens

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';

function App() {
  return (
    <ConfigProvider
      theme={{
        token: {
          colorPrimary: '#00b96b',
          colorSuccess: '#52c41a',
          colorWarning: '#faad14',
          colorError: '#ff4d4f',
          borderRadius: 4,
          fontFamily: 'Arial, sans-serif',
        },
      }}
    >
      <YourApp />
    </ConfigProvider>
  );
}
```

### Example: Component Theme Customization

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';

function App() {
  return (
    <ConfigProvider
      theme={{
        components: {
          Button: {
            colorPrimary: '#00b96b',
            borderRadius: 2,
          },
          Input: {
            borderRadius: 4,
          },
        },
      }}
    >
      <YourApp />
    </ConfigProvider>
  );
}
```

### Key Points

- Use `ConfigProvider` with `theme` prop
- Customize design tokens via `token` property
- Customize component styles via `components` property
- Theme changes apply to all child components
- Supports both Less variables and CSS variables
- Can switch themes dynamically
