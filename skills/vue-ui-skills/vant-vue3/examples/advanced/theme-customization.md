# Theme Customization | 主题定制

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: ConfigProvider / 主题定制


## Instructions

This example demonstrates how to customize Vant theme.

### Key Concepts

- Using ConfigProvider
- Customizing theme variables
- CSS variables
- Theme switching

### Example: Basic Theme Customization

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <van-button type="primary">Primary Button</van-button>
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider, Button as VanButton } from 'vant'

const themeVars = {
  primaryColor: '#07c160',
  successColor: '#07c160',
  dangerColor: '#ee0a24'
}
</script>
```

### Example: Customizing Multiple Variables

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <van-button type="primary">Button</van-button>
    <van-cell title="Cell" />
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider, Button as VanButton, Cell as VanCell } from 'vant'

const themeVars = {
  buttonPrimaryBackground: '#07c160',
  buttonPrimaryBorderColor: '#07c160',
  cellFontSize: '16px',
  cellTextColor: '#323233'
}
</script>
```

### Example: Using CSS Variables

```vue
<template>
  <van-config-provider :theme-vars="themeVars">
    <App />
  </van-config-provider>
</template>

<script setup>
import { ConfigProvider as VanConfigProvider } from 'vant'

const themeVars = {
  primaryColor: 'var(--my-primary-color)',
  successColor: 'var(--my-success-color)'
}
</script>

<style>
:root {
  --my-primary-color: #07c160;
  --my-success-color: #07c160;
}
</style>
```

### Key Points

- Use `ConfigProvider` with `theme-vars` prop
- Customize theme variables via `theme-vars` property
- Theme changes apply to all child components
- Supports CSS variables
- Can switch themes dynamically
- Theme variables follow Vant naming convention

### Related local files

- Config API: `api/config-provider.md`
- Project scaffold: `templates/project-setup.md`
