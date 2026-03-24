# ConfigProvider API | ConfigProvider API

## API Reference

ConfigProvider component API for global configuration.

### ConfigProvider

Provides global configuration for Ant Design components.

**Props:**
- `locale`: Locale object for internationalization
- `theme`: Theme configuration object
- `componentSize`: Global component size
- `direction`: Text direction (ltr, rtl)
- `autoInsertSpaceInButton`: Auto insert space in Chinese button
- `renderEmpty`: Custom empty component renderer

### Theme Configuration

```typescript
interface ThemeConfig {
  token?: {
    colorPrimary?: string;
    borderRadius?: number;
    // ... other design tokens
  };
  components?: {
    Button?: {
      colorPrimary?: string;
      // ... component-specific tokens
    };
    // ... other components
  };
}
```

### Example: Basic Usage

```javascript
import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh-CN';

<ConfigProvider locale={zhCN}>
  <App />
</ConfigProvider>
```

### Example: With Theme

```javascript
<ConfigProvider
  theme={{
    token: {
      colorPrimary: '#00b96b',
    },
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
