---
name: tauri-app-opener
description: "Open external URLs and files in the default system application using the Tauri v2 opener plugin with protocol allowlisting. Use when opening links in the browser, launching files in their default app, or restricting which protocols and paths can be opened."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Opening external links or URLs from a Tauri app
- Launching files in their default application
- Protocol or path allowlisting for the opener

**Trigger phrases include:**
- "open link", "open URL", "open file", "default browser", "opener", "launch"

## How to use this skill

1. **Install the opener plugin**:
   ```bash
   cargo add tauri-plugin-opener
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_opener::init())
   ```
3. **Configure capabilities** with allowed URLs/protocols in `src-tauri/capabilities/default.json`:
   ```json
   {
     "permissions": [
       { "identifier": "opener:allow-open-url", "allow": [{ "url": "https://**" }] },
       "opener:allow-open-path"
     ]
   }
   ```
4. **Open URLs and files from the frontend**:
   ```typescript
   import { openUrl, openPath } from '@tauri-apps/plugin-opener';
   await openUrl('https://tauri.app');
   await openPath('/path/to/document.pdf');
   ```
5. **Restrict allowed protocols** to https:// and specific schemes only (never allow arbitrary URLs)
6. **Validate paths** before opening to prevent path traversal attacks

## Outputs

- Opener plugin setup with protocol-scoped permissions
- URL and file opening patterns
- Security validation for paths and protocols

## References

- https://v2.tauri.app/plugin/opener/

## Keywords

tauri opener, open URL, open file, default browser, external links, allowlist
