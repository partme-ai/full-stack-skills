# Usage: tauri-app-http-client

This document provides at least 5 usage examples for the **tauri-app-http-client** skill.

## Example 1: GET Request

```typescript
import { fetch } from '@tauri-apps/plugin-http';

const response = await fetch('https://api.example.com/data');
const data = await response.json();
```

## Example 2: POST Request

```typescript
import { fetch } from '@tauri-apps/plugin-http';

const response = await fetch('https://api.example.com/users', {
  method: 'POST',
  body: JSON.stringify({ name: 'Tauri' }),
  headers: { 'Content-Type': 'application/json' }
});
```

## Example 3: Request with Headers

```typescript
const response = await fetch('https://api.example.com/secret', {
  headers: {
    'Authorization': 'Bearer token'
  }
});
```

## Example 4: Set Request Timeout

```typescript
import { fetch } from '@tauri-apps/plugin-http';
// Timeout is often handled via AbortController in standard fetch API
const controller = new AbortController();
const id = setTimeout(() => controller.abort(), 5000);
await fetch(url, { signal: controller.signal });
```

## Example 5: Configure Allowed URLs

```typescript
// In src-tauri/capabilities/default.json
{
  "permissions": [
    {
      "identifier": "http:default",
      "allow": [{ "url": "https://*.example.com" }]
    }
  ]
}
```

