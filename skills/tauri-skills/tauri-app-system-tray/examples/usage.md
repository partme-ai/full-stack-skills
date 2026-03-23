# Usage: tauri-app-system-tray

This document provides at least 5 usage examples for the **tauri-app-system-tray** skill.

## Example 1: Initialize App System Tray

```typescript
// Example initialization for App System Tray
import { init } from 'tauri-plugin-system-tray';

await init();
```

## Example 2: Basic Usage of App System Tray

```typescript
// Basic operation
const result = await invoke('plugin:system-tray|do_something');
console.log(result);
```

## Example 3: Configure App System Tray Settings

```typescript
// Update tauri.conf.json
{
  "plugins": {
    "system-tray": {
      "enabled": true
    }
  }
}
```

## Example 4: Handle App System Tray Errors

```typescript
try {
  await performAction();
} catch (error) {
  console.error('App System Tray Error:', error);
}
```

## Example 5: Advanced App System Tray Integration

```typescript
// Combine with other Tauri APIs
import { emit } from '@tauri-apps/api/event';

emit('tauri-app-system-tray-event', { status: 'active' });
```

