---
name: tauri-app-updater
description: "Configure OTA (over-the-air) app updates using the Tauri v2 updater plugin with signing keys and update server setup. Use when implementing auto-update checks, generating signing key pairs, or configuring update server endpoints and metadata."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Auto-updates or OTA updates for the app
- Signing keys for update verification
- Update server configuration

**Trigger phrases include:**
- "updater", "auto-update", "OTA", "signing key", "update server", "app update"

## How to use this skill

1. **Install the updater plugin**:
   ```bash
   cargo add tauri-plugin-updater
   ```
2. **Generate signing keys**:
   ```bash
   npx @tauri-apps/cli signer generate -w ~/.tauri/myapp.key
   ```
3. **Configure the updater** in `tauri.conf.json`:
   ```json
   {
     "plugins": {
       "updater": {
         "endpoints": ["https://releases.example.com/{{target}}/{{arch}}/{{current_version}}"],
         "pubkey": "dW50cnVzdGVkIGNvbW1lbnQ..."
       }
     }
   }
   ```
4. **Register the plugin and check for updates**:
   ```typescript
   import { check } from '@tauri-apps/plugin-updater';
   const update = await check();
   if (update) {
     await update.downloadAndInstall();
     // Optionally restart the app
   }
   ```
5. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["updater:default"] }
   ```
6. **Set up your update server** to serve JSON metadata with version, download URL, and signature

## Outputs

- Updater plugin setup with signing keys
- Update check and install flow
- Update server endpoint configuration

## References

- https://v2.tauri.app/plugin/updater/

## Keywords

tauri updater, auto-update, OTA, signing key, update server, app update
