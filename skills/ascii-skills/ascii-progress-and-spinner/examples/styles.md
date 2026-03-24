# ascii-progress-and-spinner：样式库示例

## Progress bars（determinate）

宽度=20 示例（固定宽度，避免抖动）：

1) block
```
[#######-------------] 35%
```

2) line
```
|=======-------------| 35%
```

3) dots
```
(ooooooo.............) 35%
```

## Spinners（indeterminate）

1) classic
```
| / - \ (循环)
```

2) dots
```
loading.
loading..
loading...
```

## Log fallback（non-TTY）
```
task=build step=compile progress=35%
task=build step=compile progress=36%
```
