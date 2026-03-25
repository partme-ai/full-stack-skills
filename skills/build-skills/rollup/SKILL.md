---
name: rollup
description: "Provides comprehensive guidance for Rollup bundler including configuration, plugins, code splitting, tree shaking, and multi-format library bundling. Use when the user asks about Rollup, needs to bundle JavaScript libraries, optimize output with tree shaking, or configure ESM/CJS builds."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Bundle JavaScript libraries with tree shaking and multi-format output (ESM/CJS/UMD)
- Configure Rollup input, output, plugins, and external dependencies
- Optimize bundle size with code splitting and dead code elimination
- Build libraries for npm distribution

## How to use this skill

### Workflow

1. **Configure** — create `rollup.config.js` with input, output, and plugins
2. **Build** — run `rollup -c` to generate bundles
3. **Validate** — check output formats, bundle size, and tree shaking effectiveness
4. **Publish** — set `main`, `module`, and `exports` in `package.json`

### Quick Start Example

```javascript
// rollup.config.js
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';

export default {
  input: 'src/index.js',
  output: [
    {
      file: 'dist/index.cjs.js',
      format: 'cjs',
      sourcemap: true,
    },
    {
      file: 'dist/index.esm.js',
      format: 'es',
      sourcemap: true,
    },
  ],
  external: ['react', 'react-dom'], // Don't bundle peer deps
  plugins: [
    resolve(),
    commonjs(),
    terser(), // Minify for production
  ],
};
```

```bash
# Build
npx rollup -c

# Watch mode for development
npx rollup -c --watch
```

```json
// package.json — library distribution fields
{
  "main": "dist/index.cjs.js",
  "module": "dist/index.esm.js",
  "exports": {
    ".": {
      "import": "./dist/index.esm.js",
      "require": "./dist/index.cjs.js"
    }
  },
  "files": ["dist"],
  "sideEffects": false
}
```

### Code Splitting Example

```javascript
// Dynamic imports create separate chunks
export default {
  input: 'src/index.js',
  output: {
    dir: 'dist',
    format: 'es',
    chunkFileNames: 'chunks/[name]-[hash].js',
  },
  plugins: [resolve(), commonjs()],
};
```

## Best Practices

- Mark peer dependencies as `external` to avoid bundling them
- Enable sourcemaps for debugging; disable in production if not needed
- Use `sideEffects: false` in `package.json` to enable maximum tree shaking
- For large dependencies, externalize them to reduce bundle size
- Use code splitting with dynamic `import()` for on-demand loading

## Reference

- Official documentation: https://rollupjs.org/

## Keywords

rollup, bundler, ESM, CJS, tree-shaking, code splitting, library bundling, plugins
