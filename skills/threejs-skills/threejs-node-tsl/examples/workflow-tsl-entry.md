# Workflow: finding the right TSL entry

## Steps

1. Open https://threejs.org/docs/TSL.html and locate the function or node category matching the effect (lighting, texture, math).

2. Cross-check [Nodes](https://threejs.org/docs/#Nodes) for class-style nodes if TSL links to underlying node types.

3. Pair with `WebGPURenderer` setup from **threejs-renderers**.

4. For post effects expressed as nodes, compare with addon `EffectComposer` path in **threejs-postprocessing** and pick one pipeline per project.

Do not duplicate upstream example code here—link to the official example filename instead.
