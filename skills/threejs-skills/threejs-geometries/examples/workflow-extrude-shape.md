# Workflow: extrude a 2D shape

## Steps

1. Create `THREE.Shape()` and draw with `moveTo` / `lineTo` / `quadraticCurveTo` / `bezierCurveTo` or holes via `shape.holes.push(innerShape)`.

2. Build `ExtrudeGeometry(shape, { depth, bevelEnabled, ... })` per [ExtrudeGeometry](https://threejs.org/docs/ExtrudeGeometry.html).

3. Center/pivot by wrapping in `Object3D` or translating geometry once.

4. Assign `MeshStandardMaterial` (**threejs-materials**) and add lights (**threejs-lights**).

For path-based tubes use `TubeGeometry` + `Curve` subclasses instead.
