---
name: tauri-app-websocket
description: "Establish WebSocket connections from the Rust side using the Tauri v2 websocket plugin, bypassing WebView limitations. Use when implementing real-time messaging, managing WebSocket connection lifecycle, or configuring host allowlists for secure connections."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- WebSocket connections in a Tauri app
- Real-time messaging or live updates
- WebSocket connect/disconnect lifecycle

**Trigger phrases include:**
- "websocket", "realtime", "live updates", "ws connection", "socket"

## How to use this skill

1. **Install the websocket plugin**:
   ```bash
   cargo add tauri-plugin-websocket
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_websocket::init())
   ```
3. **Configure capabilities** with allowed hosts in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["websocket:default"] }
   ```
4. **Connect and send messages from the frontend**:
   ```typescript
   import WebSocket from '@tauri-apps/plugin-websocket';
   const ws = await WebSocket.connect('wss://api.example.com/ws');
   ws.addListener((msg) => {
     console.log('Received:', msg.data);
   });
   await ws.send('Hello server!');
   await ws.disconnect();
   ```
5. **Implement reconnection logic** to handle network interruptions gracefully
6. **Restrict allowed hosts** in capabilities to prevent connections to unauthorized servers

## Outputs

- WebSocket plugin setup with connection lifecycle
- Message send/receive pattern with listeners
- Reconnection and error handling strategy

## References

- https://v2.tauri.app/plugin/websocket/

## Keywords

tauri websocket, realtime, live updates, WebSocket connection, socket
