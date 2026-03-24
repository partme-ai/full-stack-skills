# Project Todo List

- [ ] **Phase 1: Initialization**
    - [ ] Run `npm create tauri-app@latest`
    - [ ] Configure `tauri.conf.json` (Bundle ID, Icons)
    - [ ] Initialize Git repository

- [ ] **Phase 2: Core Plugins Setup**
    - [ ] Add Plugin: `npm run tauri add [plugin]`
    - [ ] Register Plugin in `lib.rs`
    - [ ] Configure Capabilities in `capabilities/default.json`

- [ ] **Phase 3: Backend Logic (Rust)**
    - [ ] Define `AppState` struct
    - [ ] Implement Commands
    - [ ] Register Commands in `lib.rs`

- [ ] **Phase 4: Frontend Implementation**
    - [ ] Install JS dependencies
    - [ ] Build UI Components
    - [ ] Integrate Tauri APIs (`invoke`, `emit`)

- [ ] **Phase 5: Testing & Build**
    - [ ] Test on Desktop
    - [ ] Test on Mobile (if applicable)
    - [ ] Build Production Release
