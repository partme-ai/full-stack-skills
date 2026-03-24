## Instructions

- Use import.meta.hot to accept updates.
- Clean up side effects in dispose.
- Invalidate when full reload is needed.

### Example

```ts
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    console.log('HMR update', newModule)
  })
}
```

### Example

```ts
let timer: ReturnType<typeof setInterval> | null = null

function start() {
  timer = setInterval(() => console.log('tick'), 1000)
}

start()

if (import.meta.hot) {
  import.meta.hot.dispose(() => {
    if (timer) clearInterval(timer)
  })
}
```

### Notes

- Use import.meta.hot.data to preserve state.

Reference: https://cn.vitejs.dev/guide/api-hmr.html
