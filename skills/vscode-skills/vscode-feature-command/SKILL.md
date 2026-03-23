---
name: vscode-feature-command
description: Add a new command to the VS Code extension.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when the user wants to add a new functional command (e.g., "Hello World", "Format Text") to the extension.

## How to use this skill

Adding a command requires updates to two files: `package.json` and `src/extension.ts`.

### Step 1: Update `package.json`

Add the command definition to the `contributes.commands` array.

```json
// package.json
{
  "contributes": {
    "commands": [
      {
        "command": "extension.myCommand", // Unique ID
        "title": "My Extension: Do Something" // Display Name
      }
    ]
  }
}
```

### Step 2: Update `src/extension.ts`

Register the command in the `activate` function.

```typescript
// src/extension.ts
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    // ... existing code ...

    let disposable = vscode.commands.registerCommand('extension.myCommand', () => {
        // Implementation logic here
        vscode.window.showInformationMessage('Command executed!');
    });

    context.subscriptions.push(disposable);
}
```

## Best Practices

*   **Command ID Naming**: Use `extensionName.actionName` format to avoid conflicts.
*   **Async Handling**: If the command logic is asynchronous, use `async () => { await ... }`.
*   **Error Handling**: Wrap logic in try-catch blocks if it involves external operations.
