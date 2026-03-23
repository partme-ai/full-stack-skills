# Custom Browser Executable | 自定义浏览器可执行文件

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to use a custom browser executable instead of the bundled Chromium.

### Key Concepts

- Custom browser executable path
- Serverless deployment (lightweight builds)
- System browsers
- Custom builds
- Environment variable vs CLI flag

### Example: Via CLI Flag

```bash
# Use custom browser executable
agent-browser --executable-path /path/to/chromium open example.com
agent-browser --executable-path /path/to/chromium snapshot
```

### Example: Via Environment Variable

```bash
# Set custom executable path
export AGENT_BROWSER_EXECUTABLE_PATH=/path/to/chromium

# All commands use the custom executable
agent-browser open example.com
agent-browser snapshot
```

### Example: Serverless Deployment (Vercel/AWS Lambda)

```typescript
import chromium from '@sparticuz/chromium';
import { BrowserManager } from 'agent-browser';

export async function handler() {
  const browser = new BrowserManager();
  await browser.launch({
    executablePath: await chromium.executablePath(),
    headless: true,
  });
  // ... use browser
}
```

### Example: Using System Chrome

```bash
# macOS
agent-browser --executable-path "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" open example.com

# Linux
agent-browser --executable-path /usr/bin/google-chrome open example.com

# Windows
agent-browser --executable-path "C:\Program Files\Google\Chrome\Application\chrome.exe" open example.com
```

### Example: Lightweight Builds

```bash
# Use lightweight Chromium build for serverless
export AGENT_BROWSER_EXECUTABLE_PATH=/path/to/lightweight-chromium
agent-browser open example.com
```

### Key Points

- Use `--executable-path` flag or `AGENT_BROWSER_EXECUTABLE_PATH` environment variable
- Useful for serverless deployments (lightweight builds like @sparticuz/chromium)
- Can use system browsers or custom builds
- Default bundled Chromium is ~684MB, lightweight builds are ~50MB
- Useful for environments with size constraints
