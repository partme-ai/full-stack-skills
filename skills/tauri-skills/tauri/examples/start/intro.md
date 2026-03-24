# Introduction

**官方文档**: https://v2.tauri.org.cn/ ，https://v2.tauri.app

## Overview

Tauri 2.0 是一个跨平台应用框架：前端独立（可复用任意 Web 技术栈），后端采用 Rust，深度集成系统能力（可通过 Swift 与 Kotlin 在 iOS/Android 上扩展）。

### Core Capabilities

- Frontend Independent：无需更换既有前端框架（Vue/React/Svelte/…）
- Cross Platform：单一代码库构建 Linux、macOS、Windows、Android、iOS
- Maximum Security：以安全为先，提供权限与隔离控制
- Minimal Size：依赖系统原生 Web 渲染，体积可低至约 600KB
- Native Integration：Rust 逻辑，高性能与更安全的系统访问

### Architecture

- Frontend：Web UI（HTML/CSS/JS），由前端工具链构建与提供 Dev Server
- Backend：Rust 应用逻辑与系统 API 封装，通过命令（IPC）与事件进行交互
- Runtime：原生 WebView + 平台壳，负责窗口与系统集成

### Use Cases

- 桌面与移动端跨平台应用（统一代码库）
- 对安全与体积敏感的客户端产品
- 需要原生系统集成（剪贴板、文件系统、通知、系统托盘、权限等）

### Key Points

- 前端可选任何框架，后端使用 Rust
- Dev 与 Build 流程清晰：devUrl（开发）、frontendDist（生产）
- 强安全、体积小、性能好，覆盖桌面与移动平台
