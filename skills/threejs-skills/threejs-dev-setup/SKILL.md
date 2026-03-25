---
name: threejs-dev-setup
description: "Bootstrap and toolchain guidance for three.js applications using npm, Vite/Webpack/Rollup, bare ESM import maps, and TypeScript. Covers canonical import paths for three core versus three/addons/ (examples/jsm re-exports), version alignment with threejs.org docs, and fixing module not found for loaders and controls. Use when scaffolding a new 3D project, migrating bundler, or debugging resolution of addons; do not use for rendering API details (see threejs-renderers) or asset loading logic (see threejs-loaders)."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Creating or configuring a new three.js project, Vite/Webpack/Rollup entry, or browser `importmap`
- Installing the `three` package, aligning version with documentation, or TypeScript setup (`@types/three` where applicable)
- Import errors for `three/addons/...`, `examples/jsm`, ESM vs CJS interop, or bare specifier resolution

**IMPORTANT: this skill vs runtime topics**

- **threejs-dev-setup** = install paths, bundler, module graph, and where to import addons from.
- **threejs-renderers** = `WebGLRenderer` / `WebGPURenderer`, canvas, pixel ratio, render loop—after the project loads.
- **threejs-loaders** = `GLTFLoader`, `DRACOLoader`, progress callbacks—after imports resolve.

**Trigger phrases include:**

- "vite three.js", "webpack three", "import map", "three/addons", "cannot find module", "jsm"
- "新建项目", "安装 three", "找不到模块", "ESM", "TypeScript three"

## How to use this skill

1. **Confirm delivery model**: SPA bundler (Vite/Webpack), Node tooling, or static HTML with `importmap`—each affects how `three/addons/` resolves.
2. **Pin `three` version** to a release compatible with the docs the user cites; note that addon paths follow the published package layout.
3. **Show canonical imports**: core from `three`; controls/loaders/effects from `three/addons/...` (mapped to `examples/jsm` in source tree). See [examples/workflow-scaffold.md](examples/workflow-scaffold.md).
4. **Minimal loop**: create renderer + scene + camera + one mesh to verify toolchain works.
5. **TypeScript**: enable `moduleResolution` appropriate for bundler; reference types from `three` package typings; avoid duplicating global script tag patterns unless user targets no-bundler HTML.
6. **On failure**: distinguish missing dependency vs wrong path vs SSR context (no `window`/`document`).
7. **Deepening**: link user to [three.js manual](https://threejs.org/manual/) first chapter after scaffold works.

### Example: Vite + three.js minimal verification

```bash
npm create vite@latest my-3d-app -- --template vanilla && cd my-3d-app
npm install three
```

```javascript
// main.js — canonical imports and minimal render loop
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 3;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

const mesh = new THREE.Mesh(
  new THREE.BoxGeometry(),
  new THREE.MeshStandardMaterial({ color: 0x00ff00 })
);
scene.add(mesh, new THREE.AmbientLight(0xffffff, 0.5));

renderer.setAnimationLoop(() => renderer.render(scene, camera));
```

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Manual (getting started) | https://threejs.org/manual/ |
| Docs index | https://threejs.org/docs/ |
| Package / install context | https://www.npmjs.com/package/three |

## Scope

- **In scope:** npm/install, bundlers, import maps, TypeScript basics for three, addon import paths, minimal verification snippet.
- **Out of scope:** WebGL theory, full render target or post stack (threejs-renderers, threejs-postprocessing), physics, deployment beyond "build runs".

## Common pitfalls and best practices

- Mixing multiple `three` copies in one page breaks singletons; dedupe with bundler aliases.
- Importing addons from deep `node_modules/.../examples/jsm` paths is fragile; prefer package exports `three/addons/...` when available.
- Always match **r152+** style color management docs when giving snippet defaults (output color space)—point to threejs-renderers/textures for details.
- SSR frameworks need dynamic import or client-only components for WebGL context.

## Documentation and version

Toolchain and import paths follow the **three** npm package version the user installs. The [Manual](https://threejs.org/manual/) and [docs](https://threejs.org/docs/) are updated with the library; addon paths (`three/addons/...`) must match the package layout for that release—when in doubt, cite the version number and the exact import line from the current docs.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Name the bundler or runtime (Vite, Webpack, bare ESM, `importmap`) and the intended `three` version.
2. Link https://threejs.org/manual/ and/or https://threejs.org/docs/ for authoritative setup context.
3. Distinguish **threejs-dev-setup** (resolution) from **threejs-renderers** (runtime API) failures.
4. Never assume global script tags unless the user explicitly uses CDN/no-bundler HTML.
5. Recommend deduplicating `three` in `package.json` / lockfile when duplicate singleton issues appear.

## Keywords

**English:** three.js, vite, webpack, rollup, import map, typescript, npm, three/addons, examples jsm, module resolution, scaffold

**中文：** three.js 安装、构建、importmap、模块解析、three/addons、脚手架、Vite、Webpack
