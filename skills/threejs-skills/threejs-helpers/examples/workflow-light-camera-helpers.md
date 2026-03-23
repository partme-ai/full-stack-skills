# Workflow: shadow + camera debug

## Steps

1. `const ch = new THREE.CameraHelper(light.shadow.camera); scene.add(ch);`

2. `const lh = new THREE.DirectionalLightHelper(light, size); scene.add(lh);`

3. Remove helpers once shadow frustum is tuned (**threejs-lights**).

4. Use `SkeletonHelper(boneRoot)` for skinning issues (**threejs-animation** / **threejs-objects**).

Official pages: CameraHelper, DirectionalLightHelper.
