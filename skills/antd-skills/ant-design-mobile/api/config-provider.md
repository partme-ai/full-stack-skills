# ConfigProvider API | ConfigProvider API

## API Reference

ConfigProvider component API for global configuration.

### ConfigProvider

Provides global configuration for Ant Design Mobile components.

**Props:**
- `locale`: Locale object for internationalization
- `theme`: Theme configuration object
- `componentSize`: Global component size

### Example: Basic Usage

```javascript
import { ConfigProvider } from 'antd-mobile';
import zhCN from 'antd-mobile/es/locales/zh-CN';

<ConfigProvider locale={zhCN}>
  <App />
</ConfigProvider>
```

### Example: With Theme

```javascript
<ConfigProvider
  theme={{
    primaryColor: '#00b96b',
  }}
>
  <App />
</ConfigProvider>
```

### Key Points

- Wrap app with ConfigProvider for global config
- Use locale prop for internationalization
- Use theme prop for theme customization
- ConfigProvider affects all child components
- Can nest ConfigProviders for different scopes
