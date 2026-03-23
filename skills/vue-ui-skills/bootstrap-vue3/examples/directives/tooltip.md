# Tooltip Directive | 工具提示指令

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use the v-b-tooltip directive in Bootstrap Vue 3.0.

### Key Concepts

- Basic tooltip
- Tooltip placement
- Tooltip triggers
- Tooltip with HTML content

### Example: Basic Tooltip

```vue
<template>
  <BButton v-b-tooltip="'This is a tooltip'">
    Hover me
  </BButton>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Tooltip Placement

```vue
<template>
  <div>
    <BButton v-b-tooltip.top="'Top tooltip'">Top</BButton>
    <BButton v-b-tooltip.bottom="'Bottom tooltip'">Bottom</BButton>
    <BButton v-b-tooltip.left="'Left tooltip'">Left</BButton>
    <BButton v-b-tooltip.right="'Right tooltip'">Right</BButton>
  </div>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Tooltip with Options

```vue
<template>
  <BButton
    v-b-tooltip="{
      title: 'Tooltip content',
      placement: 'top',
      trigger: 'hover'
    }"
  >
    Hover me
  </BButton>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Key Points

- Use `v-b-tooltip` directive for tooltips
- Use placement modifiers (.top, .bottom, .left, .right)
- Use object syntax for more options
- Tooltip appears on hover by default
- Supports HTML content with html option
