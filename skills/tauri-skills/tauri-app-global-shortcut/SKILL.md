---
name: tauri-app-global-shortcut
description: "Register system-wide keyboard shortcuts using the Tauri v2 global-shortcut plugin. Use when adding global hotkeys that work outside app focus, handling shortcut conflicts, or triggering app focus/commands via keyboard shortcuts."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Global hotkeys or keyboard shortcuts outside app focus
- Shortcut conflict detection and resolution
- Triggering app focus or commands via keyboard shortcuts

**Trigger phrases include:**
- "global shortcut", "hotkey", "keyboard shortcut", "keybinding", "accelerator"

## How to use this skill

1. **Install the global-shortcut plugin**:
   ```bash
   cargo add tauri-plugin-global-shortcut
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_global_shortcut::Builder::new().build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["global-shortcut:allow-register", "global-shortcut:allow-unregister"] }
   ```
4. **Register shortcuts from the frontend**:
   ```typescript
   import { register, unregister } from '@tauri-apps/plugin-global-shortcut';
   await register('CommandOrControl+Shift+K', (event) => {
     if (event.state === 'Pressed') {
       console.log('Shortcut triggered!');
     }
   });
   ```
5. **Handle conflicts** by catching registration errors when another app holds the shortcut
6. **Unregister shortcuts** on app exit to clean up system-level registrations

## Outputs

- Global shortcut registration with conflict handling
- Shortcut-to-action routing pattern
- Cleanup on app exit

## References

- https://v2.tauri.app/plugin/global-shortcut/

## Keywords

tauri global shortcut, hotkey, keyboard shortcut, keybinding, accelerator
