---
name: tauri-security
description: "Configure Tauri v2 capabilities, scoped access rules, and ACL-based permission control for production apps. Use when generating capabilities/default.json, defining scoped access per plugin, or auditing permissions for minimum-privilege compliance."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Capability or scope design for Tauri v2
- Building or editing capabilities/default.json
- ACL-based permission control or audit

**Trigger phrases include:**
- "capabilities", "scope", "ACL", "permissions", "capabilities json", "minimum privilege"

## How to use this skill

1. **Create capabilities/default.json** in `src-tauri/capabilities/`:
   ```json
   {
     "identifier": "default",
     "description": "Main window capabilities",
     "windows": ["main"],
     "permissions": [
       "core:default",
       "dialog:allow-open",
       { "identifier": "fs:allow-read-text-file", "allow": [{ "path": "$APPDATA/**" }] },
       { "identifier": "http:default", "allow": [{ "url": "https://api.example.com/**" }] }
     ]
   }
   ```
2. **Map features to capabilities**: Each feature should use the minimum permissions required
3. **Define scoped access** to restrict file paths, URLs, and other resources:
   ```json
   { "identifier": "fs:allow-write-text-file", "allow": [{ "path": "$APPDATA/config/**" }] }
   ```
4. **Assign capabilities per window** -- different windows can have different permission sets
5. **Audit permissions** before release: remove any unused permissions, verify scope restrictions
6. **Validate at runtime** by testing that restricted operations correctly fail outside their scope

## Outputs

- capabilities/default.json with minimal permissions
- Feature-to-capability mapping
- Scoped access rules for files, URLs, and plugins
- Permission audit checklist

## References

- https://v2.tauri.app/security/capabilities/
- https://v2.tauri.app/security/scope/

## Keywords

tauri security, capabilities, scope, ACL, permissions, minimum privilege
