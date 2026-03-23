# Event Template

## Backend Emit

```rust
app.emit_all("app:ready", "ok").ok();
```

## Frontend Listen

```ts
import { listen } from "@tauri-apps/api/event";

await listen<string>("app:ready", (event) => {
  const payload = event.payload;
});
```
