<div align="center">

# nvm Skills (Alpha)

**Agent Skills Collection for Node Version Manager (nvm)**

![Version](https://img.shields.io/badge/Version-0.0.1-red)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Skills](https://img.shields.io/badge/Skills-15-orange)
![Plugins](https://img.shields.io/badge/Plugins-4-brightgreen)

</div>

## 📖 Introduction

**nvm Skills** is an open-source collection of Agent Skills focused on **Node Version Manager (nvm)** installation, configuration, daily usage, shell integration, Docker/CI, and troubleshooting. It strictly follows the [Agent Skills Specification](https://agentskills.io/) and provides **15 skills** organized into **4 plugin categories**, covering the full nvm lifecycle from install and setup to verification, version switching, .nvmrc, global packages, mirrors, and platform-specific troubleshooting (macOS/Linux).

This repository participates in the **development stage** (base environment) of the「requirements → deployment」pipeline. For full pipeline stage mapping and skills ecosystem, see [full-stack-skills/docs/pipeline-stage-to-skills.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/pipeline-stage-to-skills.md) and [full-stack-skills/docs/skills-ecosystem.md](https://github.com/partme-ai/full-stack-skills/blob/main/docs/skills-ecosystem.md).

> **⚠️ Note:** This project is in Alpha and has not been rigorously tested. Feedback and suggestions are welcome.

## What are Skills?

Skills are folders of descriptions, scripts, and resources that Claude loads on demand to improve performance on specific tasks. They teach Claude to do concrete jobs in a reusable way—for example: installing nvm via curl/wget, configuring shell profiles, verifying installation, switching Node versions, or troubleshooting PATH issues.

### More Information

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Agent Skills Specification](https://agentskills.io/)

## About This Repository

**nvm-skills** is a skill library for developers and AI agents who need to install, configure, and troubleshoot **nvm** (https://github.com/nvm-sh/nvm) in scripts, docs, or automation.

### ✨ Core Features

#### 1. Open Source & Free
- **Apache 2.0 License**: All skills are Apache 2.0 and open source.
- **Standardized**: Follows the Agent Skills Specification for compatibility.

#### 2. Comprehensive Coverage
- **15 Skills**: Install, setup, verify, usage, defaults/.nvmrc, global packages, mirror/auth, shell integration, Docker/CI, uninstall, misc, project meta, and macOS/Linux troubleshooting.
- **4 Plugin Categories**: Core, Advanced, Ops, Troubleshooting.

#### 3. AI-Empowered
- **Smart Recognition**: Claude invokes the right skill for “install nvm”, “fix PATH”, “use .nvmrc”, “nvm in Docker”, etc.
- **Progressive Disclosure**: SKILL.md stays concise; details live in `examples/` and are loaded when needed.

### 🏗️ Project Architecture

```
nvm-skills/
├── .claude-plugin/
│   └── marketplace.json          # Plugin marketplace configuration
├── skills/                       # Skills directory
│   ├── nvm-install/              # Individual skill
│   │   ├── SKILL.md
│   │   ├── examples/
│   │   └── LICENSE.txt
│   ├── nvm-setup/
│   └── ...                       # 15 skills
├── spec/
│   └── agent-skills-spec.md      # Link to agentskills.io
├── template/
│   └── SKILL.md                  # Template for new skills
├── README.md                     # This file (English)
└── README_CN.md                  # Chinese documentation
```

**Plugin Categories**:

| Plugin Category   | Skill Count | Description                                      |
|------------------|-------------|--------------------------------------------------|
| nvm-core         | 5           | Install, setup, verify, basic usage              |
| nvm-advanced     | 4           | Defaults/.nvmrc, global packages, mirror, shell  |
| nvm-ops          | 4           | Docker/CI, uninstall, misc, project meta        |
| nvm-troubleshooting | 2        | macOS and Linux troubleshooting                 |

## 📖 Quick Start

### Supported Agents

These skills follow the [Agent Skills](https://agentskills.io/) standard and are supported by:

- **Claude Code**
- **Cursor**
- **Trae**
- **Windsurf**
- **GitHub Copilot**
- **Continue**
- **CodeBuddy**
- And other agents that support Agent Skills.

### Using in Claude Code

#### 1. Register Marketplace

```bash
/plugin marketplace add https://github.com/partme-ai/nvm-skills.git
```

Or shorthand (if published):

```bash
/plugin marketplace add partme-ai/nvm-skills
```

Remove:

```bash
/plugin marketplace remove nvm-skills
```

#### 2. Install Plugins

```bash
# Core: install, setup, verify, usage
/plugin install nvm-core@nvm-skills

# Advanced: .nvmrc, global packages, mirror, shell integration
/plugin install nvm-advanced@nvm-skills

# Ops: Docker/CI, uninstall, misc
/plugin install nvm-ops@nvm-skills

# Troubleshooting: macOS & Linux
/plugin install nvm-troubleshooting@nvm-skills
```

#### 3. Use Skills

After installing, mention the task in conversation; Claude will invoke the right skill. Examples:

- “How do I install nvm on macOS?”
- “Set up nvm so it loads in my zsh.”
- “Verify nvm is working.”
- “Use .nvmrc in this project.”
- “Install Node in Docker with nvm.”
- “nvm command not found after install.”

## Detailed List of Plugins and Skills

### 📦 nvm-core (Install, Setup, Verify, Usage)

**Install:** `/plugin install nvm-core@nvm-skills`

- `nvm` - Overview and entry point
- `nvm-install` - Install/update nvm (curl/wget, PROFILE, NVM_DIR)
- `nvm-setup` - Shell config and environment (NVM_DIR, nvm.sh, bash/zsh/fish)
- `nvm-verify` - Verify installation (nvm --version, node -v, npm -v, PATH)
- `nvm-usage-basics` - Install/use/list Node versions, LTS, system Node

---

### 🔧 nvm-advanced (Defaults, Global Packages, Mirror, Shell)

**Install:** `/plugin install nvm-advanced@nvm-skills`

- `nvm-defaults-and-nvmrc` - Default Node version and .nvmrc usage
- `nvm-global-packages` - Global packages migration and default-packages
- `nvm-mirror-and-auth` - Node binary mirror and auth headers
- `nvm-shell-integration` - Deeper shell integration (bash/zsh/fish), PATH restore

---

### 🚀 nvm-ops (Docker, CI, Uninstall, Misc)

**Install:** `/plugin install nvm-ops@nvm-skills`

- `nvm-docker-ci` - nvm in Docker and CI/CD (BASH_ENV, ENTRYPOINT)
- `nvm-uninstall` - Uninstall and clean (NVM_DIR, profile removal)
- `nvm-misc` - Colors, Ansible, tests, and other topics
- `nvm-project-meta` - Project support, license, maintainers

---

### 🔍 nvm-troubleshooting (macOS & Linux)

**Install:** `/plugin install nvm-troubleshooting@nvm-skills`

- `nvm-troubleshooting-macos` - macOS issues (profile, permissions, PATH)
- `nvm-troubleshooting-linux` - Linux issues (distro differences, PATH)

---

### Disclaimer

**These skills are for demonstration and education.** Behavior in your environment may differ. Test before relying on them for critical tasks.
