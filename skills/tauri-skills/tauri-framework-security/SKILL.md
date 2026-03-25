---
name: tauri-framework-security
description: "Harden a Tauri v2 app with baseline security controls including CSP, HTTP headers, runtime authority, and capability matrices. Use when performing security audits, configuring CSP/headers per window, or building a minimum-privilege capability matrix for production."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Tauri v2 security hardening or audit
- CSP, HTTP headers, or runtime authority configuration
- Building a capability matrix for minimum-privilege access

**Trigger phrases include:**
- "security hardening", "CSP", "security audit", "capability matrix", "runtime authority"

## How to use this skill

1. **Build a capability matrix** mapping each feature to minimum-required permissions:
   ```
   Feature         | Plugin     | Permission              | Scope
   Read user files | fs         | fs:allow-read-text-file | $DOCUMENT/**
   Send API calls  | http       | http:default            | https://api.example.com/**
   Notifications   | notification | notification:allow-notify | (no scope)
   ```
2. **Configure CSP** in `tauri.conf.json`:
   ```json
   { "app": { "security": { "csp": "default-src 'self'; connect-src 'self' https://api.example.com" } } }
   ```
3. **Set HTTP headers** for additional security:
   ```json
   { "app": { "security": { "headers": { "X-Content-Type-Options": "nosniff" } } } }
   ```
4. **Review runtime authority**: Ensure each window only has the capabilities it needs
5. **Audit plugin permissions** against actual usage -- remove any permissions not actively required
6. **Produce a release security checklist**: CSP validated, headers set, capabilities minimized, no debug permissions in production

## Outputs

- Capability matrix with minimal scope per feature
- CSP and HTTP headers configuration
- Release security audit checklist

## References

- https://v2.tauri.app/security/
- https://v2.tauri.app/security/capabilities/
- https://v2.tauri.app/security/csp/

## Keywords

tauri security, CSP, hardening, capability matrix, runtime authority, audit
