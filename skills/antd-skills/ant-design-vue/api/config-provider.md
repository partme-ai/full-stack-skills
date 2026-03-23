# ConfigProvider API | 全局配置 API

## ConfigProvider

Provides a uniform configuration for all components.

### Props

- `locale`: Language package setting
- `theme`: Theme configuration (V4 Design Token)
- `componentSize`: Config size for all components
- `prefixCls`: Set prefix class name
- `getPopupContainer`: To set the container of the popup element

### Design Token (Theme)

Customize the theme via `theme` prop.

```typescript
const theme = {
  token: {
    colorPrimary: '#00b96b',
    borderRadius: 2,
    fontSize: 14,
  },
  algorithm: theme.darkAlgorithm, // or defaultAlgorithm, compactAlgorithm
}
```

### Usage

```vue
<template>
  <a-config-provider :theme="theme" :locale="locale">
    <App />
  </a-config-provider>
</template>
```
