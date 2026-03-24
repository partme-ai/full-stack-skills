# Internationalization | 国际化

**官方文档**: https://ant-design-mobile.antgroup.com/zh


## Instructions

This example demonstrates how to set up internationalization in Ant Design Mobile.

### Key Concepts

- Locale configuration
- ConfigProvider with locale
- Language switching
- Custom locale
- Date and number formatting

### Example: Basic Internationalization

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import enUS from 'antd-mobile/es/locales/en-US';

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Example: Language Switching

```javascript
import React, { useState } from 'react';
import { ConfigProvider, Button } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import enUS from 'antd-mobile/es/locales/en-US';

function App() {
  const [locale, setLocale] = useState(zhCN);

  return (
    <ConfigProvider locale={locale}>
      <Button onClick={() => setLocale(locale === zhCN ? enUS : zhCN)}>
        切换语言
      </Button>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Example: Custom Locale

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';

const customLocale = {
  ...zhCN,
  Dialog: {
    ...zhCN.Dialog,
    confirm: '确定',
    cancel: '取消',
  },
};

function App() {
  return (
    <ConfigProvider locale={customLocale}>
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Example: Date and Number Formatting

```javascript
import React from 'react';
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';
import enUS from 'antd-mobile/es/locales/en-US';

function App() {
  return (
    <ConfigProvider locale={zhCN}>
      {/* Date and number formatting will use locale settings */}
      {/* Your app content */}
    </ConfigProvider>
  );
}
```

### Key Points

- Use `ConfigProvider` with `locale` prop for internationalization
- Import locale from `antd-mobile/es/locales/`
- Support for zh-CN, en-US, and other locales
- Custom locale by extending existing locale
- Date and number formatting use locale settings
- Internationalization is optimized for mobile display
