# Global Configuration

## API Reference

Element Plus global configuration options.

### Global Config Options

When using `app.use(ElementPlus, options)`, you can pass:

```typescript
interface ElementPlusOptions {
  size?: 'large' | 'default' | 'small'
  zIndex?: number
  locale?: Locale
}
```

### ConfigProvider Props

**Props:**
- `size` - Global size (large, default, small)
- `zIndex` - Global z-index (default: 3000)
- `locale` - Locale object
- `button` - Button config
- `message` - Message config

### Example: Global Config

```javascript
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'

const app = createApp(App)
app.use(ElementPlus, {
  size: 'large',
  zIndex: 3000,
  locale: zhCn
})
```

### Example: ConfigProvider

```vue
<template>
  <el-config-provider
    :size="size"
    :z-index="zIndex"
    :locale="locale"
  >
    <el-button>Button</el-button>
  </el-config-provider>
</template>

<script setup>
import { ref } from 'vue'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'

const size = ref('default')
const zIndex = ref(3000)
const locale = ref(zhCn)
</script>
```

### Size Configuration

**Options:**
- `'large'` - Large size
- `'default'` - Default size
- `'small'` - Small size

### z-index Configuration

**Default:** `3000`

Controls z-index for overlays (Dialog, Drawer, etc.).

### Locale Configuration

Import locale from `element-plus/dist/locale/`:
- `zh-cn.mjs` - Chinese (Simplified)
- `en.mjs` - English
- `es.mjs` - Spanish
- `fr.mjs` - French
- `ja.mjs` - Japanese
- `ko.mjs` - Korean

**See also:** `examples/guide/i18n.md` for i18n examples
