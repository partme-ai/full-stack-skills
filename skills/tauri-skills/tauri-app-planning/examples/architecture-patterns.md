# Tauri Orchestration Patterns

## Goal
Manage complex applications with multiple windows, shared state, and event-driven communication.

## Core Concepts

1.  **Window Management**: Opening, closing, and hiding windows programmatically.
2.  **Event System**: `emit` and `listen` for Global vs Window-specific events.
3.  **State Management**: Using `Manager::manage` in Rust to hold database connections or app state.

## Implementation Patterns

### 1. State Management (Rust)

**Pattern**: Use `tauri::State` to share data between commands.

```rust
use std::sync::Mutex;
use tauri::{Manager, State};

struct AppState {
    counter: Mutex<i32>,
    db_pool: Mutex<Option<String>>, // Mock DB connection
}

#[tauri::command]
fn increment(state: State<AppState>) -> i32 {
    let mut count = state.counter.lock().unwrap();
    *count += 1;
    *count
}

pub fn run() {
    tauri::Builder::default()
        .manage(AppState { 
            counter: Mutex::new(0),
            db_pool: Mutex::new(None)
        })
        .invoke_handler(tauri::generate_handler![increment])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

### 2. Event Communication

**Pattern**: Decoupled communication using events.

**Rust -> Frontend**:
```rust
// Emit to all windows
app.emit("update-status", "processing started");

// Emit to specific window
if let Some(window) = app.get_webview_window("main") {
    window.emit("download-progress", 50);
}
```

**Frontend -> Frontend (Window to Window)**:
```typescript
import { emit, listen } from '@tauri-apps/api/event';

// In Window A (Sender)
await emit('global-event', { message: 'Hello from Window A' });

// In Window B (Receiver)
await listen('global-event', (event) => {
  console.log('Received:', event.payload);
});
```

### 3. Window Management (Frontend)

**Pattern**: Dynamic window creation.

```typescript
import { WebviewWindow } from '@tauri-apps/api/webviewWindow';

async function openSettings() {
  const webview = new WebviewWindow('settings', {
    url: 'settings.html',
    title: 'Settings',
    width: 600,
    height: 400,
    center: true
  });
  
  webview.once('tauri://created', function () {
    console.log('Settings window created');
  });
  
  webview.once('tauri://error', function (e) {
    console.error('Error creating window', e);
  });
}
```

## Best Practices

-   **Minimize Event Payloads**: Large JSON payloads in events can be slow. Use Commands for large data transfer.
-   **Window Labels**: Use consistent naming (e.g., `main`, `settings`, `splash`) for easier targeting in Capabilities.
-   **Graceful Shutdown**: Listen for `tauri://close-requested` to save state before closing.
