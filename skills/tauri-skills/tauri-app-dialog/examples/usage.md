# Usage: tauri-app-dialog

This document provides at least 5 usage examples for the **tauri-app-dialog** skill.

## Example 1: Open File Dialog

```typescript
import { open } from '@tauri-apps/plugin-dialog';

const file = await open({
  multiple: false,
  filters: [{
    name: 'Images',
    extensions: ['png', 'jpeg']
  }]
});
```

## Example 2: Save File Dialog

```typescript
import { save } from '@tauri-apps/plugin-dialog';

const path = await save({
  filters: [{
    name: 'Text',
    extensions: ['txt']
  }]
});
```

## Example 3: Show Message Dialog

```typescript
import { message } from '@tauri-apps/plugin-dialog';

await message('Operation successful', { title: 'Tauri', type: 'info' });
```

## Example 4: Ask Confirmation Dialog

```typescript
import { ask } from '@tauri-apps/plugin-dialog';

const yes = await ask('Are you sure?', { title: 'Tauri', type: 'warning' });
if (yes) {
  // do something
}
```

## Example 5: Open Directory Dialog

```typescript
import { open } from '@tauri-apps/plugin-dialog';

const dir = await open({
  directory: true,
  multiple: false
});
```

