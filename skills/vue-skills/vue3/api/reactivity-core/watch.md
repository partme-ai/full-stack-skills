# watch()

## API Reference

Watches a reactive source and invokes a callback when it changes.

**Signature:**
```typescript
function watch<T>(
  source: WatchSource<T>,
  callback: WatchCallback<T>,
  options?: WatchOptions
): StopHandle
```

**Details:**
- Watches a single or multiple reactive sources
- Lazy by default (doesn't run immediately)
- Options: `immediate`, `deep`, `flush`
- Returns a stop function

**Example:**
```javascript
import { ref, watch } from 'vue'

const count = ref(0)
watch(count, (newVal, oldVal) => {
  console.log(`Count: ${oldVal} -> ${newVal}`)
})
```

**See also:** `examples/essentials/watchers.md`
