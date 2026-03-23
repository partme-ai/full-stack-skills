---
name: tauri-app-biometric
description: Guidance for Tauri v2 biometric plugin with authentication flow and fallback strategy.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Biometric authentication / 生物识别认证
- Face ID or fingerprint integration / Face ID 或指纹集成
- Fallback when biometric is unavailable / 生物识别不可用时的回退

**Trigger phrases include:**
- "biometric", "Face ID", "fingerprint", "auth"
- "生物识别", "Face ID", "指纹", "认证"

## How to use this skill

1. Define authentication flows and fallback requirements
2. Configure biometric plugin capabilities and permissions
3. Implement auth prompts and error handling
4. Pair biometric auth with secure storage for secrets

## Outputs

- Biometric auth flow plan / 生物识别认证流程方案
- Fallback and recovery checklist / 回退与恢复清单

## Scope

- Boundary: Biometric authentication only
- Key points: Auth flow and fallback strategy

## References

- https://v2.tauri.app/plugin/biometric/
- https://v2.tauri.app/zh-cn/plugin/biometric/

## Keywords

tauri biometric, face id, fingerprint, authentication
