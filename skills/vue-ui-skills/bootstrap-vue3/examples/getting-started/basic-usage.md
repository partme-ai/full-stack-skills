# Basic Usage | 基本用法

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates basic Bootstrap Vue component usage in Vue 3.

### Key Concepts

- Using components
- Component props
- Component events
- Composition API

### Example: Button Component

```vue
<template>
  <div>
    <BButton variant="primary">Primary</BButton>
    <BButton variant="success">Success</BButton>
    <BButton variant="danger">Danger</BButton>
  </div>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Button with Events

```vue
<template>
  <BButton variant="primary" @click="handleClick">
    Click Me
  </BButton>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'

const handleClick = () => {
  console.log('Button clicked!')
}
</script>
```

### Example: Form Input

```vue
<template>
  <BFormInput
    v-model="value"
    placeholder="Enter text"
  />
</template>

<script setup>
import { ref } from 'vue'
import { BFormInput } from 'bootstrap-vue-next'

const value = ref('')
</script>
```

### Example: Multiple Components

```vue
<template>
  <BCard title="Example Card">
    <BFormInput v-model="value" placeholder="Enter text" />
    <BButton variant="primary" class="mt-3">Submit</BButton>
  </BCard>
</template>

<script setup>
import { ref } from 'vue'
import { BCard, BFormInput, BButton } from 'bootstrap-vue-next'

const value = ref('')
</script>
```

### Key Points

- Import components from 'bootstrap-vue-next'
- Use component props to configure behavior
- Use v-model for two-way binding
- Use @click for event handling
- Use Composition API with script setup
- Components follow Bootstrap 5 styling
