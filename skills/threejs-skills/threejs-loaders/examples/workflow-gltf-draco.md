# Workflow: GLTFLoader with DRACOLoader

## Preconditions

- **threejs-dev-setup** resolves `three/addons/loaders/GLTFLoader.js` and `DRACOLoader.js`.
- Draco decoder WASM/js files are hosted at a known URL prefix (often copied to `public/draco/`).

## Steps

1. Create `DRACOLoader()` and `setDecoderPath('/draco/')` (adjust to deployment).

2. Create `GLTFLoader()` and `loader.setDRACOLoader(dracoLoader)`.

3. Call `loader.load('model.glb', onLoad, onProgress, onError)`.

4. In `onLoad`, use `gltf.scene` as root **Object3D**; animations → **threejs-animation**; materials may need color pipeline checks → **threejs-renderers** / **threejs-textures**.

5. Dispose previous scene graphs when swapping models.

## Note

Exact API names follow the current [GLTFLoader](https://threejs.org/docs/GLTFLoader.html) page—verify when upgrading three.js major versions.
