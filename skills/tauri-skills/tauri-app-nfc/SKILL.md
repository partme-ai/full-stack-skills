---
name: tauri-app-nfc
description: "Read and write NFC tags using the Tauri v2 NFC plugin with session lifecycle management. Use when adding NFC read/write features, managing NFC scan sessions, or handling NFC availability on mobile devices."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- NFC tag reading or writing in a Tauri app
- NFC session lifecycle (start, scan, stop)
- NFC hardware availability checks on mobile

**Trigger phrases include:**
- "NFC", "NFC tag", "near field", "NFC read", "NFC write", "tap to scan"

## How to use this skill

1. **Install the NFC plugin**:
   ```bash
   cargo add tauri-plugin-nfc
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_nfc::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["nfc:allow-scan", "nfc:allow-write"] }
   ```
4. **Start an NFC scan session from the frontend**:
   ```typescript
   import { scan } from '@tauri-apps/plugin-nfc';
   const tag = await scan();
   console.log('Tag ID:', tag.id);
   console.log('Records:', tag.records);
   ```
5. **Manage session lifecycle**: start scanning, process results, and stop the session when done
6. **Validate tag data** before processing and provide user feedback for successful/failed scans

## Outputs

- NFC plugin setup with scan and write capabilities
- Session lifecycle management pattern
- Tag data validation and user feedback flow

## References

- https://v2.tauri.app/plugin/nfc/

## Keywords

tauri nfc, NFC tag, near field communication, scan, read write
