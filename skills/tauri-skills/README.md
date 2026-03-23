<div align="center">

# Tauri Skills (Alpha)

**Agent Skills Collection for Full-Stack Tauri Development**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-51-orange)
![Plugins](https://img.shields.io/badge/Plugins-7-brightgreen)

</div>

## 📖 Introduction

**Tauri Skills** is an open-source collection of Agent Skills focused on **Tauri Cross-Platform Application Development**, strictly following the [Agent Skills Specification](https://agentskills.io/). It provides **51 professional skills** organized into **7 plugin categories** by functional area, covering the entire lifecycle of Tauri development from environment setup and application development to system integration, mobile adaptation, and security hardening.

With these skills, full-stack developers can leverage AI assistants like Claude to quickly master Tauri development best practices and efficiently build cross-platform desktop and mobile applications.

This repository participates in the **development stage** (desktop/cross-platform) of the「requirements → deployment」pipeline. For the full pipeline stage mapping and skills ecosystem, see [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) and [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md).

> **⚠️ Note:** This project is currently in Alpha stage and has not been rigorously tested. It is still under self-testing. Feedback and suggestions are welcome.

## What are Skills?

Skills are folders consisting of descriptions, scripts, and resources that Claude dynamically loads as needed to improve performance on specific tasks. Skills are used to teach Claude how to perform specific jobs in a reusable way, such as: initializing a Tauri project, configuring the system tray, handling file system operations, or integrating mobile features.

### More Information

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Specification](https://agentskills.io/)

## About This Repository

**tauri-skills** is a professional skill library for **Tauri Developers**, designed to empower the Tauri ecosystem through AI.

### ✨ Core Features

#### 1. Open Source & Free
- **Apache 2.0 License**: All skills are licensed under Apache 2.0 and are completely open source.
- **Standardized**: Strictly follows the Agent Skills Specification to ensure skill quality and compatibility.

#### 2. Comprehensive Coverage
- **51 Skills**: Covers core framework, system capabilities, network communication, data storage, UI interaction, mobile features, and security mechanisms.
- **7 Plugin Categories**: Organized by functional modules for clear structure and easy retrieval.

#### 3. AI-Empowered
- **Smart Recognition**: Claude automatically invokes relevant skills based on your Tauri development needs.
- **Best Practices**: Built-in official Tauri best practices and code templates.
- **Rich Examples**: Each skill includes at least 5 specific usage scenarios and example codes.

### 🏗️ Project Architecture

**Tauri Skills Organization**:

```
tauri-skills/
├── .claude-plugin/
│   └── marketplace.json          # Plugin marketplace configuration
├── skills/                       # Skills directory
│   ├── tauri-scaffold/           # Individual skill directory
│   │   ├── SKILL.md              # Main skill documentation
│   │   ├── examples/             # Example files
│   │   ├── templates/            # Template files
│   │   └── LICENSE.txt           # License
│   ├── tauri-app-window/
│   └── ...                       # 51 skills
├── README.md                     # Project documentation (English)
└── README_CN.md                  # Project documentation (Chinese)
```

**Plugin Categories**:

| Plugin Category | Skill Count | Description |
|---|---|---|
| tauri-core | 10 | Core framework and project configuration skills |
| tauri-system | 14 | System integration and native capability skills |
| tauri-network | 6 | Network communication and IPC skills |
| tauri-mobile | 6 | Mobile development and hardware access skills |
| tauri-data | 4 | Data persistence and storage skills |
| tauri-ui | 5 | UI interaction and window management skills |
| tauri-security | 6 | Security hardening and permission management skills |

## 📖 Quick Start

### Supported Agents

These skills follow the [Agent Skills](https://github.com/vercel-labs/skills) standard and are supported by:

- **Claude Code**
- **Trae**
- **Cursor**
- **Windsurf**
- **GitHub Copilot**
- **OpenHands**
- **Continue**
- **Roo Code**
- **CodeBuddy**
- And 20+ more agents (Amp, Antigravity, Cline, Codex, etc.)

You can use the `npx skills` CLI tool to manage and install these skills.

### Using in Claude Code

#### 1. Register Marketplace

Run the following command in Claude Code to register this repository as a plugin marketplace:

```bash
/plugin marketplace add https://github.com/partme-ai/tauri-skills.git
```

![add_marketplace.png](./media/add_marketplace.png)

Register Success！

![add_marketplace_success.png](media/add_marketplace_success.png)

Or use the shorthand (if published to the official source):
```bash
/plugin marketplace add partme-ai/tauri-skills
```
Remove the plugin marketplace：
```
/plugin marketplace remove tauri-skills
```

#### 2. Install Plugins

You can install specific plugin categories as needed:

```bash
# Install core development skills
/plugin install tauri-core@tauri-skills

# Install system capability skills
/plugin install tauri-system@tauri-skills

# Install all plugins (Recommended)
/plugin install tauri-core@tauri-skills
/plugin install tauri-system@tauri-skills
/plugin install tauri-network@tauri-skills
/plugin install tauri-mobile@tauri-skills
/plugin install tauri-data@tauri-skills
/plugin install tauri-ui@tauri-skills
/plugin install tauri-security@tauri-skills
```

#### 3. Use Skills

After installing the plugins, simply mention the relevant task in the conversation, and Claude will automatically invoke the skill. For example:
- "Help me create a Tauri project based on Vue and TypeScript"
- "How to configure the system tray in Tauri?"
- "How to read local files in Tauri?"

### Using on Other Platforms

These skills can also be used on other AI platforms that support the Agent Skills specification, such as Cursor, Trae, etc.

## Detailed List of Available Plugins and Skills

This repository contains **51 skills**, categorized by function as follows:

---

### 📦 tauri-core (Core Framework & Configuration)

**Install Command:** `/plugin install tauri-core@tauri-skills`

**Description:** Includes Tauri project initialization, configuration management, build processes, and development tools.

- `tauri-scaffold` - Project scaffold generation
- `tauri-setup` - Environment setup and dependency check
- `tauri-config` - `tauri.conf.json` configuration details
- `tauri-build` - Build and packaging process management
- `tauri-app-develop` - Development mode and debugging tips
- `tauri-app-creator` - Application creation wizard
- `tauri-app-frontend-selection` - Frontend framework selection and integration
- `tauri-app-planning` - Project planning and architecture design
- `tauri-framework-upgrade` - Framework version upgrade guide
- `tauri-concept` - Tauri core concept analysis

---

### 🖥️ tauri-system (System Integration)

**Install Command:** `/plugin install tauri-system@tauri-skills`

**Description:** Provides access to operating system native capabilities, such as file system, clipboard, notifications, and command line interaction.

- `tauri-app-cli` - Command line interface integration
- `tauri-app-clipboard` - Clipboard read/write operations
- `tauri-app-file-system` - File system operations (Fs)
- `tauri-app-process` - Child process management and command execution
- `tauri-app-shell` - Shell command execution
- `tauri-app-os-info` - Operating system information retrieval
- `tauri-app-dialog` - Native dialogs (open/save file, message prompts)
- `tauri-app-notification` - System notification sending
- `tauri-app-global-shortcut` - Global shortcut registration
- `tauri-app-autostart` - Auto-start configuration
- `tauri-app-deep-linking` - Deep link handling
- `tauri-app-single-instance` - Single instance application lock
- `tauri-app-system-tray` - System tray icon and menu
- `tauri-app-window-menu` - Application window menu configuration
- `tauri-app-logging` - Log file management and debugging

---

### 🌐 tauri-network (Network & Communication)

**Install Command:** `/plugin install tauri-network@tauri-skills`

**Description:** Handles network requests, WebSocket communication, and frontend-backend IPC communication.

- `tauri-app-http-client` - HTTP client requests
- `tauri-app-websocket` - WebSocket connection management
- `tauri-app-upload` - File upload functionality
- `tauri-app-localhost` - Localhost integration
- `tauri-ipc` - Frontend-backend Inter-Process Communication (IPC)
- `tauri-app-sidecar-nodejs` - Node.js Sidecar integration

---

### 📱 tauri-mobile (Mobile & Hardware)

**Install Command:** `/plugin install tauri-mobile@tauri-skills`

**Description:** Focuses on mobile features (iOS/Android) and hardware sensor access.

- `tauri-mobile` - Mobile development configuration
- `tauri-app-biometric` - Biometric authentication (Fingerprint/FaceID)
- `tauri-app-barcode-scanner` - Barcode/QR code scanning
- `tauri-app-haptics` - Haptic feedback (Vibration)
- `tauri-app-nfc` - NFC reading/writing
- `tauri-app-geolocation` - Geolocation positioning

---

### 💾 tauri-data (Data & Storage)

**Install Command:** `/plugin install tauri-data@tauri-skills`

**Description:** Provides local data persistence solutions, including SQL databases and key-value stores.

- `tauri-app-store` - Simple key-value store (Store)
- `tauri-app-sql` - SQL database integration (SQLite/MySQL/PostgreSQL)
- `tauri-app-stronghold` - Encrypted storage (Stronghold)
- `tauri-app-persisted-scope` - Persisted scope management

---

### 🎨 tauri-ui (UI & Window)

**Install Command:** `/plugin install tauri-ui@tauri-skills`

**Description:** Manages application windows, splash screens, and UI-related interactions.

- `tauri-window` - Window creation and management
- `tauri-app-splashscreen` - Splash screen
- `tauri-app-window-state` - Window state saving and restoring
- `tauri-app-positioner` - Window positioning tools
- `tauri-app-opener` - Open files/links with default application

---

### 🔒 tauri-security (Security & Permissions)

**Install Command:** `/plugin install tauri-security@tauri-skills`

**Description:** Tauri security mechanism configuration, permission management, and isolation strategies.

- `tauri-security` - Security best practices
- `tauri-framework-security` - Framework security features
- `tauri-app-plugin-permissions` - Plugin permission configuration
- `tauri-app-wasm` - WebAssembly integration security
- `tauri-allowlist` - (Integrated in config) Allowlist configuration
- `tauri-csp` - (Integrated in config) Content Security Policy

---

### Disclaimer

**These skills are for demonstration and educational purposes only.** While some capabilities may be available in Claude, the implementation and behavior you get from Claude may differ from what is shown in these skills. Before relying on them for critical tasks, please test them thoroughly in your own environment.
