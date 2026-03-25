---
name: tauri-ipc
description: "Implement frontend-to-Rust IPC using invoke calls, Tauri commands, and type-safe bindings in Tauri v2. Use when defining Rust commands callable from the frontend, setting up typed IPC contracts, or implementing bidirectional event-based communication."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Frontend-to-Rust IPC or invoke calls
- Defining Tauri commands
- Type-safe IPC bindings (tauri-specta)

**Trigger phrases include:**
- "IPC", "invoke", "tauri command", "type-safe", "tauri-specta", "calling rust"

## How to use this skill

1. **Define a Rust command**:
   ```rust
   #[tauri::command]
   fn greet(name: &str) -> String {
       format!("Hello, {}!", name)
   }
   ```
2. **Register the command** in the Tauri builder:
   ```rust
   tauri::Builder::default()
       .invoke_handler(tauri::generate_handler![greet])
   ```
3. **Call from the frontend**:
   ```typescript
   import { invoke } from '@tauri-apps/api/core';
   const greeting = await invoke<string>('greet', { name: 'World' });
   ```
4. **For type-safe bindings**, use `tauri-specta` to auto-generate TypeScript types from Rust commands:
   ```bash
   cargo add tauri-specta specta
   ```
5. **Bidirectional events** for Rust-to-frontend communication:
   ```rust
   app.emit("update", payload)?;  // Rust -> Frontend
   ```
   ```typescript
   import { listen } from '@tauri-apps/api/event';
   await listen('update', (event) => console.log(event.payload));
   ```
6. **Handle errors** by returning `Result<T, String>` from Rust commands

## Outputs

- Rust command definition and registration
- Frontend invoke call pattern
- Type-safe IPC with tauri-specta
- Bidirectional event communication

## References

- https://v2.tauri.app/develop/calling-rust/
- https://v2.tauri.app/develop/calling-frontend/

## Keywords

tauri IPC, invoke, tauri command, type-safe, tauri-specta, events
