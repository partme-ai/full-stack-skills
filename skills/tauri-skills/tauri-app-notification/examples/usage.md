# Usage: tauri-app-notification

This document provides at least 5 usage examples for the **tauri-app-notification** skill.

## Example 1: Send Basic Notification

```typescript
import { sendNotification } from '@tauri-apps/plugin-notification';

sendNotification('Hello from Tauri!');
```

## Example 2: Send Notification with Title

```typescript
import { sendNotification } from '@tauri-apps/plugin-notification';

sendNotification({ title: 'New Message', body: 'You have a new message from Alice' });
```

## Example 3: Check Permission

```typescript
import { isPermissionGranted, requestPermission } from '@tauri-apps/plugin-notification';

let permissionGranted = await isPermissionGranted();
if (!permissionGranted) {
  const permission = await requestPermission();
  permissionGranted = permission === 'granted';
}
```

## Example 4: Send Notification with Icon

```typescript
// Icon is usually set in tauri.conf.json, but some platforms support custom icons in payload if supported
```

## Example 5: Handle Notification Click

```typescript
// Currently handled via Rust backend or platform specific implementation
```

