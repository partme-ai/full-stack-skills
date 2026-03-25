---
name: tauri-app-positioner
description: "Position windows relative to the system tray or screen using the Tauri v2 positioner plugin with multi-display support. Use when aligning popup or tray windows, handling multi-monitor positioning, or ensuring consistent placement across platforms."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Positioning windows near the system tray
- Multi-monitor or multi-display window alignment
- Consistent window placement across platforms

**Trigger phrases include:**
- "positioner", "window position", "tray window", "multi-monitor", "align window"

## How to use this skill

1. **Install the positioner plugin**:
   ```bash
   cargo add tauri-plugin-positioner
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   use tauri_plugin_positioner::Position;
   tauri::Builder::default()
       .plugin(tauri_plugin_positioner::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["positioner:allow-move-window"] }
   ```
4. **Position a window from the frontend**:
   ```typescript
   import { moveWindow, Position } from '@tauri-apps/plugin-positioner';
   await moveWindow(Position.TrayCenter);    // center below tray icon
   await moveWindow(Position.TopRight);      // top-right corner of screen
   await moveWindow(Position.BottomRight);   // bottom-right corner
   ```
5. **Handle multi-display** by checking which monitor the tray icon is on and positioning relative to it
6. **Account for scaling factors** on HiDPI displays that affect coordinate calculations

## Outputs

- Positioner plugin setup with Position enum
- Tray-relative and screen-relative positioning
- Multi-display and HiDPI scaling guidance

## References

- https://v2.tauri.app/plugin/positioner/

## Keywords

tauri positioner, window position, tray window, multi-monitor, align
