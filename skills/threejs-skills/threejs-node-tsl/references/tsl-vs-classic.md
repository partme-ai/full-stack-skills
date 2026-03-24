# TSL / NodeMaterial vs classic materials

## When to prefer classic (`threejs-materials`)

- You need widely documented PBR with `MeshStandardMaterial` / `MeshPhysicalMaterial`.
- Target is WebGL-only deployments without WebGPU.
- Team maintains GLSL `ShaderMaterial` with known light setups.

## When to prefer TSL / Node path (`threejs-node-tsl`)

- You adopt `WebGPURenderer` and node-based materials in examples.
- You want composable shader pieces without huge GLSL strings.
- You follow new three.js examples that import from node/TSL modules.

## Migration sanity

- Rebuild lighting model expectations: not every classic knob maps 1:1 on day one.
- Keep references to official migration notes in the three.js repository for your version.

## Links

- https://threejs.org/docs/TSL.html
- https://threejs.org/docs/ShaderMaterial.html
