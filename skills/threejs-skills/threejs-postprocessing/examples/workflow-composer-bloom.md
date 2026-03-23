# Workflow: minimal composer with bloom

## Steps

1. Create `EffectComposer(renderer)`.

2. Add `RenderPass(scene, camera)`.

3. Add `UnrealBloomPass` with strength/radius/threshold per [UnrealBloomPass](https://threejs.org/docs/UnrealBloomPass.html).

4. In animation loop: `composer.render()` instead of `renderer.render` for the final path—or follow the exact pattern from current examples (some versions use `composer.render()` only).

5. On resize: `composer.setSize(width, height)`.

Verify against a known three.js example filename from the official repo for your version—API details shift between releases.
