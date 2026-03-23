# Window Template

## Config

```json
{
  "tauri": {
    "windows": [
      { "label": "main", "title": "{title}", "width": {width}, "height": {height} }
    ]
  }
}
```

## Runtime Control

```ts
import { appWindow } from "@tauri-apps/api/window";

await appWindow.setFocus();
await appWindow.setAlwaysOnTop(true);
```
