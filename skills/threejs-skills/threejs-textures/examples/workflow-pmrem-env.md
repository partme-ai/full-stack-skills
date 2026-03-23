# Workflow: PMREM from an equirectangular texture

## Preconditions

- An equirectangular HDR or suitable env image is already a `Texture` (often via **threejs-loaders**).

## Steps

1. Create `PMREMGenerator(renderer)`.

2. `const envMap = pmremGenerator.fromEquirectangular(equirectTexture).texture;`

3. Assign to scene or materials per your lighting model; intensity via renderer or material properties (**threejs-materials**).

4. `pmremGenerator.dispose()` when done generating; dispose intermediate textures per docs.

5. Dispose `equirectTexture` if no longer needed.

Cross-check current [PMREMGenerator](https://threejs.org/docs/PMREMGenerator.html) for API variants (`fromScene`, etc.).
