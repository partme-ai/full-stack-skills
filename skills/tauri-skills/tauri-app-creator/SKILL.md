---
name: tauri-app-creator
description: Guidance for creating Tauri v2 projects using official create-tauri-app workflows and minimal run verification.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Creating a new Tauri v2 app from scratch / 新建 Tauri v2 应用
- Choosing a create-tauri-app installation method / 选择 create-tauri-app 安装方式
- Minimal run verification for first boot / 最小启动验证流程

**Trigger phrases include:**
- "create-tauri-app", "new tauri app", "bootstrap", "dev mode"
- "创建 Tauri", "新建项目", "初始化", "启动验证"

## How to use this skill

1. Pick the create-tauri-app installation method based on environment
2. Run the creation command and select frontend template
3. Install dependencies and start the Tauri dev mode
4. Confirm the app boots with a minimal verification checklist

## Outputs

- Creation commands by package manager / 按包管理器的创建命令
- Minimal boot verification checklist / 最小启动验证清单

## Scope

- Boundary: Using create-tauri-app to create a Tauri v2 project
- Key points: Explain method trade-offs (npm, pnpm, bun, cargo, curl)

## References

- https://v2.tauri.app/
- https://v2.tauri.app/start/
- https://v2.tauri.app/start/prerequisites/
- https://v2.tauri.app/start/create-project/
- https://v2.tauri.app/start/project-structure/

## Keywords

create-tauri-app, tauri v2, new project, scaffold, dev mode
