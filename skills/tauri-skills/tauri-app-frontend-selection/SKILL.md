---
name: tauri-app-frontend-selection
description: "Select and configure a frontend framework for Tauri v2 with static export compatibility. Use when choosing between Vite, Next.js, Nuxt, SvelteKit, or other frameworks, configuring SSG/static export, or aligning output paths with Tauri asset loading."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Frontend framework selection for a Tauri v2 app
- SSG or static export configuration for Tauri
- Vite vs SSR framework decisions

**Trigger phrases include:**
- "frontend framework", "Vite", "Next.js", "Nuxt", "SvelteKit", "SSG", "static export"

## How to use this skill

1. **Default to Vite** for most Tauri apps (best DX, no SSR complexity):
   ```bash
   npm create tauri-app@latest -- --template react-ts  # or vue-ts, svelte-ts
   ```
2. **For Next.js**, enable static export in `next.config.js`:
   ```javascript
   module.exports = { output: 'export', images: { unoptimized: true } };
   ```
3. **For SvelteKit**, configure static adapter:
   ```javascript
   import adapter from '@sveltejs/adapter-static';
   export default { kit: { adapter: adapter({ fallback: 'index.html' }) } };
   ```
4. **Align output paths** in `tauri.conf.json` with the framework's build output:
   ```json
   { "build": { "frontendDist": "../out" } }
   ```
5. **Avoid SSR frameworks** unless you have a specific server-side requirement; Tauri loads local static files
6. **Verify** the build output contains an `index.html` and all assets load correctly in Tauri

## Outputs

- Framework recommendation with rationale (Vite default, SSG alternatives)
- Static export configuration for chosen framework
- Output path alignment in tauri.conf.json

## References

- https://v2.tauri.app/start/frontend/
- https://v2.tauri.app/start/frontend/nextjs/
- https://v2.tauri.app/start/frontend/sveltekit/

## Keywords

tauri frontend, vite, next.js, nuxt, sveltekit, ssg, static export
