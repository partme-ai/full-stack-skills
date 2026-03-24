---
name: tauri-app-updater
description: Guidance for Tauri v2 updater plugin with OTA updates and signing keys.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- OTA updates for the app / 应用 OTA 更新
- Signing keys or update servers / 签名密钥或更新服务器
- Automatic update checks / 自动更新检查

**Trigger phrases include:**
- "updater", "OTA", "signing key", "update server"
- "更新", "OTA", "签名", "更新服务器"

## How to use this skill

1. Generate and manage updater signing keys
2. Configure update server URLs and metadata
3. Implement update checks and user prompts
4. Validate update flow across platforms

## Outputs

- Update flow plan / 更新流程方案
- Signing and metadata checklist / 签名与元数据清单

## Scope

- Boundary: Updater plugin setup and usage only
- Key points: Signing keys and update metadata

## References

- https://v2.tauri.app/plugin/updater/
- https://v2.tauri.app/zh-cn/plugin/updater/

## Keywords

tauri updater, ota updates, signing, update server
