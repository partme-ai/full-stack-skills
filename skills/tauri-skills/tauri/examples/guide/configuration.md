# Configuration

**官方文档**: https://v2.tauri.org.cn/reference/config/

## Usage

Tauri uses tauri.conf.json for core settings.

### Example: Minimal Config

```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "MyApp",
  "version": "0.1.0",
  "build": {
    "frontendDist": "../dist",
    "devUrl": "http://localhost:5173"
  },
  "app": {
    "withGlobalTauri": false
  },
  "tauri": {
    "windows": [
      {
        "title": "MyApp",
        "width": 1024,
        "height": 768
      }
    ]
  }
}
```

### Key Points

- Keep schema updated
- Separate devUrl and frontendDist
