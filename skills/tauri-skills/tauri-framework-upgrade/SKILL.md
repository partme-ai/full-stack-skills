---
name: tauri-framework-upgrade
description: "Migrate Tauri apps from v1 to v2 or from v2 beta to v2 stable, handling breaking changes in config, plugins, and permissions. Use when upgrading Tauri versions, resolving migration errors, or updating config/capability formats for v2."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Upgrading from Tauri v1 to v2
- Migrating from v2 beta to v2 stable
- Breaking changes in config or permissions

**Trigger phrases include:**
- "migrate", "upgrade", "v1 to v2", "breaking changes", "migration", "tauri update"

## How to use this skill

1. **Run the migration command**:
   ```bash
   npx @tauri-apps/cli migrate
   ```
2. **Key breaking changes from v1 to v2**:
   - `allowlist` replaced with **capabilities system** (`src-tauri/capabilities/default.json`)
   - `tauri` config key renamed to `app`
   - Plugins moved from built-in to `cargo add tauri-plugin-*`
   - Event system now uses typed payloads
3. **Update tauri.conf.json** to v2 format:
   ```json
   {
     "identifier": "com.example.app",
     "app": { "windows": [{ "label": "main" }] },
     "build": { "frontendDist": "../dist" }
   }
   ```
4. **Create capabilities/default.json** to replace the old allowlist:
   ```json
   { "identifier": "default", "windows": ["main"], "permissions": ["core:default"] }
   ```
5. **Update Cargo.toml** dependencies to v2 versions
6. **Validate** by running `npm run tauri dev` and resolving any compile or runtime errors

## Outputs

- Migration command and automated changes
- Config format mapping (v1 to v2)
- Capabilities file replacing allowlist
- Post-migration validation checklist

## References

- https://v2.tauri.app/start/migrate/from-tauri-1/
- https://v2.tauri.app/start/migrate/from-tauri-2-beta/

## Keywords

tauri upgrade, migrate, v1 to v2, breaking changes, migration, version update
