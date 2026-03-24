# Configuration Template

## Template

```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "{product_name}",
  "version": "{version}",
  "build": {
    "frontendDist": "{frontend_dist}",
    "devUrl": "{dev_url}"
  },
  "app": {
    "withGlobalTauri": false
  },
  "tauri": {
    "windows": [
      {
        "label": "main",
        "title": "{window_title}",
        "width": {window_width},
        "height": {window_height}
      }
    ]
  }
}
```
