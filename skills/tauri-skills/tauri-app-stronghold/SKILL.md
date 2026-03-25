---
name: tauri-app-stronghold
description: "Store secrets and sensitive data in encrypted vaults using the Tauri v2 stronghold plugin with snapshot management. Use when securing API keys, tokens, or credentials on disk, managing encrypted snapshots, or pairing with biometric authentication."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Encrypted storage for secrets, credentials, or API keys
- Stronghold snapshots or vault management
- Securing sensitive data on disk

**Trigger phrases include:**
- "stronghold", "encrypted storage", "secrets", "vault", "secure storage", "credentials"

## How to use this skill

1. **Install the stronghold plugin**:
   ```bash
   cargo add tauri-plugin-stronghold
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_stronghold::Builder::new(|password| {
           // Hash the password for vault encryption
           argon2::hash_raw(password.as_bytes(), b"salt", &argon2::Config::default()).unwrap()
       }).build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["stronghold:default"] }
   ```
4. **Store and retrieve secrets from the frontend**:
   ```typescript
   import { Stronghold } from '@tauri-apps/plugin-stronghold';
   const stronghold = await Stronghold.load('vault.hold', 'user-password');
   const client = await stronghold.loadClient('main');
   const store = client.getStore();
   await store.insert('api-key', Array.from(new TextEncoder().encode('sk-12345')));
   const value = await store.get('api-key');
   ```
5. **Save snapshots** to persist the encrypted vault to disk
6. **Pair with biometric plugin** to unlock the vault using TouchID/FaceID instead of a password

## Outputs

- Stronghold plugin setup with encrypted vault
- Secret storage and retrieval pattern
- Snapshot persistence and biometric unlock integration

## References

- https://v2.tauri.app/plugin/stronghold/

## Keywords

tauri stronghold, encrypted storage, secrets, vault, credentials, secure storage
