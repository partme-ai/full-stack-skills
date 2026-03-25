---
name: tauri-mobile
description: "Set up Tauri v2 for Android and iOS development including build configuration, bundle identifiers, and mobile debugging. Use when adding mobile targets to a Tauri app, configuring Android/iOS bundle IDs, or debugging on mobile devices and emulators."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Android or iOS builds for a Tauri app
- Mobile debugging or running on devices/emulators
- Bundle identifier (bundle ID) configuration

**Trigger phrases include:**
- "mobile", "android", "ios", "bundle id", "mobile debug", "emulator"

## How to use this skill

1. **Initialize mobile support**:
   ```bash
   npm run tauri android init
   npm run tauri ios init
   ```
2. **Configure bundle identifiers** in `tauri.conf.json`:
   ```json
   { "identifier": "com.example.myapp" }
   ```
3. **Run on Android emulator or device**:
   ```bash
   npm run tauri android dev
   ```
4. **Run on iOS simulator**:
   ```bash
   npm run tauri ios dev
   ```
5. **Debug mobile**: Use Chrome DevTools for Android WebView debugging or Safari Web Inspector for iOS
6. **Prerequisites**: Android Studio with NDK installed for Android; Xcode for iOS
7. **Handle responsive UI** by testing across different screen sizes and orientations

## Outputs

- Mobile project initialization commands
- Bundle identifier configuration
- Dev/debug workflow for Android and iOS
- Prerequisite checklist (Android Studio, Xcode)

## References

- https://v2.tauri.app/mobile/
- https://v2.tauri.app/mobile/development/

## Keywords

tauri mobile, android, ios, bundle id, mobile debugging, emulator
