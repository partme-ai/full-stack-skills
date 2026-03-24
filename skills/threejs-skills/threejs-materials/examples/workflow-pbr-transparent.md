# Workflow: PBR mesh with transparency

## Steps

1. Start from `MeshStandardMaterial` with `transparent: true`, `opacity < 1`, or texture alpha.

2. Decide sorting strategy: opaque first, then transparent; or use `alphaTest` for cutouts (foliage).

3. For refractive glass-like look, consider `MeshPhysicalMaterial` with `transmission`—verify thickness and env map (see **threejs-textures** for PMREM).

4. If depth artifacts appear, tune `depthWrite` (often `false` for transparent) and render order.

5. Validate under correct `outputColorSpace` on renderer (**threejs-renderers**).

This file is guidance only—parameter names follow the current [MeshStandardMaterial](https://threejs.org/docs/MeshStandardMaterial.html) page.
