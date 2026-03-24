# Streaming | 流式传输

**官方文档**: https://github.com/vercel-labs/agent-browser/blob/main/README.md


## Instructions

This example demonstrates how to stream the browser viewport via WebSocket for live preview or "pair browsing".

### Key Concepts

- Streaming browser viewport via WebSocket
- Live preview
- Pair browsing (human + AI agent)
- WebSocket protocol
- Programmatic API

### Example: Enable Streaming

```bash
# Set stream port environment variable
export AGENT_BROWSER_STREAM_PORT=9223

# Start browser with streaming
agent-browser open example.com

# WebSocket server starts on port 9223
# Connect to ws://localhost:9223 to receive frames
```

### Example: WebSocket Protocol

**Receive frames:**
```json
{
  "type": "frame",
  "data": "<base64-encoded-jpeg>",
  "metadata": {
    "deviceWidth": 1280,
    "deviceHeight": 720,
    "pageScaleFactor": 1,
    "offsetTop": 0,
    "scrollOffsetX": 0,
    "scrollOffsetY": 0
  }
}
```

**Send mouse events:**
```json
{
  "type": "input_mouse",
  "eventType": "mousePressed",
  "x": 100,
  "y": 200,
  "button": "left",
  "clickCount": 1
}
```

**Send keyboard events:**
```json
{
  "type": "input_keyboard",
  "eventType": "keyDown",
  "key": "Enter",
  "code": "Enter"
}
```

**Send touch events:**
```json
{
  "type": "input_touch",
  "eventType": "touchStart",
  "touchPoints": [{ "x": 100, "y": 200 }]
}
```

### Example: Programmatic API

```typescript
import { BrowserManager } from 'agent-browser';

const browser = new BrowserManager();
await browser.launch({ headless: true });
await browser.navigate('https://example.com');

// Start screencast
await browser.startScreencast((frame) => {
  // frame.data is base64-encoded image
  // frame.metadata contains viewport info
  console.log('Frame received:', frame.metadata.deviceWidth, 'x', frame.metadata.deviceHeight);
}, {
  format: 'jpeg',
  quality: 80,
  maxWidth: 1280,
  maxHeight: 720,
});

// Inject mouse events
await browser.injectMouseEvent({
  type: 'mousePressed',
  x: 100,
  y: 200,
  button: 'left',
});

// Inject keyboard events
await browser.injectKeyboardEvent({
  type: 'keyDown',
  key: 'Enter',
  code: 'Enter',
});

// Stop when done
await browser.stopScreencast();
```

### Example: Pair Browsing Workflow

```bash
# 1. Start streaming
export AGENT_BROWSER_STREAM_PORT=9223
agent-browser open example.com

# 2. Human connects to ws://localhost:9223
# 3. Human can watch AI agent actions in real-time
# 4. Human can also interact (send mouse/keyboard events)
# 5. AI agent continues automation while human watches
```

### Key Points

- Set `AGENT_BROWSER_STREAM_PORT` environment variable to enable streaming
- WebSocket server starts on specified port
- Receive frames (base64-encoded JPEG) and metadata
- Send input events (mouse, keyboard, touch)
- Useful for live preview and pair browsing scenarios
- Programmatic API available for advanced use cases
