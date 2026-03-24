# Commands

**官方文档**: https://v2.tauri.org.cn/start/

## Usage

Commands are the primary way for the frontend to invoke backend logic.

### Typical Steps

1. Define a command in the backend
2. Register it in the Tauri builder
3. Call it from the frontend

### Key Points

- Keep command inputs small and validated
- Return serializable results
