# Lifecycle Hooks

## API Reference

Component lifecycle hooks in Composition API.

**Available Hooks:**
- `onBeforeMount()` - Called before component is mounted
- `onMounted()` - Called after component is mounted
- `onBeforeUpdate()` - Called before component updates
- `onUpdated()` - Called after component updates
- `onBeforeUnmount()` - Called before component is unmounted
- `onUnmounted()` - Called after component is unmounted

**Signature:**
```typescript
function onMounted(hook: () => void): void
```

**Example:**
```javascript
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  console.log('Component mounted')
  // Good for: API calls, DOM manipulation
})

onUnmounted(() => {
  console.log('Component unmounted')
  // Good for: cleanup (timers, subscriptions)
})
```

**See also:** `examples/essentials/lifecycle.md`
