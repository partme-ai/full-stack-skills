# defineProps() / defineEmits() / defineExpose()

## API Reference

Component definition macros for props, emits, and exposed properties.

**defineProps():**
```typescript
function defineProps<T>(): Props<T>
function defineProps<T>(props: T): Props<T>
```

**defineEmits():**
```typescript
function defineEmits<T>(): Emits<T>
function defineEmits<T>(emits: T): Emits<T>
```

**defineExpose():**
```typescript
function defineExpose(exposed: Record<string, any>): void
```

**Example:**
```javascript
import { defineProps, defineEmits, defineExpose } from 'vue'

const props = defineProps({
  title: String
})

const emit = defineEmits(['update'])

defineExpose({
  someMethod() {
    // ...
  }
})
```

**See also:** 
- `examples/components-in-depth/props.md`
- `examples/components-in-depth/events.md`
