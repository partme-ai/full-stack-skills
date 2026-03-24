# Vite Project Structure Templates

## Standard Vue 3 Project Structure

```
my-vue-app/
├── index.html              # Entry HTML
├── package.json
├── vite.config.js          # Vite configuration
├── tsconfig.json           # TypeScript config (if using TS)
├── .env                    # Environment variables
├── .env.local              # Local environment variables
├── .env.development        # Development environment
├── .env.production         # Production environment
├── .gitignore
├── public/                 # Static assets (copied as-is)
│   ├── favicon.ico
│   └── robots.txt
└── src/                    # Source code
    ├── assets/            # Imported assets (processed)
    │   ├── logo.png
    │   └── styles/
    │       └── main.css
    ├── components/        # Vue components
    │   ├── common/
    │   └── layout/
    ├── views/             # Page components
    ├── router/            # Vue Router
    │   └── index.js
    ├── stores/            # Pinia stores
    │   └── index.js
    ├── composables/       # Composition functions
    ├── utils/             # Utility functions
    ├── api/               # API calls
    ├── App.vue            # Root component
    └── main.js            # Entry point
```

## React Project Structure

```
my-react-app/
├── index.html
├── package.json
├── vite.config.js
├── public/
└── src/
    ├── assets/
    ├── components/
    ├── pages/
    ├── hooks/
    ├── utils/
    ├── App.jsx
    └── main.jsx
```

## Multi-page Application Structure

```
my-mpa/
├── index.html             # Main page
├── admin.html             # Admin page
├── package.json
├── vite.config.js
├── public/
└── src/
    ├── pages/
    │   ├── main/
    │   │   ├── index.js
    │   │   └── App.vue
    │   └── admin/
    │       ├── index.js
    │       └── App.vue
    └── shared/            # Shared code
        ├── components/
        └── utils/
```

## Library Project Structure

```
my-library/
├── package.json
├── vite.config.js
├── src/
│   ├── components/        # Library components
│   ├── utils/             # Library utilities
│   └── index.js           # Entry point
└── dist/                  # Build output
```
