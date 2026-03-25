---
name: vscode-feature-webview
description: "Add a Webview panel to a VS Code extension for displaying custom HTML content (forms, charts, complex layouts) using vscode.window.createWebviewPanel. Use when the user needs custom UI that cannot be achieved with standard VS Code UI elements, such as dashboards, settings forms, or rich previews."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when the user needs a custom UI (forms, charts, complex layouts) that cannot be achieved with standard VS Code UI elements.

## How to use this skill

1.  **Register Command**: First, create a command (using `vscode-feature-command`) that will open the webview.
2.  **Implement Webview Logic**: In the command callback, create the panel.

### Code Template

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let currentPanel: vscode.WebviewPanel | undefined = undefined;

    context.subscriptions.push(
        vscode.commands.registerCommand('extension.showWebview', () => {
            const columnToShowIn = vscode.window.activeTextEditor
                ? vscode.window.activeTextEditor.viewColumn
                : undefined;

            if (currentPanel) {
                // If we already have a panel, show it in the target column
                currentPanel.reveal(columnToShowIn);
            } else {
                // Otherwise, create a new panel
                currentPanel = vscode.window.createWebviewPanel(
                    'catCoding', // Identifies the type of the webview. Used internally
                    'Cat Coding', // Title of the panel displayed to the user
                    columnToShowIn || vscode.ViewColumn.One, // Editor column to show the new webview panel in.
                    {
                        enableScripts: true // Enable JS in the webview
                    }
                );

                currentPanel.webview.html = getWebviewContent();

                // Reset when the current panel is closed
                currentPanel.onDidDispose(
                    () => {
                        currentPanel = undefined;
                    },
                    null,
                    context.subscriptions
                );
            }
        })
    );
}

function getWebviewContent() {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cat Coding</title>
</head>
<body>
    <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" width="300" />
    <h1>Hello Webview</h1>
</body>
</html>`;
}
```

## Security Note

Always use `vscode-resource:` scheme for local content and Content Security Policy (CSP) in production.
