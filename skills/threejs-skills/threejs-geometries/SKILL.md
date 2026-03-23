---
name: threejs-geometries
description: >-
  three.js geometry authoring: BufferGeometry, typed BufferAttribute and interleaved layouts, InstancedBufferGeometry, primitive Geometries (box/sphere/torus/etc.), ExtrudeGeometry and Shape/Path/Curve from Extras, WireframeGeometry, and addon geometries such as TextGeometry, DecalGeometry, RoundedBoxGeometry.
  Covers merged scope of procedural curves and extrusion formerly split as extras-curves; for animation morph targets see threejs-animation; for merging buffers utilities see official BufferGeometryUtils module in docs Utils addons.
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- Building or modifying `BufferGeometry`, attributes, index buffers, draw ranges
- Instancing via `InstancedBufferAttribute` / `InstancedMesh` geometry side (**threejs-objects** for mesh wrapper)
- Extruding `Shape` along paths, `TubeGeometry`, `LatheGeometry`, `ExtrudeGeometry`
- Text or decal addon geometries

**IMPORTANT: geometries vs math**

- **threejs-geometries** = GPU-ready triangle data.
- **threejs-math** = `Box3`, `Sphere`, `Ray` tests without mesh topology.

**Trigger phrases include:**

- "BufferGeometry", "BufferAttribute", "ExtrudeGeometry", "Shape", "Curve"
- "几何体", "缓冲几何", "挤出", "文字几何"

## How to use this skill

1. Prefer built-in primitives when they fit before custom buffers.
2. For custom meshes: create `BufferGeometry`, set `position`, `normal`, `uv`, optional `index`; compute bounding volumes for culling.
3. For instancing attributes, align divisor/count with `InstancedMesh` patterns in **threejs-objects**.
4. For 2D profiles: build `Shape`/`Path`, extrude or lathe per docs; consult Extras **Curve** family for path sampling.
5. For addon NURBS knots, follow Addons **Curves** pages sparingly—cite docs instead of copying full APIs.
6. Dispose geometries when replacing meshes to avoid leaks.

See [examples/workflow-extrude-shape.md](examples/workflow-extrude-shape.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Core | https://threejs.org/docs/BufferGeometry.html |
| Geometries | https://threejs.org/docs/BoxGeometry.html |
| Extrude | https://threejs.org/docs/ExtrudeGeometry.html |
| Shape | https://threejs.org/docs/Shape.html |

## Scope

- **In scope:** Core geometries, buffer core, curve/shape/extrusion workflows, selected addon geometries.
- **Out of scope:** Physics collision mesh baking; full CAD import pipelines.

## Common pitfalls and best practices

- Missing normals break lighting; compute or import consistently.
- Wrong winding order flips faces—check side/culling.
- Huge attribute counts need LOD or simplification (modifiers in addons—mention only if user asks).

## Documentation and version

Primitives and `BufferGeometry` live under [Geometries](https://threejs.org/docs/#Geometries) and [BufferGeometry](https://threejs.org/docs/BufferGeometry.html) in [three.js docs](https://threejs.org/docs/). Curve, `Shape`, and extrusion APIs appear under **Extras** and **Geometries**—Addons **Curves** / **Geometries** document NURBS and text meshes; link those instead of copying long signatures.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `BufferGeometry`, a primitive, or `ExtrudeGeometry` / `Shape` as appropriate.
2. Point **instancing** usage to **threejs-objects** for `InstancedMesh` patterns.
3. Point morph targets and tracks to **threejs-animation** when deformation is time-driven.
4. Reference `BufferGeometryUtils` (Addons **Utils**) only by name + docs link when merging/splitting.
5. Emphasize `dispose()` when replacing large custom buffers.

## References

- https://threejs.org/docs/#Geometries
- https://threejs.org/docs/BufferGeometry.html
- https://threejs.org/docs/ExtrudeGeometry.html

## Keywords

**English:** buffergeometry, extrude, shape, path, curve, primitives, instancing, three.js

**中文：** 几何体、BufferGeometry、挤出、Shape、曲线、实例化、three.js
