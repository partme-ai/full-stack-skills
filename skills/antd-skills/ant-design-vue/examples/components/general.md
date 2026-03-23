# General Components (通用)

## Button (按钮)
To trigger an operation.

```vue
<a-button type="primary">Primary</a-button>
<a-button>Default</a-button>
<a-button type="dashed">Dashed</a-button>
<a-button type="text">Text</a-button>
<a-button type="link">Link</a-button>
```

## Icon (图标)
Semantic vector graphics.
Note: Icons are strictly separated from 4.0.

```bash
npm install @ant-design/icons-vue
```

```vue
<template>
  <step-forward-outlined />
</template>
<script setup>
import { StepForwardOutlined } from '@ant-design/icons-vue';
</script>
```

## Typography (排版)
Basic text writing, including headings, body text, lists, and more.

```vue
<a-typography-title>Introduction</a-typography-title>
<a-typography-paragraph>
  In the process of internal desktop applications development...
</a-typography-paragraph>
```
