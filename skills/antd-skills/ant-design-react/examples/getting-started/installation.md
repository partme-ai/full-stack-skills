# Installation | 安装

**官方文档**: https://4x-ant-design.antgroup.com/docs/react/introduce-cn


## Instructions

This example demonstrates how to install Ant Design React and set it up in a React project.

### Key Concepts

- Installing Ant Design
- Importing styles
- Basic component usage
- Project setup

### Example: Installation

```bash
# Using npm
npm install antd

# Using yarn
yarn add antd

# Using pnpm
pnpm add antd
```

### Example: Import Styles

```javascript
// Import CSS in your entry file (e.g., index.js or App.js)
import 'antd/dist/antd.css';

// Or import less if using less-loader
import 'antd/dist/antd.less';
```

### Example: Basic Usage

```javascript
import React from 'react';
import { Button } from 'antd';

function App() {
  return (
    <div>
      <Button type="primary">Primary Button</Button>
      <Button>Default Button</Button>
    </div>
  );
}

export default App;
```

### Example: Using ConfigProvider

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh-CN';
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
import { Button } from 'antd';

const App: React.FC = () => {
  return (
    <div>
      <Button type="primary">Primary Button</Button>
    </div>
  );
};

export default App;
```

### Key Points

- Install antd package
- Import CSS styles in entry file
- Use ConfigProvider for global configuration
- Components can be imported individually
- Works with both JavaScript and TypeScript
- Use locale prop for internationalization
