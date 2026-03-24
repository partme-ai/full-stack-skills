# computed()

## API Reference

Creates a computed property that is cached and only re-evaluates when dependencies change.

**Signature:**
```typescript
// Read-only
function computed<T>(
  getter: () => T
): Readonly<Ref<T>>

// Writable
function computed<T>(
  options: {
    get: () => T
    set: (value: T) => void
  }
): Ref<T>
```

**Details:**
- Computed properties are cached
- Only re-evaluate when reactive dependencies change
- Read-only by default
- Can have getter and setter for writable computed

**Example:**
```javascript
import { ref, computed } from 'vue'

const count = ref(0)
const doubleCount = computed(() => count.value * 2)
```

**See also:** `examples/essentials/computed-properties.md`
