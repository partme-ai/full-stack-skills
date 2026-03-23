---
name: tauri-app-http-client
description: Guidance for Tauri v2 http-client plugin with allowlisted requests and secure transport.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- HTTP requests from Rust side / Rust 侧发起 HTTP 请求
- Bypassing WebView restrictions / 绕过 WebView 限制
- Domain allowlists and secure request handling / 域名白名单与安全请求处理

**Trigger phrases include:**
- "http client", "allowlist", "requests", "WebView"
- "HTTP 请求", "白名单", "WebView"

## How to use this skill

1. Define allowed domains, methods, and headers
2. Configure http-client plugin capabilities and scope
3. Implement request timeouts, retries, and error handling
4. Validate sensitive data handling and logging hygiene

## Outputs

- Request policy and allowlist plan / 请求策略与白名单方案
- Security and logging checklist / 安全与日志清单

## Scope

- Boundary: HTTP client plugin usage only
- Key points: Domain allowlists and transport security

## References

- https://v2.tauri.app/plugin/http-client/
- https://v2.tauri.app/zh-cn/plugin/http-client/

## Keywords

tauri http client, requests, allowlist, security
