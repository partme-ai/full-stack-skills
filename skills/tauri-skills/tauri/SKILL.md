---
name: tauri
description: "Primary index and router for all Tauri v2 framework skills covering Rust backend, frontend integration, and the full plugin ecosystem. Use when any Tauri-related request is made to route to the correct specialized sub-skill with local examples and templates."
license: Complete terms in LICENSE.txt
---


## When to use this skill

Use this skill as the **primary entry point** for any Tauri-related request. It routes to specific sub-skills.

**Use when:**
- The user asks about Tauri and you need to identify the right sub-skill
- You need an overview of available Tauri capabilities
- The request spans multiple Tauri features

## How to use this skill

1. **Identify the user's intent** from their request
2. **Route to the specific sub-skill** from the map below
3. **Each sub-skill** contains local `examples/` and `templates/` directories for offline-ready guidance

### Sub-skill Map

**Planning & Architecture**
- `tauri-app-planning`: Requirements analysis, plugin selection, architecture design
- `tauri-concept`: Process model, IPC isolation, brownfield patterns

**Setup & Scaffolding**
- `tauri-setup`: Prerequisites and environment setup
- `tauri-scaffold`: Project creation with `create-tauri-app`
- `tauri-app-creator`: New project bootstrap and first-run verification
- `tauri-config`: tauri.conf.json structure and CSP
- `tauri-app-frontend-selection`: Frontend framework choice and static export

**Development & Build**
- `tauri-app-develop`: Dev workflow, debugging, testing
- `tauri-build`: Production builds, signing, distribution
- `tauri-mobile`: Android and iOS development
- `tauri-ipc`: Frontend-to-Rust invoke calls and type-safe bindings
- `tauri-app-wasm`: Rust-compiled WASM in the frontend

**System Integration**
- `tauri-app-shell`: System command execution
- `tauri-app-os-info`: OS version, arch, locale
- `tauri-app-clipboard`: Copy/paste operations
- `tauri-app-dialog`: File pickers and native dialogs
- `tauri-app-notification`: System notifications
- `tauri-app-global-shortcut`: System-wide keyboard shortcuts
- `tauri-app-autostart`: Launch on system login
- `tauri-app-biometric`: TouchID/FaceID authentication
- `tauri-app-opener`: Open URLs/files in default apps
- `tauri-app-deep-linking`: Custom URL scheme handling
- `tauri-app-geolocation`: GPS and location access
- `tauri-app-haptics`: Mobile tactile feedback
- `tauri-app-barcode-scanner`: QR/barcode scanning
- `tauri-app-nfc`: NFC tag read/write

**Data & Networking**
- `tauri-app-http-client`: CORS-free HTTP requests
- `tauri-app-websocket`: WebSocket connections
- `tauri-app-upload`: File upload with progress
- `tauri-app-sql`: SQLite/MySQL/PostgreSQL access
- `tauri-app-store`: Key-value persistence
- `tauri-app-stronghold`: Encrypted secret storage
- `tauri-app-file-system`: Scoped file read/write

**Window & UI**
- `tauri-window`: Window creation and custom titlebar
- `tauri-app-window-menu`: Native menus and shortcuts
- `tauri-app-system-tray`: Tray icon and menu
- `tauri-app-window-state`: Persist window size/position
- `tauri-app-positioner`: Tray/window positioning
- `tauri-app-single-instance`: Prevent duplicate instances
- `tauri-app-splashscreen`: Loading screen at startup

**Security**
- `tauri-security`: Capabilities and ACL configuration
- `tauri-framework-security`: Security hardening and audit
- `tauri-app-plugin-permissions`: Plugin permission authoring
- `tauri-app-persisted-scope`: Cross-session scope persistence

**Migration**
- `tauri-framework-upgrade`: v1 to v2 migration

## Keywords

Tauri, tauri v2, rust, desktop app, mobile app, plugins, capabilities, permissions
