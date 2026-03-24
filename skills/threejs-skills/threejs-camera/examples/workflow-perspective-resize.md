# Workflow: perspective camera on window resize

## Steps

1. Store `PerspectiveCamera` reference.

2. On resize: `camera.aspect = width / height; camera.updateProjectionMatrix();`

3. Pair with renderer `setSize` from **threejs-renderers** examples.

4. For orthographic cameras, recompute `left/right/top/bottom` if using fit-to-view logic.

This is the standard pattern used across three.js examples.
