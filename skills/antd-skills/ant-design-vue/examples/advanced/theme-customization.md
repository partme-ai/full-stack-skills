# Theme Customization | 主题定制

Ant Design Vue V4 uses Design Tokens for theming.

## Basic Usage

Pass `theme` prop to `ConfigProvider`.

```vue
<template>
  <a-config-provider
    :theme="{
      token: {
        colorPrimary: '#00b96b',
        fontSize: 16,
        borderRadius: 4,
      },
    }"
  >
    <a-button type="primary">Custom Button</a-button>
  </a-config-provider>
</template>
```

## Dark Mode

Use `algorithm` to switch to dark mode.

```vue
<script setup lang="ts">
import { theme } from 'ant-design-vue';
</script>

<template>
  <a-config-provider
    :theme="{
      algorithm: theme.darkAlgorithm,
    }"
  >
    <App />
  </a-config-provider>
</template>
```

## Compact Mode

```vue
<script setup lang="ts">
import { theme } from 'ant-design-vue';
</script>

<template>
  <a-config-provider
    :theme="{
      algorithm: theme.compactAlgorithm,
    }"
  >
    <App />
  </a-config-provider>
</template>
```

## Design Tokens

Commonly used tokens:

- `colorPrimary`: Brand color
- `colorSuccess`: Success state color
- `colorWarning`: Warning state color
- `colorError`: Error state color
- `colorInfo`: Info state color
- `colorTextBase`: Base text color
- `colorBgBase`: Base background color
- `fontFamily`: Font family
- `fontSize`: Base font size
- `borderRadius`: Base border radius
