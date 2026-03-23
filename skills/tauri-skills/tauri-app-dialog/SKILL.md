---
name: tauri-app-dialog
description: Guidance for Tauri v2 dialog plugin with native dialogs and unified API design.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Native alert, confirm, or file dialogs / 原生提示、确认或文件对话框
- Unified dialog APIs across platforms / 跨平台统一对话框 API
- Async dialog flows with cancellation / 异步对话框与取消流程

**Trigger phrases include:**
- "dialog", "alert", "confirm", "file picker", "native dialog"
- "对话框", "提示框", "确认框", "文件选择"

## How to use this skill

1. Define dialog types and UI flows
2. Configure dialog plugin capabilities and scope
3. Implement async dialog calls and cancellation handling
4. Provide a unified dialog service layer for reuse

## Outputs

- Dialog service design / 对话框服务设计
- Async and cancellation flow checklist / 异步与取消流程清单

## Scope

- Boundary: Dialog plugin usage only
- Key points: Async behavior and platform consistency

## References

- https://v2.tauri.app/plugin/dialog/
- https://v2.tauri.app/zh-cn/plugin/dialog/

## Keywords

tauri dialog, alert, confirm, file picker, native dialogs
