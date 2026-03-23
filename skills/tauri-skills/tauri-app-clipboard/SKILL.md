---
name: tauri-app-clipboard
description: Guidance for Tauri v2 clipboard plugin with safe copy, paste, and monitoring flows.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Reading or writing clipboard content / 读写剪贴板内容
- Clipboard monitoring or images / 剪贴板监听或图像
- Reducing clipboard abuse risk / 降低剪贴板滥用风险

**Trigger phrases include:**
- "clipboard", "copy", "paste", "monitoring"
- "剪贴板", "复制", "粘贴", "监听"

## How to use this skill

1. Identify clipboard content types and user flows
2. Configure clipboard plugin capabilities and scope
3. Implement copy, paste, and change listeners carefully
4. Restrict access to user-initiated actions only

## Outputs

- Clipboard access policy / 剪贴板访问策略
- User-initiated flow checklist / 用户触发流程清单

## Scope

- Boundary: Clipboard plugin usage only
- Key points: Permission control and user-initiated access

## References

- https://v2.tauri.app/plugin/clipboard/
- https://v2.tauri.app/zh-cn/plugin/clipboard/

## Keywords

tauri clipboard, copy, paste, permissions
