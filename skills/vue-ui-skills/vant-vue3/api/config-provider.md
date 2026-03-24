# ConfigProvider API | ConfigProvider API

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: ConfigProvider

## API Reference

ConfigProvider component API for global configuration.

### ConfigProvider

Provides global configuration for Vant components.

**Props:**
- `theme`: Theme configuration (light, dark)
- `theme-vars`: Custom theme variables
- `tag`: Root element tag
- `z-index`: Z-index for popup components

### Example: Basic Usage

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <App />
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider } from 'vant'

const themeVars = {
  primaryColor: '#07c160',
  successColor: '#07c160',
  dangerColor: '#ee0a24'
}
</script>
```

### Example: Theme Variables

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <van-button type="primary">Button</van-button>
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider, Button as VanButton } from 'vant'

const themeVars = {
  buttonPrimaryBackground: '#07c160',
  buttonPrimaryBorderColor: '#07c160'
}
</script>
```

### Key Points

- Wrap app with ConfigProvider for global config
- Use theme-vars prop for theme customization
- Use theme prop for light/dark theme
- ConfigProvider affects all child components
- Can nest ConfigProviders for different scopes
- Theme variables use CSS variables
