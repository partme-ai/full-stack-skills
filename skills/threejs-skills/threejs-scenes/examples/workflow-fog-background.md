# Workflow: fog plus solid background

## Steps

1. `scene.background = new THREE.Color(0x87ceeb);`

2. `scene.fog = new THREE.Fog(0x87ceeb, near, far);` — adjust `near`/`far` relative to world units.

3. Keep `PerspectiveCamera.far` larger than fog `far` or tune both together.

4. Remove fog by setting `scene.fog = null`.

For textured HDR backgrounds, load env via **threejs-loaders** then assign textures per **threejs-textures** / PMREM flow.
