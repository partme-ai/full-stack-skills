# Usage: tauri-app-single-instance

This document provides at least 5 usage examples for the **tauri-app-single-instance** skill.

## Example 1: Initialize App Single Instance

```typescript
// Example initialization for App Single Instance
import { init } from 'tauri-plugin-single-instance';

await init();
```

## Example 2: Basic Usage of App Single Instance

```typescript
// Basic operation
const result = await invoke('plugin:single-instance|do_something');
console.log(result);
```

## Example 3: Configure App Single Instance Settings

```typescript
// Update tauri.conf.json
{
  "plugins": {
    "single-instance": {
      "enabled": true
    }
  }
}
```

## Example 4: Handle App Single Instance Errors

```typescript
try {
  await performAction();
} catch (error) {
  console.error('App Single Instance Error:', error);
}
```

## Example 5: Advanced App Single Instance Integration

```typescript
// Combine with other Tauri APIs
import { emit } from '@tauri-apps/api/event';

emit('tauri-app-single-instance-event', { status: 'active' });
```

