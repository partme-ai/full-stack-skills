---
name: tauri
description: Comprehensive index for Tauri framework development, including Rust backend, frontend integration, and full plugin ecosystem. Acts as a router to specialized sub-skills with local examples and templates.
license: Complete terms in LICENSE.txt
---


## When to use this skill

Use this skill as the **primary entry point** for any Tauri-related request. It serves as a "Total Index" (like `nvm`) that routes you to specific sub-skills.

**Why?**
- **Token Efficiency**: Each sub-skill contains local `examples/` and `templates/` directories, providing detailed, offline-ready documentation without expensive network searches.
- **Tauri v2 Ready**: All sub-skills are updated for Tauri v2.0+ (plugins, capabilities, permissions).

## How to use this skill

1.  **Identify Intent**: Determine if the user needs setup, specific plugin functionality (FS, Dialog, SQL), or core app configuration.
2.  **Route**: Invoke the specific sub-skill listed below.
3.  **Explore**: Inside the sub-skill, use `examples/usage.md` for step-by-step guides and `templates/capabilities.json` for permission configs.

### Sub-skill Map

**Planning & Architecture**
- `tauri-app-planning`: **START HERE**. Requirement analysis, plugin selection, architecture design, and Todo list generation. Includes orchestration patterns.

**Core & Lifecycle**
- `tauri-setup`: Project initialization and environment setup.
- `tauri-scaffold`: Creating files and structures.
- `tauri-app-develop`: Development workflow (dev, build, debug).
- `tauri-app-process`: Process management and exit handling.
- `tauri-app-updater`: Auto-update configuration and API.
- `tauri-mobile`: Android and iOS specific development.

**System Integration**
- `tauri-app-shell`: Spawn sidecars and run system commands.
- `tauri-app-os-info`: Get OS version, arch, and locale.
- `tauri-app-clipboard`: Read/write to system clipboard.
- `tauri-app-dialog`: Native file open/save dialogs and message boxes.
- `tauri-app-notification`: System notifications.
- `tauri-app-global-shortcut`: Register system-wide keyboard shortcuts.
- `tauri-app-autostart`: Launch app on system login.
- `tauri-app-biometric`: TouchID/FaceID authentication.
- `tauri-app-opener`: Open URLs/files in default apps.
- `tauri-app-deep-linking`: Handle custom protocol links (e.g., `myapp://`).

**Data & Networking**
- `tauri-app-http-client`: Rust-based HTTP client (CORS-free).
- `tauri-app-websocket`: WebSocket client.
- `tauri-app-upload`: File upload utility.
- `tauri-app-sql`: SQLite, MySQL, PostgreSQL database access.
- `tauri-app-store`: Simple persistent key-value store.
- `tauri-app-stronghold`: Secure secret management and encryption.
- `tauri-app-file-system`: Read/write files (sandboxed).

**Window & UI**
- `tauri-app-window-menu`: Native application menus and context menus.
- `tauri-app-system-tray`: System tray icon and menu.
- `tauri-app-window-state`: Persist window size/position.
- `tauri-app-positioner`: Tray and window positioning.
- `tauri-app-single-instance`: Prevent multiple app instances.

## Examples and Templates

**Global Examples** (General Architecture)
- `examples/start/`: Introduction and Quick Start.
- `examples/guide/`: Architecture, Frontend/Backend patterns.

**Sub-skill Examples** (Specific Features)
**CRITICAL**: Every sub-skill above has its own local assets.
- `skills/tauri-app-dialog/examples/usage.md`: detailed Dialog plugin usage.
- `skills/tauri-app-sql/examples/usage.md`: detailed SQL plugin usage.
- `...` and so on for all skills.

## Keywords

Tauri, tauri v2, rust, desktop app, mobile app, plugins, capabilities, permissions, system tray, notifications, file system, database, sql, http, websocket, updater, sidecar, ipc, events, commands, window customization
