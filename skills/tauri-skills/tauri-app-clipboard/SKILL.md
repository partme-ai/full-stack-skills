---
name: tauri-app-clipboard
description: "Read and write text and images to the system clipboard using the Tauri v2 clipboard plugin. Use when implementing copy/paste functionality, clipboard monitoring, or restricting clipboard access to user-initiated actions only."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Reading or writing clipboard content (text or images)
- Clipboard change monitoring or listeners
- Restricting clipboard access to user-initiated actions

**Trigger phrases include:**
- "clipboard", "copy", "paste", "clipboard monitor", "copy to clipboard"

## How to use this skill

1. **Install the clipboard plugin**:
   ```bash
   cargo add tauri-plugin-clipboard-manager
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_clipboard_manager::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["clipboard-manager:allow-write-text", "clipboard-manager:allow-read-text"] }
   ```
4. **Copy and paste from the frontend**:
   ```typescript
   import { writeText, readText } from '@tauri-apps/plugin-clipboard-manager';
   await writeText('Hello from Tauri!');
   const content = await readText();
   ```
5. **Restrict access** to user-initiated actions only (button clicks) to prevent clipboard abuse
6. **Monitor changes** using clipboard event listeners when continuous monitoring is needed

## Outputs

- Clipboard read/write integration with permission controls
- User-initiated access pattern to prevent abuse
- Clipboard monitoring setup when needed

## References

- https://v2.tauri.app/plugin/clipboard/

## Keywords

tauri clipboard, copy, paste, clipboard monitor, permissions
