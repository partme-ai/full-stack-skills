---
name: tauri-app-splashscreen
description: "Configure a splashscreen window in Tauri v2 to display during app initialization and avoid white screen flashes. Use when adding a loading screen at startup, controlling splashscreen-to-main-window transitions, or handling slow frontend loads."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Splashscreen or loading screen at app startup
- Avoiding white screen flash during initialization
- Controlling when to hide the splashscreen

**Trigger phrases include:**
- "splashscreen", "splash screen", "loading screen", "white screen", "startup screen"

## How to use this skill

1. **Configure splashscreen window** in `tauri.conf.json`:
   ```json
   {
     "app": {
       "windows": [
         { "label": "splashscreen", "url": "splashscreen.html", "width": 400, "height": 300, "decorations": false, "center": true },
         { "label": "main", "url": "/", "visible": false }
       ]
     }
   }
   ```
2. **Create a splashscreen HTML file** (e.g., `splashscreen.html`) with your loading animation or logo
3. **Close the splashscreen and show main window** from Rust when the app is ready:
   ```rust
   #[tauri::command]
   async fn close_splashscreen(app: tauri::AppHandle) {
       if let Some(splash) = app.get_webview_window("splashscreen") { splash.close().unwrap(); }
       if let Some(main) = app.get_webview_window("main") { main.show().unwrap(); }
   }
   ```
4. **Trigger from the frontend** when initialization is complete:
   ```typescript
   import { invoke } from '@tauri-apps/api/core';
   await invoke('close_splashscreen');
   ```
5. **Handle slow frontend loads** by keeping the splashscreen visible until the frontend signals readiness
6. **Set a timeout** to close the splashscreen even if initialization hangs, to prevent stuck screens

## Outputs

- Splashscreen window configuration in tauri.conf.json
- Rust command to transition from splash to main window
- Timeout fallback for hung initialization

## References

- https://v2.tauri.app/learn/splashscreen/

## Keywords

tauri splashscreen, loading screen, white screen, startup, splash window
