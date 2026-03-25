---
name: threejs-node-tsl
description: "three.js node-based shading: Nodes API surface, NodeMaterial and MeshStandardNodeMaterial-style families, TSL (Three.js Shading Language) entry at TSL.html, WebGPURenderer pairing, and core PostProcessing (class) versus addon EffectComposer at a high level. Use when authoring shaders as graphs, using TSL builtins, compute-oriented nodes, or modern WebGPU pipelines; for classic ShaderMaterial GLSL use threejs-materials; for stock EffectComposer passes use threejs-postprocessing; for WebGLRenderer-only tuning use threejs-renderers."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- `NodeMaterial`, `TSL`, imports from `three/nodes` or WebGPU entry points in docs
- Building materials or post effects from nodes instead of string GLSL
- `WebGPURenderer`, `PostProcessing` (core class) in a node-centric pipeline

**IMPORTANT: node-tsl vs materials vs postprocessing**

| Situation | Skill |
|-----------|--------|
| Standard PBR tuning, no nodes | **threejs-materials** |
| TSL graph, NodeMaterial, WGSL path | **threejs-node-tsl** |
| Classic `EffectComposer` + Pass classes | **threejs-postprocessing** |
| Node post passes listed under Addons TSL in docs | **threejs-node-tsl** + **threejs-postprocessing** awareness |

**Trigger phrases include:**

- "TSL", "NodeMaterial", "three/nodes", "WebGPU", "node builder"
- "节点材质", "着色语言 TSL"

## How to use this skill

1. **Decide path**: WebGPU + nodes vs WebGL + classic materials—do not hybridize blindly.
2. **Anchor docs**: start from [Nodes index](https://threejs.org/docs/#Nodes) and [TSL.html](https://threejs.org/docs/TSL.html); use [NodeMaterial](https://threejs.org/docs/NodeMaterial.html) for material entry.
3. **Progressive disclosure**: keep SKILL.md navigational; long symbol lists live in [references/official-links.md](references/official-links.md) and [references/tsl-vs-classic.md](references/tsl-vs-classic.md); see [examples/workflow-tsl-entry.md](examples/workflow-tsl-entry.md) for navigation habits.
4. **Renderer**: enable `WebGPURenderer` per docs; fall back notes belong in **threejs-renderers**.
5. **Debugging**: use version-stamped examples in three.js repo; avoid copying deprecated import paths.
6. **Post stack**: if user names `PostProcessing` core class vs addon composer, clarify table in **threejs-renderers** / **threejs-postprocessing**.

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Nodes | https://threejs.org/docs/#Nodes |
| TSL | https://threejs.org/docs/TSL.html |
| NodeMaterial | https://threejs.org/docs/NodeMaterial.html |
| WebGPU renderer | https://threejs.org/docs/WebGPURenderer.html |

## Scope

- **In scope:** Nodes/TSL discovery, architecture, renderer pairing, where to look next, migration hints from ShaderMaterial.
- **Out of scope:** Pasting entire TSL symbol tables into SKILL.md; guaranteeing API stability across rapid releases—always cite "current docs".

## Common pitfalls and best practices

- Three.js node APIs evolve quickly—tie answers to a **version** or "current docs".
- Do not confuse **core** `PostProcessing` class with **addons** `EffectComposer`—names collide in conversation.
- WGSL vs GLSL expectations differ; TSL abstracts but limits still apply.
- Keep graphs modular; use references for lookup instead of bloating agent context.

## Documentation and version

The [Nodes](https://threejs.org/docs/#Nodes) index and [TSL](https://threejs.org/docs/TSL.html) page are large and **fast-moving**. Treat https://threejs.org/docs/ as the source of truth for the user’s installed three.js; prefer linking [NodeMaterial](https://threejs.org/docs/NodeMaterial.html) and [WebGPURenderer](https://threejs.org/docs/WebGPURenderer.html) over paraphrasing long symbol lists.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Anchor on [TSL.html](https://threejs.org/docs/TSL.html) and/or `#Nodes` rather than inventing API names.
2. Contrast **threejs-materials** (classic) vs node/TSL path explicitly.
3. Warn that WebGPU + nodes examples may require recent minors—cite version when known.
4. Point to [references/tsl-vs-classic.md](references/tsl-vs-classic.md) and [references/official-links.md](references/official-links.md) for long lookups.
5. Disambiguate core `PostProcessing` vs addon `EffectComposer` (**threejs-postprocessing**).

## References

- https://threejs.org/docs/#Nodes
- https://threejs.org/docs/TSL.html
- https://threejs.org/docs/NodeMaterial.html
- https://threejs.org/docs/WebGPURenderer.html

## Keywords

**English:** tsl, node material, nodes, webgpu, wgsl, three.js shading language, node builder, nodematerial

**中文：** TSL、节点材质、WebGPU、着色语言、NodeMaterial、three.js
