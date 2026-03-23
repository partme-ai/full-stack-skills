# Usage: tauri-app-file-system

This document provides at least 5 usage examples for the **tauri-app-file-system** skill.

## Example 1: Read Text File

```typescript
import { readTextFile, BaseDirectory } from '@tauri-apps/plugin-fs';

const content = await readTextFile('config.json', { baseDir: BaseDirectory.AppLocalData });
```

## Example 2: Write Text File

```typescript
import { writeTextFile, BaseDirectory } from '@tauri-apps/plugin-fs';

await writeTextFile('config.json', '{ "theme": "dark" }', { baseDir: BaseDirectory.AppLocalData });
```

## Example 3: Check File Existence

```typescript
import { exists, BaseDirectory } from '@tauri-apps/plugin-fs';

const hasConfig = await exists('config.json', { baseDir: BaseDirectory.AppLocalData });
```

## Example 4: Create Directory

```typescript
import { mkdir, BaseDirectory } from '@tauri-apps/plugin-fs';

await mkdir('logs', { baseDir: BaseDirectory.AppLocalData, recursive: true });
```

## Example 5: Read Directory

```typescript
import { readDir, BaseDirectory } from '@tauri-apps/plugin-fs';

const entries = await readDir('plugins', { baseDir: BaseDirectory.Resource });
```

