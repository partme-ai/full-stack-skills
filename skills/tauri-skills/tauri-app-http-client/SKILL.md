---
name: tauri-app-http-client
description: "Make HTTP requests from the Rust side using the Tauri v2 http-client plugin, bypassing WebView CORS restrictions. Use when sending API requests with domain allowlists, configuring secure transport, or handling request timeouts and retries."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- HTTP requests from Tauri (bypassing WebView CORS)
- Domain allowlists for API requests
- Configuring request timeouts, retries, or headers

**Trigger phrases include:**
- "http client", "fetch", "API request", "CORS", "allowlist", "http plugin"

## How to use this skill

1. **Install the http plugin**:
   ```bash
   cargo add tauri-plugin-http
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_http::init())
   ```
3. **Configure scoped access** in `src-tauri/capabilities/default.json`:
   ```json
   {
     "permissions": [
       { "identifier": "http:default", "allow": [{ "url": "https://api.example.com/**" }] }
     ]
   }
   ```
4. **Make requests from the frontend**:
   ```typescript
   import { fetch } from '@tauri-apps/plugin-http';
   const response = await fetch('https://api.example.com/data', {
     method: 'GET',
     headers: { 'Authorization': 'Bearer token' },
     connectTimeout: 10000,
   });
   const data = await response.json();
   ```
5. **Restrict allowed domains** to only the APIs your app needs (principle of least privilege)
6. **Handle errors** with proper timeout, retry, and network failure patterns

## Outputs

- HTTP client setup with domain-scoped permissions
- Request pattern with headers and timeout configuration
- Error handling and retry strategy

## References

- https://v2.tauri.app/plugin/http-client/

## Keywords

tauri http client, fetch, API request, CORS, allowlist, http plugin
