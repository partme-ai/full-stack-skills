# Build Integration

## 构建工具集成

将 Sass 集成到各种构建工具中。

### Webpack

```javascript
const path = require('path');
const sass = require('sass');

module.exports = {
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        'style-loader',
        'css-loader',
        {
          loader: 'sass-loader',
          options: {
            implementation: sass,
            sassOptions: {
              outputStyle: 'compressed'
            }
          }
        }
      ]
    }]
  }
};
```

### Vite

```javascript
import { defineConfig } from 'vite';

export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/styles/variables" as *;`
      }
    }
  }
});
```

### Gulp

```javascript
const gulp = require('gulp');
const sass = require('sass');
const sassCompiler = require('gulp-sass')(sass);

gulp.task('sass', function() {
  return gulp.src('src/scss/**/*.scss')
    .pipe(sassCompiler({
      outputStyle: 'compressed'
    }))
    .pipe(gulp.dest('dist/css'));
});

gulp.task('sass:watch', function() {
  gulp.watch('src/scss/**/*.scss', gulp.series('sass'));
});
```

### Rollup

```javascript
import sass from 'rollup-plugin-sass';

export default {
  plugins: [
    sass({
      output: 'dist/css/style.css',
      options: {
        outputStyle: 'compressed'
      }
    })
  ]
};
```
