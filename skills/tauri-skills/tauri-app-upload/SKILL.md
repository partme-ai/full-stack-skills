---
name: tauri-app-upload
description: Guidance for Tauri v2 upload plugin with file transfer, progress reporting, and headers.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Uploading large files from desktop or mobile / 桌面或移动端的大文件上传
- Progress callbacks or custom headers / 进度回调或自定义头
- Reliable file transfer from local disk / 本地磁盘可靠文件传输

**Trigger phrases include:**
- "upload", "progress", "headers", "retry"
- "上传", "进度", "请求头", "重试"

## How to use this skill

1. Define upload endpoints and file selection flow
2. Configure upload plugin capabilities and scope
3. Implement progress callbacks and error handling
4. Validate performance and retries for large files

## Outputs

- Upload flow and retry plan / 上传流程与重试方案
- Permission and performance checklist / 权限与性能清单

## Scope

- Boundary: Upload plugin usage only
- Key points: Progress handling and custom headers

## References

- https://v2.tauri.app/plugin/upload/
- https://v2.tauri.app/zh-cn/plugin/upload/

## Keywords

tauri upload, file transfer, progress, headers
