# Workflow: pick mesh with Raycaster

## Steps

1. `const raycaster = new THREE.Raycaster(); const pointer = new THREE.Vector2();`

2. On pointer event: `pointer.x = (x / width) * 2 - 1; pointer.y = -(y / height) * 2 + 1;`

3. `raycaster.setFromCamera(pointer, camera);`

4. `const hits = raycaster.intersectObjects(scene.children, true);` — tune recursive/layers.

5. Read `hits[0].object`, `face`, `uv`, `distance` per application.

6. Throttle on pointermove if needed for performance.

Details: https://threejs.org/docs/Raycaster.html
