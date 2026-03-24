# Project Setup Template | 项目设置模板

## Basic React + Ant Design Mobile Setup

```javascript
// package.json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "antd-mobile": "^5.0.0"
  }
}
```

```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'antd-mobile/es/global.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

```javascript
// src/App.js
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import Main from './Main';

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <Main />
    </ConfigProvider>
  );
}

export default App;
```

## With TypeScript

```typescript
// src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import 'antd-mobile/es/global.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(<App />);
```

```typescript
// src/App.tsx
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import Main from './Main';

const App: React.FC = () => {
  return (
    <ConfigProvider locale={zhCN}>
      <Main />
    </ConfigProvider>
  );
};

export default App;
```

## With Custom Theme

```javascript
// src/App.js
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';

function App() {
  return (
    <ConfigProvider
      locale={zhCN}
      theme={{
        primaryColor: '#00b96b',
      }}
    >
      <Main />
    </ConfigProvider>
  );
}
```
