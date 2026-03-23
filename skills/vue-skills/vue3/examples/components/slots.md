## Instructions

- Use slots for content distribution.
- Use named slots for multiple regions.
- Use scoped slots to expose data.

### Example

```vue
<template>
  <header><slot name="header" /></header>
  <main><slot /></main>
</template>
```

Reference: https://cn.vuejs.org/guide/components/slots.html
