# TagInput Component

**官方文档**: https://www.layui-vue.com/zh-CN/components/tag-input


## Instructions

This example demonstrates the TagInput component in Layui Vue.

### Key Concepts

- Tag input
- Tag management
- Tag validation
- Tag events

### Example: Basic TagInput

```vue
<template>
  <lay-tag-input v-model="tags"></lay-tag-input>
</template>

<script setup>
import { ref } from 'vue'
import { LayTagInput } from '@layui/layui-vue'

const tags = ref([])
</script>
```

### Example: TagInput with Validation

```vue
<template>
  <lay-tag-input 
    v-model="tags"
    :max-length="5"
    @change="handleChange"
  ></lay-tag-input>
</template>

<script setup>
import { ref } from 'vue'
import { LayTagInput } from '@layui/layui-vue'

const tags = ref([])

const handleChange = (tags) => {
  console.log('Tags:', tags)
}
</script>
```

### Example: TagInput with Placeholder

```vue
<template>
  <lay-tag-input 
    v-model="tags"
    placeholder="Enter tags"
  ></lay-tag-input>
</template>
```

### Key Points

- Use v-model for two-way binding
- Tags stored as array
- Support max length validation
- Handle change events
- Customize placeholder
