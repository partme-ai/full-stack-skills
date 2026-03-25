---
name: tauri-app-haptics
description: "Trigger tactile feedback on mobile devices using the Tauri v2 haptics plugin with vibration patterns and graceful fallback. Use when adding haptic feedback to touch interactions, selecting vibration patterns, or handling unsupported devices silently."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Tactile or haptic feedback on mobile devices
- Vibration patterns or feedback types
- Fallback for devices without haptic support

**Trigger phrases include:**
- "haptics", "vibration", "tactile feedback", "haptic feedback", "vibrate"

## How to use this skill

1. **Install the haptics plugin**:
   ```bash
   cargo add tauri-plugin-haptics
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_haptics::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["haptics:allow-vibrate", "haptics:allow-impact-feedback", "haptics:allow-notification-feedback"] }
   ```
4. **Trigger haptic feedback from the frontend**:
   ```typescript
   import { impactFeedback, notificationFeedback, ImpactFeedbackStyle } from '@tauri-apps/plugin-haptics';
   await impactFeedback(ImpactFeedbackStyle.Medium);
   await notificationFeedback('success');
   ```
5. **Use appropriate feedback types**: impact for touch interactions, notification for success/error/warning
6. **Handle unsupported devices** with try/catch and silent fallback (no error shown to user)

## Outputs

- Haptic feedback integration with appropriate feedback types
- Pattern selection guidance (impact vs notification)
- Silent fallback for unsupported devices

## References

- https://v2.tauri.app/plugin/haptics/

## Keywords

tauri haptics, vibration, tactile feedback, mobile, haptic patterns
