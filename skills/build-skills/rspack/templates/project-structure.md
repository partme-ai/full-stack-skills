# Rspack Project Structure Templates

## Basic Structure

```
project/
├── src/
│   ├── index.js
│   └── ...
├── public/
│   └── index.html
├── rspack.config.js
├── package.json
└── node_modules/
```

## TypeScript Structure

```
project/
├── src/
│   ├── index.ts
│   └── ...
├── public/
│   └── index.html
├── rspack.config.ts
├── tsconfig.json
├── package.json
└── node_modules/
```

## React Structure

```
project/
├── src/
│   ├── index.tsx
│   ├── App.tsx
│   └── components/
├── public/
│   └── index.html
├── rspack.config.ts
├── tsconfig.json
├── package.json
└── node_modules/
```

## Multi-Entry Structure

```
project/
├── src/
│   ├── app/
│   │   └── index.js
│   └── admin/
│       └── index.js
├── rspack.config.js
└── package.json
```
