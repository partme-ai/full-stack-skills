# Workflow: minimal scaffold (toolchain check)

Use after `three` is installed and the bundler resolves `three` and `three/addons/...`.

## Steps

1. Import core and one addon (e.g. `OrbitControls`) using your bundler’s supported syntax.

```javascript
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
```

2. Create `WebGLRenderer`, append `domElement`, size to canvas container.

3. Create `Scene`, `PerspectiveCamera`, add a `Mesh` with `BoxGeometry` + `MeshStandardMaterial`.

4. Instantiate `OrbitControls(camera, renderer.domElement)` and drive `requestAnimationFrame` calling `controls.update()` then `renderer.render(scene, camera)`.

5. If this runs without module errors, **threejs-dev-setup** is satisfied; tune color space and lighting via **threejs-renderers** and **threejs-lights**.

## Official examples (reference only)

Browse live examples under the three.js repository `examples/`—do not paste entire files; pick patterns matching your bundler.
