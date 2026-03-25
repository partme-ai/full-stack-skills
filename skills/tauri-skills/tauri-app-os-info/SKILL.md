---
name: tauri-app-os-info
description: "Retrieve OS version, architecture, locale, and platform information using the Tauri v2 os-info plugin. Use when collecting system diagnostics, checking platform compatibility, or displaying system info in the app with data minimization."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Getting OS version, architecture, or locale info
- System diagnostics or platform compatibility checks
- Displaying system information in the app

**Trigger phrases include:**
- "os info", "system info", "platform", "architecture", "diagnostics", "os version"

## How to use this skill

1. **Install the os plugin**:
   ```bash
   cargo add tauri-plugin-os
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_os::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["os:default"] }
   ```
4. **Query OS information from the frontend**:
   ```typescript
   import { platform, version, arch, locale } from '@tauri-apps/plugin-os';
   const os = await platform();   // 'macos', 'windows', 'linux'
   const ver = await version();   // '14.0'
   const cpu = await arch();      // 'x86_64', 'aarch64'
   const lang = await locale();   // 'en-US'
   ```
5. **Minimize data collection** to only what your app needs (privacy by default)
6. **Redact sensitive data** before sending diagnostics to remote servers

## Outputs

- OS info plugin setup with platform/version/arch/locale queries
- Data minimization pattern for diagnostics
- Redaction guidance for remote reporting

## References

- https://v2.tauri.app/plugin/os-info/

## Keywords

tauri os info, platform, architecture, system info, diagnostics, version
