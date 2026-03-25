---
name: tauri-scaffold
description: "Scaffold a Tauri v2 project with create-tauri-app, configure project structure, and set up static export for frontend frameworks. Use when creating a new project, understanding the Tauri project structure, or configuring SSG/static export for Next.js or SvelteKit."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Scaffolding a new Tauri v2 project
- Understanding the Tauri project structure
- Static export or SSG configuration

**Trigger phrases include:**
- "scaffold", "create-tauri-app", "project structure", "static export", "SSG", "new project"

## How to use this skill

1. **Scaffold with create-tauri-app**:
   ```bash
   npm create tauri-app@latest my-app -- --template react-ts
   ```
2. **Project structure** after scaffolding:
   ```
   my-app/
   ├── src/               # Frontend code
   ├── src-tauri/
   │   ├── src/main.rs    # Rust entry point
   │   ├── Cargo.toml     # Rust dependencies
   │   ├── tauri.conf.json # Tauri configuration
   │   └── capabilities/  # Permission files
   └── package.json       # Frontend dependencies
   ```
3. **Configure static export** for SSR frameworks (Tauri needs static files):
   - Next.js: `output: 'export'` in `next.config.js`
   - SvelteKit: `@sveltejs/adapter-static`
4. **Align output paths** in `tauri.conf.json`:
   ```json
   { "build": { "frontendDist": "../dist" } }
   ```
5. **Verify the scaffold** by running `npm run tauri dev` and confirming the window opens
6. **Add plugins** to `Cargo.toml` as needed for your app features

## Outputs

- Scaffolded Tauri v2 project with chosen frontend
- Project structure overview
- Static export configuration for SSR frameworks

## References

- https://v2.tauri.app/start/create-project/
- https://v2.tauri.app/start/project-structure/

## Keywords

tauri scaffold, create-tauri-app, project structure, static export, SSG
