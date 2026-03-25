---
name: tauri-app-upload
description: "Upload files from the local filesystem using the Tauri v2 upload plugin with progress reporting and custom headers. Use when uploading large files with progress callbacks, configuring custom request headers, or implementing retry logic for reliable transfers."
license: Complete terms in LICENSE.txt
---


## When to use this skill

**ALWAYS use this skill when the user mentions:**
- Uploading files from desktop or mobile
- Progress tracking during file upload
- Custom headers or retry logic for uploads

**Trigger phrases include:**
- "upload", "file upload", "upload progress", "upload headers", "file transfer"

## How to use this skill

1. **Install the upload plugin**:
   ```bash
   cargo add tauri-plugin-upload
   ```
2. **Register the plugin** in your Tauri builder:
   ```rust
   tauri::Builder::default()
       .plugin(tauri_plugin_upload::init())
   ```
3. **Configure capabilities** in `src-tauri/capabilities/default.json`:
   ```json
   { "permissions": ["upload:allow-upload"] }
   ```
4. **Upload a file with progress from the frontend**:
   ```typescript
   import { upload } from '@tauri-apps/plugin-upload';
   await upload('https://api.example.com/upload', '/path/to/file.zip', (progress, total) => {
     console.log(`Uploaded ${progress} of ${total} bytes`);
   }, { 'Authorization': 'Bearer token' });
   ```
5. **Implement retry logic** for large file uploads that may fail due to network interruptions
6. **Combine with dialog plugin** to let users select files before uploading

## Outputs

- Upload plugin setup with progress callbacks
- File transfer pattern with custom headers
- Retry and error handling strategy

## References

- https://v2.tauri.app/plugin/upload/

## Keywords

tauri upload, file upload, progress, transfer, custom headers, retry
