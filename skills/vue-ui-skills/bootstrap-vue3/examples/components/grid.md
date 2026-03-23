# Grid | 栅格系统

**官方文档**: https://bootstrap-vue.org


## Instructions

This example demonstrates how to use the Grid system in Bootstrap Vue 3.0.

### Key Concepts

- Container component
- Row component
- Col component
- Responsive breakpoints
- Grid alignment

### Example: Basic Grid

```vue
<template>
  <BContainer>
    <BRow>
      <BCol>Column 1</BCol>
      <BCol>Column 2</BCol>
      <BCol>Column 3</BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

### Example: Responsive Grid

```vue
<template>
  <BContainer>
    <BRow>
      <BCol cols="12" md="6" lg="4">Column 1</BCol>
      <BCol cols="12" md="6" lg="4">Column 2</BCol>
      <BCol cols="12" md="6" lg="4">Column 3</BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

### Example: Grid with Offsets

```vue
<template>
  <BContainer>
    <BRow>
      <BCol cols="4" offset="4">Centered Column</BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

### Example: Grid Alignment

```vue
<template>
  <BContainer>
    <BRow align-v="center" align-h="center">
      <BCol cols="6">Centered Content</BCol>
    </BRow>
  </BContainer>
</template>

<script setup>
import { BContainer, BRow, BCol } from 'bootstrap-vue-next'
</script>
```

### Key Points

- Use `BContainer` for container
- Use `BRow` for rows
- Use `BCol` for columns
- Use `cols` prop for column width
- Use responsive props (sm, md, lg, xl, xxl)
- Use `offset` prop for column offset
- Use `align-v` and `align-h` for alignment
