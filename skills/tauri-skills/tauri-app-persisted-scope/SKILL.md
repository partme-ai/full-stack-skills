---
name: tauri-app-persisted-scope
description: "Persist file system and other plugin scopes across app restarts using the Tauri v2 persisted-scope plugin. Use when retaining user-granted file access between sessions, implementing scope expiration policies, or managing scope revocation flows."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Persisting plugin scopes across app restarts
- Remembering file access permissions between sessions
- Scope expiration or revocation flows

**Trigger phrases include:**
- "persisted scope", "remember access", "scope persistence", "re-authorization", "scope expiration"

## How to use this skill

1. **Install the persisted-scope plugin**:
   ```bash
   cargo add tauri-plugin-persisted-scope
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_persisted_scope::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["persisted-scope:allow-save", "persisted-scope:allow-load"] }
   ```
4. **How it works**: When the user grants file access (e.g., via a dialog picker), the persisted-scope plugin automatically saves those scope entries to disk and restores them on next launch
5. **Implement expiration** by periodically checking saved scopes and removing stale entries
6. **Add revocation UI** to let users manage which persistent access grants remain active
7. **Avoid permanent over-privilege** by reviewing persisted scopes during app startup

## Outputs

- Persisted scope plugin setup for cross-session access retention
- Expiration and revocation flow patterns
- Scope audit guidance to prevent over-privilege

## References

- https://v2.tauri.app/plugin/persisted-scope/

## Keywords

tauri persisted scope, scope persistence, file access, re-authorization, expiration
