---
name: tauri-app-process
description: "Access process information and control app lifecycle using the Tauri v2 process plugin, including app restart and exit. Use when querying process info, implementing graceful shutdown, or programmatically restarting the app."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Getting process info (PID, app version) in a Tauri app
- Programmatic app restart or exit
- Graceful shutdown and cleanup

**Trigger phrases include:**
- "process", "restart app", "exit app", "shutdown", "app lifecycle", "process info"

## How to use this skill

1. **Install the process plugin**:
   ```bash
   cargo add tauri-plugin-process
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_process::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["process:allow-restart", "process:allow-exit"] }
   ```
4. **Control the process from the frontend**:
   ```typescript
   import { exit, relaunch } from '@tauri-apps/plugin-process';
   await relaunch();  // restart the app (e.g., after an update)
   await exit(0);     // graceful exit with code 0
   ```
5. **Implement graceful shutdown** by saving state before calling exit
6. **Restrict process capabilities** to only restart/exit -- avoid exposing unnecessary process data

## Outputs

- Process plugin setup with restart and exit capabilities
- Graceful shutdown pattern with state saving
- Minimal capability configuration

## References

- https://v2.tauri.app/plugin/process/

## Keywords

tauri process, restart, exit, shutdown, app lifecycle, process info
