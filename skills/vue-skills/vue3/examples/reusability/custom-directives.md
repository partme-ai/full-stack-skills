## Instructions

- Use directives for low-level DOM access.
- Define directive hooks on mount/update.
- Keep directives small and focused.

### Example

```ts
export const vFocus = {
  mounted(el: HTMLElement) {
    el.focus()
  }
}
```

Reference: https://cn.vuejs.org/guide/reusability/custom-directives.html
