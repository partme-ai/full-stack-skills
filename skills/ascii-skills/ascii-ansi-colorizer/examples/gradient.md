# ascii-ansi-colorizer：渐变示例

## Input

```
PARTME
AI CLI
```

## Script usage

```bash
python3 scripts/colorize.py --mode gradient --direction lr < ./input.txt
```

## Output（示意，带 ANSI）

```
\x1b[38;5;33mP\x1b[0m\x1b[38;5;39mA\x1b[0m\x1b[38;5;45mR\x1b[0m...
```

## Notes
- 真实终端中会显示为渐变色文字
- 若重定向到文件，建议禁用颜色并输出无色版本
