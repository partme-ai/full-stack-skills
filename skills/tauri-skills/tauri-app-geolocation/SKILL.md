---
name: tauri-app-geolocation
description: "Access device location using the Tauri v2 geolocation plugin with permission handling and privacy controls. Use when adding location tracking, configuring accuracy/frequency, or implementing privacy-safe opt-out defaults."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Location access or GPS tracking in a Tauri app
- Geolocation permission flow and privacy constraints
- Location accuracy and update frequency tuning

**Trigger phrases include:**
- "geolocation", "location", "GPS", "tracking", "coordinates", "privacy"

## How to use this skill

1. **Install the geolocation plugin**:
   ```bash
   cargo add tauri-plugin-geolocation
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_geolocation::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["geolocation:allow-get-current-position", "geolocation:allow-watch-position"] }
   ```
4. **Get current position from the frontend**:
   ```typescript
   import { getCurrentPosition, watchPosition } from '@tauri-apps/plugin-geolocation';
   const pos = await getCurrentPosition();
   console.log(`Lat: ${pos.coords.latitude}, Lon: ${pos.coords.longitude}`);
   ```
5. **Handle permission denial** gracefully with user-facing messages and fallback behavior
6. **Provide opt-out defaults** and minimize data collection for privacy compliance

## Outputs

- Geolocation plugin setup with position APIs
- Permission request and denial handling
- Privacy-safe defaults and opt-out pattern

## References

- https://v2.tauri.app/plugin/geolocation/

## Keywords

tauri geolocation, location, GPS, tracking, privacy, permissions
