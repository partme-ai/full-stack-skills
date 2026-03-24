# Installation | 安装

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to install Ant Design Mobile and set it up in a React project.

### Key Concepts

- Installing Ant Design Mobile
- Importing styles
- Basic component usage
- Project setup

### Example: Installation

```bash
# Using npm
npm install antd-mobile

# Using yarn
yarn add antd-mobile

# Using pnpm
pnpm add antd-mobile
```

### Example: Import Styles

```javascript
// Import CSS in your entry file (e.g., index.js or App.js)
import 'antd-mobile/es/global.css';
```

### Example: Basic Usage

```javascript
import React from 'react';
import { Button } from 'antd-mobile';

function App() {
  return (
    <div>
      <Button color="primary">Primary Button</Button>
      <Button>Default Button</Button>
    </div>
  );
}

export default App;
```

### Example: Using ConfigProvider

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import App from './App';

function Root() {
  return (
    <ConfigProvider locale={zhCN}>
      <App />
    </ConfigProvider>
  );
}

export default Root;
```

### Example: TypeScript Setup

```typescript
import React from 'react';
import { Button } from 'antd-mobile';

const App: React.FC = () => {
  return (
    <div>
      <Button color="primary">Primary Button</Button>
    </div>
  );
};

export default App;
```

### Key Points

- Install antd-mobile package
- Import global CSS styles in entry file
- Use ConfigProvider for global configuration
- Components can be imported individually
- Works with both JavaScript and TypeScript
- Use locale prop for internationalization
- Optimized for mobile devices
