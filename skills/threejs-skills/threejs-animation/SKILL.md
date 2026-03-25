---
name: threejs-animation
description: "three.js keyframe animation system: AnimationMixer, AnimationClip, AnimationAction, KeyframeTrack variants, PropertyBinding, PropertyMixer, AnimationObjectGroup, AnimationUtils; mixing and crossfading clips, loop modes, timeScale, weight; addon AnimationClipCreator and CCDIKSolver for procedural rigs. Use when playing glTF clips, blending actions, or authoring procedural tracks; for skin deformation rigging on meshes see threejs-objects; for math interpolants without clips see threejs-math only when not tied to AnimationMixer."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- `AnimationMixer.update`, `AnimationAction` play/pause/stop, crossfade, synchronized clips
- `AnimationClip` from glTF or `AnimationClipCreator`, retargeting caveats at API level
- Keyframe tracks: position/rotation/scale/color tracks, boolean/string tracks where applicable
- IK: `CCDIKSolver` / `CCDIKHelper` from addons

**IMPORTANT: animation vs objects**

- **threejs-animation** = time evaluation and tracks.
- **threejs-objects** = `SkinnedMesh`/`Skeleton` attachment, bind pose—mesh side.

**Trigger phrases include:**

- "AnimationMixer", "AnimationAction", "AnimationClip", "crossFade", "KeyframeTrack"
- "动画混合", "骨骼动画", "剪辑", "淡入淡出"

## How to use this skill

1. **Collect clips** from `gltf.animations` or create with utilities / `AnimationClipCreator`.
2. **Create mixer** bound to root object (often `scene` or rig root).
3. **Create actions** per clip via `mixer.clipAction(clip)`; configure loop mode (`LoopOnce`, `LoopRepeat`, `LoopPingPong`).
4. **Per frame**: compute delta seconds (use `Clock` from core—documented under Core in docs index), call `mixer.update(delta)`.
5. **Blending**: adjust `weight`, `crossFadeTo`, `enabled` flags; watch for additive vs full replacement semantics per docs.
6. **PropertyBinding**: understand path strings targeting bones/morphs—errors often from wrong object names.
7. **IK addon**: attach solver after base animation if using CCD IK from examples.

See [examples/workflow-mixer-action.md](examples/workflow-mixer-action.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Animation (index) | https://threejs.org/docs/#Animation |
| Action | https://threejs.org/docs/AnimationAction.html |
| Mixer | https://threejs.org/docs/AnimationMixer.html |
| Clip | https://threejs.org/docs/AnimationClip.html |
| Tracks | https://threejs.org/docs/KeyframeTrack.html |

More: [references/official-sections.md](references/official-sections.md).

## Scope

- **In scope:** Core Animation module, keyframe pipeline, listed addons for clip creation and IK.
- **Out of scope:** DCC export best practices; physics ragdoll; audio sync (link conceptually only).

## Common pitfalls and best practices

- Forgetting `mixer.update` freezes animation; double `update` per frame speeds up.
- Mixing clips with incompatible hierarchies causes violent pops—validate bind pose.
- Root motion must be handled in game logic if not baked—document explicitly.
- Large track counts cost CPU—strip unused tracks in preprocessing when possible.

## Documentation and version

Behavior of `AnimationMixer`, tracks, and glTF animation import can change between three.js majors. Treat the [Animation](https://threejs.org/docs/#Animation) section of the [docs index](https://threejs.org/docs/) as authoritative for the user’s installed version; when upgrading, check the three.js repository release notes and migration notes for renamed properties or loader output.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Cite the exact class (`AnimationMixer`, `AnimationAction`, etc.) or addon (`CCDIKSolver`) from the official docs.
2. Include at least one `https://threejs.org/docs/...` link (e.g. [AnimationAction](https://threejs.org/docs/AnimationAction.html)).
3. Relate clips to `SkinnedMesh` / skeleton via **threejs-objects** when deformation is involved.
4. Mention `mixer.update(delta)` and a stable time source (`Clock`) explicitly.
5. Reference official **examples** by name only (no full file paste).

## References

- https://threejs.org/docs/#Animation
- https://threejs.org/docs/AnimationMixer.html
- https://threejs.org/docs/AnimationAction.html
- https://threejs.org/docs/PropertyBinding.html

## Keywords

**English:** animationmixer, animationaction, animationclip, keyframetrack, crossfade, skinning, propertybinding, three.js

**中文：** 动画混合、AnimationMixer、AnimationAction、关键帧、骨骼动画、剪辑、淡入淡出、three.js
