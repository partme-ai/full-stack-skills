---
name: tauri-app-opener
description: Guidance for Tauri v2 opener plugin with safe external links and file handling.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Opening external links or files / 打开外部链接或文件
- Allowlisted protocols or paths / 协议或路径白名单
- Safe opener wrapper / 安全打开封装

**Trigger phrases include:**
- "opener", "open link", "protocol allowlist", "open file"
- "打开链接", "打开文件", "协议白名单", "安全打开"

## How to use this skill

1. Define allowed protocols and target paths
2. Configure opener plugin capabilities and scope
3. Implement a safe open API with strict validation
4. Validate behavior across platforms and error cases

## Outputs

- Opener policy and allowlist plan / 打开策略与白名单方案
- Cross-platform behavior checklist / 跨平台行为清单

## Scope

- Boundary: Opener plugin usage only
- Key points: Protocol and path allowlisting

## References

- https://v2.tauri.app/plugin/opener/
- https://v2.tauri.app/zh-cn/plugin/opener/

## Keywords

tauri opener, external links, allowlist, security
