# Internationalization | 国际化

## Instructions

This example demonstrates how to implement internationalization with Ant Design React.

### Key Concepts

- Using ConfigProvider with locale
- Importing locale files
- Switching languages
- Custom locale messages

### Example: Basic i18n Setup

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh-CN';
import enUS from 'antd/locale/en_US';

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      <YourApp />
    </ConfigProvider>
  );
}
```

### Example: Language Switching

```javascript
import React, { useState } from 'react';
import { ConfigProvider, Button } from 'antd';
import zhCN from 'antd/locale/zh-CN';
import enUS from 'antd/locale/en_US';

function App() {
  const [locale, setLocale] = useState(zhCN);

  const switchLocale = () => {
    setLocale(locale === zhCN ? enUS : zhCN);
  };

  return (
    <ConfigProvider locale={locale}>
      <Button onClick={switchLocale}>Switch Language</Button>
      <YourApp />
    </ConfigProvider>
  );
}
```

### Example: Custom Locale

```javascript
import React from 'react';
import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh-CN';

const customLocale = {
  ...zhCN,
  DatePicker: {
    ...zhCN.DatePicker,
    lang: {
      ...zhCN.DatePicker.lang,
      month: '月',
      year: '年',
    },
  },
};

function App() {
  return (
    <ConfigProvider locale={customLocale}>
      <YourApp />
    </ConfigProvider>
  );
}
```

### Key Points

- Import locale from 'antd/locale/'
- Use `ConfigProvider` with `locale` prop
- Switch languages by changing locale prop
- Can customize locale messages
- Supports all Ant Design components
- Works with date pickers, calendars, etc.
