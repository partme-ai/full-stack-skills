---
name: threejs-objects
description: "three.js scene graph objects: Object3D transforms and hierarchy, Group, Mesh, InstancedMesh, SkinnedMesh, BatchedMesh, LOD, Line/LineLoop/LineSegments, Points, Sprite, Bone, Skeleton, ClippingGroup; interaction via Raycaster, Layers masks, and EventDispatcher patterns. Use when building scene hierarchies, picking objects with Raycaster, or configuring instanced/skinned meshes; for pure vector math use threejs-math; for skeletal clips use threejs-animation."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Parent/child relationships, `position/rotation/scale`, `matrixAutoUpdate`, `updateMatrixWorld`
- Choosing mesh types: static vs instanced vs skinned vs batched LOD
- **Picking**: `Raycaster.setFromCamera`, `intersectObjects`, recursive flag, face/uv results
- **Layers**: selective visibility for cameras/lights/objects

**IMPORTANT: objects vs math**

| Need | Skill |
|------|--------|
| Scene graph + picking | **threejs-objects** |
| Box/ray math only | **threejs-math** |

**Trigger phrases include:**

- "Object3D", "InstancedMesh", "SkinnedMesh", "Raycaster", "layers"
- "父子节点", "射线拾取", "图层"

## How to use this skill

1. **Compose** scenes with `Group` and transforms; minimize deep hierarchies where possible.
2. **Instancing** — set per-instance matrices; understand `count` and frustum culling behavior.
3. **SkinnedMesh** — bind skeleton; clips in **threejs-animation**; skinning material flags in **threejs-materials**.
4. **Picking** — normalize device coords, set ray from camera, filter by layers, validate intersections are sorted by distance before processing.
5. **Events** — `EventDispatcher` on custom objects; patterns only, not DOM frameworks.
6. **Clipping** — `ClippingGroup` usage per docs when user needs sectional cuts.
7. **Dispose** — call `dispose()` on geometries/materials/textures when removing objects permanently.

### Example: Raycaster picking with validation

```javascript
import * as THREE from 'three';

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();

function onPointerMove(event) {
  // Normalize device coordinates (-1 to +1)
  pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
  pointer.y = -(event.clientY / window.innerHeight) * 2 + 1;
}

function pick(camera, scene) {
  raycaster.setFromCamera(pointer, camera);
  const intersections = raycaster.intersectObjects(scene.children, true);

  // Validate: intersections are sorted by distance (nearest first)
  if (intersections.length > 0) {
    console.log('Nearest hit:', intersections[0].object.name,
                'at distance:', intersections[0].distance);
  }
  return intersections;
}
```

See [examples/workflow-raycaster-pick.md](examples/workflow-raycaster-pick.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Core | https://threejs.org/docs/Object3D.html |
| Objects | https://threejs.org/docs/Mesh.html |
| Objects | https://threejs.org/docs/InstancedMesh.html |
| Core | https://threejs.org/docs/Raycaster.html |

## Scope

- **In scope:** Object3D graph, renderable object types, raycasting, layers, dispatcher basics.
- **Out of scope:** Physics engines; XR input mapping (**threejs-webxr**).

## Common pitfalls and best practices

- Forgetting `updateMatrixWorld` before world-space ray tests on moved objects.
- Raycaster without `layers` set picks unintended objects—set masks consistently on camera and objects.
- InstancedMesh raycast hits need per-instance handling—check docs for your version.

## Documentation and version

`Object3D`, mesh types, `Raycaster`, and `Layers` are documented under [Objects](https://threejs.org/docs/#Objects) and [Core](https://threejs.org/docs/Raycaster.html) in [three.js docs](https://threejs.org/docs/). Behavior of picking and layers can shift slightly—link the exact page for the user’s three.js line.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `Object3D`, `Mesh`, `InstancedMesh`, `Raycaster`, or `Layers` as needed.
2. Pair skeletal animation with **threejs-animation** and skinned mesh setup.
3. Route pure linear-algebra questions without a scene graph to **threejs-math**.
4. Route XR input to **threejs-webxr** when sessions/controllers are involved.
5. Mention `dispose()` for geometries/materials when removing objects permanently.

## References

- https://threejs.org/docs/Object3D.html
- https://threejs.org/docs/Raycaster.html
- https://threejs.org/docs/Layers.html
- https://threejs.org/docs/InstancedMesh.html

## Keywords

**English:** object3d, mesh, instancedmesh, skinnedmesh, raycaster, layers, scene graph, three.js

**中文：** 场景图、Object3D、Mesh、实例化、骨骼网格、射线拾取、图层、three.js
