# Usage: tauri-app-creator

This document provides at least 5 usage examples for the **tauri-app-creator** skill.

## Example 1: Initialize App Creator

```typescript
// Example initialization for App Creator
import { init } from 'tauri-plugin-creator';

await init();
```

## Example 2: Basic Usage of App Creator

```typescript
// Basic operation
const result = await invoke('plugin:creator|do_something');
console.log(result);
```

## Example 3: Configure App Creator Settings

```typescript
// Update tauri.conf.json
{
  "plugins": {
    "creator": {
      "enabled": true
    }
  }
}
```

## Example 4: Handle App Creator Errors

```typescript
try {
  await performAction();
} catch (error) {
  console.error('App Creator Error:', error);
}
```

## Example 5: Advanced App Creator Integration

```typescript
// Combine with other Tauri APIs
import { emit } from '@tauri-apps/api/event';

emit('tauri-app-creator-event', { status: 'active' });
```

