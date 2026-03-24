---
name: tauri-app-logging
description: Guidance for Tauri v2 logging plugin with levels, filtering, and safe diagnostics.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Unified logging for dev and release builds / 开发与发布统一日志
- Log filtering or persistence / 日志过滤或持久化
- Safe diagnostics without leaking secrets / 安全诊断不泄露敏感信息

**Trigger phrases include:**
- "logging", "log levels", "filtering", "persistence", "diagnostics"
- "日志", "级别", "过滤", "持久化", "诊断"

## How to use this skill

1. Define log levels and redaction rules
2. Configure logging plugin outputs and filters
3. Implement diagnostic toggles for release builds
4. Validate log storage location and rotation policy

## Outputs

- Logging strategy and configuration / 日志策略与配置
- Redaction and rotation checklist / 脱敏与滚动清单

## Scope

- Boundary: Logging plugin usage only
- Key points: Redaction and environment-specific verbosity

## References

- https://v2.tauri.app/plugin/logging/
- https://v2.tauri.app/zh-cn/plugin/logging/

## Keywords

tauri logging, log levels, diagnostics, redaction
