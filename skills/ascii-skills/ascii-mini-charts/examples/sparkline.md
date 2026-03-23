# ascii-mini-charts：sparkline 示例

## Input

```json
{
  "series": [3, 4, 5, 8, 6, 9, 12, 10, 11, 14]
}
```

## Output（ASCII-only，示意）

minimal：

```
..:-=+**#@
```

annotated：

```
..:-=+**#@  min=3 max=14 cur=14
```

## Script usage

```bash
cat << 'JSON' | python3 scripts/mini_charts.py --type sparkline --width 20
{ "series": [3,4,5,8,6,9,12,10,11,14] }
JSON
```
