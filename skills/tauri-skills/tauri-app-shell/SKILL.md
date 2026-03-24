---
name: tauri-app-shell
description: Guidance for Tauri v2 shell plugin with secure command execution and open behavior.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Executing commands or opening external links / 执行命令或打开外部链接
- Shell plugin permissions or security risks / Shell 插件权限或安全风险
- Command allowlists and argument control / 命令白名单与参数控制

**Trigger phrases include:**
- "shell", "allow-execute", "allow-open", "command execution"
- "shell", "执行命令", "打开链接", "白名单"

## How to use this skill

1. Identify command and open requirements with allowed targets
2. Configure capabilities for shell allow-execute and allow-open
3. Apply strict allowlist or regex constraints for arguments
4. Validate behavior across platforms and error handling

## Outputs

- Shell capability allowlist plan / Shell 权限白名单方案
- Safe execution and open policy / 安全执行与打开策略

## Scope

- Boundary: Shell plugin capability and usage patterns only
- Key points: High-risk plugin requires strict permission control

## References

- https://v2.tauri.app/plugin/shell/
- https://v2.tauri.app/zh-cn/plugin/shell/

## Keywords

tauri shell, command execution, allow-execute, allow-open, security
