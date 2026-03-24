# CLI API

## API Reference

Vite CLI commands and options.

### vite

Start development server.

**Usage:**
```bash
vite [root]
```

**Options:**
- `--host [host]` - Specify hostname
- `--port <port>` - Specify port
- `--open [path]` - Open browser on startup
- `--force` - Force optimizer to re-bundle
- `--cors` - Enable CORS
- `--strictPort` - Exit if port is in use
- `--https` - Use TLS
- `-c, --config <file>` - Specify config file
- `-m, --mode <mode>` - Specify env mode

### vite build

Build for production.

**Usage:**
```bash
vite build [root]
```

**Options:**
- `--target <target>` - Build target
- `--outDir <dir>` - Output directory
- `--assetsDir <dir>` - Assets directory
- `--minify <minifier>` - Minifier (esbuild|terser)
- `--sourcemap` - Generate source maps
- `-w, --watch` - Watch mode
- `-c, --config <file>` - Specify config file
- `-m, --mode <mode>` - Specify env mode

### vite preview

Preview production build.

**Usage:**
```bash
vite preview [root]
```

**Options:**
- `--host [host]` - Specify hostname
- `--port <port>` - Specify port
- `--open [path]` - Open browser
- `--outDir <dir>` - Output directory
- `-c, --config <file>` - Specify config file

### vite optimize

Pre-bundle dependencies.

**Usage:**
```bash
vite optimize [root]
```

**Options:**
- `--force` - Force re-bundling
- `-c, --config <file>` - Specify config file

**See also:** `examples/getting-started.md`
