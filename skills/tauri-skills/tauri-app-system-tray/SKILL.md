---
name: tauri-app-system-tray
description: "Create and manage system tray icons with menus and click handlers in Tauri v2, handling platform differences. Use when adding a tray icon, building tray menus, toggling window visibility from the tray, or handling macOS/Windows/Linux tray conventions."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- System tray icon or status bar icon
- Tray menu with actions (show, hide, quit)
- Platform-specific tray behavior differences

**Trigger phrases include:**
- "system tray", "tray icon", "tray menu", "status bar", "minimize to tray"

## How to use this skill

1. **Configure a tray icon** in your Tauri builder:
   ```rust
   use tauri::{tray::TrayIconBuilder, menu::{Menu, MenuItem}};
   tauri::Builder::default()
       .setup(|app| {
           let show = MenuItem::with_id(app, "show", "Show", true, None::<&str>)?;
           let quit = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
           let menu = Menu::with_items(app, &[&show, &quit])?;
           TrayIconBuilder::new()
               .icon(app.default_window_icon().unwrap().clone())
               .menu(&menu)
               .on_menu_event(|app, event| match event.id.as_ref() {
                   "show" => { app.get_webview_window("main").unwrap().show().unwrap(); }
                   "quit" => { app.exit(0); }
                   _ => {}
               })
               .build(app)?;
           Ok(())
       })
   ```
2. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["core:default", "tray:default"] }
   ```
3. **Handle tray icon clicks** to toggle window visibility (show/hide on click)
4. **Handle platform differences**: macOS uses left-click for menu, Windows uses right-click; tray positioning varies
5. **Combine with positioner plugin** for accurate tray-relative window placement

## Outputs

- System tray setup with icon and menu
- Menu event handling with show/hide/quit actions
- Platform-specific behavior guidance

## References

- https://v2.tauri.app/learn/system-tray/

## Keywords

tauri system tray, tray icon, tray menu, status bar, minimize to tray
