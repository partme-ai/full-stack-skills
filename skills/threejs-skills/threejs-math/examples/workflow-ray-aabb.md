# Workflow: test Ray against Box3

## Steps

1. Build `THREE.Ray(origin, direction)`; ensure `direction` is normalized if using distance-sensitive APIs.

2. Compute world-space `Box3` for an object: `new THREE.Box3().setFromObject(mesh)`.

3. `const hit = ray.intersectBox(box, targetPoint);` — check return value per [Ray](https://threejs.org/docs/Ray.html).

4. For mesh-accurate picking, prefer `Raycaster` in **threejs-objects** instead of manual triangle tests unless you optimize custom cases.
