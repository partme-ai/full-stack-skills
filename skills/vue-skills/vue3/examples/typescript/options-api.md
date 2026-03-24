## Instructions

- Use defineComponent for Options API typing.
- Type props and data explicitly.
- Use `this` typing carefully.

### Example

```ts
import { defineComponent } from 'vue'

export default defineComponent({
  props: { title: { type: String, required: true } }
})
```

Reference: https://cn.vuejs.org/guide/typescript/options-api.html
