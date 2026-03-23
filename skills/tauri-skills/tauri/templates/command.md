# Command Template

## Backend

```rust
#[tauri::command]
fn greet(name: String) -> String {
  format!("Hello, {}!", name)
}
```

## Frontend

```ts
import { invoke } from "@tauri-apps/api/tauri";

const msg = await invoke<string>("greet", { name: "world" });
```
