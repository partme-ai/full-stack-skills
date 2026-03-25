---
name: tauri-app-notification
description: "Send system notifications using the Tauri v2 notification plugin with permission handling and click callbacks. Use when displaying native notifications, requesting notification permissions, or routing notification clicks to specific app views."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- System notifications in a Tauri app
- Notification permission requests
- Handling notification click events or actions

**Trigger phrases include:**
- "notification", "system alert", "push notification", "notify", "toast"

## How to use this skill

1. **Install the notification plugin**:
   ```bash
   cargo add tauri-plugin-notification
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_notification::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["notification:allow-notify", "notification:allow-request-permission", "notification:allow-is-permission-granted"] }
   ```
4. **Send a notification from the frontend**:
   ```typescript
   import { sendNotification, requestPermission, isPermissionGranted } from '@tauri-apps/plugin-notification';
   if (!(await isPermissionGranted())) {
     await requestPermission();
   }
   sendNotification({ title: 'Update Complete', body: 'Your file has been saved.' });
   ```
5. **Handle permission denial** gracefully with in-app fallback messaging
6. **Route notification clicks** to specific views or actions in your app

## Outputs

- Notification plugin setup with permission flow
- Send notification with title and body
- Click handling and in-app fallback pattern

## References

- https://v2.tauri.app/plugin/notification/

## Keywords

tauri notification, system alert, push notification, notify, permissions
