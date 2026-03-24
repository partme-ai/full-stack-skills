# Loader API

## API Reference

Loader API for writing custom loaders.

### Loader Function

Loader function signature.

**Type:**
```typescript
function loader(
  this: LoaderContext,
  source: string | Buffer,
  sourceMap?: SourceMap
): string | Buffer | void
```

### Example: Basic Loader

```javascript
module.exports = function(source) {
  return `export default ${JSON.stringify(source)}`;
};
```

### Example: Loader with Options

```javascript
module.exports = function(source) {
  const options = this.getOptions();
  return source.replace(/{{name}}/g, options.name);
};
```

### Example: Async Loader

```javascript
module.exports = function(source) {
  const callback = this.async();
  
  setTimeout(() => {
    callback(null, source);
  }, 1000);
};
```

### Loader Context

Loader context provides utilities.

**Properties:**
- `this.resourcePath` - Path to resource
- `this.query` - Query string
- `this.getOptions()` - Get loader options
- `this.async()` - Make loader async

### Example: Using Loader Context

```javascript
module.exports = function(source) {
  const options = this.getOptions();
  const resourcePath = this.resourcePath;
  
  return `// Loaded from ${resourcePath}\n${source}`;
};
```

**See also:** `examples/config/module.md`
