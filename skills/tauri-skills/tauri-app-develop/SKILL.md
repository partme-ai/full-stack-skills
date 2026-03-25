---
name: tauri-app-develop
description: "Guide the daily Tauri v2 development workflow including dev server configuration, Rust+WebView debugging, sidecar management, and testing strategies. Use when setting up dev workflow, debugging both Rust and frontend, managing resources/sidecars, or choosing testing approaches."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Day-to-day Tauri v2 development workflow
- Dev server vs static assets configuration
- Debugging Rust backend + WebView frontend simultaneously
- Sidecar or resource management
- Testing strategies for Tauri apps

**Trigger phrases include:**
- "dev workflow", "tauri dev", "debug", "sidecar", "resources", "testing tauri"

## How to use this skill

1. **Start development mode** with hot-reload:
   ```bash
   npm run tauri dev
   ```
2. **Configure dev server** in `tauri.conf.json`:
   ```json
   { "build": { "devUrl": "http://localhost:5173", "frontendDist": "../dist" } }
   ```
3. **Debug Rust backend** using VS Code with `lldb` or RustRover:
   - Set breakpoints in `src-tauri/src/main.rs`
   - Attach debugger to the Tauri process
4. **Debug WebView frontend** using browser DevTools (right-click > Inspect in dev mode)
5. **Manage resources** by placing files in `src-tauri/resources/` and referencing them in `tauri.conf.json`
6. **Configure sidecars** for external binaries that ship with your app
7. **Test strategies**: Use `cargo test` for Rust, WebDriver for e2e, and `@tauri-apps/api/mocks` for frontend unit tests

## Outputs

- Dev server and hot-reload configuration
- Dual-side debugging setup (Rust + WebView)
- Resource and sidecar management patterns
- Testing strategy recommendation

## References

- https://v2.tauri.app/develop/
- https://v2.tauri.app/develop/debug/
- https://v2.tauri.app/develop/tests/

## Keywords

tauri develop, dev server, debugging, sidecar, resources, testing, hot reload
