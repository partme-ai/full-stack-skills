---
name: tauri-app-planning
description: "Plan and architect Tauri 2.0 applications from requirements to implementation, including plugin selection, capability design, and state management. Use when starting a new Tauri project, creating a technical roadmap, or mapping features to specific tauri-app-* plugins."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user:**
- Wants to start a new Tauri project and needs a plan
- Asks for a "plan", "roadmap", or "architecture" for a Tauri app
- Needs to map requirements to specific Tauri features/plugins
- Asks about orchestrating windows, state, or events

**Trigger phrases include:**
- "plan tauri app", "architecture", "roadmap", "what plugins do I need", "design"

## How to use this skill

1. **Requirement Analysis**: Clarify what the user wants to build:
   - Target platforms (macOS, Windows, Linux, Android, iOS)
   - Core features (file access, database, notifications, etc.)
   - UI framework preference (React, Vue, Svelte, etc.)
2. **Plugin Selection**: Map features to `tauri-app-*` plugins:
   ```
   File storage    → tauri-app-file-system + tauri-app-store
   Database        → tauri-app-sql (SQLite/Postgres/MySQL)
   Authentication  → tauri-app-biometric + tauri-app-stronghold
   System tray     → tauri-app-system-tray + tauri-app-positioner
   Auto-update     → tauri-app-updater
   ```
3. **Architecture Decision**: Define the app structure:
   - Monolith vs sidecar pattern
   - Multi-window topology
   - State management (Rust-managed vs frontend state)
4. **Security Scope**: Build a capability matrix mapping features to minimal permissions
5. **Execution Plan**: Generate a step-by-step implementation checklist

## Outputs

- Technical design document with stack, plugins, and architecture
- Plugin-to-feature mapping table
- Capability matrix with minimal-privilege permissions
- Ordered implementation checklist

## References

- https://v2.tauri.app/
- https://v2.tauri.app/start/

## Keywords

tauri planning, architecture, roadmap, plugin selection, project design
