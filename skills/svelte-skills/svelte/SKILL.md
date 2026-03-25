---
name: svelte
description: "Guides Svelte and SvelteKit development including reactive components, stores, transitions, lifecycle hooks, SSR, file-based routing, and deployment. Use when the user needs to build Svelte components, create SvelteKit applications, implement reactivity patterns, or configure Svelte with Vite."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Build Svelte components with reactive declarations and bindings
- Create a SvelteKit application with file-based routing and SSR
- Implement Svelte stores for shared state management
- Add transitions, animations, or lifecycle hooks (onMount, onDestroy)
- Configure Svelte with Vite or deploy a SvelteKit app

## How to use this skill

### Workflow

1. **Set up the project** - `npm create svelte@latest my-app` for SvelteKit or Vite+Svelte
2. **Create components** - Write `.svelte` files with script, markup, and style blocks
3. **Add reactivity** - Use `$:` reactive declarations and Svelte stores
4. **Build and deploy** - `npm run build` with adapter-auto, adapter-node, or adapter-static

### Quick-Start Example: Reactive Counter Component

```svelte
<script>
  let count = 0;
  $: doubled = count * 2;
  $: if (count > 10) console.log('Count is high!');

  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  Clicked {count} {count === 1 ? 'time' : 'times'}
</button>
<p>Doubled: {doubled}</p>

<style>
  button {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    background: #ff3e00;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>
```

### Store Example: Shared State

```javascript
// stores.js
import { writable, derived } from 'svelte/store';

export const todos = writable([]);
export const completedCount = derived(todos, $todos =>
  $todos.filter(t => t.done).length
);
```

```svelte
<script>
  import { todos, completedCount } from './stores.js';
  let newTodo = '';

  function addTodo() {
    todos.update(t => [...t, { text: newTodo, done: false }]);
    newTodo = '';
  }
</script>

<input bind:value={newTodo} />
<button on:click={addTodo}>Add</button>
<p>Completed: {$completedCount}</p>
```

## Best Practices

1. **Keep reactive dependencies explicit** - Avoid side effects in `$:` blocks; use them for derived values
2. **Split into small components** - Each `.svelte` file should handle one concern
3. **Use stores for shared state** - Avoid prop drilling; writable/derived stores are lightweight
4. **Add TypeScript** - Use `<script lang="ts">` for type safety in components
5. **Leverage SvelteKit features** - Use `+page.server.ts` for server-side data loading, form actions for mutations

## Resources

- **Official Docs**: https://svelte.dev/docs
- **SvelteKit Docs**: https://kit.svelte.dev/docs

## Keywords

svelte, SvelteKit, reactive, component, store, transition, SSR, Vite, 响应式, 编译时, file-based routing
