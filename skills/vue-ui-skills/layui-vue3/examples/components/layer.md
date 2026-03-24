# Layer Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/layer


## Instructions

This example demonstrates the Layer component in Layui Vue.

### Key Concepts

- Layer component usage
- Layer API methods
- Modal dialogs
- Drawer
- Message and confirm

### Example: Layer Component

```vue
<template>
  <lay-layer v-model="visible" title="Title">
    <p>Content</p>
  </lay-layer>
  <lay-button @click="visible = true">Open</lay-button>
</template>

<script setup>
import { ref } from 'vue'
import { LayLayer, LayButton } from '@layui/layui-vue'

const visible = ref(false)
</script>
```

### Example: Layer API - Open

```vue
<template>
  <lay-button @click="openLayer">Open Layer</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const openLayer = () => {
  layer.open({
    title: 'Title',
    content: 'Content',
    area: ['500px', '300px']
  })
}
</script>
```

### Example: Layer API - Message

```vue
<template>
  <lay-button @click="showMessage">Show Message</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const showMessage = () => {
  layer.msg('Hello World')
}
</script>
```

### Example: Layer API - Confirm

```vue
<template>
  <lay-button @click="showConfirm">Confirm</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const showConfirm = () => {
  layer.confirm('Are you sure?', {
    yes: (index) => {
      console.log('Confirmed')
      layer.close(index)
    }
  })
}
</script>
```

### Example: Layer API - Loading

```vue
<template>
  <lay-button @click="showLoading">Loading</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const showLoading = () => {
  const index = layer.load()
  setTimeout(() => {
    layer.close(index)
  }, 2000)
}
</script>
```

### Example: Drawer

```vue
<template>
  <lay-button @click="openDrawer">Open Drawer</lay-button>
</template>

<script setup>
import { LayButton } from '@layui/layui-vue'
import { layer } from '@layui/layui-vue'

const openDrawer = () => {
  layer.drawer({
    content: 'Drawer Content',
    direction: 'right'
  })
}
</script>
```

### Key Points

- Use component or API methods
- layer.open() for modals
- layer.msg() for messages
- layer.confirm() for confirmations
- layer.load() for loading
- layer.drawer() for drawers
