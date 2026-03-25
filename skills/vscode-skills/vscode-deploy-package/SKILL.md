---
name: vscode-deploy-package
description: "Package a VS Code extension into a .vsix file for distribution using vsce, verify pre-flight checklist (publisher, README, CHANGELOG), and install locally via CLI or GUI. Use when development is complete and the user wants to package, distribute, or install a VS Code extension."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when the development is complete and the user wants to install the extension or share it.

## How to use this skill

1.  **Install `vsce`**: Ensure the packaging tool is installed.
    ```bash
    npm install -g vsce
    ```
2.  **Package**: Run the package command in the project root.
    ```bash
    vsce package
    ```
3.  **Result**: This generates a `.vsix` file (e.g., `my-extension-0.0.1.vsix`).

## Pre-flight Checklist

Before packaging, ensure:
*   `package.json` has a valid `publisher` field. (If not, user can use any string for local testing, e.g., "local").
*   `README.md` is updated.
*   `CHANGELOG.md` is updated.
*   No strict linting errors prevent compilation.

## Installation

To install the `.vsix` file:
*   **GUI**: Open VS Code Extensions view -> "..." menu -> "Install from VSIX..."
*   **CLI**: `code --install-extension my-extension-0.0.1.vsix`
