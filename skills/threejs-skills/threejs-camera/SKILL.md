---
name: threejs-camera
description: "three.js cameras: Camera base, PerspectiveCamera, OrthographicCamera, CubeCamera, ArrayCamera, StereoCamera; projection matrices, aspect, FOV, orthographic frustum sizes, near/far planes, and dynamic environment maps with CubeCamera. Use when placing views, rendering reflections, or multi-view splits; for XR projections and eye matrices use threejs-webxr; for post pass camera tricks use threejs-postprocessing alongside threejs-renderers."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Switching perspective vs orthographic, `fov`, `aspect`, `zoom`, `near`, `far`
- `CubeCamera` for real-time environment maps or reflections (update rate caveats)
- `ArrayCamera`/`StereoCamera` for multi-view or stereo off-axis projection (non-XR)

**IMPORTANT: camera vs webxr vs post**

| Topic | Skill |
|-------|--------|
| Standard desktop projection | **threejs-camera** |
| XR reference spaces, IPD | **threejs-webxr** |
| Offscreen pass cameras inside composer | **threejs-postprocessing** |

**Trigger phrases include:**

- "PerspectiveCamera", "OrthographicCamera", "CubeCamera", "aspect", "near", "far"
- "透视相机", "正交", "立方体相机"

## How to use this skill

1. **Perspective**: set `aspect` = width/height; update on resize (**threejs-renderers** example workflow).
2. **Orthographic**: define `left/right/top/bottom` in world units for CAD/2.5D views.
3. **Near/far**: balance depth precision vs containing scene bounds; relate to fog (**threejs-scenes**).
4. **CubeCamera**: position at reflection probe; call `update` when scene static enough; use render target outputs per docs.
5. **Stereo/Array**: advanced; cite docs for eye parameters; defer XR to **threejs-webxr**.
6. **Projection matrix**: call `updateProjectionMatrix()` after parameter edits.
7. **Helpers**: `CameraHelper` lives in **threejs-helpers**.

### Example: Resize handler with updateProjectionMatrix

```javascript
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

See [examples/workflow-perspective-resize.md](examples/workflow-perspective-resize.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Cameras (index) | https://threejs.org/docs/#Cameras |
| Cameras | https://threejs.org/docs/Camera.html |
| Perspective | https://threejs.org/docs/PerspectiveCamera.html |
| Orthographic | https://threejs.org/docs/OrthographicCamera.html |
| Cube | https://threejs.org/docs/CubeCamera.html |
| Multi-view | https://threejs.org/docs/ArrayCamera.html |
| Stereo (non-XR) | https://threejs.org/docs/StereoCamera.html |

## Scope

- **In scope:** Core camera classes and parameters; cube/array/stereo overview.
- **Out of scope:** WebXR reference spaces, eye matrices, session lifecycle (**threejs-webxr**); shadow map camera tuning (**threejs-lights**); pass-internal cameras in composer (**threejs-postprocessing**).

## Common pitfalls and best practices

- Wrong `aspect` after resize stretches image—always sync with canvas.
- Too small `near` hurts depth precision in large worlds.
- `CubeCamera` every frame is expensive—throttle for performance.

## Documentation and version

Camera parameters and `CubeCamera` update behavior follow the [Cameras](https://threejs.org/docs/#Cameras) section of [three.js docs](https://threejs.org/docs/). WebXR uses different projection paths—hand off to **threejs-webxr** when the user mentions headsets or reference spaces.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `PerspectiveCamera`, `OrthographicCamera`, or `CubeCamera` as relevant.
2. Pair resize with **threejs-renderers** `setSize` / DPR patterns when relevant.
3. Route `XR`/`WebXRManager` questions to **threejs-webxr** after one-line renderer mention.
4. Mention `updateProjectionMatrix()` after intrinsic changes.
5. Use **threejs-helpers** `CameraHelper` for shadow frustum debug when discussing lights.

## References

- https://threejs.org/docs/#Cameras
- https://threejs.org/docs/PerspectiveCamera.html
- https://threejs.org/docs/CubeCamera.html

## Keywords

**English:** perspectivecamera, orthographiccamera, cubecamera, projection, aspect, near, far, three.js

**中文：** 相机、透视、正交、投影、近裁剪、远裁剪、CubeCamera、three.js
