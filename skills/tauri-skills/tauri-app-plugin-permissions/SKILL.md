---
name: tauri-app-plugin-permissions
description: Guidance for Tauri v2 plugin permission authoring, capability generation, and platform differences.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Writing or auditing plugin permissions / 编写或审计插件权限
- Plugin capability templates / 插件权限模板
- Cross-platform permission differences / 跨平台权限差异

**Trigger phrases include:**
- "plugin permissions", "capability template", "permissions schema"
- "插件权限", "权限模板", "平台差异"

## How to use this skill

1. Enumerate feature → plugin permission needs / 功能与插件权限需求映射
2. Separate plugin-defined permissions from app-enabled capabilities / 区分插件权限与应用能力
3. Generate capabilities/default.json with minimal scope / 生成最小权限配置
4. Validate Windows/platform differences and adjust / 校验平台差异并调整

## Outputs

- Permission template per plugin / 插件权限模板
- Capability file with minimal scope / 最小权限能力文件
- Cross-platform audit checklist / 跨平台审计清单

## Scope

- Boundary: Plugin permissions and capability configuration only / 仅限权限配置
- Key points: Windows and platform capability differences / 平台差异
- Out of scope: plugin implementation details / 不涉及插件实现

## References

- https://v2.tauri.app/learn/using-plugin-permissions/
- https://v2.tauri.app/zh-cn/learn/security/using-plugin-permissions/
- https://v2.tauri.app/learn/security/capabilities-for-windows-and-platforms/
- https://v2.tauri.app/zh-cn/learn/security/capabilities-for-windows-and-platforms/
- https://v2.tauri.app/learn/security/writing-plugin-permissions/
- https://v2.tauri.app/zh-cn/learn/security/writing-plugin-permissions/

## Keywords

tauri permissions, plugin permissions, capabilities, scope, security, 插件权限, 权限模板, 平台差异
