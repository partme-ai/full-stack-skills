---
name: tauri-app-localhost
description: "Serve your Tauri v2 frontend via a localhost server using the localhost plugin for frameworks requiring a server. Use when your frontend framework needs a local HTTP server, separating dev/production localhost behavior, or controlling port exposure."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Serving frontend via localhost in a Tauri app
- Local server exposure and port configuration
- Dev vs production localhost behavior differences

**Trigger phrases include:**
- "localhost", "local server", "localhost plugin", "port", "serve frontend"

## How to use this skill

1. **Install the localhost plugin**:
   ```bash
   cargo add tauri-plugin-localhost
   ```
2. **Register the plugin** with a specific port in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_localhost::Builder::new(3030).build())
   ```
3. **Configure the frontend URL** in `tauri.conf.json` for production:
   ```json
   { "build": { "frontendDist": "../dist" } }
   ```
4. **Bind only to 127.0.0.1** to prevent external access to the local server
5. **Separate dev-mode access** (Vite dev server on port 5173) from production (localhost plugin on a fixed port)
6. **Audit access patterns** to ensure minimal exposure in production builds

## Outputs

- Localhost plugin configuration with fixed port
- Dev vs production server separation
- Security checklist for minimal exposure

## References

- https://v2.tauri.app/plugin/localhost/

## Keywords

tauri localhost, local server, port, serve frontend, dev server
