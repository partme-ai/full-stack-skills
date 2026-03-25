---
name: tauri-build
description: "Build production-ready Tauri v2 app bundles with code signing and distribution packaging for all platforms. Use when creating release builds, configuring code signing for macOS/Windows, or setting up CI pipelines for app distribution."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Production builds or release packaging
- Code signing for macOS, Windows, or Linux
- CI/CD pipelines for app distribution

**Trigger phrases include:**
- "build", "release", "signing", "distribution", "packaging", "installer", "dmg", "msi"

## How to use this skill

1. **Create a production build**:
   ```bash
   npm run tauri build
   ```
2. **Build output** is located in `src-tauri/target/release/bundle/` with platform-specific installers:
   - macOS: `.dmg`, `.app` bundle
   - Windows: `.msi`, `.exe` (NSIS)
   - Linux: `.deb`, `.rpm`, `.AppImage`
3. **Configure signing** in environment variables:
   ```bash
   # macOS
   export APPLE_SIGNING_IDENTITY="Developer ID Application: Your Name"
   # Windows
   export TAURI_SIGNING_PRIVATE_KEY="path/to/key"
   ```
4. **Set bundle identifiers** in `tauri.conf.json`:
   ```json
   { "identifier": "com.example.myapp", "bundle": { "icon": ["icons/icon.png"] } }
   ```
5. **Set up GitHub Actions** for CI/CD using the official Tauri publish action
6. **Validate artifacts** by testing installers on each target platform before release

## Outputs

- Production build commands and output paths
- Code signing configuration per platform
- CI/CD pipeline setup guidance

## References

- https://v2.tauri.app/distribute/
- https://v2.tauri.app/distribute/sign/macos/
- https://v2.tauri.app/distribute/pipelines/github/

## Keywords

tauri build, release, signing, distribution, packaging, installer, dmg, msi
