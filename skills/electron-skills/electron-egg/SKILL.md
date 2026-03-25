---
name: electron-egg
description: "Build desktop applications with the Electron EGG framework, covering project setup, main/renderer process communication, window management, plugin system, and build/packaging. Use when the user asks about Electron EGG, electron-egg, needs to create Electron applications with EGG, or work with Electron EGG patterns."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Install and set up Electron EGG in a project
- Create Electron desktop applications
- Use Electron EGG core features
- Configure Electron EGG
- Handle main process and renderer process communication
- Use Electron EGG API methods
- Build and package Electron applications
- Troubleshoot Electron EGG issues

## How to use this skill

This skill is organized to match the Electron EGG official documentation structure (https://www.kaka996.com/, https://www.kaka996.com/pages/987b1c/, https://www.kaka996.com/pages/a99b72/). When working with Electron EGG:

1. **Identify the topic** from the user's request:
   - Installation/安装 → `examples/guide/installation.md`
   - Quick Start/快速开始 → `examples/guide/quick-start.md`
   - Features/功能特性 → `examples/features/`
   - API/API 文档 → `api/`

2. **Load the appropriate example file** from the `examples/` directory:

   **Guide (使用文档)**:
   - `examples/guide/intro.md` - Introduction to Electron EGG
   - `examples/guide/installation.md` - Installation guide
   - `examples/guide/quick-start.md` - Quick start guide
   - `examples/guide/project-structure.md` - Project structure
   - `examples/guide/configuration.md` - Configuration
   - `examples/guide/build.md` - Build and package

   **Features (功能特性)**:
   - `examples/features/main-process.md` - Main process
   - `examples/features/renderer-process.md` - Renderer process
   - `examples/features/ipc-communication.md` - IPC communication
   - `examples/features/window-management.md` - Window management
   - `examples/features/menu.md` - Menu
   - `examples/features/tray.md` - System tray
   - `examples/features/auto-updater.md` - Auto updater
   - `examples/features/plugin-system.md` - Plugin system

3. **Follow the specific instructions** in that example file for syntax, structure, and best practices

   **Important Notes**:
   - Electron EGG is based on Electron and Egg.js
   - Main process and renderer process separation
   - IPC communication between processes
   - Each example file includes key concepts, code examples, and key points

4. **Reference API documentation** in the `api/` directory when needed:
   - `api/main-api.md` - Main process API
   - `api/renderer-api.md` - Renderer process API
   - `api/ipc-api.md` - IPC API
   - `api/window-api.md` - Window API
   - `api/config-api.md` - Configuration API

   **API Files:**
   - `api/main-api.md` - Application class, BrowserWindow, ipcMain, app methods
   - `api/renderer-api.md` - ipcRenderer, contextBridge, DOM APIs
   - `api/ipc-api.md` - IPC communication methods and events
   - `api/window-api.md` - Window creation and management
   - `api/config-api.md` - Configuration options and environment variables

5. **Use templates** from the `templates/` directory:
   - `templates/installation.md` - Installation templates
   - `templates/project-setup.md` - Project setup templates
   - `templates/configuration.md` - Configuration templates

### 1. Understanding Electron EGG

Electron EGG is a desktop application development framework based on Electron and Egg.js, providing a complete development toolchain and best practices.

**Key Concepts**:
- **Electron**: Cross-platform desktop application framework
- **Egg.js**: Node.js enterprise application framework
- **Main Process**: Main application process
- **Renderer Process**: UI rendering process
- **IPC**: Inter-process communication
- **Plugin System**: Extensible plugin architecture

### 2. Installation

**Using npm**:

```bash
npm install electron-egg
```

**Using yarn**:

```bash
yarn add electron-egg
```

**Using pnpm**:

```bash
pnpm add electron-egg
```

### 3. Basic Setup

```javascript
// main.js
const { Application } = require('electron-egg')

const app = new Application({
  // Configuration
})

app.start()
```


### Doc mapping (one-to-one with official documentation)

- `examples/` → https://www.kaka996.com/pages/987b1c/
- `api/` → https://www.kaka996.com/pages/a99b72/

## API Reference (`api/`)

- `api/main-api.md` - Application class, BrowserWindow, ipcMain, lifecycle hooks
- `api/renderer-api.md` - ipcRenderer, contextBridge, DOM APIs
- `api/ipc-api.md` - IPC communication methods and channels
- `api/window-api.md` - Window creation, management, events
- `api/config-api.md` - Configuration options and environment variables

## Best Practices

1. **Separate processes**: Keep main process and renderer process code separate
2. **Use IPC**: Use IPC for inter-process communication
3. **Handle errors**: Properly handle errors in both processes
4. **Security**: Follow Electron security best practices
5. **Performance**: Optimize application performance
6. **Build configuration**: Configure build and package properly
7. **Plugin system**: Use plugin system for extensibility

## Resources

- **Official Documentation**: https://www.kaka996.com/
- **Usage Guide**: https://www.kaka996.com/pages/987b1c/
- **API Documentation**: https://www.kaka996.com/pages/a99b72/
- **Gitee Repository**: https://gitee.com/dromara/electron-egg

## Keywords

Electron EGG, electron-egg, Electron, Egg.js, desktop application, 桌面应用, 主进程, 渲染进程, IPC, 进程间通信, 窗口管理, 菜单, 系统托盘, 自动更新, 插件系统, main process, renderer process, inter-process communication, window management, menu, system tray, auto updater, plugin system
