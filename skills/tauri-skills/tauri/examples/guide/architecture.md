# Architecture

**官方文档**: https://v2.tauri.org.cn/start/

## Overview

Tauri uses a dual process model with a web frontend and a Rust backend.

### Components

- Frontend: Web UI, bundled by a frontend toolchain
- Backend: Rust core and commands
- Runtime: WebView + native shell

### Flow

1. UI renders in WebView
2. Frontend calls backend commands
3. Backend returns results or emits events

### Key Points

- Clear separation between UI and system operations
- Commands are the primary interaction channel
