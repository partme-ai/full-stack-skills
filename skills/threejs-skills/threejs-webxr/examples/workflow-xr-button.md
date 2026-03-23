# Workflow: VR entry button

## Steps

1. Ensure site served over HTTPS and `navigator.xr` checked.

2. `document.body.appendChild(VRButton.createButton(renderer));` per [VRButton](https://threejs.org/docs/VRButton.html) for your three version.

3. `renderer.xr.enabled = true;` Use `renderer.setAnimationLoop` callback for render + updates.

4. Handle session end to restore window `resize` behavior if needed.

5. For AR passthrough use `ARButton` instead—see **threejs-webxr** doc map.

Always verify against the official example that matches your three.js revision.
