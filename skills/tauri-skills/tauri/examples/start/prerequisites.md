# Prerequisites

**官方文档**: https://v2.tauri.org.cn/start/

## Requirements

- Node.js v16+
- Rust (stable)
- Platform dependencies

### macOS

```bash
xcode-select --install
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install libwebkit2gtk-4.0-dev build-essential curl wget libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
```

### Windows

- Microsoft Visual Studio C++ Build Tools
- WebView2 runtime

### Verify

```bash
node -v
rustc --version
cargo -V
```

### Key Points

- Install platform dependencies before building
- Verify versions and toolchains
