# Basic Usage

## Button Example

```vue
<template>
  <a-button type="primary">Primary Button</a-button>
</template>
<script setup lang="ts">
// Components are auto-imported if unplugin-vue-components is configured
// Otherwise: import { Button as AButton } from 'ant-design-vue';
</script>
```

## Internationalization

```vue
<template>
  <a-config-provider :locale="locale">
    <App />
  </a-config-provider>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import zhCN from 'ant-design-vue/es/locale/zh-CN';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';

dayjs.locale('zh-cn');
const locale = ref(zhCN);
</script>
```
