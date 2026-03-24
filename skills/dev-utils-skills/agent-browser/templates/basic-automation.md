# Basic Automation Template | 基础自动化模板

## Template

Basic browser automation workflow using agent-browser.

```bash
#!/bin/bash

# Step 1: Open the page
agent-browser open https://example.com --session my-task

# Step 2: Get snapshot with refs
agent-browser snapshot --session my-task

# Step 3: Interact with elements using refs
agent-browser click @e1 --session my-task
agent-browser fill @e2 "text" --session my-task
agent-browser click @e3 --session my-task

# Step 4: Verify changes
agent-browser snapshot --session my-task

# Step 5: Take screenshot
agent-browser screenshot output.png --session my-task
```

## Usage

1. Install agent-browser: `npm install -g agent-browser && agent-browser install`
2. Copy the template script
3. Customize URLs and selectors
4. Run the script: `bash script.sh`

## Customization

- Change the URL in `open` command
- Modify refs based on snapshot output
- Add more interaction commands
- Adjust session name
- Add error handling
