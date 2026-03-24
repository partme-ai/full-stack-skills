---
name: tauri-app-websocket
description: Guidance for Tauri v2 websocket plugin with Rust-managed connections and lifecycle handling.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- WebSocket connections without WebView limits / 绕开 WebView 限制的 WebSocket
- Connect, message, and disconnect events / 连接、消息与断开事件
- Realtime updates in a Tauri app / Tauri 应用实时更新

**Trigger phrases include:**
- "websocket", "realtime", "connect", "disconnect"
- "WebSocket", "实时", "连接", "断开"

## How to use this skill

1. Define WebSocket endpoints and reconnect strategy
2. Configure plugin capabilities and allowed hosts
3. Handle connect, message, and disconnect lifecycle events
4. Validate error handling and network recovery

## Outputs

- Realtime communication plan / 实时通信方案
- Host allowlist and recovery checklist / 主机白名单与恢复清单

## Scope

- Boundary: WebSocket plugin usage only
- Key points: Lifecycle management and host allowlisting

## References

- https://v2.tauri.app/plugin/websocket/
- https://v2.tauri.app/zh-cn/plugin/websocket/

## Keywords

tauri websocket, realtime, connect, disconnect
