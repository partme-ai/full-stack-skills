# Next.js Project Structure Templates

## App Router Structure

```
my-app/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── loading.tsx
│   ├── error.tsx
│   ├── not-found.tsx
│   ├── globals.css
│   ├── (group)/
│   │   └── page.tsx
│   ├── [slug]/
│   │   └── page.tsx
│   └── api/
│       └── route.ts
├── components/
├── lib/
├── public/
├── next.config.js
└── package.json
```

## Pages Router Structure

```
my-app/
├── pages/
│   ├── _app.tsx
│   ├── _document.tsx
│   ├── index.tsx
│   ├── about.tsx
│   └── api/
│       └── hello.ts
├── components/
├── lib/
├── public/
├── next.config.js
└── package.json
```

## Hybrid Structure (Both Routers)

```
my-app/
├── app/              # App Router
│   └── ...
├── pages/            # Pages Router
│   └── ...
├── components/
├── lib/
├── public/
└── next.config.js
```
