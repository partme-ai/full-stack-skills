---
name: tauri-security
description: Guidance for Tauri v2 capabilities, scope configuration, and ACL-based permission control.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Capability/Scope design or ACL permission control / 能力、Scope、ACL 权限控制
- Building capabilities/default.json / 生成或校验 capabilities/default.json
- Tightening plugin access in production / 生产环境权限收敛

**Trigger phrases include:**
- "capabilities", "scope", "acl", "permissions file"
- "权限配置", "能力文件", "Scope 配置", "ACL"

## How to use this skill

1. Translate features into plugin capabilities / 业务功能映射为插件能力
2. Define scoped access rules per capability / 为能力定义 Scope 规则
3. Generate and validate capabilities/default.json / 生成并校验能力文件
4. Verify runtime behavior matches minimum-privilege policy / 验证最小权限运行效果

## Outputs

- Capability-to-scope mapping / 能力到 Scope 的映射
- Validated capabilities/default.json / 可直接使用的能力文件
- Permission audit checklist / 权限审计清单

## Scope

- Boundary: Capabilities, scope, and ACL configuration only / 仅限权限配置
- v2 focus: Capabilities & scope are mandatory controls / v2 强制配置
- Out of scope: app feature design or backend auth / 不含功能设计与后端鉴权

## References

- https://v2.tauri.app/security/capabilities/
- https://v2.tauri.app/security/scope/
- https://v2.tauri.app/security/acl/

## Keywords

tauri security, capabilities, scope, acl, permissions, 权限配置, 能力文件, 最小权限
