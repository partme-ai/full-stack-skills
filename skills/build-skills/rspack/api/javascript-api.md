# JavaScript API

## API Reference

Rspack JavaScript API for programmatic usage.

### rspack()

Create a compiler instance.

**Type:**
```typescript
function rspack(
  options: Configuration,
  callback?: (err: Error | null, stats: Stats) => void
): Compiler
```

**Example:**
```javascript
const rspack = require('@rspack/core');

const compiler = rspack({
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
  },
});

compiler.run((err, stats) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(stats.toString());
});
```

### Compiler

Compiler instance for building.

**Methods:**
- `run(callback)` - Run the compiler
- `watch(options, callback)` - Watch for changes
- `close(callback)` - Close the compiler

**Example:**
```javascript
compiler.watch({}, (err, stats) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Build completed');
});
```

### Stats

Build statistics object.

**Methods:**
- `toString(options)` - Get stats as string
- `toJson(options)` - Get stats as JSON

**See also:** `examples/config/configuration-file.md`
