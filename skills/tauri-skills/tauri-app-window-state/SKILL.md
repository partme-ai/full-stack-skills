---
name: tauri-app-window-state
description: "Persist and restore window size, position, and maximized state across sessions using the Tauri v2 window-state plugin. Use when remembering window layout between app launches, configuring StateFlags, or handling multi-display restore behavior."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Remembering window size and position between sessions
- StateFlags configuration for window state persistence
- Restoring window state on multi-display setups

**Trigger phrases include:**
- "window state", "remember window size", "restore position", "StateFlags", "persist window"

## How to use this skill

1. **Install the window-state plugin**:
   ```bash
   cargo add tauri-plugin-window-state
   ```
2. **Register the plugin** with desired StateFlags:
   ```rust
   use tauri_plugin_window_state::{AppHandleExt, StateFlags};
   tauri::Builder::default()
       .plugin(tauri_plugin_window_state::Builder::new()
           .with_state_flags(StateFlags::SIZE | StateFlags::POSITION | StateFlags::MAXIMIZED)
           .build())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["window-state:allow-restore-state", "window-state:allow-save-window-state"] }
   ```
4. **State is restored automatically** on app startup for each window
5. **Choose StateFlags carefully**: `SIZE`, `POSITION`, `MAXIMIZED`, `VISIBLE`, `DECORATIONS`, `FULLSCREEN`
6. **Handle multi-display edge cases** where a saved position may be off-screen if the display layout changed

## Outputs

- Window-state plugin setup with StateFlags
- Automatic save/restore configuration
- Multi-display edge case handling

## References

- https://v2.tauri.app/plugin/window-state/

## Keywords

tauri window state, persist window, restore position, StateFlags, window size
