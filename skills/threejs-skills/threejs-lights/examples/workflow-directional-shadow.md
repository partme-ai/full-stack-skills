# Workflow: directional sun with shadows

## Steps

1. `renderer.shadowMap.enabled = true;` (**threejs-renderers**).

2. Create `DirectionalLight`, `light.castShadow = true`, position and `target`.

3. Tune `light.shadow.mapSize`, `camera` frustum on `light.shadow.camera` for your scene bounds.

4. Mark meshes: `mesh.castShadow` / `receiveShadow` as needed.

5. Adjust `bias` / `normalBias` if acne or peter-panning appears.

6. Use `CameraHelper(light.shadow.camera)` temporarily (**threejs-helpers**).

Official reference: https://threejs.org/docs/DirectionalLight.html
