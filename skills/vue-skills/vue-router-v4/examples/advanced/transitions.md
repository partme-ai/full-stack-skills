# Transitions | 过渡效果

**官方文档**: https://router.vuejs.org/guide/advanced/transitions.html


## Instructions

This example demonstrates how to add transitions between route changes.

### Key Concepts

- Wrapping RouterView with Transition
- Transition modes
- Per-route transitions
- Dynamic transitions

### Example: Basic Transition

```vue
<template>
  <RouterView v-slot="{ Component, route }">
    <Transition name="fade" mode="out-in">
      <component :is="Component" :key="route.path" />
    </Transition>
  </RouterView>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
```

### Example: Slide Transition

```vue
<template>
  <RouterView v-slot="{ Component, route }">
    <Transition name="slide" mode="out-in">
      <component :is="Component" :key="route.path" />
    </Transition>
  </RouterView>
</template>

<style>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s;
}

.slide-enter-from {
  transform: translateX(100%);
}

.slide-leave-to {
  transform: translateX(-100%);
}
</style>
```

### Example: Per-Route Transition

```vue
<template>
  <RouterView v-slot="{ Component, route }">
    <Transition :name="route.meta.transition || 'fade'">
      <component :is="Component" :key="route.path" />
    </Transition>
  </RouterView>
</template>
```

### Key Points

- Use Transition component with RouterView
- Use `mode="out-in"` for smooth transitions
- Key on route.path for proper transitions
- Can use route meta for per-route transitions
- CSS transitions or JavaScript hooks available
