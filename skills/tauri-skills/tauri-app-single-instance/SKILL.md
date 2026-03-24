---
name: tauri-app-single-instance
description: Guidance for Tauri v2 single-instance behavior and second-launch argument handling.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Preventing multiple app instances / 防止多开实例
- Handling second-launch arguments / 处理二次启动参数
- Deep-linking or CLI with single-instance / 深链或 CLI 与单实例联动

**Trigger phrases include:**
- "single instance", "second launch", "arguments", "deep linking"
- "单实例", "二次启动", "参数", "深链"

## How to use this skill

1. Enable single-instance and define init behavior
2. Capture and route second-launch arguments to the app
3. Focus or restore the main window on re-entry
4. Validate behavior with deep-linking or CLI scenarios

## Outputs

- Single-instance behavior plan / 单实例行为方案
- Second-launch routing checklist / 二次启动路由清单

## Scope

- Boundary: Single-instance configuration and runtime behavior
- Key points: Safe argument passing and window focus behavior

## References

- https://v2.tauri.app/plugin/single-instance/
- https://v2.tauri.app/zh-cn/plugin/single-instance/

## Keywords

tauri single instance, second launch, args, focus window
