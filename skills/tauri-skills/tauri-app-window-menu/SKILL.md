---
name: tauri-app-window-menu
description: "Create native application menus with keyboard shortcuts and event handlers in Tauri v2. Use when defining window menu bars, handling menu item click events, binding keyboard accelerators, or adapting menus for macOS/Windows/Linux conventions."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Native window menus or menu bars
- Menu item click events and handlers
- Keyboard shortcuts or accelerators in menus

**Trigger phrases include:**
- "window menu", "menu bar", "menu item", "keyboard shortcut", "accelerator", "context menu"

## How to use this skill

1. **Build a menu** in your Tauri app setup:
   ```rust
   use tauri::menu::{Menu, Submenu, MenuItem, PredefinedMenuItem};
   tauri::Builder::default()
       .setup(|app| {
           let file_menu = Submenu::with_items(app, "File", true, &[
               &MenuItem::with_id(app, "new", "New", true, Some("CmdOrCtrl+N"))?,
               &MenuItem::with_id(app, "open", "Open", true, Some("CmdOrCtrl+O"))?,
               &PredefinedMenuItem::separator(app)?,
               &MenuItem::with_id(app, "quit", "Quit", true, Some("CmdOrCtrl+Q"))?,
           ])?;
           let menu = Menu::with_items(app, &[&file_menu])?;
           app.set_menu(menu)?;
           Ok(())
       })
       .on_menu_event(|app, event| match event.id.as_ref() {
           "new" => { /* handle new */ }
           "quit" => { app.exit(0); }
           _ => {}
       })
   ```
2. **Assign keyboard accelerators** using the `Some("CmdOrCtrl+N")` format
3. **Handle menu events** in the `on_menu_event` callback with match on event IDs
4. **Adapt for platform conventions**: macOS has the app menu (About, Preferences, Quit); Windows uses File/Edit/Help
5. **Use PredefinedMenuItem** for standard items like separator, copy, paste, and quit

## Outputs

- Native menu setup with submenus and items
- Keyboard accelerator bindings
- Cross-platform menu convention guidance

## References

- https://v2.tauri.app/learn/window-menu/

## Keywords

tauri menu, window menu, menu bar, keyboard shortcut, accelerator, context menu
