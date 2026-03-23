---
name: tauri-framework-security
description: Guidance for Tauri v2 security model, baseline hardening, and runtime authority controls.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Tauri v2 security baseline, hardening, or audit / Tauri v2 安全基线、加固或审计
- CSP, HTTP headers, or runtime authority / CSP、HTTP 头或运行时权限
- Capability/Scope design for security posture / 能力与 Scope 的安全设计

**Trigger phrases include:**
- "security baseline", "hardening", "CSP", "security checklist"
- "安全基线", "安全加固", "权限收敛", "上线审计"

## How to use this skill

1. Clarify app context: platforms, windows, data sensitivity / 明确平台、窗口与数据敏感度
2. Build a capability matrix: feature → plugin → capability → scope / 建立能力矩阵
3. Define CSP and HTTP headers per window / 为每个窗口定义 CSP 与 Headers
4. Review runtime authority and plugin permissions / 校验运行时权限与插件权限
5. Produce a release security checklist and validation plan / 输出上线安全检查清单

## Outputs

- Capability matrix with minimal scope / 最小权限能力矩阵
- CSP & headers plan per window / 每个窗口的 CSP 与 Headers 方案
- Release security checklist / 上线安全检查清单

## Scope

- Boundary: Tauri v2 security model and baseline hardening / 仅限安全模型与基线
- In scope: Capabilities, Scope, CSP, headers, runtime authority / 权限与运行时控制
- Out of scope: backend auth or server security / 不涉及后端鉴权与服务器安全

## References

- https://v2.tauri.app/security/
- https://v2.tauri.app/security/permissions/
- https://v2.tauri.app/security/scope/
- https://v2.tauri.app/security/capabilities/
- https://v2.tauri.app/security/csp/
- https://v2.tauri.app/security/http-headers/
- https://v2.tauri.app/security/ecosystem/
- https://v2.tauri.app/security/lifecycle/
- https://v2.tauri.app/security/future/
- https://v2.tauri.app/security/runtime-authority/

## Keywords

tauri security, csp, headers, permissions, capabilities, runtime authority, 安全基线, 权限收敛, 运行时权限
