---
name: tauri-app-wasm
description: "Compile Rust code to WebAssembly and run it in the Tauri v2 frontend for high-performance computation. Use when offloading CPU-intensive work to WASM in the WebView, deciding between WASM vs IPC for Rust logic, or optimizing frontend performance with Rust-compiled modules."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Running Rust code as WASM in the Tauri frontend
- WASM vs IPC performance trade-offs
- High-performance frontend computation

**Trigger phrases include:**
- "WASM", "WebAssembly", "wasm-pack", "Rust in browser", "frontend performance"

## How to use this skill

1. **Set up a WASM crate** alongside your Tauri project:
   ```bash
   cargo install wasm-pack
   wasm-pack new my-wasm-lib
   ```
2. **Build Rust code to WASM**:
   ```bash
   wasm-pack build --target web my-wasm-lib
   ```
3. **Import the WASM module** in your frontend:
   ```typescript
   import init, { process_data } from '../my-wasm-lib/pkg';
   await init();
   const result = process_data(inputBuffer);
   ```
4. **Choose WASM vs IPC**:
   - Use **WASM** for CPU-bound computation that doesn't need system APIs (image processing, crypto, parsing)
   - Use **IPC** (invoke) for anything requiring OS access (file system, network, notifications)
5. **Monitor bundle size** impact -- WASM modules add to the frontend bundle
6. **Benchmark** to verify WASM gives measurable performance gains over JavaScript

## Outputs

- WASM crate setup and build pipeline
- Frontend WASM module import pattern
- WASM vs IPC decision framework

## References

- https://v2.tauri.app/develop/calling-rust/#wasm
- https://crates.io/crates/tauri-wasm

## Keywords

tauri wasm, WebAssembly, wasm-pack, Rust wasm, frontend performance
