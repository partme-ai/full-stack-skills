---
name: tauri-app-file-system
description: "Read and write local files using the Tauri v2 file-system plugin with scoped directory access. Use when implementing file read/write operations, configuring safe directory scopes, or building import/export file workflows."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Reading or writing local files in a Tauri app
- Configuring file system scope for safe access
- File import/export workflows

**Trigger phrases include:**
- "file system", "read file", "write file", "fs plugin", "file access", "scope"

## How to use this skill

1. **Install the file-system plugin**:
   ```bash
   cargo add tauri-plugin-fs
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_fs::init())
   ```
3. **Configure scoped access** in `src-tauri/capabilities/default.json`:
   ```json
   {
     "permissions": [
       { "identifier": "fs:allow-read-text-file", "allow": [{ "path": "$APPDATA/**" }] },
       { "identifier": "fs:allow-write-text-file", "allow": [{ "path": "$APPDATA/**" }] }
     ]
   }
   ```
4. **Read and write files from the frontend**:
   ```typescript
   import { readTextFile, writeTextFile, BaseDirectory } from '@tauri-apps/plugin-fs';
   const content = await readTextFile('config.json', { baseDir: BaseDirectory.AppData });
   await writeTextFile('config.json', JSON.stringify(data), { baseDir: BaseDirectory.AppData });
   ```
5. **Define minimal directory scopes** to restrict access to only the directories your app needs
6. **Validate access boundaries** and handle permission errors gracefully

## Outputs

- File system plugin setup with scoped directory access
- Read/write operations using BaseDirectory constants
- Minimal-scope permission configuration

## References

- https://v2.tauri.app/plugin/file-system/

## Keywords

tauri file system, read file, write file, scope, fs plugin, file access
