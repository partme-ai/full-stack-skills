---
name: tauri-app-creator
description: "Create new Tauri v2 projects using create-tauri-app with frontend template selection and minimal boot verification. Use when bootstrapping a new Tauri app, choosing between npm/pnpm/bun/cargo installation methods, or verifying first-run dev mode."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Creating a new Tauri v2 app from scratch
- Choosing a create-tauri-app installation method
- Verifying first boot in dev mode

**Trigger phrases include:**
- "create-tauri-app", "new tauri app", "bootstrap", "start new project", "init tauri"

## How to use this skill

1. **Create the project** using the preferred package manager:
   ```bash
   # npm
   npm create tauri-app@latest
   # pnpm
   pnpm create tauri-app
   # cargo
   cargo install create-tauri-app && cargo create-tauri-app
   ```
2. **Select a frontend template** (Vanilla, React, Vue, Svelte, etc.) when prompted
3. **Install dependencies** and start dev mode:
   ```bash
   cd my-tauri-app
   npm install
   npm run tauri dev
   ```
4. **Verify the app boots**: confirm the window opens with the default template UI
5. **Check the project structure**: `src-tauri/` contains Rust code, `src/` contains frontend code, `src-tauri/tauri.conf.json` is the main config
6. **Choose installation method** based on trade-offs: npm/pnpm for JS-centric workflows, cargo for Rust-first setups

## Outputs

- Working Tauri v2 project with chosen frontend framework
- Dev mode verification confirming app window opens
- Project structure overview for next steps

## References

- https://v2.tauri.app/start/create-project/
- https://v2.tauri.app/start/project-structure/

## Keywords

create-tauri-app, tauri v2, new project, scaffold, bootstrap, dev mode
