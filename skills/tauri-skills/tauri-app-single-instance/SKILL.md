---
name: tauri-app-single-instance
description: "Prevent multiple app instances and handle second-launch arguments using the Tauri v2 single-instance plugin. Use when enforcing single-instance behavior, forwarding CLI arguments from a second launch, or focusing the existing window on re-entry."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Preventing multiple app instances from running
- Handling second-launch arguments or deep links
- Focusing the existing window when re-launched

**Trigger phrases include:**
- "single instance", "prevent duplicate", "second launch", "one instance only"

## How to use this skill

1. **Install the single-instance plugin**:
   ```bash
   cargo add tauri-plugin-single-instance
   ```
2. **Register the plugin** in your Tauri builder with a callback:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_single_instance::init(|app, args, _cwd| {
           // Focus the main window when a second instance is launched
           if let Some(window) = app.get_webview_window("main") {
               window.set_focus().unwrap();
           }
           // Forward args to the running instance
           println!("Second launch args: {:?}", args);
       }))
   ```
3. **The callback receives**: the app handle, command-line arguments, and the working directory from the second launch
4. **Combine with deep-linking** to route `myapp://` URLs from the second instance to the existing window
5. **Combine with CLI plugin** to forward parsed arguments to the running app
6. **The second instance exits automatically** after the callback runs

## Outputs

- Single-instance plugin setup with window focus callback
- Second-launch argument forwarding pattern
- Integration with deep-linking and CLI plugins

## References

- https://v2.tauri.app/plugin/single-instance/

## Keywords

tauri single instance, prevent duplicate, second launch, window focus, args
