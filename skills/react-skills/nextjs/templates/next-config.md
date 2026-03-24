# Next.js Configuration Templates

## Basic Configuration

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
```

## Configuration with TypeScript

```typescript
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactStrictMode: true,
}

export default nextConfig
```

## Configuration with Images

```javascript
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
      },
    ],
  },
}
```

## Configuration with Environment Variables

```javascript
module.exports = {
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },
}
```

## Configuration with Redirects

```javascript
module.exports = {
  async redirects() {
    return [
      {
        source: '/old',
        destination: '/new',
        permanent: true,
      },
    ]
  },
}
```

## Configuration with Rewrites

```javascript
module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://api.example.com/:path*',
      },
    ]
  },
}
```
