---
name: tauri-app-persisted-scope
description: Guidance for Tauri v2 persisted-scope plugin with expiration and revocation flows.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Persisting plugin scopes across sessions / 跨会话持久化插件 Scope
- Scope expiration or revocation / Scope 过期或撤销
- Re-authorization workflow / 重新授权流程

**Trigger phrases include:**
- "persisted scope", "expiration", "revocation", "re-authorization"
- "持久化权限", "过期", "撤销", "重新授权"

## How to use this skill

1. Define which scopes can be persisted and for how long
2. Configure persisted-scope plugin capabilities
3. Implement expiration, revocation, and re-approval flows
4. Validate scope restoration and downgrade handling

## Outputs

- Scope persistence policy / Scope 持久化策略
- Expiration and revocation checklist / 过期与撤销清单

## Scope

- Boundary: Persisted-scope plugin usage only
- Key points: Avoid permanent over-privilege

## References

- https://v2.tauri.app/plugin/persisted-scope/
- https://v2.tauri.app/zh-cn/plugin/persisted-scope/

## Keywords

tauri persisted scope, permissions, expiration, security
