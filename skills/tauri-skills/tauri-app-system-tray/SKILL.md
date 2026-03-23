---
name: tauri-app-system-tray
description: Guidance for Tauri v2 system tray interactions and platform behavior differences.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- System tray or status bar behavior / 系统托盘或状态栏行为
- Tray menu and window visibility / 托盘菜单与窗口可见性
- Platform-specific tray conventions / 跨平台托盘约定

**Trigger phrases include:**
- "system tray", "status bar", "tray menu", "visibility"
- "系统托盘", "状态栏", "托盘菜单", "可见性"

## How to use this skill

1. Define tray icon behavior and menu actions
2. Map actions to window show, hide, and focus
3. Handle macOS, Windows, and Linux behavior differences
4. Ensure security gating for sensitive actions

## Outputs

- Tray interaction and visibility plan / 托盘交互与可见性方案
- Platform differences checklist / 跨平台差异清单

## Scope

- Boundary: System tray interaction patterns only
- Key points: Platform differences and secure actions

## References

- https://v2.tauri.app/learn/system-tray/
- https://v2.tauri.app/zh-cn/learn/system-tray/

## Keywords

tauri system tray, status bar, menu, cross-platform
