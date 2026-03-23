---
name: tauri-app-window-state
description: Guidance for Tauri v2 window-state plugin to persist window size and position.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Remembering window size and position / 记住窗口大小与位置
- StateFlags or restore behavior / StateFlags 或恢复行为
- Consistent window state across sessions / 跨会话一致窗口状态

**Trigger phrases include:**
- "window state", "StateFlags", "restore", "window size"
- "窗口状态", "StateFlags", "恢复", "窗口大小"

## How to use this skill

1. Choose StateFlags to persist size, position, and maximized state
2. Enable window-state plugin in the app setup
3. Restore window state at startup with correct timing
4. Validate multi-display behavior and scaling differences

## Outputs

- Window restore plan / 窗口恢复方案
- StateFlags and timing checklist / StateFlags 与时机清单

## Scope

- Boundary: Window-state plugin usage only
- Key points: StateFlags and restore timing

## References

- https://v2.tauri.app/plugin/window-state/
- https://v2.tauri.app/zh-cn/plugin/window-state/

## Keywords

tauri window state, StateFlags, restore, window size
