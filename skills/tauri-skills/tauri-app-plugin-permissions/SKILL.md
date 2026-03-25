---
name: tauri-app-plugin-permissions
description: "Author and audit Tauri v2 plugin permissions, generate capability files, and handle cross-platform permission differences. Use when writing plugin permission schemas, generating capabilities/default.json, or auditing permissions across Windows/macOS/Linux/mobile."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Writing or auditing plugin permissions
- Generating capability templates or permissions schemas
- Cross-platform permission differences

**Trigger phrases include:**
- "plugin permissions", "capability template", "permissions schema", "capabilities json"

## How to use this skill

1. **Map features to plugin permissions**:
   ```
   Feature: "Read user files"
   Plugin:  fs
   Permission: fs:allow-read-text-file
   Scope: { "path": "$DOCUMENT/**" }
   ```
2. **Generate capabilities/default.json** with minimal scope:
   ```json
   {
     "identifier": "default",
     "description": "Main app capabilities",
     "windows": ["main"],
     "permissions": [
       "fs:allow-read-text-file",
       "dialog:allow-open",
       { "identifier": "http:default", "allow": [{ "url": "https://api.example.com/**" }] }
     ]
   }
   ```
3. **Separate plugin-defined permissions** (what a plugin exposes) from app-enabled capabilities (what your app allows)
4. **Handle platform differences**: Some permissions behave differently on Windows vs macOS (e.g., shell execution, file paths)
5. **Audit permissions** by reviewing each capability entry against the minimum required for each feature
6. **Run `cargo tauri build`** to validate that all required permissions are declared

## Outputs

- Feature-to-permission mapping table
- Minimal capabilities/default.json file
- Cross-platform permission audit checklist

## References

- https://v2.tauri.app/learn/using-plugin-permissions/
- https://v2.tauri.app/learn/security/writing-plugin-permissions/

## Keywords

tauri permissions, plugin permissions, capabilities, scope, capability template
