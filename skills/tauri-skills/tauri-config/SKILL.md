---
name: tauri-config
description: "Configure tauri.conf.json for Tauri v2 apps including app metadata, build settings, plugins, CSP, and platform-specific sections. Use when editing tauri.conf.json, migrating config from v1 to v2, or setting up CSP and platform-specific configuration."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Editing or understanding tauri.conf.json
- Config changes from Tauri v1 to v2
- CSP configuration or platform-specific config sections

**Trigger phrases include:**
- "tauri.conf.json", "tauri config", "CSP", "configuration", "build config"

## How to use this skill

1. **Understand the config structure** -- key sections of `tauri.conf.json`:
   ```json
   {
     "productName": "My App",
     "version": "1.0.0",
     "identifier": "com.example.myapp",
     "build": {
       "devUrl": "http://localhost:5173",
       "frontendDist": "../dist"
     },
     "app": {
       "windows": [{ "label": "main", "title": "My App", "width": 1024, "height": 768 }],
       "security": { "csp": "default-src 'self'; script-src 'self'" }
     },
     "plugins": {}
   }
   ```
2. **Configure CSP** in `app.security.csp` to restrict content loading sources
3. **Add plugin configuration** under the `plugins` key (e.g., updater endpoints, CLI schema)
4. **Platform-specific overrides** go in the appropriate config sections for Android/iOS
5. **v2 migration notes**: `tauri` key renamed to `app`, `allowlist` replaced with capabilities system, plugins moved to `plugins` key
6. **Validate config** by running `npm run tauri dev` which reports config errors on startup

## Outputs

- tauri.conf.json structure overview with key sections
- CSP configuration for content security
- v1 to v2 config migration mapping

## References

- https://v2.tauri.app/reference/config/
- https://v2.tauri.app/security/csp/

## Keywords

tauri config, tauri.conf.json, CSP, build configuration, app settings
