<div align="center">

# Full Stack Skills

**460+ Agent Skills. 40+ Skills Packages. One Ecosystem.**

*Frontend · Backend · Mobile · DevOps · AI Design Tools — production-ready, independently installable.*

[![Stars](https://img.shields.io/github/stars/partme-ai/full-stack-skills?style=social)](https://github.com/partme-ai/full-stack-skills)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple)](https://agentskills.io)

[简体中文](./README.md)

[Introduction](#-introduction) ·
[Install](#-install) ·
[Skill Catalog](#-skill-catalog) ·
[Architecture](#-architecture) ·
[For Claude Code](#-for-claude-code-users) ·
[Ecosystem](#-ecosystem) ·
[Contributing](#-contributing)

</div>

---

## Introduction

**Full Stack Skills** is the navigation hub for the most comprehensive collection of Agent Skills for AI coding agents. Originally a monorepo with 460+ stars, we've split into **42 independently installable packages** under the [full-stack-skills](https://github.com/full-stack-skills) GitHub organization.

Each package provides specialized knowledge, workflows, and reference materials that AI agents load on-demand — keeping context footprint minimal while delivering deep domain expertise when needed.

> **Migration Complete (June 2026)**: All 454 skills have been migrated to individual repos. This repo is now the catalog & navigation hub. All existing stars and history are preserved here.

### Problems We Solve

| Gap | Problem | Solution |
|-----|---------|----------|
| **Context overflow** | Loading all skills at once exceeds token limits | Per-package on-demand loading via `npx skills add` |
| **Domain expertise** | Generic AI lacks deep framework knowledge | 454 specialized skills across 15 domains |
| **Discoverability** | Skills scattered across repos, hard to find | This catalog — one README, all packages linked |
| **Version lock** | Monorepo forces coordinated releases | Each package independently versioned and published |

---

## Install

Install any skill package with one command:

```bash
npx skills add full-stack-skills/vue-skills      # Vue.js ecosystem (7 skills)
npx skills add full-stack-skills/tauri-skills     # Tauri desktop/mobile (52 skills)
npx skills add full-stack-skills/spring-skills    # Spring Boot ecosystem (7 skills)
```

Or install a specific skill from a package:

```bash
npx skills add full-stack-skills/vue-skills --skill vue3
```

---

## Skill Catalog

### 🌟 Recommended Packages

| Package | ⭐ Stars | Skills | Install |
|---------|:------:|:------:|---------|
| [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 21.4k | 21 | `npx skills add JimLiu/baoyu-skills` |

### Frontend Frameworks (15 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [vue-skills](https://github.com/full-stack-skills/vue-skills) | 7 | `npx skills add full-stack-skills/vue-skills` |
| [react-skills](https://github.com/full-stack-skills/react-skills) | 6 | `npx skills add full-stack-skills/react-skills` |
| [angular-skills](https://github.com/full-stack-skills/angular-skills) | 1 | `npx skills add full-stack-skills/angular-skills` |
| [svelte-skills](https://github.com/full-stack-skills/svelte-skills) | 1 | `npx skills add full-stack-skills/svelte-skills` |

### Frontend UI Libraries (13 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [vue-ui-skills](https://github.com/full-stack-skills/vue-ui-skills) | 4 | `npx skills add full-stack-skills/vue-ui-skills` |
| [antd-skills](https://github.com/full-stack-skills/antd-skills) | 4 | `npx skills add full-stack-skills/antd-skills` |
| [uview-skills](https://github.com/full-stack-skills/uview-skills) | 2 | `npx skills add full-stack-skills/uview-skills` |
| [avue-skills](https://github.com/full-stack-skills/avue-skills) | 3 | `npx skills add full-stack-skills/avue-skills` |

### Build & Tooling (44 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [build-skills](https://github.com/full-stack-skills/build-skills) | 6 | `npx skills add full-stack-skills/build-skills` |
| [nvm-skills](https://github.com/full-stack-skills/nvm-skills) | 15 | `npx skills add full-stack-skills/nvm-skills` |
| [vscode-skills](https://github.com/full-stack-skills/vscode-skills) | 4 | `npx skills add full-stack-skills/vscode-skills` |
| [utility-skills](https://github.com/full-stack-skills/utility-skills) | 7 | `npx skills add full-stack-skills/utility-skills` |
| [dev-utils-skills](https://github.com/full-stack-skills/dev-utils-skills) | 12 | `npx skills add full-stack-skills/dev-utils-skills` |

### Charts & ASCII Art (15 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [chart-skills](https://github.com/full-stack-skills/chart-skills) | 2 | `npx skills add full-stack-skills/chart-skills` |
| [ascii-skills](https://github.com/full-stack-skills/ascii-skills) | 13 | `npx skills add full-stack-skills/ascii-skills` |

### Backend Frameworks (19 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [spring-skills](https://github.com/full-stack-skills/spring-skills) | 7 | `npx skills add full-stack-skills/spring-skills` |
| [nodejs-skills](https://github.com/full-stack-skills/nodejs-skills) | 4 | `npx skills add full-stack-skills/nodejs-skills` |
| [python-skills](https://github.com/full-stack-skills/python-skills) | 3 | `npx skills add full-stack-skills/python-skills` |
| [go-skills](https://github.com/full-stack-skills/go-skills) | 2 | `npx skills add full-stack-skills/go-skills` |
| [java-skills](https://github.com/full-stack-skills/java-skills) | 3 | `npx skills add full-stack-skills/java-skills` |
| [rust-skills](https://github.com/actionbook/rust-skills) | — | `npx skills add actionbook/rust-skills` |
| [zig-skills](https://github.com/full-stack-skills/zig-skills) | 5 | `npx skills add full-stack-skills/zig-skills` |

### Cross-Platform & Desktop (72 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [uniapp-skills](https://github.com/full-stack-skills/uniapp-skills) | 13 | `npx skills add full-stack-skills/uniapp-skills` |
| [flutter-skills](https://github.com/full-stack-skills/flutter-skills) | 2 | `npx skills add full-stack-skills/flutter-skills` |
| [electron-skills](https://github.com/full-stack-skills/electron-skills) | 3 | `npx skills add full-stack-skills/electron-skills` |
| [tauri-skills](https://github.com/full-stack-skills/tauri-skills) | 52 | `npx skills add full-stack-skills/tauri-skills` |
| [mobile-native-skills](https://github.com/full-stack-skills/mobile-native-skills) | 2 | `npx skills add full-stack-skills/mobile-native-skills` |

### 3D & Game (19 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [threejs-skills](https://github.com/full-stack-skills/threejs-skills) | 18 | `npx skills add full-stack-skills/threejs-skills` |
| [cocos-skills](https://github.com/full-stack-skills/cocos-skills) | 1 | `npx skills add full-stack-skills/cocos-skills` |

### Architecture & Design Patterns (35 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [ddd-skills](https://github.com/full-stack-skills/ddd-skills) | 16 | `npx skills add full-stack-skills/ddd-skills` |
| [design-skills](https://github.com/full-stack-skills/design-skills) | 4 | `npx skills add full-stack-skills/design-skills` |
| [drawio-skills](https://github.com/full-stack-skills/drawio-skills) | 2 | `npx skills add full-stack-skills/drawio-skills` |
| [document-skills](https://github.com/full-stack-skills/document-skills) | 8 | `npx skills add full-stack-skills/document-skills` |
| [ocrmypdf-skills](https://github.com/full-stack-skills/ocrmypdf-skills) | 5 | `npx skills add full-stack-skills/ocrmypdf-skills` |

### Database & Storage (5 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [database-skills](https://github.com/full-stack-skills/database-skills) | 5 | `npx skills add full-stack-skills/database-skills` |

### DevOps & Containers (22 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [devops-skills](https://github.com/full-stack-skills/devops-skills) | 6 | `npx skills add full-stack-skills/devops-skills` |
| [docker-skills](https://github.com/full-stack-skills/docker-skills) | 16 | `npx skills add full-stack-skills/docker-skills` |

### Testing (9 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [testing-skills](https://github.com/full-stack-skills/testing-skills) | 9 | `npx skills add full-stack-skills/testing-skills` |

### Spec-Driven Development (28 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [speckit-skills](https://github.com/full-stack-skills/speckit-skills) | 13 | `npx skills add full-stack-skills/speckit-skills` |
| [openspec-skills](https://github.com/full-stack-skills/openspec-skills) | 15 | `npx skills add full-stack-skills/openspec-skills` |

### AI Design Tools — MCP (153 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [stitch-skills](https://github.com/full-stack-skills/stitch-skills) | 28 | `npx skills add full-stack-skills/stitch-skills` |
| [pencil-skills](https://github.com/full-stack-skills/pencil-skills) | 28 | `npx skills add full-stack-skills/pencil-skills` |
| [t2ui-skills](https://github.com/full-stack-skills/t2ui-skills) | 97 | `npx skills add full-stack-skills/t2ui-skills` |

### Teaching & Learning (3 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [teaching-skills](https://github.com/full-stack-skills/teaching-skills) | 3 | `npx skills add full-stack-skills/teaching-skills` |

### Social & Communication (2 skills)

| Package | Skills | Install |
|---------|--------|---------|
| [social-skills](https://github.com/full-stack-skills/social-skills) | 2 | `npx skills add full-stack-skills/social-skills` |

---

## Architecture

### How Skills Work

Each skill follows the [Agent Skills Specification](https://agentskills.io):

```
<package>/
├── skills/
│   ├── <skill-name>/
│   │   ├── SKILL.md          # Required — loaded on-demand by AI agents
│   │   ├── examples/         # Optional — usage examples
│   │   ├── references/       # Optional — detailed reference docs
│   │   └── scripts/          # Optional — executable scripts
│   └── ...
├── .claude-plugin/           # Plugin metadata
└── README.md
```

### On-Demand Loading

Skills use **progressive disclosure**:
1. **At startup**: Only skill names and descriptions are loaded (minimal context)
2. **On demand**: Full `SKILL.md` is loaded when the agent identifies a relevant task
3. **Deep dive**: Reference files are read only when explicitly needed

This keeps context footprint minimal while providing deep expertise when required.

### Package Organization

| Category | Packages | Total Skills |
|----------|----------|--------------|
| Frontend Frameworks | 4 | 15 |
| Frontend UI Libraries | 4 | 13 |
| Build & Tooling | 5 | 44 |
| Charts & ASCII Art | 2 | 15 |
| Backend Frameworks | 5 | 19 |
| Cross-Platform & Desktop | 5 | 72 |
| 3D & Game | 2 | 19 |
| Architecture & Design | 5 | 35 |
| Database & Storage | 1 | 5 |
| DevOps & Containers | 2 | 22 |
| Testing | 1 | 9 |
| Spec-Driven Dev | 2 | 28 |
| AI Design Tools (MCP) | 3 | 153 |
| Teaching & Learning | 1 | 3 |
| Social & Communication | 1 | 2 |
| **Total** | **42** | **454** |

---

## For Claude Code Users

Install individual skill packages:

```bash
npx skills add full-stack-skills/tauri-skills    # 52 Tauri skills
npx skills add full-stack-skills/spring-skills   # 7 Spring Boot skills
npx skills add full-stack-skills/threejs-skills  # 18 Three.js skills
```

Or manually copy skills to your project:

```bash
git clone https://github.com/full-stack-skills/<skill-name>.git
cp -r <skill-name>/skills/* .claude/skills/
```

---

## Ecosystem

| Resource | Link |
|----------|------|
| **All Packages** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |
| **Skills Directory** | [skills.sh](https://skills.sh) |
| **PartMe.AI** | [github.com/partme-ai](https://github.com/partme-ai) |

---

## Contributing

We welcome contributions! Each skill package is an independent repo under the [full-stack-skills](https://github.com/full-stack-skills) organization.

1. Fork the relevant package repo
2. Add your skill following the [Agent Skills Spec](https://agentskills.io)
3. Submit a PR

See [AGENTS.md](AGENTS.md) for detailed guidelines on creating skills.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).

---

<div align="center">

**If this project helps you, please give us a ⭐️**

Made with ❤️ by PartMe.AI Team

</div>
