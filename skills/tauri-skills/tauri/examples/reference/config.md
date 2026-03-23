# Config Reference

**官方文档**: https://v2.tauri.org.cn/reference/config/

## Sections

- build
- app
- tauri

### Example: Windows

```json
{
  "tauri": {
    "windows": [
      { "label": "main", "title": "MyApp" }
    ]
  }
}
```

### Key Points

- Validate config with schema
- Keep devUrl separate from production
