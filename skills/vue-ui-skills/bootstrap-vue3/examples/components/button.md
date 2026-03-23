# Button | 按钮

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use the Button component in Bootstrap Vue 3.0.

### Key Concepts

- Button variants (primary, success, danger, etc.)
- Button sizes (sm, md, lg)
- Button states (disabled, loading)
- Button with icons
- Button groups

### Example: Button Variants

```vue
<template>
  <div>
    <BButton variant="primary">Primary</BButton>
    <BButton variant="success">Success</BButton>
    <BButton variant="danger">Danger</BButton>
    <BButton variant="warning">Warning</BButton>
    <BButton variant="info">Info</BButton>
    <BButton variant="light">Light</BButton>
    <BButton variant="dark">Dark</BButton>
  </div>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Button Sizes

```vue
<template>
  <div>
    <BButton variant="primary" size="lg">Large</BButton>
    <BButton variant="primary">Default</BButton>
    <BButton variant="primary" size="sm">Small</BButton>
  </div>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Button with Icon

```vue
<template>
  <BButton variant="primary">
    <BIcon icon="search" />
    Search
  </BButton>
</template>

<script setup>
import { BButton, BIcon } from 'bootstrap-vue-next'
</script>
```

### Example: Disabled Button

```vue
<template>
  <div>
    <BButton variant="primary" disabled>Disabled Primary</BButton>
    <BButton disabled>Disabled Default</BButton>
  </div>
</template>

<script setup>
import { BButton } from 'bootstrap-vue-next'
</script>
```

### Example: Button Group

```vue
<template>
  <BButtonGroup>
    <BButton variant="primary">Left</BButton>
    <BButton variant="primary">Middle</BButton>
    <BButton variant="primary">Right</BButton>
  </BButtonGroup>
</template>

<script setup>
import { BButton, BButtonGroup } from 'bootstrap-vue-next'
</script>
```

### Key Points

- Use `variant` prop for button style (primary, success, danger, etc.)
- Use `size` prop for button size (sm, md, lg)
- Use `disabled` prop to disable button
- Use `BIcon` for icons
- Use `BButtonGroup` for button groups
- Button supports all standard HTML button attributes
