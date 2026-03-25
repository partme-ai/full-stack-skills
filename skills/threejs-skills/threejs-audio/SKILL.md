---
name: threejs-audio
description: "three.js audio spatialization: AudioListener attached to camera rig, Audio and PositionalAudio sources, AudioAnalyser for FFT/time-domain data, and integration with Web Audio API contexts; AudioLoader is referenced from threejs-loaders for file decoding. Use when placing 3D sound, configuring panner parameters, or building audio visualization; not a replacement for full game audio middleware."
---

## When to use this skill

**ALWAYS use this skill when the user mentions:**

- `AudioListener` on `Camera`, `Audio` vs `PositionalAudio`, distance models, refDistance/maxDistance/rolloff
- `AudioAnalyser` for visualization bars/spectrum
- Browser autoplay policies blocking audio start

**IMPORTANT: audio vs loaders**

| Step | Skill |
|------|--------|
| Decode mp3/ogg buffer | **threejs-loaders** (`AudioLoader`) |
| Spatial playback API | **threejs-audio** |

**Trigger phrases include:**

- "PositionalAudio", "AudioListener", "AudioAnalyser", "panner"
- "空间音频", "音量衰减", "频谱"

## How to use this skill

1. **Attach listener** to camera object so head-related audio follows view.
2. **Validate AudioContext state** — check `listener.context.state` before playback; resume if suspended.
3. **Create context** compatible with user gesture unlock patterns in browsers.
4. **PositionalAudio** — set `refDistance`, `maxDistance`, `rolloffFactor`, `distanceModel` per docs.
5. **Load buffer** via `AudioLoader` (**threejs-loaders**), then `positionalAudio.setBuffer`.
6. **Analyser** — connect graph `listener.context.createAnalyser()` pathways per examples; watch performance.
7. **Update** — audio nodes usually need no per-frame update unless following moving sources manually.

### Example: PositionalAudio with context validation

```javascript
import * as THREE from 'three';

const listener = new THREE.AudioListener();
camera.add(listener);

// Validate AudioContext state before attempting playback
function ensureAudioContext() {
  if (listener.context.state === 'suspended') {
    listener.context.resume();
  }
}

// Resume on user gesture (required by browser autoplay policy)
document.addEventListener('click', ensureAudioContext, { once: true });

const sound = new THREE.PositionalAudio(listener);
const loader = new THREE.AudioLoader();
loader.load('sound.mp3', (buffer) => {
  sound.setBuffer(buffer);
  sound.setRefDistance(20);
  sound.setRolloffFactor(1);
});
mesh.add(sound); // Attach to a scene object for spatial positioning
```

See [examples/workflow-positional-audio.md](examples/workflow-positional-audio.md).

## Doc map (official)

| Docs section | Representative links |
|--------------|----------------------|
| Audio | https://threejs.org/docs/AudioListener.html |
| Audio | https://threejs.org/docs/Audio.html |
| Audio | https://threejs.org/docs/PositionalAudio.html |
| Audio | https://threejs.org/docs/AudioAnalyser.html |

Extended list: [references/official-sections.md](references/official-sections.md).

## Scope

- **In scope:** Core Audio classes, spatialization parameters, analyser usage overview.
- **Out of scope:** FMOD/Wwise-style authoring tools.

## Common pitfalls and best practices

- Autoplay restrictions require user interaction to resume AudioContext.
- Too many positional sources hurt CPU—pool or LOD audio.
- Ensure world units match distance model expectations.

## Documentation and version

Audio classes are under [Audio](https://threejs.org/docs/#Audio) in [three.js docs](https://threejs.org/docs/). Decoding buffers uses `AudioLoader`—see **threejs-loaders**. Browser Web Audio policies are external but must be mentioned when `AudioContext` is suspended.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `AudioListener`, `PositionalAudio`, or `AudioAnalyser` as relevant.
2. Delegate file loading of sound buffers to **threejs-loaders** (`AudioLoader`).
3. Note autoplay / user-gesture requirements for resuming context.
4. Relate distance attenuation to world units and **threejs-objects** placement.
5. Avoid promising DAW-level mixing—stay within three.js audio scope.

## References

- https://threejs.org/docs/#Audio
- https://threejs.org/docs/AudioListener.html
- https://threejs.org/docs/PositionalAudio.html

## Keywords

**English:** audio, positional audio, listener, analyser, spatial sound, web audio, three.js

**中文：** 音频、空间音频、AudioListener、PositionalAudio、Web Audio、three.js
