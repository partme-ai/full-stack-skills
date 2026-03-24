# toRef() / toRefs()

## API Reference

Creates a ref for a property on a reactive object, or converts a reactive object to a plain object with refs.

**Signature:**
```typescript
function toRef<T extends object, K extends keyof T>(
  object: T,
  key: K
): ToRef<T[K]>

function toRefs<T extends object>(
  object: T
): ToRefs<T>
```

**Details:**
- `toRef()` creates a ref for a single property
- `toRefs()` converts all properties to refs
- Useful when destructuring reactive objects
- Maintains reactivity after destructuring

**Example:**
```javascript
import { reactive, toRefs } from 'vue'

const state = reactive({
  count: 0,
  name: 'Vue'
})

const { count, name } = toRefs(state)
// Both are refs, maintaining reactivity
```

**See also:** `examples/essentials/reactivity-fundamentals.md`
