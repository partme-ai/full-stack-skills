---
name: webpack
description: "Provides comprehensive guidance for Webpack bundler including configuration, loaders, plugins, code splitting, optimization, and development setup. Use when the user asks about Webpack, needs to configure build pipelines, optimize bundles, or work with Webpack plugins and loaders."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Bundle JavaScript, CSS, and assets with Webpack loaders and plugins
- Configure multi-entry points, code splitting, caching, and optimization
- Set up HMR with webpack-dev-server for development
- Optimize production builds with tree shaking and minification

## How to use this skill

### Workflow

1. **Configure** — define entry, output, loaders, and plugins in `webpack.config.js`
2. **Develop** — run dev server with HMR for fast iteration
3. **Build** — run production build with optimizations
4. **Analyze** — inspect bundle size with webpack-bundle-analyzer

### Quick Start Example

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (env, argv) => {
  const isProd = argv.mode === 'production';

  return {
    entry: './src/index.js',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: isProd ? '[name].[contenthash].js' : '[name].js',
      clean: true,
    },
    module: {
      rules: [
        {
          test: /\.jsx?$/,
          exclude: /node_modules/,
          use: 'babel-loader',
        },
        {
          test: /\.css$/,
          use: [
            isProd ? MiniCssExtractPlugin.loader : 'style-loader',
            'css-loader',
          ],
        },
        {
          test: /\.(png|svg|jpg|gif)$/,
          type: 'asset/resource',
        },
      ],
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: './src/index.html',
      }),
      ...(isProd ? [new MiniCssExtractPlugin({
        filename: '[name].[contenthash].css',
      })] : []),
    ],
    optimization: {
      splitChunks: {
        chunks: 'all', // Extract vendor code into separate chunk
      },
    },
    devServer: {
      hot: true,
      port: 3000,
    },
    devtool: isProd ? 'source-map' : 'eval-source-map',
  };
};
```

```bash
# Development with HMR
npx webpack serve --mode development

# Production build
npx webpack --mode production

# Analyze bundle
npx webpack --mode production --analyze
```

### Code Splitting Example

```javascript
// Lazy load a route/component
const loadDashboard = () => import(
  /* webpackChunkName: "dashboard" */
  './pages/Dashboard'
);
```

## Best Practices

- Order loaders correctly (right-to-left execution); use `exclude: /node_modules/` for Babel
- Enable `splitChunks` for vendor code extraction and tree shaking in production mode
- Use content hashing (`[contenthash]`) for long-term caching
- For new projects, consider Vite or Rspack for faster build times
- Use `webpack-bundle-analyzer` to identify oversized chunks

## Reference

- Official documentation: https://webpack.js.org/

## Keywords

webpack, bundler, loader, plugin, code splitting, HMR, tree-shaking, optimization, build tool
