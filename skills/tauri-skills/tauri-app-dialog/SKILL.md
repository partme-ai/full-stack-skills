---
name: tauri-app-dialog
description: "Display native file open/save dialogs, alerts, and confirmation prompts using the Tauri v2 dialog plugin. Use when showing file pickers, alert/confirm dialogs, or building a unified dialog service layer across platforms."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Native file open/save dialogs or file pickers
- Alert, confirm, or message box dialogs
- Cross-platform dialog behavior consistency

**Trigger phrases include:**
- "dialog", "alert", "confirm", "file picker", "save dialog", "open dialog"

## How to use this skill

1. **Install the dialog plugin**:
   ```bash
   cargo add tauri-plugin-dialog
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_dialog::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["dialog:allow-open", "dialog:allow-save", "dialog:allow-message", "dialog:allow-ask"] }
   ```
4. **Open a file picker from the frontend**:
   ```typescript
   import { open, save, message, ask } from '@tauri-apps/plugin-dialog';
   const file = await open({ filters: [{ name: 'Images', extensions: ['png', 'jpg'] }] });
   const confirmed = await ask('Are you sure?', { title: 'Confirm', kind: 'warning' });
   ```
5. **Handle cancellation** by checking for null/undefined return values from open/save
6. **Build a unified dialog service** that wraps plugin calls for consistent UX across the app

## Outputs

- Dialog plugin setup with file picker and alert dialogs
- Cancellation and error handling patterns
- Unified dialog service wrapper

## References

- https://v2.tauri.app/plugin/dialog/

## Keywords

tauri dialog, file picker, alert, confirm, save dialog, native dialogs
