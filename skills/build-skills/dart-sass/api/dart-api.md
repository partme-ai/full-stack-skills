# Dart API

## Dart API

Dart Sass 提供了 Dart API，可以在 Dart 项目中使用。

### 安装

在 `pubspec.yaml` 中添加：

```yaml
dependencies:
  sass: ^1.69.5
```

运行：

```bash
dart pub get
```

### 基本用法

#### 导入包

```dart
import 'package:sass/sass.dart' as sass;
```

#### 编译文件

```dart
import 'package:sass/sass.dart' as sass;
import 'dart:io';

void main() {
  final result = sass.compile('styles.scss');
  File('styles.css').writeAsStringSync(result.css);
}
```

#### 编译字符串

```dart
import 'package:sass/sass.dart' as sass;

void main() {
  final scss = '''
    \$primary: #409EFF;
    .button {
      background-color: \$primary;
    }
  ''';
  
  final result = sass.compileString(scss);
  print(result.css);
}
```

### 选项

#### 输出样式

```dart
final result = sass.compile(
  'styles.scss',
  outputStyle: sass.OutputStyle.compressed,
);
```

#### Source Map

```dart
final result = sass.compile(
  'styles.scss',
  sourceMap: true,
);
```

#### 加载路径

```dart
final result = sass.compile(
  'styles.scss',
  loadPaths: ['node_modules', 'src/styles'],
);
```

### 完整示例

```dart
import 'package:sass/sass.dart' as sass;
import 'dart:io';

void main() {
  try {
    final result = sass.compile(
      'src/styles/main.scss',
      outputStyle: sass.OutputStyle.compressed,
      sourceMap: true,
      loadPaths: ['node_modules', 'src/styles'],
    );
    
    // 写入 CSS
    File('dist/css/main.css').writeAsStringSync(result.css);
    
    // 写入 source map
    if (result.sourceMap != null) {
      File('dist/css/main.css.map')
        .writeAsStringSync(result.sourceMap!);
    }
    
    print('Compilation successful!');
  } catch (e) {
    print('Compilation error: $e');
  }
}
```

### 错误处理

```dart
import 'package:sass/sass.dart' as sass;

void main() {
  try {
    final result = sass.compile('styles.scss');
    print(result.css);
  } on sass.SassException catch (e) {
    print('Sass error: ${e.message}');
    print('File: ${e.span?.url}');
    print('Line: ${e.span?.start.line}');
  } catch (e) {
    print('Error: $e');
  }
}
```

### 异步编译

```dart
import 'package:sass/sass.dart' as sass;

Future<void> main() async {
  final result = await sass.compileAsync('styles.scss');
  print(result.css);
}
```

### 最佳实践

1. **错误处理**：始终处理编译错误
2. **异步操作**：在异步环境中使用异步 API
3. **配置选项**：根据环境配置不同选项
4. **性能优化**：使用缓存和增量编译
5. **类型安全**：利用 Dart 的类型系统
