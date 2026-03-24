## Instructions

- Use <Suspense> for async dependencies.
- Provide default and fallback slots.
- Combine with async components.

### Example

```vue
<template>
  <Suspense>
    <template #default>
      <AsyncView />
    </template>
    <template #fallback>
      <p>Loading...</p>
    </template>
  </Suspense>
</template>
```

Reference: https://cn.vuejs.org/guide/built-ins/suspense.html
