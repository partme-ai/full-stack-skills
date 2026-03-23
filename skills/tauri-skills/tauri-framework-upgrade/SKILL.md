---
name: tauri-framework-upgrade
description: Guidance for upgrading to stable Tauri v2 from v1 or v2 beta with migration checks.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Upgrading from Tauri v1 to v2 / 从 v1 升级到 v2
- Migrating from v2 beta to v2 stable / v2 beta 迁移到稳定版
- Breaking changes in config or permissions / 配置或权限变更

**Trigger phrases include:**
- "migrate", "upgrade", "breaking changes", "v1 to v2"
- "升级", "迁移", "配置变更", "权限变更"

## How to use this skill

1. Identify current version and target / 确认当前版本与目标版本
2. Review breaking changes across config, plugins, permissions / 盘点变更点
3. Update tauri.conf.json and plugin layouts / 更新配置与插件位置
4. Migrate capabilities/default.json and scopes / 迁移能力与 Scope
5. Validate IPC, CSP, and runtime behavior / 验证 IPC、CSP 与运行行为

## Outputs

- Migration checklist / 迁移清单
- Updated config mapping / 更新后的配置映射
- Post-upgrade validation plan / 升级后验证计划

## Scope

- Boundary: Version migration and validation only / 仅限迁移与验证
- Key points: Config structure and capability system changes / 配置与权限体系
- Out of scope: feature redesign / 不包含功能重构

## References

- https://v2.tauri.app/start/migrate/
- https://v2.tauri.app/start/migrate/from-tauri-1/
- https://v2.tauri.app/start/migrate/from-tauri-2-beta/

## Keywords

tauri upgrade, migrate, v2, breaking changes, config migration, 升级, 迁移, 配置变更
