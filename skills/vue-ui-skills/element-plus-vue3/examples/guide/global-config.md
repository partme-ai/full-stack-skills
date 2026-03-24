# Global Configuration

## Instructions

This example demonstrates how to configure Element Plus globally.

### Key Concepts

- Global config options
- ConfigProvider
- Size configuration
- z-index configuration

### Example: Global Config

```javascript
// main.js
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus, {
  size: 'large',
  zIndex: 3000,
  locale: zhCn
})
app.mount('#app')
```

### Example: Using ConfigProvider

```vue
<template>
  <el-config-provider :size="size" :z-index="zIndex" :locale="locale">
    <el-button>Button</el-button>
    <el-input v-model="input" />
  </el-config-provider>
</template>

<script setup>
import { ref } from 'vue'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'

const size = ref('default')
const zIndex = ref(3000)
const locale = ref(zhCn)
const input = ref('')
</script>
```

### Example: Size Configuration

```vue
<template>
  <el-config-provider :size="size">
    <el-button>Button</el-button>
    <el-input v-model="input" />
  </el-config-provider>
</template>

<script setup>
import { ref } from 'vue'

const size = ref('default') // 'large' | 'default' | 'small'
</script>
```

### Example: z-index Configuration

```vue
<template>
  <el-config-provider :z-index="zIndex">
    <el-dialog v-model="visible" title="Dialog">
      Content
    </el-dialog>
  </el-config-provider>
</template>

<script setup>
import { ref } from 'vue'

const zIndex = ref(3000)
const visible = ref(false)
</script>
```

### Key Points

- Configure globally via app.use()
- Use ConfigProvider for component-level config
- Size: 'large' | 'default' | 'small'
- z-index: number (default: 3000)
- Locale: locale object
