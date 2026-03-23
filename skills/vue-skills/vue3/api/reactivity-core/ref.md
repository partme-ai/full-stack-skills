# ref()

## API Reference

Creates a reactive reference for a single value.

**Signature:**
```typescript
function ref<T>(value: T): Ref<UnwrapRef<T>>
```

**Details:**
- Returns a reactive and mutable ref object
- The ref object has a single property `.value` that points to the inner value
- In templates, refs are automatically unwrapped (no `.value` needed)
- In script, use `.value` to access/modify the value

**Example:**
```javascript
import { ref } from 'vue'

const count = ref(0)
console.log(count.value)  // 0

count.value++
console.log(count.value)  // 1
```

**See also:** `examples/essentials/reactivity-fundamentals.md`
