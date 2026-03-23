# Workflow: play one glTF clip

## Steps

1. After **threejs-loaders** provides `gltf` with `animations` array non-empty.

2. `const mixer = new THREE.AnimationMixer(gltf.scene);`

3. `const clip = gltf.animations[0]; const action = mixer.clipAction(clip); action.play();`

4. In the render loop: `const delta = clock.getDelta(); mixer.update(delta);` then render (**threejs-renderers**).

5. To switch clips, prepare second `clipAction`, then `action.crossFadeTo(nextAction, duration, false)` per docs.

6. Dispose mixer when discarding the rig if your app hot-swaps characters.

## Anchor

- https://threejs.org/docs/AnimationMixer.html
- https://threejs.org/docs/AnimationAction.html
