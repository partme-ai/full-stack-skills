---
name: tauri-app-barcode-scanner
description: "Integrate the Tauri v2 barcode scanner plugin for QR code and barcode scanning with camera permissions. Use when adding barcode/QR scanning features, handling camera permissions, or processing scan results on mobile platforms."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Barcode or QR code scanning in a Tauri app
- Camera permissions for scanning features
- Processing scan results or handling scan errors on mobile

**Trigger phrases include:**
- "barcode", "QR code", "scanner", "camera permissions", "scan"

## How to use this skill

1. **Install the barcode scanner plugin**:
   ```bash
   cargo add tauri-plugin-barcode-scanner
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_barcode_scanner::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["barcode-scanner:allow-scan", "barcode-scanner:allow-cancel"] }
   ```
4. **Trigger a scan from the frontend**:
   ```typescript
   import { scan, Format } from '@tauri-apps/plugin-barcode-scanner';
   const result = await scan({ formats: [Format.QRCode, Format.EAN13] });
   console.log('Scanned:', result.content);
   ```
5. **Handle permission denial** gracefully and prompt the user to enable camera access
6. **Provide fallback** when camera is unavailable (e.g., manual code entry)

## Outputs

- Barcode scanner plugin setup with format-specific scanning
- Permission flow with denial handling
- Fallback strategy for unsupported devices

## References

- https://v2.tauri.app/plugin/barcode-scanner/

## Keywords

tauri barcode scanner, qr code, camera, scan, permissions
