# Workflow: responsive renderer and DPR cap

## Goal

Keep drawing buffer size in sync with the canvas element and limit device pixel ratio on high-DPI displays.

## Steps

1. Listen to `window` `resize` (or ResizeObserver on the canvas parent).

2. Read `clientWidth` / `clientHeight` of the element hosting the canvas.

3. Call `renderer.setSize(width, height, false)` when the third argument should match CSS pixels (typical for full-window).

4. Set `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))` (adjust cap per project).

5. If using composer or effects that depend on resolution, update passes after resize—see **threejs-postprocessing**.

6. Update projection `camera.aspect` for perspective cameras and `camera.updateProjectionMatrix()`.

This complements **threejs-camera**; do not duplicate XR projection here.
