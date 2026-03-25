---
name: tauri-app-store
description: "Persist key-value data to disk using the Tauri v2 store plugin for app settings and preferences. Use when saving app configuration, choosing between Store and LazyStore, or implementing persistent settings with automatic disk writes."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Persistent key-value storage for app settings
- Store vs LazyStore selection
- Saving user preferences or configuration to disk

**Trigger phrases include:**
- "store", "key-value", "app settings", "persistence", "preferences", "local storage"

## How to use this skill

1. **Install the store plugin**:
   ```bash
   cargo add tauri-plugin-store
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_store::Builder::new().build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["store:allow-get", "store:allow-set", "store:allow-save", "store:allow-load"] }
   ```
4. **Use the store from the frontend**:
   ```typescript
   import { Store } from '@tauri-apps/plugin-store';
   const store = await Store.load('settings.json');
   await store.set('theme', 'dark');
   await store.set('language', 'en');
   const theme = await store.get<string>('theme');
   await store.save(); // persist to disk
   ```
5. **Choose Store vs LazyStore**: Use `Store` for settings loaded at startup; use `LazyStore` for data loaded on-demand
6. **Auto-save** can be configured to persist changes automatically without manual `save()` calls

## Outputs

- Store plugin setup with settings file
- Get/set/save patterns for key-value data
- Store vs LazyStore selection guidance

## References

- https://v2.tauri.app/plugin/store/

## Keywords

tauri store, key-value, persistence, app settings, preferences, local storage
