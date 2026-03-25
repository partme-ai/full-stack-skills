---
name: tauri-app-deep-linking
description: "Configure Tauri v2 deep-linking plugin to handle custom URL schemes (e.g., myapp://) and route external URLs into the app. Use when registering custom protocols, routing deep link parameters to frontend views, or validating external input for security."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Deep links or custom URL schemes (e.g., `myapp://`)
- Routing external URLs into the app
- Secure handling of external link payloads

**Trigger phrases include:**
- "deep link", "url scheme", "custom protocol", "app link", "myapp://"

## How to use this skill

1. **Install the deep-linking plugin**:
   ```bash
   cargo add tauri-plugin-deep-link
   ```
2. **Register the plugin** and define your scheme in `tauri.conf.json`:
   ```json
   { "plugins": { "deep-link": { "desktop": { "schemes": ["myapp"] } } } }
   ```
3. **Listen for deep link events** on the frontend:
   ```typescript
   import { onOpenUrl } from '@tauri-apps/plugin-deep-link';
   await onOpenUrl((urls) => {
     console.log('Deep link received:', urls);
     // Route to appropriate view based on URL path
   });
   ```
4. **Sanitize all external input** before using deep link parameters in your app logic
5. **Combine with single-instance plugin** to forward deep links to the existing running instance
6. **Register the scheme** with the OS (automatic on install for macOS/Windows, manual for Linux)

## Outputs

- Deep link scheme registration in tauri.conf.json
- Frontend event handler for incoming URLs
- Input validation and sanitization pattern

## References

- https://v2.tauri.app/plugin/deep-linking/

## Keywords

tauri deep linking, url scheme, custom protocol, routing, security
