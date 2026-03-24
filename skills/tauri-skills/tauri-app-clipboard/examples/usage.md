# Usage: tauri-app-clipboard

This document provides at least 5 usage examples for the **tauri-app-clipboard** skill.

## Example 1: Write Text to Clipboard

```typescript
import { writeText } from '@tauri-apps/plugin-clipboard-manager';

await writeText('Hello Tauri!');
```

## Example 2: Read Text from Clipboard

```typescript
import { readText } from '@tauri-apps/plugin-clipboard-manager';

const text = await readText();
console.log(text);
```

## Example 3: Clear Clipboard

```typescript
import { writeText } from '@tauri-apps/plugin-clipboard-manager';

await writeText(''); // Write empty string to clear
```

## Example 4: Handle Write Errors

```typescript
try {
  await writeText('Sensitive Data');
} catch (e) {
  console.error('Failed to write to clipboard:', e);
}
```

## Example 5: Check Clipboard Permission

```typescript
// In src-tauri/capabilities/default.json ensure 'clipboard-manager:allow-write-text' is present
```

