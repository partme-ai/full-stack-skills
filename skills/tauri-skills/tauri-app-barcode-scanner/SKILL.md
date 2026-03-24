---
name: tauri-app-barcode-scanner
description: Guidance for Tauri v2 barcode scanner plugin with permissions and scan lifecycle.
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Barcode or QR code scanning / 条码或二维码扫描
- Camera permissions or scan callbacks / 相机权限或扫描回调
- Platforms with camera capabilities / 具备相机能力的平台

**Trigger phrases include:**
- "barcode", "QR code", "scanner", "camera permissions"
- "扫码", "二维码", "条码", "相机权限"

## How to use this skill

1. Identify supported platforms and camera permissions
2. Configure barcode scanner plugin capabilities
3. Implement scan trigger, result handling, and error flows
4. Validate fallback when camera is unavailable

## Outputs

- Scan flow and permission plan / 扫描流程与权限方案
- Fallback and error-handling checklist / 回退与错误处理清单

## Scope

- Boundary: Barcode scanner plugin usage only
- Key points: Permission handling and result callbacks

## References

- https://v2.tauri.app/plugin/barcode-scanner/
- https://v2.tauri.app/zh-cn/plugin/barcode-scanner/

## Keywords

tauri barcode scanner, qr code, camera, permissions
