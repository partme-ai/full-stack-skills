---
name: threejs-postprocessing
description: "Addon screen-space post-processing for three.js using EffectComposer, Pass base class, RenderPass, and stock passes such as UnrealBloomPass, SSAOPass, SSRPass, BokehPass, OutlinePass, FXAAPass/SMAAPass, TAARenderPass, and ShaderPass; references the Shaders addon group for underlying shader modules. Use when building composer chains for bloom, SSAO, or other screen-space effects; not for basic renderer tone mapping alone (threejs-renderers)."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- `EffectComposer`, `RenderPass`, stacking passes, resize of composer
- Bloom, SSAO, SSR, DOF, outline, glitch, film grain, TAA—**addon** pass names
- `ShaderPass` with shader modules from Addons **Shaders** group

**IMPORTANT: postprocessing vs renderers vs node-tsl**

| Pipeline | Skill |
|----------|--------|
| Classic composer + passes | **threejs-postprocessing** |
| Renderer output color/tone only | **threejs-renderers** |
| Node/TSL post nodes | **threejs-node-tsl** |

**Trigger phrases include:**

- "EffectComposer", "RenderPass", "UnrealBloomPass", "SSAOPass", "后期"
- "泛光", "环境光遮蔽", "描边"

## How to use this skill

1. **Chain** — `RenderPass` → effect passes → output; ensure size matches renderer and DPR changes.
2. **Resize** — call `composer.setSize` alongside renderer resize workflows.
3. **Half-float** — many passes expect appropriate render target types; cite docs for your version.
4. **Performance** — each pass has cost; profile with `renderer.info` to check draw calls and triangles.
5. **Validate output** — render a simple test scene through the composer first to verify passes work before adding complexity.
6. **Shader modules** — link Addons **Shaders** list instead of inlining huge GLSL in SKILL.
7. **Output** — final pass should align color management with renderer (**threejs-renderers**).
8. **Contrast** — mention core `PostProcessing` class separately to avoid name collision confusion.

### Example: EffectComposer with bloom and debugging

```javascript
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));

const bloomPass = new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5, // strength
  0.4, // radius
  0.85 // threshold
);
composer.addPass(bloomPass);

// Resize handler — must match renderer size
window.addEventListener('resize', () => {
  renderer.setSize(window.innerWidth, window.innerHeight);
  composer.setSize(window.innerWidth, window.innerHeight);
});

// Render loop: use composer.render() instead of renderer.render()
function animate() {
  composer.render();
}
renderer.setAnimationLoop(animate);
```

See [examples/workflow-composer-bloom.md](examples/workflow-composer-bloom.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Postprocessing | https://threejs.org/docs/EffectComposer.html |
| Postprocessing | https://threejs.org/docs/RenderPass.html |
| Postprocessing | https://threejs.org/docs/UnrealBloomPass.html |
| Shaders (addon modules) | https://threejs.org/docs/module-CopyShader.html |

## Scope

- **In scope:** Addon postprocessing passes and composer wiring; pointers to shader modules.
- **Out of scope:** Custom full-screen pipeline design outside three docs; engine-level frame graphs.

## Common pitfalls and best practices

- Forgetting composer resize produces smeared or low-res effects.
- Pass order matters—bloom often after main scene pass, outline may need masks.
- Some passes need depth—ensure depth buffer availability per pass docs.

## Documentation and version

Addon passes live under [Postprocessing](https://threejs.org/docs/#Postprocessing) and **Shaders** modules in [three.js docs](https://threejs.org/docs/). Pass constructors and required buffers change across versions—link the specific pass page (e.g. `UnrealBloomPass`) rather than guessing uniform names.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `EffectComposer`, `RenderPass`, or the named pass (`SSAOPass`, …).
2. Contrast **addon** composer stack with core `PostProcessing` + **threejs-node-tsl** when users mix terms.
3. Require `setSize` on composer when **threejs-renderers** resizes.
4. Point to **Shaders** group for raw shader modules used by `ShaderPass`.
5. Warn about VR frame-time when stacking heavy passes (**threejs-webxr**).

## References

- https://threejs.org/docs/#Postprocessing
- https://threejs.org/docs/EffectComposer.html
- https://threejs.org/docs/RenderPass.html

## Keywords

**English:** effectcomposer, renderpass, bloom, ssao, ssr, outline, postprocessing, three.js

**中文：** 后期、EffectComposer、泛光、SSAO、SSR、屏幕空间、three.js
