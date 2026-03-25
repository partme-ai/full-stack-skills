---
name: tauri-concept
description: "Explain Tauri v2 architecture concepts including the process model, IPC isolation, and brownfield integration patterns. Use when understanding how Tauri works internally, choosing between isolation and brownfield modes, or making architecture decisions before implementation."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- How Tauri works internally or its architecture
- Process model (core process vs WebView process)
- Isolation mode vs brownfield integration

**Trigger phrases include:**
- "architecture", "process model", "isolation", "brownfield", "how tauri works"

## How to use this skill

1. **Explain the process model**: Tauri runs two processes:
   - **Core Process** (Rust): Manages app lifecycle, system APIs, plugins
   - **WebView Process**: Renders the frontend UI, communicates via IPC
2. **Describe IPC communication**:
   ```
   Frontend (JS) --invoke()--> Core (Rust) --return--> Frontend (JS)
   Core (Rust) --emit()--> Frontend (JS)  // events
   ```
3. **Explain isolation mode** (default in v2): Frontend code runs in a sandboxed iframe that validates all IPC messages through a crypto-signed script
4. **Explain brownfield mode**: Skips the isolation iframe for existing web apps being ported to Tauri (less secure but simpler migration)
5. **Map to architecture decisions**:
   - Security-critical apps should always use isolation mode
   - Brownfield is acceptable for internal tools with trusted frontend code
6. **Explain app size**: Tauri apps are small (typically 2-10MB) because they use the system WebView instead of bundling Chromium

## Outputs

- Process model overview (core + WebView)
- IPC communication patterns
- Isolation vs brownfield decision guidance

## References

- https://v2.tauri.app/concept/architecture/
- https://v2.tauri.app/concept/process-model/
- https://v2.tauri.app/concept/inter-process-communication/isolation/

## Keywords

tauri architecture, process model, IPC, isolation, brownfield, how tauri works
