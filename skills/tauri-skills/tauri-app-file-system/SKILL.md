---
name: tauri-app-file-system
description: Guidance for Tauri v2 file-system plugin with scoped access and safe file operations.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Reading or writing local files / 读写本地文件
- Safe directory scope configuration / 安全目录 Scope 配置
- Import or export file workflows / 文件导入导出流程

**Trigger phrases include:**
- "file system", "file access", "scope", "read", "write"
- "文件系统", "文件访问", "Scope", "读写"

## How to use this skill

1. Define the minimal directories and file patterns to access
2. Configure file-system plugin scope and capabilities
3. Implement file selection, read, and write flows
4. Validate access boundaries and error handling

## Outputs

- File access scope plan / 文件访问 Scope 方案
- Import/export flow checklist / 导入导出流程清单

## Scope

- Boundary: File-system plugin usage only
- Key points: Scope restrictions for safe access

## References

- https://v2.tauri.app/plugin/file-system/
- https://v2.tauri.app/zh-cn/plugin/file-system/

## Keywords

tauri file system, scope, read write, file access
