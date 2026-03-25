---
name: threejs-textures
description: "three.js textures: Texture, DataTexture, CubeTexture, CompressedTexture variants, DepthTexture, VideoTexture, CanvasTexture, 3D/array textures, Source; sampling parameters, mipmaps, anisotropy, wrap/mag/min filters; PMREMGenerator in Extras for environment map prefiltering. Use when configuring GPU texture objects and PMREM; for Draco/KTX2 transcoder file paths use threejs-loaders; for material map slots use threejs-materials; for output color pipeline use threejs-renderers."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- `texture.wrapS` / `wrapT`, `minFilter`, `magFilter`, `generateMipmaps`, `anisotropy`
- `colorSpace` / correct handling of sRGB vs linear data maps
- Creating `DataTexture`, `CubeTexture`, compressed GPU formats, video/canvas driven textures
- `PMREMGenerator` from environment maps for IBL

**IMPORTANT: textures vs loaders**

| Step | Skill |
|------|--------|
| Decode file / HTTP | **threejs-loaders** |
| Configure GPU `Texture` | **threejs-textures** |

**Trigger phrases include:**

- "Texture", "CubeTexture", "PMREM", "colorSpace", "mipmap", "各向异性"
- "环境贴图", "数据纹理", "压缩纹理"

## How to use this skill

1. **Classify** texture dimensionality and format (2D, cube, depth, compressed, data).
2. **Color pipeline**: set `colorSpace` appropriately; normal/roughness maps are non-color data.
3. **Sampling**: choose filters; enable mipmaps when minification occurs; consider max anisotropy.
4. **PMREM**: feed env map through `PMREMGenerator` per docs; assign result to scene/env/intensity paths as required.
5. **Video/canvas**: understand update needs each frame for `VideoTexture` / `CanvasTexture`.
6. **Disposal**: `dispose()` textures when replacing to free GPU memory.
7. **KTX2/Basis**: transcoder wiring belongs in **threejs-loaders** before this step.

See [examples/workflow-pmrem-env.md](examples/workflow-pmrem-env.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Textures | https://threejs.org/docs/Texture.html |
| Cube | https://threejs.org/docs/CubeTexture.html |
| Data | https://threejs.org/docs/DataTexture.html |
| PMREM | https://threejs.org/docs/PMREMGenerator.html |

## Scope

- **In scope:** Core Textures + PMREMGenerator; sampling and color pipeline at texture level.
- **Out of scope:** Loader configuration; post-processing passes that sample buffers (threejs-postprocessing).

## Common pitfalls and best practices

- sRGB albedo in linear workflow without proper colorSpace looks wrong next to renderer output.
- Non-power-of-two textures have mip/wrap limitations unless padded.
- Forgetting texture disposal on hot reload leaks VRAM.

## Documentation and version

Texture classes and `PMREMGenerator` are documented under [Textures](https://threejs.org/docs/#Textures) and [PMREMGenerator](https://threejs.org/docs/PMREMGenerator.html) in [three.js docs](https://threejs.org/docs/). Compressed and KTX2 paths often depend on **threejs-loaders** for transcoder setup before this skill applies.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `Texture`, `DataTexture`, `CubeTexture`, or `PMREMGenerator` as appropriate.
2. Tie `colorSpace` / filtering to **threejs-renderers** output and **threejs-materials** maps.
3. Send Draco/KTX2 **decoder wiring** questions to **threejs-loaders** first.
4. Emphasize `dispose()` when replacing env maps or large atlases.
5. Mention [Global](https://threejs.org/docs/#Global) constants only when wrapping/filter enums matter.

## References

- https://threejs.org/docs/#Textures
- https://threejs.org/docs/Texture.html
- https://threejs.org/docs/PMREMGenerator.html

## Keywords

**English:** texture, cubemap, pmrem, mipmap, colorspace, compressed texture, data texture, three.js

**中文：** 纹理、立方体贴图、PMREM、mipmap、色彩空间、压缩纹理、three.js
