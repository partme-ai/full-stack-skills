# Internationalization | 国际化

**官方文档**: https://avuejs.com/


## Instructions

This example demonstrates how to configure internationalization in Avue.

### Key Concepts

- Locale setup
- Language switching
- Custom translations
- i18n integration

### Example: Basic i18n Setup

```javascript
// main.js
import Vue from 'vue'
import Avue from '@smallwei/avue'
import AvueLocale from '@smallwei/avue/lib/locale'
import zhLocale from '@smallwei/avue/lib/locale/lang/zh-CN'
import enLocale from '@smallwei/avue/lib/locale/lang/en'

// Set default locale
AvueLocale.use(zhLocale)

Vue.use(Avue)
```

### Example: Language Switching

```vue
<template>
  <div>
    <el-select v-model="locale" @change="handleLocaleChange">
      <el-option label="中文" value="zh-CN" />
      <el-option label="English" value="en" />
    </el-select>
    <avue-form :option="option" v-model="form" />
  </div>
</template>

<script>
import AvueLocale from '@smallwei/avue/lib/locale'
import zhLocale from '@smallwei/avue/lib/locale/lang/zh-CN'
import enLocale from '@smallwei/avue/lib/locale/lang/en'

export default {
  data() {
    return {
      locale: 'zh-CN',
      form: {},
      option: {
        column: [
          {
            label: 'Name',
            prop: 'name',
            type: 'input'
          }
        ]
      }
    }
  },
  methods: {
    handleLocaleChange(locale) {
      if (locale === 'zh-CN') {
        AvueLocale.use(zhLocale)
      } else {
        AvueLocale.use(enLocale)
      }
      this.$forceUpdate()
    }
  }
}
</script>
```

### Key Points

- Import locale files from @smallwei/avue/lib/locale/lang
- Use AvueLocale.use() to set locale
- Switch locale dynamically
- Locale affects component labels and messages
- Can integrate with vue-i18n
