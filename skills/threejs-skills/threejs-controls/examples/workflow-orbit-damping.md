# Workflow: OrbitControls with damping

## Steps

1. `const controls = new OrbitControls(camera, renderer.domElement);`

2. `controls.enableDamping = true; controls.dampingFactor = 0.05;`

3. Each frame before render: `controls.update();`

4. Listen to `controls.addEventListener('change', render)` only if using lazy rendering; continuous apps already render in rAF.

5. On destroy: `controls.dispose()`.

API: https://threejs.org/docs/OrbitControls.html
