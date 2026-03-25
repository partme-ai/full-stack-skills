---
name: tauri-window
description: "Create and configure Tauri v2 windows including multi-window patterns, custom titlebars, and frameless window UI. Use when creating new windows, managing window lifecycle events, implementing custom titlebar drag regions, or building multi-window architectures."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Creating or configuring Tauri windows
- Multi-window patterns or window lifecycle
- Custom titlebar or frameless window UI

**Trigger phrases include:**
- "window", "titlebar", "frameless", "multi-window", "window lifecycle", "new window"

## How to use this skill

1. **Configure windows** in `tauri.conf.json`:
   ```json
   {
     "app": {
       "windows": [
         { "label": "main", "title": "My App", "width": 1024, "height": 768, "decorations": true },
         { "label": "settings", "title": "Settings", "width": 600, "height": 400, "url": "/settings" }
       ]
     }
   }
   ```
2. **Create windows at runtime** from Rust:
   ```rust
   tauri::WebviewWindowBuilder::new(&app, "popup", tauri::WebviewUrl::App("/popup".into()))
       .title("Popup")
       .inner_size(400.0, 300.0)
       .build()?;
   ```
3. **Create a frameless window** with custom titlebar:
   ```json
   { "label": "main", "decorations": false, "transparent": true }
   ```
4. **Add a drag region** in your custom titlebar HTML:
   ```html
   <div data-tauri-drag-region class="titlebar">My App</div>
   ```
5. **Manage window lifecycle** by listening to close, focus, and resize events
6. **Assign different capabilities** to each window label for security isolation

## Outputs

- Window configuration in tauri.conf.json
- Runtime window creation from Rust
- Custom titlebar with drag region
- Multi-window capability assignment

## References

- https://v2.tauri.app/learn/window-customization/
- https://v2.tauri.app/reference/config/#windows-config

## Keywords

tauri window, titlebar, frameless, multi-window, window lifecycle, custom titlebar
