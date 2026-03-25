---
name: threejs-controls
description: "Addon camera and object manipulation controls: OrbitControls, MapControls, FlyControls, FirstPersonControls, TrackballControls, ArcballControls, DragControls, PointerLockControls, TransformControls; damping, target focal point, and integration with the animation loop. Use for editor-style navigation and gizmos—not a full game character controller stack; pair with Raycaster selection patterns in threejs-objects when transforming selections."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Orbiting/panning/dolly around a target, inertia/damping, min/max distance/polar angles
- Map-like pan (MapControls) or flying (FlyControls)
- Transform gizmo translate/rotate/scale with `TransformControls`
- Dragging objects in plane (DragControls), pointer lock FPS (PointerLockControls)

**IMPORTANT: controls vs webxr**

| Context | Skill |
|---------|--------|
| Desktop/browser camera nav | **threejs-controls** |
| XR controller poses | **threejs-webxr** |

**Trigger phrases include:**

- "OrbitControls", "TransformControls", "MapControls", "PointerLockControls"
- "轨道", "变换控制器", "漫游"

## How to use this skill

1. **Import** from addons path (**threejs-dev-setup**).
2. **Construct** with `(camera, domElement)`; for `TransformControls` also attach to renderer events.
3. **Animation loop**: when `enableDamping`, call `controls.update()` each frame.
4. **TransformControls**: wire `dragging-changed` to disable Orbit temporarily; sync with selection from **threejs-objects**.
5. **Constraints**: set min/max distance/angles to avoid flipping or underground views.
6. **Dispose**: `controls.dispose()` when tearing down.

### Example: OrbitControls with damping

```javascript
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.minDistance = 2;
controls.maxDistance = 50;

// Must call update() each frame when damping is enabled
function animate() {
  controls.update();
  renderer.render(scene, camera);
}
renderer.setAnimationLoop(animate);
```

See [examples/workflow-orbit-damping.md](examples/workflow-orbit-damping.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Controls | https://threejs.org/docs/OrbitControls.html |
| Controls | https://threejs.org/docs/TransformControls.html |
| Controls | https://threejs.org/docs/MapControls.html |
| Controls (index) | https://threejs.org/docs/#Controls |

## Scope

- **In scope:** Official addons controls usage patterns.
- **Out of scope:** Full physics character motor; mobile gesture frameworks.

## Common pitfalls and best practices

- Forgetting `update()` with damping enabled causes drift never settling.
- TransformControls fighting with Orbit—pause one while using the other.
- Pointer lock requires user gesture and exit handling.

## Documentation and version

Controls are under [Controls](https://threejs.org/docs/#Controls) (Addons) in [three.js docs](https://threejs.org/docs/). API details (`enableDamping`, events) evolve—link `OrbitControls` / `TransformControls` pages for the user’s three.js version.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link the specific controls class from the docs.
2. State `controls.update()` when damping is on, every frame.
3. Coordinate `TransformControls` with selection / **threejs-objects** raycasting.
4. Separate desktop navigation from **threejs-webxr** locomotion.
5. Call `dispose()` on controls when unmounting canvas.

## References

- https://threejs.org/docs/#Controls
- https://threejs.org/docs/OrbitControls.html
- https://threejs.org/docs/TransformControls.html

## Keywords

**English:** orbitcontrols, transformcontrols, mapcontrols, damping, camera controls, three.js

**中文：** OrbitControls、轨道、TransformControls、变换控制器、阻尼、three.js
