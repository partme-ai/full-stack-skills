# Plugin API

## API Reference

Plugin API for writing custom plugins.

### Plugin Interface

Plugin must have apply method.

**Type:**
```typescript
interface Plugin {
  apply(compiler: Compiler): void;
}
```

### Compiler Hooks

Compiler lifecycle hooks.

**Common Hooks:**
- `beforeRun` - Before compiler starts
- `run` - When compiler starts
- `compile` - Before compilation
- `compilation` - When compilation is created
- `emit` - Before emitting assets
- `done` - When compilation completes

### Example: Using Compiler Hooks

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.done.tap('MyPlugin', (stats) => {
      console.log('Build completed');
    });
  }
}
```

### Compilation Hooks

Compilation lifecycle hooks.

**Common Hooks:**
- `buildModule` - Before building module
- `optimizeChunks` - When optimizing chunks
- `optimizeAssets` - When optimizing assets

### Example: Using Compilation Hooks

```javascript
class MyPlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('MyPlugin', (compilation) => {
      compilation.hooks.optimizeChunks.tap('MyPlugin', () => {
        console.log('Optimizing chunks');
      });
    });
  }
}
```

### Hook Types

- `SyncHook` - Synchronous hooks
- `AsyncSeriesHook` - Async series hooks
- `AsyncParallelHook` - Async parallel hooks

**See also:** `examples/plugins/writing-plugins.md`
