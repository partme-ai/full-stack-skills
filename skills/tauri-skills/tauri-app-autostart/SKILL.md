---
name: tauri-app-autostart
description: "Configure Tauri v2 autostart plugin to launch the app on system login. Use when enabling or disabling autostart, handling platform-specific startup behavior, or adding a user-controlled autostart toggle."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Enabling or disabling app autostart / launch at login
- Platform-specific autostart behavior (macOS Login Items, Windows Registry, Linux XDG autostart)
- User-controlled autostart toggle in app settings

**Trigger phrases include:**
- "autostart", "startup", "login items", "boot launch", "launch on startup"

## How to use this skill

1. **Install the autostart plugin** and add it to `Cargo.toml` and `tauri.conf.json`:
   ```bash
   cargo add tauri-plugin-autostart
   ```
2. **Register the plugin** in your Tauri builder with the desired macro type:
   ```rust
   use tauri_plugin_autostart::MacosLauncher;
   tauri::Builder::default()
       .plugin(tauri_plugin_autostart::init(
           MacosLauncher::LaunchAgent,
           Some(vec!["--minimized"]),
       ))
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["autostart:allow-enable", "autostart:allow-disable", "autostart:allow-is-enabled"] }
   ```
4. **Toggle autostart from the frontend**:
   ```typescript
   import { enable, disable, isEnabled } from '@tauri-apps/plugin-autostart';
   await enable();   // register autostart
   await disable();  // remove autostart
   const status = await isEnabled(); // check current state
   ```
5. **Handle platform differences**: macOS uses LaunchAgent or AppleEvent, Windows uses the Registry, Linux uses XDG autostart directories
6. **Verify** by restarting the system or checking platform-specific autostart entries

## Outputs

- Autostart plugin setup with platform-appropriate launcher type
- User-facing toggle for enable/disable with status check
- Platform-specific verification checklist

## References

- https://v2.tauri.app/plugin/autostart/

## Keywords

tauri autostart, startup, login items, launch on boot, enable disable
