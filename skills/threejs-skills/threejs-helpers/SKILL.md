---
name: threejs-helpers
description: >-
  Debug and visualization helpers in three.js Core Helpers (AxesHelper, GridHelper, CameraHelper, light helpers, SkeletonHelper, bounding box helpers, PlaneHelper, PolarGridHelper, ArrowHelper) and Addons Helpers (VertexNormalsHelper, VertexTangentsHelper, RectAreaLightHelper, LightProbeHelper, ViewHelper, OctreeHelper, TextureHelper, PositionalAudioHelper, AnimationPathHelper, RapierHelper).
  Use only for development and editor overlays—not for shipping art; for gizmo-style manipulation use threejs-controls.
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Visualizing axes, grids, camera frusta, shadow cameras, light directions
- Showing skeleton bones, bounding boxes, normals/tangents for mesh inspection
- Light probe or rect area visualization via helper classes

**IMPORTANT: helpers vs production meshes**

- Helpers are **debug** objects; do not use as final scene geometry.

**Trigger phrases include:**

- "AxesHelper", "GridHelper", "CameraHelper", "SkeletonHelper", "VertexNormalsHelper"
- "辅助线", "法线显示", "包围盒调试"

## How to use this skill

1. **Attach** helper to the object it describes (e.g., `CameraHelper(light.shadow.camera)`).
2. **Update** when targets move—some helpers need per-frame refresh.
3. **Remove** in production builds or behind debug flags.
4. **Performance**: helpers add draw calls—disable when profiling performance issues.
5. **Addons**: import from `three/addons/helpers/...` paths per **threejs-dev-setup**.

See [examples/workflow-light-camera-helpers.md](examples/workflow-light-camera-helpers.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Helpers | https://threejs.org/docs/AxesHelper.html |
| Helpers | https://threejs.org/docs/GridHelper.html |
| Helpers | https://threejs.org/docs/CameraHelper.html |
| Helpers | https://threejs.org/docs/SkeletonHelper.html |

## Scope

- **In scope:** Core + Addons helpers for visualization.
- **Out of scope:** Production meshes or shipping art (**threejs-geometries**, **threejs-lights**); orbit/transform gizmo behavior (**threejs-controls**); editor UX parity with DCC tools; physics debug beyond helper stubs.

## Common pitfalls and best practices

- Too many helpers obscures view—toggle per subsystem.
- Wrong attachment parent misaligns helper transforms.
- Helpers inherit scene graph transforms—parent under a debug group to batch hide/show.
- Some helpers duplicate geometry cost; strip in production or use `#ifdef DEBUG` style flags.
- `CameraHelper` for shadow cameras must reference `light.shadow.camera`, not the main view camera.

## Documentation and version

Helpers are listed under [Helpers](https://threejs.org/docs/#Helpers) (core) and **Addons → Helpers** in [three.js docs](https://threejs.org/docs/). They are for **debug** only; production meshes and lighting should use real geometry/lights (**threejs-geometries**, **threejs-lights**).

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link the helper class (`AxesHelper`, `CameraHelper`, …) being used.
2. State that helpers are not shipping art—strip or gate behind debug flags.
3. Pair shadow/light helpers with **threejs-lights** tuning workflows.
4. Mention performance cost when many helpers are enabled.
5. Import paths follow **threejs-dev-setup** addon conventions.

## References

- Manual (debug workflow context): https://threejs.org/manual/
- Docs index (Helpers group): https://threejs.org/docs/#Helpers
- Examples: https://threejs.org/docs/DirectionalLightHelper.html

## Keywords

**English:** helper, debug, axes, grid, skeleton, normals, light helper, three.js

**中文：** 辅助、调试、坐标轴、网格、骨架、法线、Helper、three.js
