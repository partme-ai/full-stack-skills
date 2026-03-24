# Technical Implementation Plan: [Project Name]

## 1. Overview
**Goal**: [Brief description of the app]
**Platforms**: [Desktop (Win/Mac/Linux), Mobile (iOS/Android)]

## 2. Skills & Plugins Strategy

| Capability | Tauri Plugin | Usage |
| :--- | :--- | :--- |
| File Storage | `tauri-plugin-fs` | Reading/Writing local files |
| Database | `tauri-plugin-sql` | Local SQLite data |
| Networking | `tauri-plugin-http` | API requests |
| ... | ... | ... |

## 3. Architecture Design

### Frontend
- **Framework**: [Vue/React/Svelte]
- **State Management**: [Pinia/Redux/Context]
- **Router**: [Vue Router/React Router]

### Backend (Rust)
- **State**: `AppState` struct holding [components].
- **Commands**:
    - `get_data`
    - `save_settings`
    - ...

### Orchestration
- **Windows**:
    - `main`: Primary interface.
    - `[other]`: [Purpose]
- **Events**:
    - `[event-name]`: [Trigger] -> [Action]

## 4. Security Scope (Capabilities)

**Identifier**: `default`
**Windows**: `main`
**Permissions**:
- `core:default`
- `fs:allow-read-text-file` (Scope: `$APP_DATA/*`)
- ...

## 5. Implementation Roadmap

1.  [ ] **Setup**: Initialize project and Git.
2.  [ ] **Core**: Implement Rust State and basic Commands.
3.  [ ] **UI**: Build the main layout.
4.  [ ] **Feature A**: Implement [Feature A].
5.  [ ] **Feature B**: Implement [Feature B].
6.  [ ] **Release**: Build and Sign.
