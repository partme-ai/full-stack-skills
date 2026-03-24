---
name: tauri-app-wasm
description: Guidance for running Rust-compiled WASM in the Tauri v2 frontend.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- High-performance frontend computation / 高性能前端计算
- WASM vs IPC trade-offs / WASM 与 IPC 取舍
- Rust logic running in the WebView / Rust 逻辑运行于 WebView

**Trigger phrases include:**
- "WASM", "WebAssembly", "IPC", "performance"
- "WASM", "WebAssembly", "性能", "IPC"

## How to use this skill

1. Identify workloads suitable for WASM execution
2. Build Rust code to WASM and integrate with the frontend
3. Keep system API access in Rust core via IPC when needed
4. Validate performance gains and bundle size impact

## Outputs

- WASM integration plan / WASM 集成方案
- Performance and bundle checklist / 性能与包体清单

## Scope

- Boundary: Frontend WASM usage only
- Key points: WASM vs IPC responsibilities

## References

- https://crates.io/crates/tauri-wasm
- https://v2.tauri.app/develop/calling-rust/#wasm
- https://github.com/p1mo/tauri-wasm
- https://zhuanlan.zhihu.com/p/533025312
- https://blog.csdn.net/qq_63401240/article/details/147340217

## Keywords

tauri wasm, rust wasm, frontend compute, performance
