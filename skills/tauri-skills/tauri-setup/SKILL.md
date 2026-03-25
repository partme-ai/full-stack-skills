---
name: tauri-setup
description: "Install Tauri v2 prerequisites and configure the development environment across macOS, Windows, Linux, Android, and iOS. Use when setting up Rust toolchain, Node.js, platform build tools, or mobile development prerequisites (Xcode, Android Studio)."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Tauri v2 prerequisites or environment setup
- Installing Rust toolchain, Node.js, or platform build tools
- Mobile development setup (Xcode, Android Studio/NDK)

**Trigger phrases include:**
- "setup", "prerequisites", "install tauri", "toolchain", "Xcode", "Android Studio"

## How to use this skill

1. **Install Rust** (required on all platforms):
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
2. **Install Node.js** (LTS recommended):
   ```bash
   # Using nvm
   nvm install --lts
   ```
3. **Platform-specific prerequisites**:
   - **macOS**: Xcode Command Line Tools: `xcode-select --install`
   - **Windows**: Visual Studio Build Tools with C++ workload, WebView2
   - **Linux**: `sudo apt install libwebkit2gtk-4.1-dev build-essential libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev`
4. **Mobile prerequisites**:
   - **Android**: Android Studio with NDK, add Rust targets: `rustup target add aarch64-linux-android armv7-linux-androideabi`
   - **iOS**: Xcode with iOS SDK, add Rust targets: `rustup target add aarch64-apple-ios`
5. **Verify setup**:
   ```bash
   rustc --version && cargo --version && node --version
   ```
6. **Create a test project** to confirm everything works: `npm create tauri-app@latest`

## Outputs

- Platform-specific prerequisite installation commands
- Mobile development prerequisites (Android Studio, Xcode)
- Verification commands to confirm setup

## References

- https://v2.tauri.app/start/prerequisites/

## Keywords

tauri setup, prerequisites, Rust, Node.js, Xcode, Android Studio, toolchain
