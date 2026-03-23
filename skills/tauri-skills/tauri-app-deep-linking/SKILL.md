---
name: tauri-app-deep-linking
description: Guidance for Tauri v2 deep-linking plugin with URL schemes and safe routing.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Deep links or custom URL schemes / 深链或自定义 URL Scheme
- Routing external URLs to the app / 外部 URL 路由到应用
- Secure handling for external input / 外部输入安全处理

**Trigger phrases include:**
- "deep link", "url scheme", "app link", "routing"
- "深链", "URL Scheme", "应用链接", "路由"

## How to use this skill

1. Define supported schemes and link patterns
2. Configure deep-linking plugin and OS registration
3. Validate and sanitize all external link payloads
4. Route parameters to frontend with single-instance support

## Outputs

- Deep-linking registration and routing plan / 深链注册与路由方案
- Input validation checklist / 输入校验清单

## Scope

- Boundary: Deep-linking registration and handling
- Key points: Input validation and single-instance integration

## References

- https://v2.tauri.app/plugin/deep-linking/
- https://v2.tauri.app/zh-cn/plugin/deep-linking/

## Keywords

tauri deep linking, url scheme, routing, security
