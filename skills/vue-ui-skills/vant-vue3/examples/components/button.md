# Button | 按钮

**官方文档入口**: https://vant-ui.github.io/vant/#/zh-CN
**官方对应章节**: Button / 按钮


## Instructions

This example demonstrates how to use the Button component in Vant.

### Key Concepts

- Button types (primary, success, warning, danger)
- Button sizes (large, normal, small, mini)
- Button shapes (square, round)
- Button states (disabled, loading)
- Button with icons
- Button groups

### Example: Button Types

```vue
<template>
  <van-button type="primary">Primary</van-button>
  <van-button type="success">Success</van-button>
  <van-button type="warning">Warning</van-button>
  <van-button type="danger">Danger</van-button>
  <van-button type="default">Default</van-button>
</template>

<script setup>
import { Button as VanButton } from 'vant'
</script>
```

### Example: Button Sizes

```vue
<template>
  <van-button type="primary" size="large">Large</van-button>
  <van-button type="primary" size="normal">Normal</van-button>
  <van-button type="primary" size="small">Small</van-button>
  <van-button type="primary" size="mini">Mini</van-button>
</template>

<script setup>
import { Button as VanButton } from 'vant'
</script>
```

### Example: Button with Icon

```vue
<template>
  <van-button type="primary" icon="plus">Add</van-button>
  <van-button type="primary" icon="search">Search</van-button>
</template>

<script setup>
import { Button as VanButton } from 'vant'
</script>
```

### Example: Loading State

```vue
<template>
  <van-button
    type="primary"
    :loading="loading"
    loading-text="Loading..."
    @click="handleClick"
  >
    Click Me
  </van-button>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton } from 'vant'

const loading = ref(false)

const handleClick = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 2000)
}
</script>
```

### Example: Disabled Button

```vue
<template>
  <van-button type="primary" disabled>Disabled</van-button>
  <van-button :disabled="disabled">Toggle Disabled</van-button>
</template>

<script setup>
import { ref } from 'vue'
import { Button as VanButton } from 'vant'

const disabled = ref(false)
</script>
```

### Example: Button Group

```vue
<template>
  <van-button-group>
    <van-button type="primary">Left</van-button>
    <van-button type="primary">Middle</van-button>
    <van-button type="primary">Right</van-button>
  </van-button-group>
</template>

<script setup>
import { Button as VanButton, ButtonGroup as VanButtonGroup } from 'vant'
</script>
```

### Key Points

- Use `type` prop for button style (primary, success, warning, danger, default)
- Use `size` prop for button size (large, normal, small, mini)
- Use `icon` prop for icon buttons
- Use `loading` prop for loading state
- Use `disabled` prop to disable button
- Use `van-button-group` for button groups
- Button supports all standard HTML button attributes

### Related local files

- API summary: `api/components.md`
- Form submit button pattern: `examples/components/form.md`
