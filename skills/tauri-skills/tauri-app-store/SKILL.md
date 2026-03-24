---
name: tauri-app-store
description: Guidance for Tauri v2 store plugin with key-value persistence and lazy loading.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Lightweight persistent storage / 轻量持久化存储
- Store vs LazyStore decision / Store 与 LazyStore 选择
- Saving app settings to disk / 应用配置落盘保存

**Trigger phrases include:**
- "store", "lazystore", "persistence", "key-value"
- "持久化", "本地存储", "配置保存", "键值"

## How to use this skill

1. Decide between Store and LazyStore based on load timing
2. Define the storage file location and schema
3. Restrict access via capabilities and scope
4. Validate persistence lifecycle and error handling

## Outputs

- Store selection guidance / Store 选择指导
- Persistence plan for app settings / 应用配置持久化方案

## Scope

- Boundary: Store plugin usage only
- Key points: Store vs LazyStore differences

## References

- https://v2.tauri.app/plugin/store/
- https://v2.tauri.app/zh-cn/plugin/store/

## Keywords

tauri store, key-value, persistence, local storage
