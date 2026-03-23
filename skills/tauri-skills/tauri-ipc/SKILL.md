---
name: tauri-ipc
description: Guidance for Tauri v2 IPC with frontend invoke calls, Rust commands, and type-safe bindings.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Frontend-to-Rust IPC or invoke calls / 前端到 Rust 的 IPC 或 invoke 调用
- Tauri commands or type-safe bindings / Tauri 命令或类型安全绑定
- Bidirectional messaging or event-based IPC / 双向消息或事件驱动 IPC

**Trigger phrases include:**
- "IPC", "invoke", "command", "tauri-specta", "type safety"
- "IPC", "调用命令", "类型安全", "tauri-specta"

## How to use this skill

1. Define Rust commands and register them in the Tauri builder
2. Use invoke on the frontend with typed payloads
3. Apply type generation tools to avoid any-typed IPC
4. Establish error handling and response contracts

## Outputs

- Typed IPC request/response contract / 类型化 IPC 请求响应契约
- Error handling and validation guidance / 错误处理与校验指导

## Scope

- Boundary: invoke calls and command definitions only
- v2 focus: type-safe IPC with tauri-specta or official generators

## References

- https://v2.tauri.app/concept/inter-process-communication/
- https://v2.tauri.app/develop/calling-rust/
- https://v2.tauri.app/develop/calling-frontend/

## Keywords

tauri ipc, invoke, tauri command, type safety, tauri-specta
