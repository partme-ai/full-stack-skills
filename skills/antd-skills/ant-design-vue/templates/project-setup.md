# Project Setup Template | 项目配置模板

## Vite Setup with Auto Import

`vite.config.ts`:

```typescript
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite';
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers';

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        AntDesignVueResolver({
          importStyle: false, // css in js
        }),
      ],
    }),
  ],
});
```

## Main Entry (main.ts)

```typescript
import { createApp } from 'vue';
import App from './App.vue';
import 'ant-design-vue/dist/reset.css'; // Important for V4

const app = createApp(App);
app.mount('#app');
```

## Global Config Layout (App.vue)

```vue
<template>
  <a-config-provider :locale="locale" :theme="theme">
    <a-app>
      <router-view />
    </a-app>
  </a-config-provider>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import zhCN from 'ant-design-vue/es/locale/zh-CN';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';
import { theme as antdTheme } from 'ant-design-vue';

dayjs.locale('zh-cn');

const locale = ref(zhCN);
const theme = {
  algorithm: antdTheme.defaultAlgorithm,
  token: {
    colorPrimary: '#1890ff',
  },
};
</script>
```
