# Frontend

**官方文档**: https://v2.tauri.org.cn/start/

## Goals

- Choose a frontend framework
- Connect dev server to Tauri
- Output a static build for production

### Example: Dev Server Flow

1. Start your frontend dev server
2. Run `npm run tauri dev`
3. Tauri loads the dev server URL

### Example: Production Build Flow

1. Build frontend assets
2. Run `npm run tauri build`
3. Tauri bundles native binaries with static assets

### Key Points

- Any web framework works
- Dev uses live server URL
- Build uses static assets
