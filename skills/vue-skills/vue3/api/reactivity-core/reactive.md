# reactive()

## API Reference

Creates a reactive proxy of an object.

**Signature:**
```typescript
function reactive<T extends object>(target: T): UnwrapNestedRefs<T>
```

**Details:**
- Returns a reactive proxy of the object
- The conversion is "deep" - it affects all nested properties
- Only works with objects (arrays and objects)
- Cannot be reassigned (unlike `ref()`)

**Example:**
```javascript
import { reactive } from 'vue'

const state = reactive({
  count: 0,
  nested: {
    value: 1
  }
})

state.count++
state.nested.value++
```

**See also:** `examples/essentials/reactivity-fundamentals.md`
