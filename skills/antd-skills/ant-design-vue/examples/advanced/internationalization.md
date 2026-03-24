# Internationalization | 国际化

## Configuration

Ant Design Vue provides a React component `ConfigProvider` for global configuration of internationalization.

```vue
<template>
  <a-config-provider :locale="locale">
    <App />
  </a-config-provider>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import zhCN from 'ant-design-vue/es/locale/zh-CN';
import enUS from 'ant-design-vue/es/locale/en_US';
import dayjs from 'dayjs';
import 'dayjs/locale/zh-cn';

dayjs.locale('zh-cn');

const locale = ref(zhCN);

const switchLocale = () => {
  locale.value = locale.value.locale === 'en' ? zhCN : enUS;
  dayjs.locale(locale.value.locale === 'en' ? 'en' : 'zh-cn');
};
</script>
```

## Supported Languages

Ant Design Vue supports many languages. Import from `ant-design-vue/es/locale/`.

Examples:
- `zh_CN`: Simplified Chinese
- `zh_TW`: Traditional Chinese
- `en_US`: English
- `ja_JP`: Japanese
- `ko_KR`: Korean
