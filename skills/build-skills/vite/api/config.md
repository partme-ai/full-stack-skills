# Vite Config API

## API Reference

Vite configuration options and their types.

### defineConfig()

Helper function for better TypeScript support.

**Signature:**
```typescript
function defineConfig(config: UserConfig | ((env: ConfigEnv) => UserConfig)): UserConfig
```

**Example:**
```typescript
import { defineConfig } from 'vite'

export default defineConfig({
  // config options
})
```

### Configuration Options

#### root

**Type:** `string`  
**Default:** `process.cwd()`

Project root directory.

#### base

**Type:** `string`  
**Default:** `/`

Base public path when served in development or production.

#### mode

**Type:** `string`  
**Default:** `'development'` for serve, `'production'` for build

Mode to use.

#### plugins

**Type:** `(Plugin | Plugin[])[]`

Array of plugins to use.

#### publicDir

**Type:** `string | false`  
**Default:** `'public'`

Directory to serve as static assets.

#### server

**Type:** `ServerOptions`

Development server options.

**Properties:**
- `host?: string` - Server hostname
- `port?: number` - Server port
- `strictPort?: boolean` - Exit if port is in use
- `open?: boolean | string` - Open browser on start
- `cors?: boolean | CorsOptions` - CORS options
- `https?: boolean | https.ServerOptions` - HTTPS options
- `proxy?: Record<string, string | ProxyOptions>` - Proxy configuration

#### build

**Type:** `BuildOptions`

Build options.

**Properties:**
- `outDir?: string` - Output directory
- `assetsDir?: string` - Assets directory
- `sourcemap?: boolean | 'inline'` - Source maps
- `minify?: boolean | 'esbuild' | 'terser'` - Minification
- `target?: string | string[]` - Target browsers
- `cssCodeSplit?: boolean` - CSS code splitting
- `rollupOptions?: RollupOptions` - Rollup options

#### resolve

**Type:** `ResolveOptions`

Resolve options.

**Properties:**
- `alias?: Record<string, string>` - Path aliases
- `extensions?: string[]` - File extensions to resolve

#### css

**Type:** `CSSOptions`

CSS options.

**Properties:**
- `modules?: CSSModulesOptions` - CSS Modules options
- `preprocessorOptions?: Record<string, any>` - Preprocessor options

#### optimizeDeps

**Type:** `OptimizeDepsOptions`

Dependency optimization options.

**Properties:**
- `include?: string[]` - Dependencies to include
- `exclude?: string[]` - Dependencies to exclude

**See also:** `examples/config.md`
