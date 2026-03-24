# Workflow: positional loop with loader

## Steps

1. Create `AudioListener`, `camera.add(listener)`.

2. `const sound = new THREE.PositionalAudio(listener);`

3. `const loader = new THREE.AudioLoader();` (**threejs-loaders**) `loader.load('file.ogg', buffer => { sound.setBuffer(buffer); sound.setRefDistance(1); sound.play(); });`

4. Add `sound` as child of moving mesh or update position each frame.

5. Connect `AudioAnalyser` only if visualization required—extra CPU.

Browser autoplay: resume context on first click if needed.
