---
name: tauri-app-sidecar-nodejs
description: "Bundle and run a Node.js process as a sidecar alongside a Tauri v2 app with lifecycle management. Use when integrating a Node.js backend as a sidecar binary, managing sidecar start/stop lifecycle, or packaging Node.js executables per platform."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Running Node.js as a sidecar process in Tauri
- Packaging Node.js binaries alongside the app
- Managing sidecar lifecycle (start, stop, logging)

**Trigger phrases include:**
- "sidecar", "node.js sidecar", "nodejs backend", "sidecar packaging", "bundled node"

## How to use this skill

1. **Compile Node.js to a standalone binary** using tools like `pkg` or `nexe`:
   ```bash
   npx pkg server.js -t node18-macos-x64,node18-win-x64,node18-linux-x64
   ```
2. **Place sidecar binaries** in `src-tauri/binaries/` with platform-specific naming:
   ```
   src-tauri/binaries/node-server-x86_64-apple-darwin
   src-tauri/binaries/node-server-x86_64-pc-windows-msvc.exe
   src-tauri/binaries/node-server-x86_64-unknown-linux-gnu
   ```
3. **Configure the sidecar** in `tauri.conf.json`:
   ```json
   { "bundle": { "externalBin": ["binaries/node-server"] } }
   ```
4. **Start the sidecar from Rust**:
   ```rust
   let sidecar = app.shell().sidecar("node-server").unwrap();
   let (mut rx, child) = sidecar.spawn().unwrap();
   ```
5. **Configure shell permissions** for the sidecar in capabilities
6. **Manage lifecycle**: stop the sidecar gracefully on app exit using the child process handle

## Outputs

- Sidecar binary packaging per platform
- Sidecar configuration in tauri.conf.json
- Start/stop lifecycle management in Rust

## References

- https://v2.tauri.app/learn/sidecar-nodejs/

## Keywords

tauri sidecar, node.js, nodejs backend, sidecar packaging, bundled binary
