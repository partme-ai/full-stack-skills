# Installation

**官方文档**: https://v2.tauri.org.cn/ ，https://v2.tauri.app

## Prerequisites

- Node.js ≥ 16
- Rust（stable）
- 平台依赖（macOS、Linux、Windows、Android、iOS）

### Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustc --version
cargo -V
```

### Install Tauri CLI（多包管理器）

```bash
# npm
npm install -D @tauri-apps/cli
# yarn
yarn add -D @tauri-apps/cli
# pnpm
pnpm add -D @tauri-apps/cli
# bun
bun add -d @tauri-apps/cli
# cargo
cargo install tauri-cli
```

### Create a Project（多环境）

```bash
# Bash / zsh / fish 可用的在线脚本
sh <(curl https://create.tauri.app/sh)

# npm / yarn / pnpm / bun
npm create tauri-app
yarn create tauri-app
pnpm create tauri-app
bun create tauri-app

# Cargo
cargo tauri init
```

### System Dependencies

**macOS**
```bash
xcode-select --install
```

**Linux（Ubuntu/Debian）**
```bash
sudo apt update
sudo apt install libwebkit2gtk-4.0-dev build-essential curl wget libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
```

**Windows**
- Microsoft Visual Studio C++ Build Tools
- WebView2 runtime

### Key Points

- 先装 Rust，再装 CLI 与平台依赖
- 创建项目可选脚本与多包管理器
- 验证 Node/Rust/CLI 版本与工具链是否可用
