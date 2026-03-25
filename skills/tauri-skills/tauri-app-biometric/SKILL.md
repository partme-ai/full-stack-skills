---
name: tauri-app-biometric
description: "Implement Tauri v2 biometric authentication using TouchID, FaceID, or fingerprint sensors with fallback strategies. Use when adding biometric login, securing sensitive actions with biometric confirmation, or handling devices without biometric support."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Biometric authentication (TouchID, FaceID, fingerprint)
- Securing sensitive actions with biometric confirmation
- Fallback when biometric hardware is unavailable

**Trigger phrases include:**
- "biometric", "Face ID", "Touch ID", "fingerprint", "biometric login"

## How to use this skill

1. **Install the biometric plugin**:
   ```bash
   cargo add tauri-plugin-biometric
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_biometric::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["biometric:allow-authenticate", "biometric:allow-status"] }
   ```
4. **Check availability and authenticate from the frontend**:
   ```typescript
   import { authenticate, status } from '@tauri-apps/plugin-biometric';
   const bioStatus = await status();
   if (bioStatus.isAvailable) {
     await authenticate('Confirm your identity', { allowDeviceCredential: true });
   }
   ```
5. **Implement fallback** for devices without biometric support (PIN or password entry)
6. **Pair with stronghold plugin** for unlocking encrypted secrets after biometric confirmation

## Outputs

- Biometric authentication flow with availability check
- Fallback strategy for unsupported devices
- Integration pattern with secure storage

## References

- https://v2.tauri.app/plugin/biometric/

## Keywords

tauri biometric, face id, touch id, fingerprint, authentication, fallback
