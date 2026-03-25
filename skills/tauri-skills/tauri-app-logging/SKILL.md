---
name: tauri-app-logging
description: "Add unified logging across Rust and frontend using the Tauri v2 logging plugin with configurable levels, filtering, and file output. Use when setting up app-wide logging, configuring log levels for dev vs release, or implementing safe diagnostics without leaking secrets."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Unified logging for Tauri apps (dev and release)
- Log level configuration, filtering, or file output
- Safe diagnostics without leaking sensitive data

**Trigger phrases include:**
- "logging", "log levels", "log plugin", "diagnostics", "log file", "debug logs"

## How to use this skill

1. **Install the logging plugin**:
   ```bash
   cargo add tauri-plugin-log
   ```
2. **Register the plugin** with level and target configuration:
   ```rust
   use tauri_plugin_log::{Target, TargetKind};
   tauri::Builder::default()
       .plugin(tauri_plugin_log::Builder::new()
           .targets([Target::new(TargetKind::Stdout), Target::new(TargetKind::LogDir { file_name: None })])
           .level(log::LevelFilter::Info)
           .build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["log:default"] }
   ```
4. **Log from the frontend**:
   ```typescript
   import { info, warn, error } from '@tauri-apps/plugin-log';
   await info('App started');
   await error('Something went wrong');
   ```
5. **Use different log levels** for dev (Debug/Trace) vs release (Info/Warn) builds
6. **Redact sensitive data** before logging (never log tokens, passwords, or PII)

## Outputs

- Logging plugin setup with file and stdout targets
- Level-based filtering for dev vs release
- Redaction rules for sensitive data

## References

- https://v2.tauri.app/plugin/logging/

## Keywords

tauri logging, log levels, log plugin, diagnostics, log file, redaction
