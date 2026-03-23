# CLI API

## API Reference

Rspack CLI commands and options.

### rspack build

Build the project.

**Usage:**
```bash
rspack build
```

**Options:**
- `--config <path>` - Path to config file
- `--mode <mode>` - Mode (development, production)
- `--watch` - Watch mode
- `--env <env>` - Environment variables

**Example:**
```bash
rspack build --config rspack.config.js --mode production
```

### rspack serve

Start development server.

**Usage:**
```bash
rspack serve
```

**Options:**
- `--config <path>` - Path to config file
- `--port <port>` - Port number
- `--host <host>` - Hostname
- `--open` - Open browser

**Example:**
```bash
rspack serve --port 3000 --open
```

### Common Options

- `-h, --help` - Show help
- `-v, --version` - Show version
- `--config <path>` - Config file path
- `--mode <mode>` - Build mode
- `--env <env>` - Environment variables

**See also:** `examples/start/quick-start.md`
