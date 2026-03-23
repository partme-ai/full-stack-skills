# Backend

**官方文档**: https://v2.tauri.org.cn/start/

## Structure

- src-tauri/tauri.conf.json
- src-tauri/src/main.rs
- src-tauri/Cargo.toml

### Example: Backend Responsibilities

- Define commands for frontend calls
- Access system APIs and filesystem
- Emit events to the frontend

### Key Points

- Rust backend is the system boundary
- Keep business logic in Rust where needed
