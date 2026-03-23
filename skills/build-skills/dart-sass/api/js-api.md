# JavaScript API

## JavaScript API

Dart Sass 提供了 JavaScript API，可以在 Node.js 项目中使用。

### 安装

```bash
npm install sass
```

### 基本用法

#### compile

同步编译文件。

```javascript
const sass = require('sass');

const result = sass.compile('styles.scss', {
  style: 'compressed',
  sourceMap: true
});

console.log(result.css);
console.log(result.sourceMap);
```

#### compileString

从字符串编译。

```javascript
const sass = require('sass');

const scss = `
  $primary: #409EFF;
  .button {
    background-color: $primary;
  }
`;

const result = sass.compileString(scss, {
  style: 'expanded'
});

console.log(result.css);
```

### 异步 API

#### compileAsync

异步编译文件。

```javascript
const sass = require('sass');

sass.compileAsync('styles.scss', {
  style: 'compressed'
}).then(result => {
  console.log(result.css);
});
```

#### compileStringAsync

异步字符串编译。

```javascript
const sass = require('sass');

const scss = `...`;

sass.compileStringAsync(scss).then(result => {
  console.log(result.css);
});
```

### 选项

#### style

输出样式：`'expanded'` | `'compressed'` | `'compact'` | `'nested'`

```javascript
sass.compile('styles.scss', {
  style: 'compressed'
});
```

#### sourceMap

是否生成 source map。

```javascript
sass.compile('styles.scss', {
  sourceMap: true
});
```

#### loadPaths

加载路径数组。

```javascript
sass.compile('styles.scss', {
  loadPaths: ['node_modules', 'src/styles']
});
```

#### quietDeps

静默依赖警告。

```javascript
sass.compile('styles.scss', {
  quietDeps: true
});
```

#### verbose

详细输出。

```javascript
sass.compile('styles.scss', {
  verbose: true
});
```

### 完整示例

```javascript
const sass = require('sass');
const fs = require('fs');

const result = sass.compile('src/styles/main.scss', {
  style: 'compressed',
  sourceMap: true,
  loadPaths: ['node_modules', 'src/styles']
});

// 写入 CSS
fs.writeFileSync('dist/css/main.css', result.css);

// 写入 source map
if (result.sourceMap) {
  fs.writeFileSync('dist/css/main.css.map', JSON.stringify(result.sourceMap));
}
```

### 错误处理

```javascript
const sass = require('sass');

try {
  const result = sass.compile('styles.scss');
  console.log(result.css);
} catch (error) {
  console.error('Sass compilation error:', error.message);
  console.error('File:', error.span?.url);
  console.error('Line:', error.span?.start.line);
}
```

### 在构建工具中使用

#### Webpack

```javascript
const sass = require('sass');

module.exports = {
  module: {
    rules: [{
      test: /\.scss$/,
      use: [{
        loader: 'sass-loader',
        options: {
          implementation: sass,
          sassOptions: {
            style: 'compressed'
          }
        }
      }]
    }]
  }
};
```

#### Gulp

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
```

### 最佳实践

1. **使用异步 API**：在 Node.js 中优先使用异步 API
2. **错误处理**：始终处理编译错误
3. **配置选项**：根据环境配置不同选项
4. **性能优化**：使用缓存和增量编译
5. **Source Maps**：开发环境启用，生产环境禁用
